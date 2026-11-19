# Exams

Two exams, Basic and Advanced, for testing BPMN modelling skills after the exercises. Each exam has four questions, and
each question exists in five equivalent variants (v1 to v5) that test the same constructs for the same points with a
different case. An exam is put together by drawing one variant per question. Version A uses variant 1 of every question,
version B variant 2, and so on, but variants can also be mixed. All texts, models and solutions are in German and English.

## Blueprint

Both exams: 60 minutes, 40 points.

| Question | Type | Points | Minutes | Basic | Advanced |
|---|---|---|---|---|---|
| Q1 | 8 multiple-choice items, 1 point each | 8 | 8 | labels, XOR and AND, joins, timer and message events, pool and lane, data, error boundary event | loop and multi-instance, OR, event-based gateway, interrupting and non-interrupting, message flow, signal and conditional, error and escalation, compensation and transaction |
| Q2 | find and fix four errors in a given model | 8 | 12 | noun label, unlabelled XOR, AND split closed by XOR, missing end event | loop instead of multi-instance, AND join after OR split, interrupting instead of non-interrupting timer, task after event-based gateway |
| Q3 | modelling task | 12 | 20 | XOR and AND split and join, intermediate timer or message event | own pool and collapsed partner pool, message start, four message flows, event-based gateway with message and timer |
| Q4 | modelling task | 12 | 20 | one pool with three lanes, XOR, data object with state, data store | expanded subprocess with error end event, error boundary event, non-interrupting timer boundary event |

Q1 has eight slots with five items each. For an exam, one item is drawn per slot (`slot`, `variant` in `items.yaml`).

## Scoring

Q2: per error 1 point for finding and naming it and 1 point for the correct fix. Q3 and Q4: rubric in each
`question.yaml`. Points can be converted to a grade with the linear scale grade = 1 + 5 × points / 40 (4.0 at 24 points).

## Variants

Basic

| Question | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| Q2 | [Return of a construction machine](basic/Q2/v1/question.en.md) (machinery) | [Planning a home care order](basic/Q2/v2/question.en.md) (health) | [Regrinding a cutting tool](basic/Q2/v3/question.en.md) (production) | [Handling an online return](basic/Q2/v4/question.en.md) (supply chain) | [Resident parking permit](basic/Q2/v5/question.en.md) (public administration) |
| Q3 | [Quoting a lift modernisation](basic/Q3/v1/question.en.md) (machinery) | [Releasing a yoghurt batch](basic/Q3/v2/question.en.md) (production) | [Clearing an import container](basic/Q3/v3/question.en.md) (supply chain) | [Hotel group booking](basic/Q3/v4/question.en.md) (services) | [Radiology examination](basic/Q3/v5/question.en.md) (health) |
| Q4 | [Engineering change](basic/Q4/v1/question.en.md) (production) | [Admission to a day clinic](basic/Q4/v2/question.en.md) (health) | [New client at an accounting firm](basic/Q4/v3/question.en.md) (services) | [Damaged pallet](basic/Q4/v4/question.en.md) (supply chain) | [Event permit](basic/Q4/v5/question.en.md) (public administration) |

Advanced

| Question | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| Q2 | [Commissioning a filling line](advanced/Q2/v1/question.en.md) (machinery) | [Procuring school furniture](advanced/Q2/v2/question.en.md) (public administration) | [Refrigerated transport of medicines](advanced/Q2/v3/question.en.md) (supply chain) | [Hospital discharge](advanced/Q2/v4/question.en.md) (health) | [Rolling out laptops for a client](advanced/Q2/v5/question.en.md) (services) |
| Q3 | [Specialist translation](advanced/Q3/v1/question.en.md) (services) | [Laboratory analysis for a medical practice](advanced/Q3/v2/question.en.md) (health) | [Pick-up from a shipper](advanced/Q3/v3/question.en.md) (supply chain) | [Tax assessment with a query](advanced/Q3/v4/question.en.md) (public administration) | [Fault on a machine tool](advanced/Q3/v5/question.en.md) (machinery) |
| Q4 | [Manufacturing a special part](advanced/Q4/v1/question.en.md) (production) | [Preparing an infusion in a hospital pharmacy](advanced/Q4/v2/question.en.md) (health) | [Picking an order](advanced/Q4/v3/question.en.md) (supply chain) | [Data migration](advanced/Q4/v4/question.en.md) (services) | [Overhauling a gearbox](advanced/Q4/v5/question.en.md) (machinery) |

## Files

```
<level>/Q1/items.yaml                  multiple-choice items with key
<level>/Q<n>/v<k>/question.yaml        task text, points, rubric or errors (source)
<level>/Q<n>/v<k>/question.de.md/.en.md
<level>/Q<n>/v<k>/solution.de.bpmn/.svg, solution.en.bpmn/.svg
<level>/Q2/v<k>/model.de.bpmn/.svg     model with four errors, handed out with the question
sheets/<level>-<A..E>-exam.<lang>.pdf, sheets/<level>-<A..E>-solution.<lang>.pdf
```

The sheets are generated with `python tools/build_exams.py --pdf`. Since the solutions are public, the exams are
suitable for practice and for supervised tests where students do not have access to the repository during the test.
