# Modelling guideline for sample solutions

Every sample solution in this corpus follows these rules. They combine the Seven Process Modeling
Guidelines (7PMG, Mendling, Reijers and van der Aalst 2010), the style rules of Bruce Silver's
*BPMN Method and Style*, and the Swiss standard eCH-0158 *BPMN-Modellierungskonventionen für die
öffentliche Verwaltung* (V1.0, 2014). Rules marked **(check)** are tested by `tools/check.py`.

## Structure

| No. | Rule | Source |
|---|---|---|
| G1 | Use as few elements as possible; only the elements of the exercise's topic and earlier topics. | 7PMG 1 |
| G2 | Exactly one start event per process level; at least one end event; every element lies on a path from start to end; no dead ends. **(check)** | 7PMG 2, Silver |
| G3 | Model left to right; avoid backward flows and crossings; all shapes of one type have the same size; no colours. | eCH-0158 3.3 |
| G4 | Activities and events have one incoming and one outgoing sequence flow; splits and joins use explicit gateways. A gateway either splits or joins. Every split is closed by a join of the same type, unless the paths end in separate end events. Exceptions: conditional flows with a default flow out of an activity (topic 2 Advanced), compensation activities, event subprocesses and the content of ad-hoc subprocesses have no normal sequence flow. **(check)** | 7PMG 3, 4, Silver |
| G5 | One end event per distinct result; do not merge paths that end differently. | Silver |
| G6 | Expanded pools for the own process, collapsed pools for external partners; message flow only between pools. Pools from topic 4 on, or earlier when message flow is needed. | eCH-0158 4.3, 4.9 |

## Labels

| No. | Rule | Source |
|---|---|---|
| L1 | Activities: object + verb in the infinitive (DE "Rechnung erstellen"), verb + object (EN "Create invoice"). **(check, DE)** | 7PMG 6, eCH-0158 4.6 |
| L2 | Start and end events: a state, as noun + participle (DE "Lieferung eingetroffen", EN "Delivery arrived"). End events name the result. The start event of a subprocess is not labelled. **(check)** | eCH-0158 4.5, Silver |
| L3 | Timer events: the time rule ("24 Stunden", "Alle 6 Monate"). | eCH-0158 4.5 |
| L4 | XOR and OR splits: a question ending in "?"; outgoing flows labelled with the answer ("ja"/"nein", "yes"/"no"). Joins, AND and event-based gateways are not labelled. Other sequence flows are only labelled when they are conditional or default flows. **(check)** | eCH-0158 4.7, 4.8, 7PMG 6 |
| L5 | Lanes: role in the singular; pools: organisation or partner. | eCH-0158 4.3, 4.4 |
| L6 | One term per thing, no abbreviations, no manual line breaks; Swiss spelling (ss, not sharp s). **(check: ss, no dashes)** | eCH-0158 3.2 |
| L7 | German and English solutions have the same elements and IDs; only the labels differ. | own rule |

## What `tools/check.py` cannot check

Whether the model matches the text, whether labels are good business language, the layout rules in G3 and
whether the topic's elements were used correctly. These are part of the review (`REVIEW.md`).
