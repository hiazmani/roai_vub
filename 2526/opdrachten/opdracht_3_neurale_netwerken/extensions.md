# Extensions

## R Script Analysis: `rashevsky_model.R`

The file [rashevsky_model.R](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R) complements the notebook well. It is not mainly a time-series demo like the current Python notebook. It is a phase-plane reproduction script that tries to recreate the graphical analysis from Rashevsky's paper.

### What the R file does

In [rashevsky_model.R:3](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R#L3), it defines a 2-variable ODE system:

- `dy[1] = (1 - exp(-a * max(0, y[2] - h2))) - y[1] / alpha`
- `dy[2] = (1 - exp(-a * max(0, y[1] - h1))) - y[2] / alpha`

This is a symmetric recurrent excitatory system with:

- thresholding via `max(0, ...)`
- saturation via `1 - exp(...)`
- linear decay via `-y/alpha`

That is very close in spirit to the notebook's `rashevsky_rhs`, but it uses a simpler parameterization:

- one common gain `a`
- one common decay timescale `alpha`
- thresholds `h1`, `h2`
- no separate `I`, `theta`, `A`, `gamma`

Then the script does three things.

1. It defines one parameter regime in [rashevsky_model.R:12-18](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R#L12).
   Current values:
   - `h1 = h2 = 0.3`
   - `a = 4`
   - `alpha = 1`

2. It plots the two nullcline-like curves in [rashevsky_model.R:21-25](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R#L21):
   - first curve: `e1 = 1 - exp(-a * max(0, e2 - h2))`
   - second curve: `e2 = 1 - exp(-a * max(0, e1 - h1))`

   In the plot, one is drawn solid and the other dashed. This is the core geometric picture from the paper.

3. It integrates many trajectories from initial conditions placed along the boundary of the square `[0, 1.5] x [0, 1.5]` in [rashevsky_model.R:27-58](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R#L27).
   That gives a phase portrait: students can see which initial states flow to rest and which flow to a persistent active state.

Finally, in [rashevsky_model.R:60-63](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R#L60), it adds one special trajectory starting from `(0, 0.9779547)`, likely intended to highlight a separatrix or near-threshold behavior.

### Why this is pedagogically interesting

This script is valuable because it shows the model in the way Rashevsky actually analyzed it:

- not just `e(t)` over time
- but as geometry in the `(e1, e2)` plane
- with nullclines plus trajectories from many initial conditions

That is more historically faithful than the current notebook, which already has phase-plane and nullcline sections but treats them more numerically and less as a direct paper-style reconstruction.

### Relationship to the current notebook

The notebook already has three nearby pieces:

- phase-plane trajectories
- nullclines
- multiple initial conditions

What is missing is the specific paper-reproduction version:

- the simplified symmetric parameterization from the R file
- plotting the paper-style curves directly as explicit functions
- launching trajectories from the boundary of the square
- highlighting the special initial condition near the basin boundary

So this does not require a completely new notebook section. It needs one focused addition that bridges the notebook to the PI's R script.

### Simplification Decision

For this extension, the notebook should use the same simplified symmetric form as the R script rather than the more general parameterization currently used elsewhere in the notebook.

That means:

- one shared coupling/amplitude parameter `A`
- one shared saturation parameter `alpha`
- thresholds `h1`, `h2`
- no separate parameters for neuron 1 and neuron 2

The goal is to keep this section as simple and paper-like as possible, so students can focus on the geometry and qualitative behavior rather than bookkeeping across many parameters.

## What to Add to the Notebook

Add one new section after the current phase-plane/nullcline material:

`## Reproducing Rashevsky's graphical analysis`

Then include four pieces.

1. A short markdown explanation.
   Explain that the original paper studies the system graphically in the phase plane. State that the next cells reproduce that style more directly, using a simplified symmetric version of the model.

2. A Python version of the R model.
   Use the simplified symmetric parameterization directly, instead of the more general `I1`, `I2`, `A1`, `A2`, `gamma1`, `gamma2`, etc.

   Example:

   ```python
   def rashevsky_paper_rhs(state, t, params):
       e1, e2 = state
       A = params["A"]
       alpha = params["alpha"]
       h1 = params["h1"]
       h2 = params["h2"]

       de1dt = A * (1 - np.exp(-alpha * np.maximum(0, e2 - h2))) - e1
       de2dt = A * (1 - np.exp(-alpha * np.maximum(0, e1 - h1))) - e2
       return [de1dt, de2dt]
   ```

   This keeps the two equations symmetric and avoids introducing separate per-neuron parameters in this historical reconstruction section.

3. A direct reproduction plot.
   Make one figure with:
   - the two nullclines as explicit curves
   - trajectories started from the four boundaries
   - the highlighted special trajectory

   This is the key addition. It should mirror the R script visually.

4. A short exploration exercise.
   Ask students to vary:
   - `h1`, `h2`
   - `A`
   - `alpha`

   and observe:
   - whether the nonzero equilibrium still exists
   - whether the basin of attraction grows or shrinks
   - whether the special initial condition still separates behaviors

## Minimal Integration Plan

For the least disruption to the notebook, add:

- one markdown cell introducing the R-script reproduction
- one code cell defining `rashevsky_paper_rhs`
- one code cell plotting the paper-style nullclines and trajectories
- one markdown cell with three exploration questions

That is enough to make the PI's material available to students without restructuring the notebook.

## Important Teaching Note

The R script is not written as a student-facing explanation. It is a compact research-style plotting script. If it is exposed in the notebook, students will need explicit framing:

- what the two curves mean
- why the boundary initial conditions are chosen
- what the special dashed trajectory is supposed to illustrate

Without that framing, they will be able to run it, but many will miss the point.
