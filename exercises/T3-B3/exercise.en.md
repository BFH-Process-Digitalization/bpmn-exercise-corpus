# T3-B3 Producing precast concrete elements

Topic 3: Events, Basic | Time: 10 minutes

## Task

A precast concrete plant produces staircase elements. As soon as the formwork is ready, an employee pours the concrete. The concrete then has to cure in the formwork for 24 hours. After that the employee strips the formwork and measures the element. The element is then stored in the yard. After 7 days quality assurance releases the element for delivery. The process ends when the element is ready for delivery. Model the process.

## Learning goal

Model waiting times as timer intermediate events labelled with the time rule.

Elements: none, message and timer events (start, intermediate, end), throw vs catch

## Sample solution

![Sample solution](solution.en.svg)

BPMN: [solution.en.bpmn](solution.en.bpmn)

## Typical mistakes

- Waiting time modelled as an activity instead of a timer intermediate event.
- Timer event labelled without the duration.
- Timer start event used instead of a none start event.

---
Licence: CC BY 4.0
