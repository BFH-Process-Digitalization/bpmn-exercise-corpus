# Review checklist

Each exercise needs a second person's review before it is released. Record the reviewer and date
under `review:` in `exercise.yaml` and note it in the pull request.

**Text**
- [ ] One reading only: every activity, decision and wait in the solution is stated in the text, and nothing else is.
- [ ] Order words are unambiguous ("danach", "gleichzeitig", "andernfalls"; "then", "at the same time", "otherwise").
- [ ] Solvable in the time limit (Basic 10 min, Advanced 15 min) by a student who knows the earlier topics.
- [ ] German and English say the same; Swiss spelling (ss); no em dashes.
- [ ] Setting (industry, no place names) is plausible and contains no real company names, people or legal claims beyond the case.
- [ ] The case is not taken from another corpus or textbook (see `README.md`, comparison).

**Sample solution**
- [ ] `python tools/check.py` passes.
- [ ] Opens in bpmn-js (for example demo.bpmn.io) without warnings; layout is readable (left to right, no crossings, labels not covered).
- [ ] Follows every rule in `GUIDELINES.md`.
- [ ] Uses only the elements of the topic and earlier topics.
- [ ] The expected mistakes in `exercise.yaml` are real alternatives a student would draw, and each one is wrong.
