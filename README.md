# Open BPMN exercise corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24315290.svg)](https://doi.org/10.5281/zenodo.24315290)

Exercises for learning BPMN 2.0, each with a task text in German and English, a sample solution and the
mistakes students typically make. Developed for the BPMN Tutor at Bern University of Applied Sciences (BFH) and published under CC BY 4.0 (`LICENSE`).

- Cases come from services, machinery, production, supply chain, health and public administration; no place names.
- Texts and solutions are written by the team, not generated and not copied from textbooks or other corpora.
- Every solution follows `GUIDELINES.md` (7PMG, Silver's Method and Style, eCH-0158) and passes
  `tools/check.py`. Each exercise is reviewed by a second person (`REVIEW.md`).

## Structure

```
exercises/T<topic>-<slot>/   exercise.yaml (source), exercise.de.md / exercise.en.md (readable),
                     solution.de.bpmn / solution.en.bpmn, solution.de.svg / solution.en.svg
assessment/                  entry assessment: items.yaml, PRE/ (modelling task), README.md
booklet/                     exercises-de.pdf, exercises-en.pdf (task page, then solution page)
index.csv                    one row per exercise
tools/                       check.py, render_svg.py, build_release.py
GUIDELINES.md  REVIEW.md  LICENSE  CITATION.cff  .zenodo.json
```

`exercise.yaml` is the source. The Markdown pages, SVGs, CSV index and booklets are generated from it:

```
python tools/check.py
python tools/render_svg.py      # needs playwright
python tools/build_release.py --pdf
```

Slots: `B`, `B2`, `B3` (Basic, 10 min) and `A`, `A2`, `A3`
(Advanced, 15 min). The core set is `B` and `B2` of topics 1 to 6.

`exercise.yaml` fields: `id`, `topic`, `level`, `slot`, `core`, `sector`, `setting`, `time_limit_minutes`,
`elements`, `skills`, `title`, `learning_goal`, `text` (each with `de` and `en`), `expected_mistakes`, `solution`,
`licence`, `status` (draft, reviewed, released), `authors`, `review`.

## Exercises

| Topic | Basic 1 (core) | Basic 2 (core) | Basic 3 |
|---|---|---|---|
| 1 Activities | Tyre change at a garage | Goods receipt at a distribution centre | Maintenance of a CNC milling machine |
| 2 Gateways | Service visit to a heat pump (XOR) | Preparing a production order (AND) | Shipping a spare part abroad (XOR + AND) |
| 3 Events | Monthly payroll (timer start, message end) | Fixing a lift breakdown (message throw and catch) | Precast concrete elements (timer intermediate) |
| 4 Pools and lanes | Outpatient treatment at a hospital | Answering a customer enquiry | Building application in a municipality |
| 5 Data | Issuing a tool | Inspecting a production batch | Incident at an IT service desk, regional administration |
| 6 Exceptions | Analysing a laboratory sample | Calibrating a measuring machine | Calling off drive units |

| Topic | Advanced 1 | Advanced 2 | Advanced 3 |
|---|---|---|---|
| 1 Activities | Calibration order for an industrial scale (task types) | Commissioning a filling line (subprocess, call activity) | Launching hearing aids (ad-hoc, loop, multi-instance) |
| 2 Gateways | Fixing defects after inspection (OR, default flow) | Reacting to a quote (event-based gateway) | Cold chain shipment (AND sync, conditional flow) |
| 3 Events | Cable car breakdown (interrupting and non-interrupting timers) | Testing a food batch (signal, terminate) | Train overhaul (conditional event, event subprocess) |
| 4 Collaboration | Ordering a ventilation unit (two expanded pools) | Requesting components (multi-instance pool) | Exporting sea freight (lanes and two partners) |
| 5 Data | Annual stocktaking (data input and output, collections) | Complaint about a medical device (data across a subprocess) | Calibrating instruments (multi-instance subprocess over a list) |
| 6 Exceptions | Special valve (escalation vs error) | Cancelled production order (compensation) | Heavy transport (transaction, cancel) |

Topic 7 (conversation and choreography) is not included: the BPMN Tutor's web editor (bpmn-js) cannot draw these diagrams.

## How this differs from existing corpora

We use other corpora to compare, not to copy:

| Corpus | Their cases | Our choice |
|---|---|---|
| Camunda bpmn-for-research | Warenversand (shipping with carrier choice), Regressnahme, Schufascoring, Selbstbedienungsrestaurant | No shipping-mode, credit-scoring or restaurant cases; our dispatch case (T2-B3) decides on stock vs. production, not on the carrier |
| hdBPMN | 11 general exercises for hand-drawn models | Each exercise targets one topic and level, with expected mistakes |
| Friedrich / PET / Mangler | Process descriptions from many domains, mostly English, no levels | German and English, one learning goal per exercise |
| Textbooks (Dumas et al., Freund and Rücker, Silver) | Order-to-cash, insurance claim, loan application, pizza ordering | None of these cases; services, industry and public administration instead |

What we add: graded topics and levels, two languages with identical solutions, expected
mistakes per exercise, and an automated guideline check.

## Check

```
python tools/check.py
```

Prints every rule violation and exits with 1 if there is one.

## Status

Released (`status: released`). All 36 exercises and the entry assessment pass the check, load without warnings in
bpmn-moddle and render in bpmn-js. The second-person review (`REVIEW.md`) is still open and is recorded under
`review:` in each `exercise.yaml` when done.

## Citation

Maier, M., & Tekle Hailu, S. (2026). *Open BPMN Exercise Corpus: 36 BPMN 2.0 exercises with sample solutions and an
entry assessment (German and English)* (Version 1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.24315290

Machine-readable citation metadata is in `CITATION.cff`.
