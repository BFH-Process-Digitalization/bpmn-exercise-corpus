# T1-B2 Wareneingang im Verteilzentrum

Thema 1: Aktivitäten, Grundlagen | Zeit: 10 Minuten, Kernaufgabe

## Aufgabe

Im Verteilzentrum eines Detailhändlers treffen täglich Lieferungen ein. Sobald ein Lastwagen an der Rampe steht, prüft ein Lagermitarbeiter den Lieferschein. Danach entlädt er die Paletten und kontrolliert die Ware stichprobenweise. Anschliessend bucht er den Wareneingang im Lagerverwaltungssystem und lagert die Ware ein. Der Ablauf endet, wenn die Ware eingelagert ist. Modellieren Sie den Ablauf.

## Lernziel

Einen linearen Ablauf vom auslösenden Ereignis bis zum Ergebnis modellieren.

Elemente: task, sequence flow, start and end event

## Musterlösung

![Musterlösung](solution.de.svg)

BPMN: [solution.de.bpmn](solution.de.bpmn)

## Typische Fehler

- Startereignis als Aktivität ("Lastwagen kommt an") statt als Zustand benannt.
- Zwei Tätigkeiten in einer Aktivität zusammengefasst ("Paletten entladen und kontrollieren").
- Reihenfolge von Buchen und Einlagern vertauscht.

---
Lizenz: CC BY 4.0
