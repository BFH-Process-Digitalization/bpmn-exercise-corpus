# Open BPMN exercise corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24315290.svg)](https://doi.org/10.5281/zenodo.24315290)

36 BPMN 2.0 exercises in German and English, with sample solutions and an entry assessment. Six topics, each with
three Basic and three Advanced exercises. Developed for the BPMN Tutor at Bern University of Applied Sciences (BFH).

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

## Structure

```
exercises/T<topic>-<slot>/   exercise.yaml, exercise.de.md / .en.md, solution.de.bpmn / .en.bpmn, solution.de.svg / .en.svg
assessment/                  entry assessment: multiple-choice items, modelling task, levelling rule
booklet/                     exercises-de.pdf, exercises-en.pdf
index.csv                    one row per exercise
tools/                       check.py, render_svg.py, build_release.py
GUIDELINES.md                modelling guideline for the sample solutions
```

`exercise.yaml` is the source; the other files are generated from it:

```
python tools/check.py
python tools/render_svg.py
python tools/build_release.py --pdf
```

## Licence

Content CC BY 4.0, tools MIT (`LICENSE`).

## Citation

Maier, M., & Tekle Hailu, S. (2026). *Open BPMN Exercise Corpus: 36 BPMN 2.0 exercises with sample solutions and an
entry assessment (German and English)* (Version 1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.24315290
