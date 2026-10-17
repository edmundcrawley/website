# Narration

Text-to-speech version of `script.md` for the narrated web deck. Each `###`
block is the audio for one build step, keyed `slide.step` exactly as in the
deck's URL hash (`#4.3` = slide 4, end of build step 3), so the player can
play block 4.3 while it animates build step 3 of slide 4. Everything below a
`###` header up to the next header is read aloud; the label after the key is
only for orientation.

Written to be spoken: symbols and numbers are spelled out the way they should
be said, and references to the room are dropped. Names keep their normal
spelling here (so the captions read correctly); the lexicon at the end tells
the voice how to say them.

---

## 1. Title

### 1.1 · Title

Household Consumption Does Not Respond Directly to Interest Rates: Evidence
from Ten Macroeconomic Shocks. By Edmund Crawley and Will Gamber, of the
Federal Reserve Board.

The views expressed in this presentation are solely the responsibility of the
authors, and should not be interpreted as reflecting the views of the Board of
Governors of the Federal Reserve System, or of anyone else associated with the
Federal Reserve System.


---

## 2. How do households respond to interest rates?

### 2.1 · RANK

The question we want to answer is how household consumption responds to interest rates. In the
representative-agent New Keynesian model, almost all of monetary transmission runs directly through the response of household consumption to the real interest rate itself: when rates
rise, households postpone consumption to take advantage of the higher return on
saving. That's the thick arrow across the top: the direct channel.

### 2.2 · HANK

Heterogeneous-agent models changed this picture. Many households are close to or at
their borrowing constraint and aren't on their Euler equation, so the direct
channel is dampened. More of the action runs through the indirect channel along
the bottom: higher rates reduce investment, firms hire less, wages and, ultimately, income
fall. Because constrained households have high marginal propensities to consume, they reduce spending.

### 2.3 · The question

But these are statements about models. What we want to know is what the data
say.  To do
that, we've developed a new method that uses the macro data while making far
fewer assumptions about the rest of the economy than previous work estimating
HANK models. I'll show you how it works in a moment.

### 2.4 · The answer

Here's the answer. The direct channel is even smaller than HANK says. Even a
HANK model calibrated to match the micro evidence overstates it. We find
the direct effect of interest rates on consumption is zero.
Transmission to households is all indirect.

---

## 3. Our approach: estimate only the household block

### 3.1 · Zoom into the household block

Here's the idea. Think of any full macro model: it may have firms, banks, the government,
price and wage setting, or any other structure and frictions. 
In a standard one-asset HANK model, the household block
sits inside that model and takes in just two things from it: the expected path
of interest rates, and the expected path of after-tax income. Given those two
paths, aggregate consumption is pinned down. Everything else in the model
matters for households only through what it does to income and rates.

### 3.2 · Three shocks flow through

This is also why the question is hard. Interest rates are general-equilibrium
outcomes, so we can never move rates while holding everything else fixed. But
we don't need to. A monetary shock, a fiscal shock and a technology shock each
move income and interest rates by different routes, and in different
combinations. As far as households are concerned, each one is just another
experiment on the same household block. What we need from a shock is that it
affects consumption only through income and interest rates. The pandemic is an
obvious example that fails this test, since people stopped spending for reasons
that had nothing to do with their income or interest rates. But the standard monetary, fiscal and
technology shocks in the literature are thought to work through exactly these
channels.

### 3.3 · Estimate just this block

So we estimate only the household block, and we never have to write down the
rest of the general-equilibrium model. Previous work estimates a full HANK
model, so its household estimates are only as good as the rest of the model.
Because we estimate only the household block, we're robust to misspecification
elsewhere, and agnostic about the rest of the structure. That lets us bring ten
externally identified shocks to bear on the same question, without having to
model how each one moves the economy. As the line at the bottom puts
it: households don't know, or care, why their income and interest rates moved.

---

## 4. Households see two paths

### 4.1 · Setup

Take the consumption block of a standard one-asset HANK model, and differentiate aggregate consumption
with respect to the paths of interest rates and income. Linearized around the steady state, the
consumption response is two matrices multiplied by those two paths. These matrices are
Jacobians. The entry in row t and column s says how much consumption at date t
moves when the household learns today that income, or the interest rate, will move at date s. Individual policy
functions can be fully nonlinear; we only linearize the aggregate around its
steady state. Let me show you how this works with one shock: the Romer and
Romer monetary tightening.

### 4.2 · Income flows in

First, feed in the path of income. After the tightening, income falls
gradually, and the household block turns that into lower spending. That's the
orange area.

### 4.3 · Theta for income

Both Jacobians depend on parameters, which I'll call theta. For now, think of
theta as a dial that shapes the size and timing of the Jacobians. 

### 4.4 · Rates flow in

Now feed in the path of interest rates, which rise after the tightening.

### 4.5 · Theta for rates

Depending on theta, the response to interest
rates ranges from a large, immediate fall in spending, to nothing. 

### 4.6 · Measured response

Now bring in what consumption actually did after the shock, with its ninety
percent band. Notice that spending doesn't drop on impact; it falls gradually.

### 4.7 · Search over theta

We turn the dial to find the theta that best matches the measured response.

### 4.8 · The verdict

And at the best fit, the income part does essentially all the work. The
interest-rate part is estimated to be close to zero.

---

## 5. Two approaches

### 5.1 · Structural

In the paper we take two approaches to estimating the household block. The first is
structural. We use a standard one-asset HANK consumer block, calibrated to
micro data, with two free parameters. Theta-Y measures how slowly households update
their expectations about income, and theta-R how slowly they update their
expectations about interest rates.

### 5.2 · Non-parametric

The second approach is non-parametric, and it makes far fewer assumptions. We
keep the income side at the structural estimate, which is disciplined by the
micro data, and let the data draw the interest-rate Jacobian almost freely. The
only restriction is that it's smooth above the diagonal, where households
respond to rate changes they anticipate, and below it, where they respond to
rate changes that have already happened. Every structural model we
know of satisfies that. So instead of asking which value of a parameter fits
best, we ask what response to interest rates the data want, with very little
model in the way.

---

## 6. Structural model: HANK consumers with sticky expectations

### 6.1 · The household problem

Let's begin with the structural approach. The structural model is a standard one-asset consumption-savings problem. V is
the value of a household that starts the quarter with some assets and some
level of productivity. It chooses how much to consume and how much to save. It
earns after-tax income that depends on its own productivity and on aggregate
income, earns the real interest rate on its savings, and can't borrow below a
fixed limit. The only aggregate inputs are the paths of after-tax income and
the real interest rate.

### 6.2 · Sticky expectations

On top of this we add sticky expectations, following Carroll, Crawley,
Slacalek and White. Each quarter, a fraction one minus theta of households
update their beliefs about the path of income, and separately about the path
of interest rates. Theta equal to zero is full-information rational
expectations. Theta equal to one means households never update. We don't take
sticky expectations literally. A theta-R near one is observationally
equivalent to a number of other frictions that make households less responsive
to news about interest rates. It can be thought of as a convenient, one-parameter way to turn
the direct channel up or down.

### 6.3 · What theta-R does

Here's what theta-R does. Take a shock to interest rates that dies away
gradually. With full information, consumption falls sharply on impact, and then
recovers. As theta-R rises, the response becomes smaller and hump-shaped, and
at theta-R equal to one there is no response at all. So theta-R equal to one
means no direct channel.

---

## 7. Calibrated to microdata

### 7.1 · Lottery winners

Before we turn to the macro data, the income side of the model has to be
disciplined by the best micro evidence we have. Here, that's Fagereng, Holm and
Natvik's evidence on how Norwegian lottery winners spend their winnings, year
by year. The dots are the data, and the green line is the model. We use a
standard earnings process from Kaplan, Moll and Violante, progressive taxes,
and log utility, and we choose the discount factors to hit a wealth-to-income
ratio of six point six, and this spending profile. The model matches it
closely. Households spend about half of a win in the first year, and keep
spending out of it for several years after. This profile is the first column
of the income Jacobian: the response to a one-time income gain today. In our
model, that column is the same with or without sticky expectations, because
households always see the income they actually receive. So the micro data pin
it down before we estimate anything. 

---

## 8. Data and shocks

### 8.1 · Consumption and income

Now the macro data. We use quarterly U.S. data from 1970 to 2024. Consumption
is real personal consumption expenditures. For income, we use the parts of
disposable income that don't come from investments: compensation, proprietors'
income and transfers, net of social insurance contributions and the share of
taxes that falls on labor income. That matches the income concept in the
model.

### 8.2 · The interest rate

The interest rate has two pieces. After an MIT shock, with no arbitrage, every asset
earns the same expected return, so from the next quarter on, the short real
rate, the real federal funds rate, is the right return. The one moment wealth
revalues unexpectedly is the quarter the shock hits, so there we use the
realized real return on the household portfolio of stocks and bonds. This isn't
a strong assumption. The results are the same if we replace that first-quarter
return with the fed funds rate, or set it to zero, and the same if we use
Treasury yields or mortgage rates from the second quarter on.

### 8.3 · Ten shocks

For shocks, we didn't pick and choose. We took every shock for which local
projections are plotted in Valerie Ramey's chapter of the Handbook of
Macroeconomics: two monetary, five fiscal and three technology shocks,
identified with narrative, high-frequency and VAR methods. No single shock
needs to convince you on its own. What matters is the weight of evidence across
all ten.

---

## 9. Estimation: local projections, then a quasi-likelihood

### 9.1 · Local projections

Estimation has two steps. First, for each shock and each horizon out to four
years, we run local projections with Ramey's controls, to measure how
consumption, income and the real interest rate respond. On the right are the
three responses to the Romer and Romer shock.

### 9.2 · Quasi-likelihood

Second, for any value of theta, we take measured consumption, and subtract the
part the model says comes from income, and the part it says comes from
interest rates. What's left is a residual, and if the model is right, that
residual is just sampling noise. The bottom row shows this for Romer and Romer
at the best fit: measured consumption, minus the income part, minus the rate
part, leaves a residual close to zero. One important detail is that the inputs
are estimated too. So the covariance of the residual accounts for sampling
error in the income and rate responses, as well as in consumption, and for
correlation across shocks. We can do this one shock at a time, or jointly
across all ten.

---

## 10. Example: Romer and Romer (2004) monetary shock

### 10.1 · Inputs and measured consumption

Here's the Romer and Romer shock again, now with the actual estimates. After a
monetary tightening, the real rate rises, and income and consumption fall
gradually.

### 10.2 · Full information

Start with full information. The model predicts that spending falls sharply on
impact, far below what we measure. Households react straight away, both to the
expected fall in income and to the higher path of interest rates. That's the
key intuition. With perfect foresight, consumption should respond immediately
to an interest rate change, whether the real rate jumps or follows a
hump-shaped path, because households on their Euler equation react the moment
the path is announced. We don't see that in the data. There's no drop on
impact, just a gradual decline that tracks income. Sticky expectations spread
the reaction to rates out over time, and at theta-R equal to one, it
disappears.

### 10.3 · Sticky income expectations

Making income expectations sticky barely helps. Spending still falls too much
on impact.

### 10.4 · Sticky rate expectations

Making rate expectations sticky does much more. Switching off the immediate
response to interest rates closes most of the gap.

### 10.5 · Both

With both, theta-Y around zero point nine and theta-R equal to one, the model
tracks the measured response. The stickiness of rate expectations is doing
almost all the work.

### 10.6 · All ten shocks

That was one shock. Here it is for all ten, each estimated on its own. In every
panel, the dotted line is what full information predicts, and the green line is
the fit with sticky expectations. Full information is clearly rejected for some
shocks, like Gertler and Karadi, and Leeper and coauthors, where it predicts a
sharp drop on impact that isn't in the data. For others, like Blanchard and
Perotti, or Mertens and Ravn, the individual responses are too noisy to reject
it. But the fitted path stays inside the band for every shock. No single shock
settles the question on its own; pooling them is what makes the answer sharp,
and that's where we turn next.

---

## 11. Results: theta-R is about one for every shock, and jointly

### 11.1 · All estimates

Now all ten shocks. Each row is one shock, with the posterior mode and the
ninety percent interval: income stickiness on the left, and rate stickiness on
the right. Income stickiness is not precisely estimated shock by shock. That's
what we'd expect: income responds gradually after most of these shocks, so
consumption responds gradually almost regardless of theta-Y. For our question,
it's the secondary parameter. Rate stickiness is the main result. For every
shock, the mode is at or very close to one, and one lies inside the ninety
percent interval for all ten. Monetary, fiscal and technology shocks,
identified in completely different ways, all give the same answer: households
don't respond directly to interest rates. Pooling all ten shocks, theta-R is
estimated at one, with an interval from zero point nine eight to one. Theta-Y
is about zero point seven, so roughly thirty percent of households update their
income expectations each quarter. And no single shock is driving this. If we
drop any one, two or three of the shocks, the mode for theta-R never falls
below zero point nine eight.

---

## 12. Non-parametric approach: let the data draw the interest-rate Jacobian

### 12.1 · The setup

Now the second approach, which drops the sticky-expectations structure for the interest rate Jacobian. We hold
the income Jacobian at its estimate from the structural approach, take the income part out of
consumption, and ask what interest-rate Jacobian explains what's left.

### 12.2 · Minimal structure and the prior

The only restriction is the one I mentioned earlier. The Jacobian is smooth
within two regions, the response to rate changes that have already happened,
and the response to rate changes still to come, with a break on the diagonal
between them. Every structural model we know of has this shape. We build it
from B-splines and estimate seventy-two coefficients. We center the prior on
full information, the Jacobian of the standard HANK model, which predicts a
large direct response. So we aren't starting anywhere near zero. If the answer
comes out at zero, it's because the data pulled it there.

---

## 13. Non-parametric result: the data pull the interest-rate Jacobian to zero

### 13.1 · The rate shock

To see what the estimated Jacobian implies, we feed it a one percentage point
rise in the real rate, which decays with a half-life of four quarters.

### 13.2 · The prior

Here's the prior. Under full information, consumption falls by about zero point
seven percent on impact. The prior band is deliberately wide.

### 13.3 · The posterior

And here's what the data do. The posterior is pulled to zero. After impact, the
posterior mean is about zero at every horizon, the band is much tighter, and it
includes zero throughout.

### 13.4 · The remaining bullets

This clearly rejects the full-information prediction. The small dip on impact
comes from the prior, not the data. If we center the prior on zero instead, it
disappears.

---

## 14. Conclusions and implications

### 14.1 · No direct response

To sum up. Across ten shocks and two methods, we find no detectable direct
response of consumption to interest rates.

### 14.2 · HANK

For HANK models, that means heterogeneity and borrowing constraints aren't
enough. Even a model calibrated to the best micro evidence overstates the
direct channel, so it needs an extra friction: extreme stickiness, myopia, or
something equivalent.

### 14.3 · Forward guidance

It also bears on the forward guidance puzzle. If households don't react to
future interest rates, the puzzle largely goes away.

### 14.4 · Transmission

And it changes how we think about transmission. Here's the picture we started
with. The direct channel, the one the Euler equation was supposed to carry, is
all but gone. Monetary policy reaches households through the indirect channel:
through investment, hiring and wages, and then their income. That suggests the
investment channel may be doing most of the work, and points to firms as the
place to look next. Thanks for listening.

---

## Lexicon

How the voice should say names and terms it is likely to get wrong. The
respellings are a first guess: check them, especially the ones marked (?).
The TTS step will turn these into the service's pronunciation format.

| Written | Say it like |
|---|---|
| Euler | OY-ler |
| HANK | hank |
| RANK | rank |
| Crawley | CRAW-lee |
| Gamber | GAM-ber |
| Slacalek | SLAH-ka-lek (?) |
| Fagereng | FAH-geh-reng |
| Natvik | NAHT-veek |
| Violante | vee-oh-LAHN-tay |
| Ramey | RAY-mee |
| Gertler | GERT-ler |
| Karadi | kah-RAH-dee |
| Perotti | peh-ROT-tee |
| Blanchard | blahn-SHARD |
| Mertens | MER-tens |
| Ravn | RAHVEN (?) |
| Leeper | LEE-per |
| VAR | V-A-R (spelled out) |
| MIT shock | M-I-T shock (spelled out) |
| B-splines | bee-splines |
| theta-R, theta-Y | THAY-tuh R, THAY-tuh Y |
