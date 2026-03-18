# TODO

## Remaining notebook polish

- Remove the broken citation token from the markdown in the "How the model works" section if it is still present.
- Remove the duplicate import cell so the notebook has a cleaner execution flow.
- Decide whether the notebook should remain a guided worked example or be turned into a more incomplete student worksheet.

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
