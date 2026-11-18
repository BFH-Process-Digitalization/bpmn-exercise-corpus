# Open BPMN exercise corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24315290.svg)](https://doi.org/10.5281/zenodo.24315290)

36 BPMN 2.0 exercises in German and English, with sample solutions and an entry assessment. Six topics, each with
three Basic and three Advanced exercises. Developed for the BPMN Tutor at Bern University of Applied Sciences (BFH).

## Exercises

Industry: ⚙️ machinery, 🏭 production, 🚚 supply chain, 🛠️ services, 🏥 health, 🏛️ public administration. The BPMN icons show the main elements of each solution (hover for the name).

### Basic (10 min)

| Topic | Basic 1 (core) | Basic 2 (core) | Basic 3 |
|---|---|---|---|
| 1 Activities | 🛠️ [Tyre change at a garage](exercises/T1-B/)<br><img src="icons/task.svg" width="20" alt="Task" title="Task"> | 🚚 [Goods receipt at a distribution centre](exercises/T1-B2/)<br><img src="icons/task.svg" width="20" alt="Task" title="Task"> | ⚙️ [Maintenance of a CNC milling machine](exercises/T1-B3/)<br><img src="icons/task.svg" width="20" alt="Task" title="Task"> |
| 2 Gateways | 🛠️ [Service visit to a heat pump](exercises/T2-B/)<br><img src="icons/xor.svg" width="20" alt="Exclusive gateway (XOR)" title="Exclusive gateway (XOR)"> | 🏭 [Preparing a production order](exercises/T2-B2/)<br><img src="icons/and.svg" width="20" alt="Parallel gateway (AND)" title="Parallel gateway (AND)"> | ⚙️ [Shipping a spare part abroad](exercises/T2-B3/)<br><img src="icons/xor.svg" width="20" alt="Exclusive gateway (XOR)" title="Exclusive gateway (XOR)"> <img src="icons/and.svg" width="20" alt="Parallel gateway (AND)" title="Parallel gateway (AND)"> |
| 3 Events | 🛠️ [Monthly payroll](exercises/T3-B/)<br><img src="icons/timer-start.svg" width="20" alt="Timer start event" title="Timer start event"> <img src="icons/message-end.svg" width="20" alt="Message end event" title="Message end event"> | 🛠️ [Fixing a lift breakdown](exercises/T3-B2/)<br><img src="icons/message-throw.svg" width="20" alt="Message throw event" title="Message throw event"> <img src="icons/message-catch.svg" width="20" alt="Message catch event" title="Message catch event"> | 🏭 [Precast concrete elements](exercises/T3-B3/)<br><img src="icons/timer-catch.svg" width="20" alt="Timer intermediate event" title="Timer intermediate event"> |
| 4 Pools and lanes | 🏥 [Outpatient treatment at a hospital](exercises/T4-B/)<br><img src="icons/pool-lanes.svg" width="20" alt="Pool with lanes" title="Pool with lanes"> | ⚙️ [Answering a customer enquiry](exercises/T4-B2/)<br><img src="icons/pool-lanes.svg" width="20" alt="Pool with lanes" title="Pool with lanes"> <img src="icons/xor.svg" width="20" alt="Exclusive gateway (XOR)" title="Exclusive gateway (XOR)"> | 🏛️ [Building application in a municipality](exercises/T4-B3/)<br><img src="icons/pool-lanes.svg" width="20" alt="Pool with lanes" title="Pool with lanes"> <img src="icons/timer-catch.svg" width="20" alt="Timer intermediate event" title="Timer intermediate event"> |
| 5 Data | 🏭 [Issuing a tool](exercises/T5-B/)<br><img src="icons/data-object.svg" width="20" alt="Data object" title="Data object"> <img src="icons/data-store.svg" width="20" alt="Data store" title="Data store"> | 🏭 [Inspecting a production batch](exercises/T5-B2/)<br><img src="icons/data-object.svg" width="20" alt="Data object" title="Data object"> <img src="icons/data-store.svg" width="20" alt="Data store" title="Data store"> | 🏛️ [Incident at an IT service desk](exercises/T5-B3/)<br><img src="icons/data-object.svg" width="20" alt="Data object" title="Data object"> <img src="icons/data-store.svg" width="20" alt="Data store" title="Data store"> <img src="icons/annotation.svg" width="20" alt="Text annotation" title="Text annotation"> |
| 6 Exceptions | 🏥 [Analysing a laboratory sample](exercises/T6-B/)<br><img src="icons/error-end.svg" width="20" alt="Error end event" title="Error end event"> <img src="icons/error-boundary.svg" width="20" alt="Error boundary event" title="Error boundary event"> | ⚙️ [Calibrating a measuring machine](exercises/T6-B2/)<br><img src="icons/error-end.svg" width="20" alt="Error end event" title="Error end event"> <img src="icons/error-boundary.svg" width="20" alt="Error boundary event" title="Error boundary event"> | 🚚 [Calling off drive units](exercises/T6-B3/)<br><img src="icons/error-end.svg" width="20" alt="Error end event" title="Error end event"> <img src="icons/error-boundary.svg" width="20" alt="Error boundary event" title="Error boundary event"> |

### Advanced (15 min)

| Topic | Advanced 1 | Advanced 2 | Advanced 3 |
|---|---|---|---|
| 1 Activities | ⚙️ [Calibration order for an industrial scale](exercises/T1-A/)<br><img src="icons/user-task.svg" width="20" alt="User task" title="User task"> <img src="icons/service-task.svg" width="20" alt="Service task" title="Service task"> <img src="icons/script-task.svg" width="20" alt="Script task" title="Script task"> | ⚙️ [Commissioning a filling line](exercises/T1-A2/)<br><img src="icons/subprocess.svg" width="20" alt="Subprocess" title="Subprocess"> <img src="icons/call-activity.svg" width="20" alt="Call activity" title="Call activity"> | 🏥 [Launching hearing aids](exercises/T1-A3/)<br><img src="icons/adhoc.svg" width="20" alt="Ad-hoc subprocess" title="Ad-hoc subprocess"> <img src="icons/loop.svg" width="20" alt="Loop" title="Loop"> <img src="icons/mi-parallel.svg" width="20" alt="Multi-instance" title="Multi-instance"> |
| 2 Gateways | 🛠️ [Fixing defects after inspection](exercises/T2-A/)<br><img src="icons/or.svg" width="20" alt="Inclusive gateway (OR)" title="Inclusive gateway (OR)"> | ⚙️ [Reacting to a quote](exercises/T2-A2/)<br><img src="icons/event-based.svg" width="20" alt="Event-based gateway" title="Event-based gateway"> <img src="icons/message-catch.svg" width="20" alt="Message catch event" title="Message catch event"> <img src="icons/timer-catch.svg" width="20" alt="Timer intermediate event" title="Timer intermediate event"> | 🚚 [Cold chain shipment](exercises/T2-A3/)<br><img src="icons/and.svg" width="20" alt="Parallel gateway (AND)" title="Parallel gateway (AND)"> |
| 3 Events | ⚙️ [Cable car breakdown](exercises/T3-A/)<br><img src="icons/timer-boundary.svg" width="20" alt="Interrupting timer boundary event" title="Interrupting timer boundary event"> <img src="icons/timer-boundary-nonint.svg" width="20" alt="Non-interrupting timer boundary event" title="Non-interrupting timer boundary event"> | 🏭 [Testing a food batch](exercises/T3-A2/)<br><img src="icons/signal-throw.svg" width="20" alt="Signal throw event" title="Signal throw event"> <img src="icons/terminate-end.svg" width="20" alt="Terminate end event" title="Terminate end event"> | ⚙️ [Train overhaul](exercises/T3-A3/)<br><img src="icons/conditional-catch.svg" width="20" alt="Conditional event" title="Conditional event"> <img src="icons/event-subprocess.svg" width="20" alt="Event subprocess" title="Event subprocess"> |
| 4 Pools and lanes | 🏭 [Ordering a ventilation unit](exercises/T4-A/)<br><img src="icons/pool.svg" width="20" alt="Pool" title="Pool"> <img src="icons/message-flow.svg" width="20" alt="Message flow" title="Message flow"> | ⚙️ [Requesting components](exercises/T4-A2/)<br><img src="icons/mi-pool.svg" width="20" alt="Multi-instance pool" title="Multi-instance pool"> <img src="icons/message-flow.svg" width="20" alt="Message flow" title="Message flow"> | 🚚 [Exporting sea freight](exercises/T4-A3/)<br><img src="icons/pool-lanes.svg" width="20" alt="Pool with lanes" title="Pool with lanes"> <img src="icons/message-flow.svg" width="20" alt="Message flow" title="Message flow"> |
| 5 Data | 🏭 [Annual stocktaking](exercises/T5-A/)<br><img src="icons/data-input.svg" width="20" alt="Data input" title="Data input"> <img src="icons/data-output.svg" width="20" alt="Data output" title="Data output"> <img src="icons/data-store.svg" width="20" alt="Data store" title="Data store"> | 🏥 [Complaint about a medical device](exercises/T5-A2/)<br><img src="icons/data-object.svg" width="20" alt="Data object" title="Data object"> <img src="icons/subprocess.svg" width="20" alt="Subprocess" title="Subprocess"> | ⚙️ [Calibrating instruments](exercises/T5-A3/)<br><img src="icons/data-object.svg" width="20" alt="Data object" title="Data object"> <img src="icons/mi-parallel.svg" width="20" alt="Multi-instance" title="Multi-instance"> |
| 6 Exceptions | 🏭 [Special valve](exercises/T6-A/)<br><img src="icons/escalation.svg" width="20" alt="Escalation event" title="Escalation event"> <img src="icons/error-boundary.svg" width="20" alt="Error boundary event" title="Error boundary event"> | 🏭 [Cancelled production order](exercises/T6-A2/)<br><img src="icons/compensation.svg" width="20" alt="Compensation event" title="Compensation event"> | 🚚 [Heavy transport](exercises/T6-A3/)<br><img src="icons/transaction.svg" width="20" alt="Transaction" title="Transaction"> <img src="icons/cancel.svg" width="20" alt="Cancel event" title="Cancel event"> |

## Structure

```
exercises/T<topic>-<slot>/   exercise.yaml, exercise.de.md / .en.md, solution.de.bpmn / .en.bpmn, solution.de.svg / .en.svg
assessment/                  entry assessment: multiple-choice items, modelling task, levelling rule
booklet/                     exercises-de.pdf, exercises-en.pdf
index.csv                    one row per exercise
tools/                       check.py, render_svg.py, build_release.py
icons/                       BPMN icons used in this README
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
