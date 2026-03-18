# Extensions

## Current outcome

The notebook has now been significantly extended and aligned with the PI's material.

The main results are:

- the core notebook now uses a simplified symmetric formulation rather than separate per-neuron parameter sets
- a paper-style phase-plane section has been added for the original mutual-excitation Rashevsky model
- the final extension now uses the PI-style inhibitory/complementary second equation
- the final Python plots have been reshaped to match the visual style of the R plots:
  - nullclines
  - many trajectories started from the boundary of the square
  - one highlighted special trajectory
- the student notebook has been kept self-contained and no longer refers explicitly to hidden R support code

## What we learned from the R file

The original file [rashevsky_model.R](/Users/hiazmani/Documents/PhD/Teaching/roai_vub/2526/opdrachten/opdracht_3_neurale_netwerken/rashevsky_model.R) contains two relevant ideas.

### 1. Original active system

The active equations in the file are the symmetric mutual-excitation system:

- `dy[1] = (1 - exp(-a * max(0, y[2] - h2))) - y[1] / alpha`
- `dy[2] = (1 - exp(-a * max(0, y[1] - h1))) - y[2] / alpha`

This is the original recurrent excitatory loop.

### 2. Commented alternative second equation

The file also contains a commented alternative for the second equation:

- `dy[2] <- (1 - (1 - exp(...))) - y[2] / alpha`

This is the variant the PI described verbally. Conceptually:

- the first equation stays excitatory
- the second equation uses the complement of the excitatory term
- this creates an inhibitory-style or push-pull effect

That asymmetry is what makes the later phase portraits behave differently.

## What we tested

We ran both versions outside the notebook to understand which one shows the qualitative effects the PI remembered.

### Original active R equations

When varying `alpha` in the original symmetric system:

- the fixed point moves
- the trajectories change shape
- but strong spiral-like settling is not very pronounced

### `1 - equation` variant

When varying `alpha` in the complementary second-equation variant:

- the approach to equilibrium becomes much more curved
- spiral-like settling becomes visibly stronger as `alpha` increases
- this matches the PI's recollection much better

This is why the notebook's final extension was redirected toward that variant.

## Notebook alignment decisions

The notebook now uses two distinct dynamical stories on purpose.

### A. Original Rashevsky-style mutual excitation

This is used for the main historical and graphical reconstruction:

- thresholded saturation
- recurrent excitation
- persistent versus quiescent regimes
- nullclines
- boundary-started phase-plane trajectories

### B. PI-style inhibitory/complementary extension

This is used as the final extension:

- the first equation remains excitatory
- the second equation uses the complement of the excitatory term
- students explore how changing `alpha` affects the geometry of the trajectories
- the main observation is the difference between direct settling and more spiral-like settling

## Why this structure makes sense pedagogically

For a two-hour student session, the notebook should focus on:

- understanding the original recurrent excitatory model
- seeing how graphical phase-plane analysis works
- noticing how a qualitatively different second equation changes the dynamics

The final extension is therefore best treated as:

- a compact qualitative comparison
- not a long secondary parameter study

The current version supports that:

- one section introduces the inhibitory-style variant
- one plot shows the same style of phase portrait as the paper-style plots
- one short comparison across several `alpha` values lets students observe spiral-like settling directly

## Remaining optional extensions

Possible future additions, if more time is available:

- add a final reflection question comparing the geometry of the mutual-excitation and inhibitory-style systems
- add a short written explanation of why asymmetry in the equations can produce spiral-like convergence
- add a compact `README.md` for students with execution instructions and a one-paragraph roadmap
