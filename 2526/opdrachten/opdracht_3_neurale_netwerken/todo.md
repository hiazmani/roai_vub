# TODO

## Notebook review status

- Reviewed file: `rashevsky_conditioning_student_notebook.ipynb`
- Current role: this notebook is effectively the solution key / worked example, not a student worksheet.
- Main design decision: keep this as the clean solution version, then derive the student version by deleting or partially deleting function implementations and plotting code.

## Issues found

- Fixed: Exercise 2 previously described a self-driven system in the pseudocode (`AE1`, `AE2`) while the code correctly implemented cross-coupling (`AE2`, `AE1`). The markdown has now been corrected to match the recurrent loop.
- Release hygiene: the notebook save state is not fully clean. Some code cells have `execution_count: null` while later cells have outputs, and execution counts are not monotone. Before distributing a final solution notebook, rerun top-to-bottom and save once.
- Environment check: the notebook was not executed end-to-end in the current shell because the local environment used for review did not have `matplotlib` installed. The project metadata does declare the needed dependencies, but the notebook should still be verified in the intended student/teaching environment.

## Content assessment

- The pedagogical sequence is strong: historical context, nonlinearity, recurrent loop, initial-condition sensitivity, phase plane, paper-style nullclines, then the inhibitory/complementary variant.
- The notebook is internally self-contained and no longer appears to rely on hidden R support code.
- The previously noted broken citation token does not appear to be present anymore.
- The previously noted duplicate import cell does not appear to be present anymore.

## Optional teaching improvements

- Add a short closing markdown note that summarizes the difference between:
  - the original mutual-excitation loop
  - the inhibitory-style `1 - equation` variant
- Add one short interpretation prompt after the final `alpha` comparison asking students what changes as spiral-like settling becomes more visible.
- Consider adding a short `README.md` in the assignment folder with run instructions and a one-paragraph overview for students.

## Current status

- Exercise numbering has been fixed by adding Exercise 8.
- The notebook now uses a simplified symmetric parameterization in the core sections.
- The paper-style phase portrait from the original Rashevsky model has been added.
- The final extension now uses the PI-style inhibitory/complementary second equation.
- The final plots now match the style of the R figures much more closely:
  - nullclines
  - boundary-started trajectories
  - highlighted special trajectory
- The notebook has been kept self-contained for students and no longer refers to hidden R support code.
