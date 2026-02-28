# Website Redesign Ideas for edmundcrawley.com

## Current State

Your site is a clean, hand-crafted single-page HTML site. It's functional and well-structured with good SEO, responsive breakpoints, and expandable abstracts/BibTeX. But visually it reads as a classic academic homepage — light gray background, system fonts, flat list of papers, no visual hierarchy beyond headings. The CSS has accumulated some redundancy (multiple `.container` declarations, `!important` overrides) that a redesign would clean up.

The ideas below are organized from quickest wins to most ambitious changes. Each is labeled so you can pick and choose.

---

## A. Quick Visual Wins (keep current HTML/CSS, no new tools)

### A1. Modern Typography

Replace the system font stack with a web font that signals "modern but serious." Load it from Google Fonts with a single `<link>` tag.

- **Body text:** [Inter](https://fonts.google.com/specimen/Inter) (clean, designed for screens) or [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3)
- **Headings:** [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) (pairs well with Inter, adds an academic touch without looking old-fashioned)
- Increase base font size to 16–17px and line-height to 1.6 for better readability

### A2. Dark / Light Mode Toggle

The single most impactful "I'm tech-savvy" signal on an academic website. You already use CSS custom properties in `:root`, so this is straightforward:

- Define a `[data-theme="dark"]` set of variables (e.g., background `#1a1a2e`, text `#e0e0e0`, links `#7eb8da`)
- Add a small sun/moon toggle button in the top-right corner
- Use `localStorage` to remember the user's preference
- Respect `prefers-color-scheme` media query as the default

### A3. Card-Based Paper Layout

Instead of a flat list separated by `<hr>`, wrap each paper in a card with:

- Subtle background (`white` in light mode, slightly lighter dark in dark mode)
- Rounded corners (`border-radius: 8px`)
- Soft shadow (`box-shadow: 0 1px 3px rgba(0,0,0,0.08)`)
- Slight elevation on hover (`transform: translateY(-2px)` with `transition`)
- 1rem padding inside the card

This immediately makes the page feel more designed and helps users scan papers more easily.

### A4. Accent Color

Your current palette is grayscale + dark blue links. Pick a single accent color and use it consistently for:

- Links and buttons
- Section heading underlines or left-border highlights
- The dark/light toggle
- Hover states

Suggestions: a muted teal (`#2a9d8f`), a warm navy (`#264653`), or Federal Reserve blue (`#003366`) with a brighter accent for interactive elements.

### A5. Subtle Scroll Animations

Use the Intersection Observer API (no library, ~15 lines of JS) to fade in each paper card as it scrolls into view:

```css
.paper { opacity: 0; transform: translateY(20px); transition: opacity 0.5s, transform 0.5s; }
.paper.visible { opacity: 1; transform: translateY(0); }
```

This transforms a static page into one that feels alive. The key is subtlety — keep the animation under 500ms and the translate small.

### A6. Better Headshot Treatment

- Crop to a circle or rounded rectangle (`border-radius: 50%` or `12px`)
- Add a subtle border in your accent color
- On desktop, consider placing it inside a hero section rather than floating right

---

## B. Structural Improvements (moderate effort, still plain HTML)

### B1. Sticky Navigation Bar

As visitors scroll, a slim nav bar appears at the top with section anchors:

```
Edmund Crawley    |  Working Papers  |  Published  |  Policy  |  Projects  |  CV
```

- Use `position: sticky` with a `backdrop-filter: blur(10px)` for a modern glassmorphism effect
- Highlight the active section as the user scrolls (Intersection Observer again)
- On mobile, collapse to a hamburger menu or just show initials + hamburger

### B2. Hero / About Section

Replace the current header with a proper hero section:

- Your name in large, bold type
- A one-line research tagline (e.g., *"Studying how households consume, save, and respond to policy"*)
- Affiliation and email below
- Social icons row: Google Scholar, GitHub, LinkedIn, Twitter/X — using simple SVG icons
- The disclaimer can move to a small footer or a subtle tooltip

This gives visitors an immediate sense of who you are before they see the paper list.

### B3. Featured Paper Highlight

Pick your most impactful or newest paper and give it prime real estate:

- A larger card at the top of the research section
- Include a key figure from the paper (see Section C below)
- "Read Paper" and "View Code" buttons styled prominently
- A one-sentence summary in larger text

This creates visual hierarchy — not all papers are equal, and visitors should see your best work first.

### B4. Research Impact Numbers

A horizontal strip showing key metrics at a glance:

```
  6 Published Papers  |  3 Working Papers  |  AEJ: Macro, Econometrica, ...  |  Econ-ARK Contributor
```

Style with large numbers and small labels. This is a common pattern on modern portfolio sites and quickly communicates your track record.

### B5. Positions as a Timeline

Replace the flat list of positions with a vertical timeline:

- A thin vertical line on the left
- Each position as a node with a dot, date range, and description
- Subtle animation as each node scrolls into view

This is more visually interesting than a plain list and better conveys career progression.

### B6. Footer

Add a proper footer with:

- Links to Google Scholar, GitHub, LinkedIn, Twitter/X
- "Last updated: [date]"
- The Fed disclaimer (move it out of the header)
- A subtle "Built with [tech]" credit if you want

---

## C. Key Figures from Papers

You mentioned wanting to highlight key figures. Here are specific ideas:

### C1. Hero Figure

Embed one striking chart from your most important paper directly in the hero section or featured paper card. Candidates:

- A figure from "Do Households Substitute Intertemporally?" showing the 10 structural shocks
- The MPC heterogeneity chart from "Consumption Heterogeneity"
- A policy comparison figure from "Welfare and Spending Effects"

Export as SVG for crispness at any size, or use a high-res PNG with `loading="lazy"`.

### C2. Paper Thumbnails

For each paper card, include a small thumbnail of a key figure (say 200x150px). This:

- Breaks up the wall of text
- Gives a visual preview of what the paper is about
- Makes the page look more like a research portfolio than a CV

### C3. Interactive Chart (ambitious but impressive)

Embed one interactive visualization using [Observable Plot](https://observablehq.com/plot/) or [Chart.js](https://www.chartjs.org/):

- Could show a key time series from your research
- Or an interactive version of a paper figure where users can hover for values
- Even a simple animated chart that draws itself on scroll would be striking

---

## D. Technology Migration Options

### D1. Astro (Recommended)

[Astro](https://astro.build/) is a modern static site generator that would be ideal for your needs:

- **Islands architecture:** Mostly static HTML (fast!) with isolated interactive components (charts, dark mode toggle) that hydrate independently
- **Markdown content:** Write each paper as a markdown file with frontmatter — easier to maintain than editing raw HTML
- **Tailwind CSS:** Built-in support for utility-first CSS, making responsive design and dark mode trivial
- **Component reuse:** Header, footer, paper card become reusable components
- **MDX support:** Can embed interactive charts directly in markdown
- Good template to start from: [Dante Astro Theme](https://dante-astro-theme.netlify.app/) ([GitHub](https://github.com/JustGoodUI/dante-astro-theme)) — clean, dark/light toggle, content-focused

### D2. Hugo with Pascal Michaillat's Template

[Pascal Michaillat](https://pascalmichaillat.org/) (an economist at UCSC) built a beautiful minimalist Hugo template specifically for academic economists:

- [Template repository](https://github.com/pmichaillat/hugo-website)
- Clean, content-first layout with sections for Papers, Courses, and a **live data dashboard**
- The dashboard feature is particularly relevant — an economist at the Fed could have a live business-cycle dashboard that auto-updates
- KaTeX math rendering built in
- Fast builds, excellent SEO
- Less flexible than Astro for custom interactivity, but purpose-built for your use case

### D3. HugoBlox Academic Theme (formerly Wowchemy)

The most popular academic website theme, used by 250,000+ researchers:

- [Live demo](https://academic-demo.netlify.app/) | [GitHub](https://github.com/HugoBlox/hugo-theme-academic-cv)
- 12 built-in color themes, dark/light toggle
- Widget-based homepage (profile card, featured publications, experience timeline)
- Auto-imports citations from BibTeX
- Powerful but heavier and more opinionated than the other options

---

## E. "Outside the Academic Mainstream" Ideas

These are features that would make your site stand out from the typical academic page:

### E1. Live Data Dashboard

Inspired by Pascal Michaillat's [business-cycle dashboard](https://pascalmichaillat.org/dashboard/). You could have a small dashboard section showing:

- A key macro indicator relevant to your research (e.g., consumption growth, income inequality metric)
- Updated periodically via FRED API or a scheduled data pull
- This immediately signals "I am a quantitative researcher who builds things"

### E2. Animated Number Counters

When the "Research Impact" section scrolls into view, the numbers animate from 0 to their final value (a common portfolio site technique). Small touch, but it catches the eye.

### E3. Paper Filter / Tag System

Add clickable tags to papers (consumption, fiscal policy, HANK, income uncertainty, intertemporal substitution) that filter the paper list dynamically. This is useful for visitors who care about a specific topic and makes the site feel like a research tool, not just a list.

### E4. Reading Time / TL;DR

For each paper, add a one-line "TL;DR" visible without clicking — a plain-English sentence summarizing the main finding. This is uncommon in economics and very reader-friendly.

### E5. Subtle Background Pattern or Gradient

Instead of flat `#eaebed`, use a very subtle gradient or geometric pattern. Examples:

- A faint diagonal line pattern (like graph paper)
- A gradient from white to very light blue
- Subtle animated gradient that shifts slowly (see [stripe.com](https://stripe.com) for inspiration — their animated gradient hero is iconic)

### E6. Custom Cursor or Micro-interactions

- Links that underline with a smooth animation from left to right on hover
- Paper cards that subtly glow on hover
- A custom SVG cursor on interactive elements
- These are small but cumulatively create a polished feel

---

## F. Inspiration Links

### Academic Economist Sites
| Site | What's Notable |
|------|---------------|
| [pascalmichaillat.org](https://pascalmichaillat.org/) | Gold standard minimalist economist site. Live data dashboard. Hugo template available on GitHub. |
| [HugoBlox Academic Demo](https://academic-demo.netlify.app/) | Feature-rich academic theme with dark mode, widgets, 12 color themes |
| [Sites for Scholars Portfolio](https://www.sitesforscholars.com/portfolio/) | Gallery of professionally designed academic sites — good for layout ideas |

### Modern Portfolio / Personal Sites
| Site | What's Notable |
|------|---------------|
| [Dante Astro Theme](https://dante-astro-theme.netlify.app/) | Clean dark/light toggle, card layout, Astro + Tailwind. Great starting point. |
| [AstroWind](https://astrowind.vercel.app/) | Scroll animations, statistics callout section, hero with CTAs. Most-starred Astro theme. |
| [wattenberger.com](https://wattenberger.com/) | Data viz practitioner. Interactive scroll-driven visualizations as hero elements. Aspirational for "charts from papers" idea. |
| [stripe.com](https://stripe.com) | Iconic animated gradient hero. Shows how subtle animation creates a premium feel. |
| [Awwwards Portfolio Collection](https://www.awwwards.com/websites/portfolio/) | Curated award-winning portfolio sites. Browse for specific interaction patterns and typography ideas. |

### Tools & Resources
| Resource | Use For |
|----------|---------|
| [Astro Themes Gallery](https://astro.build/themes/) | Browse Astro templates to find a starting point |
| [Hugo Themes Gallery](https://themes.gohugo.io/) | Browse Hugo templates |
| [Observable Plot](https://observablehq.com/plot/) | Lightweight interactive charts for embedding |
| [Chart.js](https://www.chartjs.org/) | Simple, responsive charts |
| [Google Fonts](https://fonts.google.com/) | Inter, Source Serif 4, and other modern typefaces |
| [Tailwind CSS](https://tailwindcss.com/) | Utility-first CSS framework with built-in dark mode |
| [Heroicons](https://heroicons.com/) | Clean SVG icons for social links, navigation |

---

## Suggested Priority Order

If I were implementing these changes, I'd do them in this order:

1. **A1 + A2 + A4:** Typography, dark mode, accent color — biggest visual impact for least effort
2. **A3 + A5:** Card layout + scroll animations — makes it feel designed
3. **B2 + B1:** Hero section + sticky nav — establishes visual hierarchy
4. **C1 + C2:** Add key figures to papers — makes research tangible
5. **B3 + B4:** Featured paper + impact numbers — highlights your best work
6. **D1 or D2:** Migrate to Astro or Hugo — sets you up for long-term maintainability
7. **E1–E6:** The fun extras — dashboard, filters, micro-interactions

Steps 1–5 can all be done within your current plain HTML/CSS setup. Step 6 is a one-time migration that makes everything after it easier.
