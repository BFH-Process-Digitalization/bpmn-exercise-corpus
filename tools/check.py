"""Check every exercise in exercises/ against the format and the modelling guideline.

Usage: python tools/check.py
Exit code 1 if any exercise fails. Rules refer to GUIDELINES.md.
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "exercises"
B = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
REQUIRED = [
    "id",
    "topic",
    "level",
    "slot",
    "core",
    "sector",
    "setting",
    "time_limit_minutes",
    "elements",
    "skills",
    "title",
    "learning_goal",
    "text",
    "expected_mistakes",
    "solution",
    "licence",
    "status",
]
TASKS = {
    "callActivity",
    "task",
    "userTask",
    "serviceTask",
    "manualTask",
    "sendTask",
    "receiveTask",
    "scriptTask",
    "businessRuleTask",
}
GATEWAYS = {"exclusiveGateway", "parallelGateway", "inclusiveGateway", "eventBasedGateway", "complexGateway"}
SUBS = {"subProcess", "adHocSubProcess", "transaction"}
CONTAINERS = {"process"} | SUBS
BPMNDI = "http://www.omg.org/spec/BPMN/20100524/DI"
EVENTS = {"startEvent", "endEvent", "intermediateCatchEvent", "intermediateThrowEvent", "boundaryEvent"}
FORBIDDEN = {"ß": "use ss (Swiss spelling)", "\u2014": "no em dash", "\u2013": "no en dash"}


def local(el):
    return el.tag.replace(B, "")


def check_model(path: Path, lang: str) -> list[str]:
    errs = []
    root = ET.parse(path).getroot()
    if root.tag != f"{B}definitions":
        return [f"{path.name}: root is not bpmn:definitions"]
    ids = {el.get("id"): el for el in root.iter() if el.get("id")}
    containers = [el for el in root.iter() if local(el) in CONTAINERS]
    for cont in containers:
        adhoc = local(cont) == "adHocSubProcess"
        flows = [el for el in cont if local(el) == "sequenceFlow"]
        nodes = [el for el in cont if local(el) in TASKS | GATEWAYS | EVENTS | SUBS]
        inc = {n.get("id"): [] for n in nodes}
        out = {n.get("id"): [] for n in nodes}
        for f in flows:
            s, t = f.get("sourceRef"), f.get("targetRef")
            if s not in ids or t not in ids:
                errs.append(f"{path.name}: flow {f.get('id')} points to an unknown element")
                continue
            out.setdefault(s, []).append(f)
            inc.setdefault(t, []).append(f)
        starts = [n for n in nodes if local(n) == "startEvent"]
        ends = [n for n in nodes if local(n) == "endEvent"]
        if not adhoc and len(starts) != 1:
            errs.append(f"{path.name}: {cont.get('id')} needs exactly one start event (G2), has {len(starts)}")
        if not adhoc and not ends:
            errs.append(f"{path.name}: {cont.get('id')} has no end event (G2)")
        for n in nodes:
            k, nid, name = local(n), n.get("id"), (n.get("name") or "").strip()
            i, o = len(inc.get(nid, [])), len(out.get(nid, []))
            is_act = k in TASKS | SUBS
            if is_act and not name:
                errs.append(f"{path.name}: activity {nid} has no label (L1)")
            if is_act and name and lang == "de" and not re.search(r"(en|ern|eln)$", name):
                errs.append(f"{path.name}: activity '{name}' does not end with a verb in the infinitive (L1)")
            if adhoc or n.get("isForCompensation") == "true" or n.get("triggeredByEvent") == "true":
                continue
            if k == "boundaryEvent":
                compensate = n.find(f"{B}compensateEventDefinition") is not None
                if i or o != (0 if compensate else 1):
                    errs.append(f"{path.name}: boundary event {nid} has the wrong number of flows")
                continue
            if k == "startEvent" and i:
                errs.append(f"{path.name}: start event {nid} has incoming flow")
            if k == "endEvent" and o:
                errs.append(f"{path.name}: end event {nid} has outgoing flow")
            if k != "startEvent" and i == 0:
                errs.append(f"{path.name}: {nid} is not reachable (no incoming flow)")
            if k != "endEvent" and o == 0:
                errs.append(f"{path.name}: {nid} is a dead end (no outgoing flow, G2)")
            conditional_out = o > 1 and all(
                f.find(f"{B}conditionExpression") is not None or n.get("default") == f.get("id") for f in out[nid]
            )
            if (is_act or k in EVENTS) and (i > 1 or (o > 1 and not (is_act and conditional_out))):
                errs.append(f"{path.name}: {nid} has several in- or outgoing flows; use a gateway (G4)")
            if k == "endEvent" and not name:
                errs.append(f"{path.name}: end event {nid} has no state label (L2)")
            if k == "startEvent" and local(cont) == "process" and not name:
                errs.append(f"{path.name}: start event {nid} has no label (L2)")
            if k in GATEWAYS:
                split, join = o > 1, i > 1
                if split and join:
                    errs.append(f"{path.name}: gateway {nid} splits and joins at once (G4)")
                if not split and not join:
                    errs.append(f"{path.name}: gateway {nid} neither splits nor joins")
                if k in ("exclusiveGateway", "inclusiveGateway") and split:
                    if not name.endswith("?"):
                        errs.append(f"{path.name}: decision {nid} needs a question as label (L4)")
                    if any(not (f.get("name") or "").strip() for f in out[nid]):
                        errs.append(f"{path.name}: outgoing flows of decision {nid} need labels (L4)")
                if (join or k in ("parallelGateway", "eventBasedGateway")) and name:
                    errs.append(f"{path.name}: merging, AND or event-based gateway {nid} must not be labelled (L4)")
        for f in flows:
            src = ids.get(f.get("sourceRef"))
            decision = src is not None and local(src) in ("exclusiveGateway", "inclusiveGateway")
            conditional = f.find(f"{B}conditionExpression") is not None or (
                src is not None and src.get("default") == f.get("id")
            )
            if f.get("name") and not decision and not conditional:
                errs.append(f"{path.name}: flow {f.get('id')} is labelled but does not leave a decision (L4)")
        for kind in ("parallelGateway", "inclusiveGateway"):
            splits = joins = 0
            for n in cont:
                if local(n) == kind:
                    o = sum(1 for f in flows if f.get("sourceRef") == n.get("id"))
                    if o > 1:
                        splits += 1
                    else:
                        joins += 1
            if splits != joins:
                errs.append(f"{path.name}: {splits} {kind} splits but {joins} joins (G4)")
    if root.find(f"{{{BPMNDI}}}BPMNDiagram") is None:
        errs.append(f"{path.name}: no diagram information")
    return errs


def check_text(label: str, text: str) -> list[str]:
    return [f"{label}: contains '{c}' ({why})" for c, why in FORBIDDEN.items() if c in text]


def main() -> int:
    errors = []
    folders = sorted(p for p in ROOT.iterdir() if p.is_dir())
    for d in folders:
        meta_path = d / "exercise.yaml"
        if not meta_path.exists():
            errors.append(f"{d.name}: exercise.yaml missing")
            continue
        raw = meta_path.read_text(encoding="utf-8")
        meta = yaml.safe_load(raw)
        errors += check_text(f"{d.name}/exercise.yaml", raw)
        errors += [f"{d.name}: field '{k}' missing" for k in REQUIRED if k not in meta]
        if meta.get("id") != d.name:
            errors.append(f"{d.name}: id does not match folder name")
        for field in ("title", "learning_goal", "text"):
            for lang in ("de", "en"):
                if not (meta.get(field) or {}).get(lang):
                    errors.append(f"{d.name}: {field}.{lang} missing")
        for lang, fname in (meta.get("solution") or {}).items():
            p = d / fname
            if not p.exists():
                errors.append(f"{d.name}: {fname} missing")
                continue
            errors += check_text(f"{d.name}/{fname}", p.read_text(encoding="utf-8"))
            errors += [f"{d.name}/{e}" for e in check_model(p, lang)]
    n_exam = 0
    exams = ROOT.parent / "exams"
    for f in sorted(exams.glob("*/Q1/items.yaml")):
        errors += check_text(str(f.relative_to(exams)), f.read_text(encoding="utf-8"))
        for it in yaml.safe_load(f.read_text(encoding="utf-8"))["items"]:
            n_exam += 1
            if len(it["de"]["options"]) != len(it["en"]["options"]) or not 0 <= it["key"] < len(it["de"]["options"]):
                errors.append(f"{it['id']}: options or key inconsistent")
    for f in sorted(exams.glob("*/Q*/v*/question.yaml")):
        n_exam += 1
        d, rel = f.parent, str(f.parent.relative_to(exams))
        raw = f.read_text(encoding="utf-8")
        meta = yaml.safe_load(raw)
        errors += check_text(f"{rel}/question.yaml", raw)
        parts = meta.get("rubric") or meta.get("faults") or []
        if sum(x["points"] for x in parts) != meta.get("points"):
            errors.append(f"{rel}: points do not add up")
        for lang, fname in meta["solution"].items():
            sol = d / fname
            errors += check_text(f"{rel}/{fname}", sol.read_text(encoding="utf-8"))
            errors += [f"{rel}/{e}" for e in check_model(sol, lang)]
        for fname in (meta.get("model") or {}).values():
            errors += check_text(f"{rel}/{fname}", (d / fname).read_text(encoding="utf-8"))
    for e in errors:
        print(e)
    print(f"{len(folders)} exercises and {n_exam} exam items checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
