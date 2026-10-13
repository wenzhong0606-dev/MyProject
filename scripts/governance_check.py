from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/deliverables"
required = [
    "AGENTS.md", "README.md",
    "docs/governance/product-lifecycle.md",
    "docs/governance/deliverable-structure.md",
    "docs/governance/deliverables-catalog-交付物职责清单.md",
    "docs/governance/design-gates.md",
    "docs/governance/task-routes.json",
    "docs/governance/task-routing-任务路由规范.md",
    "docs/governance/templates/task-routing-record-任务路由记录.md",
    "scripts/task_router.py",
    "docs/governance/traceability.csv",
    "docs/deliverables/README.md",
    "docs/deliverables/manifest.json",
]
errors = [f"缺少: {p}" for p in required if not (ROOT / p).is_file()]
manifest = BASE / "manifest.json"
if manifest.is_file():
    stages = json.loads(manifest.read_text(encoding="utf-8")).get("stages", [])
    if [x.get("id") for x in stages] != [f"{i:02d}" for i in range(1, 13)]:
        errors.append("阶段必须按 01–12 顺序列出")
    if len({x.get("directory") for x in stages}) != len(stages):
        errors.append("阶段目录重复")
    for s in stages:
        directory = s.get("directory", "")
        if not re.fullmatch(r"\d{2}-[a-z][a-z0-9-]*-[\u4e00-\u9fff]+", directory):
            errors.append(f"阶段目录不符合中英文格式: {directory}")
            continue
        folder = BASE / directory
        if not (folder / "README.md").is_file():
            errors.append(f"缺少阶段 README: {directory}")
        if not s.get("artifacts"):
            errors.append(f"阶段无交付物: {directory}")
        for a in s.get("artifacts", []):
            filename = a.get("file", "")
            if not re.fullmatch(r"[a-z][a-z0-9-]*-[\u4e00-\u9fffA-Za-z0-9]+\.md", filename):
                errors.append(f"成果文件名不符合中英文格式: {filename}")
                continue
            if not a.get("purpose") or not a.get("exclusion"):
                errors.append(f"成果职责或排除范围缺失: {filename}")
            path = folder / filename
            if not path.is_file():
                errors.append(f"成果文件不存在: {directory}/{filename}")
            else:
                body = path.read_text(encoding="utf-8")
                for key in ["文档编号", "状态", "版本", "关联需求/功能 ID", "审批结论", "Purpose", "Input", "Required Output", "Exclusions", "Definition of Done"]:
                    if key not in body:
                        errors.append(f"成果文件缺失 {key}: {filename}")
matrix = ROOT / "docs/governance/traceability.csv"
if matrix.is_file():
    with matrix.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "requirement_id" not in reader.fieldnames:
            errors.append("追踪矩阵缺少 requirement_id")
        else:
            ids = [row["requirement_id"] for row in reader if row.get("requirement_id")]
            if len(ids) != len(set(ids)):
                errors.append("追踪矩阵 requirement_id 重复")
routes_file = ROOT / "docs/governance/task-routes.json"
if routes_file.is_file() and manifest.is_file():
    route_data = json.loads(routes_file.read_text(encoding="utf-8"))
    catalog = json.loads(manifest.read_text(encoding="utf-8"))
    stage_ids = {s["id"] for s in catalog["stages"]}
    artifact_ids = {s["id"] + ":" + a["english"] for s in catalog["stages"] for a in s["artifacts"]}
    if len(route_data.get("tasks", {})) < 8:
        errors.append("缺少基础任务路由")
    for task_name, task in route_data.get("tasks", {}).items():
        for stage_id in task.get("stages", []):
            if stage_id not in stage_ids:
                errors.append(f"任务 {task_name} 引用了未知阶段 {stage_id}")
        for token in task.get("required", []):
            if token not in artifact_ids:
                errors.append(f"任务 {task_name} 引用了未知成果 {token}")
if errors:
    raise SystemExit("\n".join(errors))
print("中英文阶段目录、46 份独立成果的基础结构和职责字段检查通过；不代表业务审批通过。")
