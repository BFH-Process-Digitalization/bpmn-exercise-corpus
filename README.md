# Open BPMN exercise corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24315290.svg)](https://doi.org/10.5281/zenodo.24315290)

36 BPMN 2.0 exercises in German and English, with sample solutions and an entry assessment. Six topics, each with
three Basic and three Advanced exercises. Developed for the BPMN Tutor at Bern University of Applied Sciences (BFH).

## Exercises

| ID | Topic | Level | Industry | Case |
|---|---|---|---|---|
| [T1-B](exercises/T1-B/) | 1 Activities | Basic (core) | Services | Tyre change at a garage |
| [T1-B2](exercises/T1-B2/) | 1 Activities | Basic (core) | Supply chain | Goods receipt at a distribution centre |
| [T1-B3](exercises/T1-B3/) | 1 Activities | Basic | Machinery | Maintenance of a CNC milling machine |
| [T1-A](exercises/T1-A/) | 1 Activities | Advanced | Machinery | Calibration order for an industrial scale (task types) |
| [T1-A2](exercises/T1-A2/) | 1 Activities | Advanced | Machinery | Commissioning a filling line (subprocess, call activity) |
| [T1-A3](exercises/T1-A3/) | 1 Activities | Advanced | Health | Launching hearing aids (ad-hoc, loop, multi-instance) |
| [T2-B](exercises/T2-B/) | 2 Gateways | Basic (core) | Services | Service visit to a heat pump (XOR) |
| [T2-B2](exercises/T2-B2/) | 2 Gateways | Basic (core) | Production | Preparing a production order (AND) |
| [T2-B3](exercises/T2-B3/) | 2 Gateways | Basic | Machinery | Shipping a spare part abroad (XOR + AND) |
| [T2-A](exercises/T2-A/) | 2 Gateways | Advanced | Services | Fixing defects after inspection (OR, default flow) |
| [T2-A2](exercises/T2-A2/) | 2 Gateways | Advanced | Machinery | Reacting to a quote (event-based gateway) |
| [T2-A3](exercises/T2-A3/) | 2 Gateways | Advanced | Supply chain | Cold chain shipment (AND sync, conditional flow) |
| [T3-B](exercises/T3-B/) | 3 Events | Basic (core) | Services | Monthly payroll (timer start, message end) |
| [T3-B2](exercises/T3-B2/) | 3 Events | Basic (core) | Services | Fixing a lift breakdown (message throw and catch) |
| [T3-B3](exercises/T3-B3/) | 3 Events | Basic | Production | Precast concrete elements (timer intermediate) |
| [T3-A](exercises/T3-A/) | 3 Events | Advanced | Machinery | Cable car breakdown (interrupting and non-interrupting timers) |
| [T3-A2](exercises/T3-A2/) | 3 Events | Advanced | Production | Testing a food batch (signal, terminate) |
| [T3-A3](exercises/T3-A3/) | 3 Events | Advanced | Machinery | Train overhaul (conditional event, event subprocess) |
| [T4-B](exercises/T4-B/) | 4 Pools and lanes | Basic (core) | Health | Outpatient treatment at a hospital |
| [T4-B2](exercises/T4-B2/) | 4 Pools and lanes | Basic (core) | Machinery | Answering a customer enquiry |
| [T4-B3](exercises/T4-B3/) | 4 Pools and lanes | Basic | Public administration | Building application in a municipality |
| [T4-A](exercises/T4-A/) | 4 Pools and lanes | Advanced | Production | Ordering a ventilation unit (two expanded pools) |
| [T4-A2](exercises/T4-A2/) | 4 Pools and lanes | Advanced | Machinery | Requesting components (multi-instance pool) |
| [T4-A3](exercises/T4-A3/) | 4 Pools and lanes | Advanced | Supply chain | Exporting sea freight (lanes and two partners) |
| [T5-B](exercises/T5-B/) | 5 Data | Basic (core) | Production | Issuing a tool |
| [T5-B2](exercises/T5-B2/) | 5 Data | Basic (core) | Production | Inspecting a production batch |
| [T5-B3](exercises/T5-B3/) | 5 Data | Basic | Public administration | Incident at an IT service desk, regional administration |
| [T5-A](exercises/T5-A/) | 5 Data | Advanced | Production | Annual stocktaking (data input and output, collections) |
| [T5-A2](exercises/T5-A2/) | 5 Data | Advanced | Health | Complaint about a medical device (data across a subprocess) |
| [T5-A3](exercises/T5-A3/) | 5 Data | Advanced | Machinery | Calibrating instruments (multi-instance subprocess over a list) |
| [T6-B](exercises/T6-B/) | 6 Exceptions | Basic (core) | Health | Analysing a laboratory sample |
| [T6-B2](exercises/T6-B2/) | 6 Exceptions | Basic (core) | Machinery | Calibrating a measuring machine |
| [T6-B3](exercises/T6-B3/) | 6 Exceptions | Basic | Supply chain | Calling off drive units |
| [T6-A](exercises/T6-A/) | 6 Exceptions | Advanced | Production | Special valve (escalation vs error) |
| [T6-A2](exercises/T6-A2/) | 6 Exceptions | Advanced | Production | Cancelled production order (compensation) |
| [T6-A3](exercises/T6-A3/) | 6 Exceptions | Advanced | Supply chain | Heavy transport (transaction, cancel) |

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
