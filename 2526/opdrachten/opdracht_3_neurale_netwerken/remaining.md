# Remaining Exercises

This file summarizes the current state of Exercises 7 to 12 in `rashevsky_conditioning_student_notebook.ipynb` and proposes a compressed structure that is more realistic for a 2-hour student assignment.

For each exercise, it records:
- what the current exercise is asking students to do
- what the main learning goal seems to be
- whether it should be kept, merged, or cut in a shorter version

## Proposed compressed structure

The current Exercises 7 to 12 contain too many repeated plotting patterns for a short assignment. The main ideas are good, but the amount of notebook mechanics is likely too large for the available time.

### Recommended shorter structure

#### New Exercise 7 — Phase plane of the two regimes

Use the current phase-plane material to introduce trajectories in `(e1, e2)` space for the persistent and quiescent regimes.

Students should:
- run provided plotting code
- compare the two phase portraits
- explain what the trajectories do in each regime

Main learning goal:
- phase-plane intuition for the earlier mutual-excitation model

This should absorb the core of the current Exercise 7 and remain interpretation-focused.

#### New Exercise 8 — Rashevsky-style graphical analysis

Merge the current paper-style phase portrait and nullcline work into one exercise.

Students should:
- run provided code for the paper-style phase portrait
- inspect the nullclines and highlighted trajectory
- explain how the geometry helps distinguish persistence from decay

Main learning goal:
- connect the notebook to Rashevsky's original graphical reasoning
- understand nullclines as a tool for qualitative analysis

This should merge the core of the current Exercises 8 and 9.

#### New Exercise 9 — Compare mutual excitation with the inhibitory-style variant

Merge the current inhibitory-variant implementation and plotting exercises into one final comparison exercise.

Students should:
- inspect provided code and plots for the inhibitory-style system
- compare its phase portrait to the earlier mutual-excitation case
- interpret what changes when the coupling becomes complementary rather than reinforcing
- optionally compare a very small number of `alpha` values

Main learning goal:
- understand how changing coupling structure changes the qualitative dynamics
- see how parameter changes affect the approach to equilibrium

This should merge the core of the current Exercises 10, 11, and 12.

### Recommended cuts

- Cut separate coding tasks for each plotting helper.
- Cut repetition where students are asked multiple times to recreate the same style of figure from scratch.
- Cut the full 4-panel `alpha` sweep unless there is still time after simplification.
- Prefer one strong interpretation question over multiple small plotting tasks.

## Exercise 7 — Explore the phase plane

### Current exercise

Students are asked to plot several trajectories in the `(e1, e2)` phase plane for the earlier mutual-excitation model.

The current code:
- defines a helper `plot_phase_plane_trajectories(...)`
- simulates several hand-picked initial conditions
- plots trajectories for both the persistent and quiescent regimes
- marks the start and end points of each trajectory

### What students currently have to do

Right now, in the notebook version, the task is still phrased as if students should produce the phase-plane plot themselves.

Concretely, that means they would need to:
- understand that phase-plane trajectories plot `(e1(t), e2(t))` rather than each variable against time
- choose several initial conditions
- call the simulator for each one
- plot the resulting curves in the plane

### Main learning goal

The main goal is not really plotting for its own sake. It is to help students see:
- how trajectories move through state space
- how different initial conditions can converge to different long-term outcomes
- how the persistent and quiescent regimes differ geometrically

The conceptual target is phase-plane intuition, not plotting boilerplate.

### Recommendation

Keep, but simplify.

Suggested role in the compressed version:
- keep as the first remaining exercise
- provide the plotting code
- ask only for interpretation of the trajectories in the two regimes

This is worth keeping because it introduces the phase plane clearly and naturally.

## Exercise 8 — Reproduce Rashevsky's graphical analysis

### Current exercise

This exercise switches from the earlier pedagogical recurrent model to a more paper-style symmetric formulation:

- shared amplitude parameter `A`
- shared saturation parameter `alpha`
- thresholds `h1` and `h2`

The current code:
- defines `rashevsky_paper_rhs(...)`
- defines `simulate_rashevsky_paper(...)`
- defines `plot_rashevsky_paper_phase_portrait(...)`
- plots explicit nullcline curves
- launches many trajectories from the boundary of the square
- highlights one near-threshold trajectory

### What students currently have to do

Students are currently asked to reproduce a paper-style phase-plane plot with:
- explicit nullclines
- boundary-started trajectories
- one highlighted near-threshold trajectory

In practice, this is a fairly large coding task because it combines:
- a new right-hand side
- simulation
- nullcline plotting
- trajectory plotting
- visual styling

### Main learning goal

The real learning goal is historical and conceptual:
- to connect the notebook to Rashevsky's original graphical method
- to show how phase portraits and nullclines encode qualitative dynamics
- to see that threshold structure and geometry can explain persistence versus decay

The exercise is more about reading and reproducing the paper's style of reasoning than about writing plotting code.

### Recommendation

Keep, but merge with Exercise 9.

Suggested role in the compressed version:
- provide the paper-style phase portrait code
- include the nullclines directly in the figure
- ask students to interpret the geometry rather than reproduce all the plotting machinery

This section is important, but it should not remain a large standalone coding exercise.

## Exercise 9 — Approximate the nullclines

### Current exercise

Students are asked to approximate the nullclines numerically and plot them.

The current code:
- builds a mesh over the `(e1, e2)` plane
- evaluates the vector field on the grid
- extracts the level sets `de1/dt = 0` and `de2/dt = 0`
- plots the nullcline curves for both the persistent and quiescent regimes

### What students currently have to do

As written, students would need to:
- understand what nullclines are
- evaluate the right-hand side on a grid
- collect the derivative values
- use contour plotting to extract the zero-level sets

### Main learning goal

The main goal is to understand:
- what nullclines represent geometrically
- how their intersections relate to equilibria
- why one regime can support a nonzero stable state and the other cannot

This is primarily a geometry-of-dynamics exercise.

### Recommendation

Merge into Exercise 8.

Suggested role in the compressed version:
- do not keep as a separate exercise
- fold the nullclines into the Rashevsky graphical-analysis section
- ask one or two direct questions about what the nullcline geometry means

The content is important, but a separate exercise is probably unnecessary for the time available.

## Exercise 10 — Compare the excitatory loop with an inhibitory-style variant

### Current exercise

This exercise introduces a new notation and a new system:
- `a` controls the steepness of the saturating term
- `alpha` sets the decay timescale
- `h1`, `h2` are thresholds

The notebook first states the original mutual-excitation version, then defines an inhibitory-style or complementary variant in which the second equation uses `1 - E1`.

The current code:
- defines `excitation_r_style(...)`
- defines `rashevsky_inhibitory_rhs(...)`
- defines `simulate_inhibitory(...)`

### What students currently have to do

Students are currently asked to implement the inhibitory-style variant in the new notation.

That means they must:
- understand the relation between the original mutual-excitation loop and the new complementary coupling
- translate the equation into code
- distinguish the new role of `alpha` from the earlier simplified notation

### Main learning goal

The main goal is to understand how changing the coupling structure changes the dynamics.

More specifically:
- the original loop reinforces itself symmetrically
- the new variant introduces push-pull or opposing behavior
- this changes the qualitative shape of trajectories and equilibria

So the conceptual goal is comparison of mechanisms, not just implementation.

### Recommendation

Keep, but merge with Exercises 11 and 12.

Suggested role in the compressed version:
- provide the inhibitory-style code
- focus on the conceptual comparison between reinforcing and complementary coupling

This is important content, but students probably do not need to implement the full variant from scratch in a short assignment.

## Exercise 11 — Plot the inhibitory-style phase portrait

### Current exercise

Students are asked to plot the phase portrait for the inhibitory-style system.

The current code:
- defines `plot_r_style_inhibitory_phase_portrait(...)`
- draws both nullclines
- launches many trajectories from the boundary of the square
- highlights one special trajectory
- uses `params_inhibitory = {"a": 4.0, "alpha": 2.0, "h1": 0.3, "h2": 0.3}`

### What students currently have to do

As written, students are asked to reproduce the whole figure:
- nullclines
- many trajectories
- one highlighted path

This is structurally very similar to Exercise 8, but for the asymmetric inhibitory-style system.

### Main learning goal

The main goal is to compare geometry:
- how the inhibitory-style phase portrait differs from the earlier symmetric one
- how the new nullclines are shaped
- how trajectories bend and settle in a different way

This is a direct visual comparison exercise.

### Recommendation

Merge into Exercise 10.

Suggested role in the compressed version:
- show the inhibitory-style phase portrait directly
- ask students to compare it to the earlier mutual-excitation phase portrait

The comparison matters; the repeated plotting mechanics do not.

## Exercise 12 — Compare a few values of `alpha`

### Current exercise

Students are asked to reproduce the inhibitory-style phase portrait for several values of `alpha`.

The current code:
- uses `alphas = [0.5, 1.0, 2.0, 4.0]`
- creates one subplot per parameter value
- reuses the same nullclines and trajectory construction
- highlights one trajectory in each panel

After the plot, there is an interpretation prompt asking what changes as the trajectories become more spiral-like.

### What students currently have to do

Students currently would need to:
- loop over several `alpha` values
- generate several phase portraits
- compare them visually
- explain what changes in the approach to equilibrium

### Main learning goal

The main goal is parameter sensitivity in the inhibitory-style system.

Students are supposed to notice:
- that changing `alpha` changes the relaxation behavior
- that some parameter values give a more direct approach to equilibrium
- while others make the trajectories more curved or spiral-like

This is a qualitative comparison exercise rather than a derivation exercise.

### Recommendation

Keep only in reduced form, as part of the merged final exercise.

Suggested role in the compressed version:
- reduce the number of `alpha` values
- possibly show only two representative cases rather than four
- keep one short interpretation question about more direct versus more curved settling

This should survive only if it sharpens the final comparison rather than making the notebook longer.

## Overall pattern in the remaining exercises

From Exercise 7 onward, most of the current notebook is no longer about basic implementation skill.

The dominant learning goals are:
- building phase-plane intuition
- reading nullclines and trajectories geometrically
- connecting numerical plots to Rashevsky's graphical reasoning
- comparing mutual excitation with an inhibitory-style variant
- seeing how parameter changes alter qualitative dynamics

So the remaining exercises mostly test:
- interpretation
- comparison
- geometric reasoning

rather than raw coding ability.

## Final recommendation

If the assignment needs to fit comfortably into 2 hours, the cleanest structure is:

1. Exercise 7: Phase plane of the two regimes
2. Exercise 8: Rashevsky-style nullclines and phase portrait
3. Exercise 9: Compare mutual excitation with the inhibitory-style variant

That keeps the essential conceptual arc:
- time-series to phase-plane reasoning
- geometry and nullclines
- comparison of two dynamical mechanisms

while removing repeated plotting work that is not central to the learning goals.
