"""Build the narrated version of the Ten Shocks deck.

    ~/.venvs/tts/Scripts/python.exe tools/build_narration.py          # audio + page
    ~/.venvs/tts/Scripts/python.exe tools/build_narration.py --only 7.1 4.3
    python tools/build_narration.py --page                           # page only (stdlib)

Audio: each `### slide.step` block of narration.md is read by Kokoro (voice
bm_george) into tenshocks-narration/<slide.step>.mp3. A block is only
re-synthesized when its text (or the voice) changes; tenshocks-narration/
manifest.json holds the hashes and durations.

Page: tenshocks-narrated.html is generated from tenshocks-slides.html (so edit
the slides there and re-run with --page), with a player that plays each build
step's clip and moves on when it ends.

The TTS environment lives outside OneDrive:
    uv venv --python 3.11 ~/.venvs/tts
    uv pip install --python ~/.venvs/tts/Scripts/python.exe \
        --extra-index-url https://download.pytorch.org/whl/cpu \
        --index-strategy unsafe-best-match "torch>=2.6" kokoro soundfile lameenc pip
"""
import argparse, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NARRATION = ROOT / "narration.md"
DECK = ROOT / "tenshocks-slides.html"
PAGE = ROOT / "tenshocks-narrated.html"
AUDIO = ROOT / "tenshocks-narration"
MANIFEST = AUDIO / "manifest.json"

VOICE, LANG, SPEED = "bm_george", "b", 1.0
RATE = 24000
LEAD, GAP_PARA, TAIL = 0.15, 0.45, 0.25  # seconds of silence

# How the voice says names and terms (the lexicon at the end of narration.md),
# as Kokoro/misaki phonemes. Order matters: longer patterns first.
LEXICON = [
    (r"\btheta-R\b", "[theta](/θˈAtə/) [R](/ˈɑː/)"),
    (r"\btheta-Y\b", "[theta](/θˈAtə/) [Y](/wˈI/)"),
    (r"\btheta\b", "[theta](/θˈAtə/)"),
    (r"\bHANK\b", "[HANK](/hˈæŋk/)"),
    (r"\bRANK\b", "[RANK](/ɹˈæŋk/)"),
    (r"\bVAR\b", "[V](/vˈiː/) [A](/ˈA/) [R](/ˈɑː/)"),
    (r"\bMIT\b", "[M](/ˈɛm/) [I](/ˈI/) [T](/tˈiː/)"),
    (r"\bB-splines\b", "[B](/bˈiː/) splines"),
    (r"\bEuler\b", "[Euler](/ˈɔɪləɹ/)"),
    (r"\bCrawley\b", "[Crawley](/kɹˈɔːli/)"),
    (r"\bGamber\b", "[Gamber](/ɡˈæmbə/)"),
    (r"\bSlacalek\b", "[Slacalek](/slˈɑːkəlɛk/)"),
    (r"\bFagereng\b", "[Fagereng](/fˈɑːɡəɹɛŋ/)"),
    (r"\bNatvik\b", "[Natvik](/nˈɑːtviːk/)"),
    (r"\bViolante\b", "[Violante](/viːoʊlˈænteɪ/)"),
    (r"\bRamey\b", "[Ramey](/ɹˈAmi/)"),
    (r"\bGertler\b", "[Gertler](/ɡˈɜːtlə/)"),
    (r"\bKaradi\b", "[Karadi](/kəɹˈɑːdi/)"),
    (r"\bPerotti\b", "[Perotti](/pəɹˈɒti/)"),
    (r"\bBlanchard\b", "[Blanchard](/blɑːnʃˈɑːd/)"),
    (r"\bMertens\b", "[Mertens](/mˈɜːtənz/)"),
    (r"\bRavn\b", "[Ravn](/ɹˈɑːvən/)"),
    (r"\bLeeper\b", "[Leeper](/lˈiːpə/)"),
]


def blocks():
    """{'4.3': [paragraph, ...]} from the ### blocks of narration.md."""
    out, key, lines = {}, None, []
    def flush():
        if key:
            paras = [" ".join(p.split()) for p in "\n".join(lines).split("\n\n")]
            out[key] = [p for p in paras if p]
    for line in NARRATION.read_text(encoding="utf-8").splitlines():
        m = re.match(r"###\s+(\d+\.\d+)\b", line)
        if m or line.startswith("## ") or line.strip() == "---":
            flush(); key, lines = (m.group(1) if m else None), []
        elif key:
            lines.append(line)
    flush()
    return out


def speakable(p):
    for pat, rep in LEXICON:
        p = re.sub(pat, rep, p)
    return p


def build_audio(only):
    import numpy as np, lameenc
    from kokoro import KPipeline
    AUDIO.mkdir(exist_ok=True)
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    todo = {}
    for k, paras in blocks().items():
        text = [speakable(p) for p in paras]
        h = hashlib.sha1(json.dumps([VOICE, SPEED, text]).encode()).hexdigest()[:12]
        stale = man.get(k, {}).get("hash") != h or not (AUDIO / f"{k}.mp3").exists()
        if (only and k in only) or (not only and stale):
            todo[k] = (text, h)
    pipe = KPipeline(lang_code=LANG, repo_id="hexgrad/Kokoro-82M") if todo else None
    sil = lambda s: np.zeros(int(s * RATE), dtype=np.float32)
    for k, (text, h) in todo.items():
        parts = [sil(LEAD)]
        for i, p in enumerate(text):
            if i: parts.append(sil(GAP_PARA))
            parts += [a.numpy() for _, _, a in pipe(p, voice=VOICE, speed=SPEED)]
        parts.append(sil(TAIL))
        audio = np.concatenate(parts)
        enc = lameenc.Encoder()
        enc.set_bit_rate(64); enc.set_in_sample_rate(RATE); enc.set_channels(1); enc.set_quality(2)
        pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes()
        (AUDIO / f"{k}.mp3").write_bytes(enc.encode(pcm) + enc.flush())
        man[k] = {"hash": h, "dur": round(len(audio) / RATE, 2)}
        MANIFEST.write_text(json.dumps(man, indent=1, sort_keys=True))
        print(f"{k:>5}  {man[k]['dur']:6.1f}s", flush=True)
    known = set(blocks())
    for k in [k for k in man if k not in known]:
        del man[k]; (AUDIO / f"{k}.mp3").unlink(missing_ok=True)
    MANIFEST.write_text(json.dumps(man, indent=1, sort_keys=True))
    print(f"total {sum(v['dur'] for v in man.values())/60:.1f} min, {len(man)} clips")


# ---------------------------------------------------------------- page

def patch(html, old, new):
    assert html.count(old) == 1, f"anchor not found exactly once: {old[:60]}"
    return html.replace(old, new)


PLAYER = r"""
<style>
html,body{touch-action:manipulation}
#nv{position:fixed;inset:0;z-index:50;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;
  background:var(--ground);color:var(--fg);text-align:center;padding:16px;cursor:pointer}
#nv h1{font-size:clamp(22px,3.4vw,44px);font-weight:500;margin:0;max-width:22em;line-height:1.2}
#nv button{font:inherit;font-size:clamp(18px,2vw,26px);padding:.55em 1.4em;border-radius:999px;border:0;cursor:pointer;
  background:var(--fg);color:var(--ground)}
#nv p{margin:0;color:var(--muted);font-size:clamp(14px,1.4vw,19px)}
#nv[hidden]{display:none}
/* control bar: real pixels, outside the scaled stage */
#nc{position:fixed;left:50%;bottom:calc(14px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:40;
  display:flex;flex-direction:column;align-items:center;gap:8px;transition:opacity .35s;font-family:system-ui,sans-serif}
#nc[hidden]{display:none}
#nc.hide{opacity:0;pointer-events:none}
#ncb{display:flex;align-items:center;gap:6px;padding:6px 14px 6px 6px;border-radius:999px;background:var(--ground);
  box-shadow:0 4px 18px rgba(0,0,0,.18);border:1px solid var(--faint)}
#ncb button{width:44px;height:44px;border:0;border-radius:50%;background:none;color:var(--fg);font-size:17px;cursor:pointer;padding:0}
#ncb button:hover{background:var(--faint)}
#ncb #ncp{width:52px;height:52px;background:var(--fg);color:var(--ground);font-size:19px}
#nct{margin-left:6px;color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums;white-space:nowrap}
#nr{display:none;color:var(--muted);font-size:14px;text-align:center}
@media (orientation:portrait){#nc.hide{opacity:1;pointer-events:auto}}
@media (orientation:portrait) and (pointer:coarse){#nr{display:block}}
</style>
<div id="nv" role="dialog" aria-label="Start the narrated talk">
  <h1>Household Consumption Does Not Respond Directly to Interest Rates</h1>
  <button id="nvb" type="button">&#9654;&#xFE0E; Play narrated talk</button>
  <p id="nvt">Space pauses &middot; &larr; &rarr; skip &middot; F for full screen</p>
</div>
<div id="nc" hidden>
  <div id="nr">&#8635; Turn your phone sideways for a bigger view</div>
  <div id="ncb">
    <button id="ncl" type="button" aria-label="Back">&#9198;&#xFE0E;</button>
    <button id="ncp" type="button" aria-label="Pause"></button>
    <button id="ncn" type="button" aria-label="Forward">&#9197;&#xFE0E;</button>
    <span id="nct"></span>
  </div>
</div>
<script>
(()=>{
const DIR="tenshocks-narration/",CLIPS=__CLIPS__,GAP=600,D=window.__deck;
const a=new Audio();a.preload="auto";
const $=id=>document.getElementById(id);
const ov=$("nv"),ob=$("nvb"),ot=$("nvt"),nc=$("nc"),np=$("ncp"),nt=$("nct");
const touch=matchMedia("(pointer:coarse)").matches;
let on=false,started=false,key=null,timer=null,hideT=null;
/* clip start times, for the elapsed / total readout */
const KEYS=Object.keys(CLIPS).sort((x,y)=>{const [a1,b1]=x.split(".").map(Number),[a2,b2]=y.split(".").map(Number);return a1-a2||b1-b2;});
const START={};let TOTAL=0;KEYS.forEach(k=>{START[k]=TOTAL;TOTAL+=CLIPS[k];});
const mmss=t=>Math.floor(t/60)+":"+String(Math.floor(t%60)).padStart(2,"0");
ot.textContent="About "+Math.round(TOTAL/60)+" minutes · "+(touch?"Swipe to skip":ot.textContent);
function time(){if(!started)return;const k=(D.cur+1)+"."+(D.step+1),t=(START[k]||0)+(ours()?a.currentTime:0);
  nt.textContent=(D.cur+1)+"/"+D.scenes.length+" · "+mmss(t)+" / "+mmss(TOTAL);}
const keyAt=(c,s)=>(c+1)+"."+(s+1);
function nextKey(){const sc=D.scenes[D.cur];return D.step<sc.n-1?keyAt(D.cur,D.step+1):D.cur<D.scenes.length-1?keyAt(D.cur+1,0):null;}
const atEnd=()=>D.cur===D.scenes.length-1&&D.step===D.scenes[D.cur].n-1;
const ours=()=>(a.getAttribute("src")||"").startsWith(DIR);  /* not the silent unlock clip */
function icon(){np.innerHTML=on?"&#10074;&#10074;":"&#9654;&#xFE0E;";np.setAttribute("aria-label",on?"Pause":"Play");}
/* controls: always shown while paused; while playing they fade after a few seconds */
function show(){nc.classList.remove("hide");clearTimeout(hideT);if(on)hideT=setTimeout(()=>nc.classList.add("hide"),3000);}
function stopTimer(){clearTimeout(timer);timer=null;}
function load(){stopTimer();time();const k=keyAt(D.cur,D.step);if(k===key)return;key=k;
  if(!(k in CLIPS)){a.removeAttribute("src");if(on)advance();return;}
  a.src=DIR+k+".mp3";if(on)a.play().catch(()=>{});
  const n=nextKey();if(n&&n in CLIPS)fetch(DIR+n+".mp3").catch(()=>{});}
function advance(){stopTimer();if(!on)return;
  if(D.busy){timer=setTimeout(advance,150);return;}  /* let the build animation finish */
  if(atEnd()){finish();return;}
  timer=setTimeout(()=>{timer=null;if(on)D.next();},GAP);}
function finish(){on=false;icon();show();ob.innerHTML="&#8635; Watch again";ot.textContent="Thanks for listening.";ov.hidden=false;nc.hidden=true;
  try{if(document.fullscreenElement)document.exitFullscreen();}catch(e){}}
function play(){on=true;icon();show();gsap.globalTimeline.resume();
  if(!ours()||a.ended)advance();else a.play().catch(()=>{});}
function pause(){on=false;icon();show();stopTimer();a.pause();gsap.globalTimeline.pause();}
const toggle=()=>on?pause():play();
a.addEventListener("ended",()=>{if(ours())advance();});
a.addEventListener("error",()=>{if(ours())advance();});
a.addEventListener("timeupdate",time);
window.addEventListener("deckstep",()=>{if(started)load();});
function begin(e){e.stopPropagation();ov.hidden=true;nc.hidden=false;
  /* unlock audio inside the click, for Safari */
  a.src="data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=";a.play().catch(()=>{});
  /* phones: full screen and landscape where the browser allows it (Android; not iPhone Safari) */
  if(touch){try{const r=document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
    if(r)r.then(()=>screen.orientation&&screen.orientation.lock&&screen.orientation.lock("landscape")).catch(()=>{});}catch(err){}}
  on=true;icon();show();key=null;
  if(started){D.goTo(0,false);return;}
  started=true;window.__deckStart();}
ov.addEventListener("click",begin);
nc.addEventListener("click",e=>{e.stopPropagation();show();});
np.addEventListener("click",toggle);
$("ncl").addEventListener("click",()=>D.prev());
$("ncn").addEventListener("click",()=>D.next());
/* on touch screens a tap shows or hides the controls instead of skipping; swipes still skip */
window.addEventListener("click",e=>{if(!touch||!ov.hidden||nc.contains(e.target))return;e.stopPropagation();
  if(nc.classList.contains("hide"))show();else if(on){clearTimeout(hideT);nc.classList.add("hide");}},true);
document.addEventListener("mousemove",()=>{if(started&&ov.hidden)show();});
window.addEventListener("keydown",e=>{
  if(!ov.hidden){if([" ","Enter"].includes(e.key)){e.preventDefault();e.stopImmediatePropagation();begin(e);}
    else if(!["f","F","t","T"].includes(e.key))e.stopImmediatePropagation();return;}
  if(e.key===" "||e.key==="k"||e.key==="K"){e.preventDefault();e.stopImmediatePropagation();toggle();}},true);
icon();
})();
</script>
"""


def build_page():
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    html = DECK.read_text(encoding="utf-8")
    html = re.sub(r"<title>(.*?)</title>", r"<title>\1 (narrated)</title>", html, count=1)
    # let the player see each step change, the deck's state, and whether a build is still animating
    html = patch(html, "function ui(){", 'function ui(){queueMicrotask(()=>window.dispatchEvent(new Event("deckstep")));')
    html = patch(html, "window.__deck={scenes,goTo};",
                 "window.__deck={scenes,goTo,next,prev,get cur(){return cur},get step(){return step},"
                 "get busy(){return !!(active&&active.isActive())}};")
    # "#4.3" starts at the end of step 2 and animates step 3, so its clip plays with the build
    html = patch(html,
        'const sc=scenes[start];cur=start;step=Math.max(0,Math.min(sc.n,jump)-1);sc.el.classList.add("on");'
        'gsap.set(sc.el,{opacity:1});sc.tl.seek("L"+Math.min(sc.n,jump),false);ui();};',
        'const sc=scenes[start],j=Math.max(1,Math.min(sc.n,jump));if(j===1){goTo(start,false);return;}'
        'cur=start;step=j-2;sc.el.classList.add("on");gsap.set(sc.el,{opacity:1});sc.tl.seek("L"+(j-1),false);next();};')
    # wait for the Play click instead of starting on load
    html = patch(html,
        "if(document.fonts&&document.fonts.ready){Promise.race([document.fonts.ready,new Promise(r=>setTimeout(r,1500))]).then(go);}else go();",
        "window.__deckStart=()=>(document.fonts&&document.fonts.ready?Promise.race([document.fonts.ready,"
        "new Promise(r=>setTimeout(r,1500))]):Promise.resolve()).then(go);")
    clips = json.dumps({k: v["dur"] for k, v in sorted(man.items())})
    html = patch(html, "</body>", PLAYER.replace("__CLIPS__", clips) + "</body>")
    PAGE.write_text(html, encoding="utf-8")
    print(f"wrote {PAGE.name} ({len(man)} clips)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="re-synthesize just these blocks, e.g. 7.1 4.3")
    ap.add_argument("--page", action="store_true", help="only rebuild the HTML page")
    args = ap.parse_args()
    if not args.page:
        build_audio(set(args.only or []))
    build_page()
