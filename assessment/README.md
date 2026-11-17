# Entry assessment

Places a new student at Basic or Advanced per topic. It takes about 20 minutes and has three parts:

| Part | Content | Time | Source |
|---|---|---|---|
| A Self-rating | Prior BPMN experience, tools used, familiarity per topic (1 to 5) | 3 min | survey |
| B Knowledge items | 14 multiple-choice items, one Basic and one Advanced item per topic | 7 min | `items.yaml` |
| C Modelling task | "Veloservice / bicycle service" (start, tasks, XOR with an empty path, AND) | 10 to 15 min | `PRE/` |

## Scoring

- Part B: 1 point per correct item, no penalty for wrong answers.
- Part C: 8 points, scored blind against `PRE/solution.*.bpmn`:

| Criterion | Points |
|---|---|
| Start and end event, end event named as a state | 1 |
| Activities labelled object + verb | 1 |
| XOR split with question and labelled flows, including the empty "nein/no" path | 2 |
| XOR merge before the AND split | 1 |
| AND split and AND join around cleaning and invoice | 2 |
| Correct order of all steps | 1 |

## Levelling rule (version 0.1, to be calibrated)

Per topic t, with B_basic(t) and B_adv(t) the two items and S(t) the self-rating:

- **Advanced** if both items of the topic are correct and S(t) >= 3.
- **Basic** otherwise.
- For topic 2, Part C must also reach at least 6 of 8 points for Advanced.

Advanced on a topic means the student may start with the Advanced exercises of that topic; the Basic ones stay
available.

## Rollout

1. **First cohort:** parts A to C run as the pre-test; everyone starts with Basic. No levelling yet,
   only data collection.
2. **Calibration:** item difficulty (share correct, target 0.3 to 0.85) and discrimination
   (item-rest correlation, target > 0.2) per item; compare the recommendation with the exercise results and
   the final test; replace weak items; set the cut-offs.
3. **Next cohort:** levelling switched on.

## Notes

- Items are text-only so they work in the survey page without images.
- The correct option position varies (`key`, 0-based); German and English have the same order.
- Parallel forms for a final test and a retention test follow the same blueprint with other cases.
