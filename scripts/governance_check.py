from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
required = ["AGENTS.md", "README.md", "docs/governance/product-lifecycle.md", "docs/governance/deliverable-structure.md", "docs/governance/design-gates.md", "docs/governance/traceability.csv", "docs/deliverables/README.md", "docs/deliverables/manifest.json"]
errors = [f"缺少: {f}" for f in required if not (ROOT / f).is_file()]
path = ROOT / "docs/deliverables/manifest.json"
if path.is_file():
    stages = json.loads(path.read_text(encoding="utf-8")).get("stages", [])
    if [s["id"] for s in stages] != [f"{i:02d}" for i in range(1, 13)]:
        errors.append("必须完整定义按顺序排列的 12 个阶段")
    if len({s["directory"] for s in stages}) != len(stages):
        errors.append("阶段目录不能重复")
    for s in stages:
        folder_name = s["directory"]
        if not folder_name.startswith(s["id"]+"-") or "/" in folder_name or ".." in folder_name:
            errors.append(f"阶段目录不合法: {folder_name}")
            continue
        folder = ROOT / "docs/deliverables" / folder_name
        if not (folder/"README.md").is_file():
            errors.append(f"阶段 README 缺失: {folder_name}")
        if not s["artifacts"]:
            errors.append(f"阶段成果为空: {folder_name}")
        for a in s["artifacts"]:
            name = a["file"]
            if "/" in name or ".." in name:
                errors.append(f"成果文件名不合法: {name}")
                continue
            f = folder / name
            if not f.is_file():
                errors.append(f"缺少阶段成果: {folder_name}/{name}")
            else:
                content = f.read_text(encoding="utf-8")
                for key in ["文档编号", "状态", "版本", "关联需求/功能 ID", "审批结论"]:
                    if key not in content:
                        errors.append(f"元数据 {key} 缺失: {folder_name}/{name}")
matrix = ROOT / "docs/governance/traceability.csv"
if matrix.is_file():
    with matrix.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "requirement_id" not in reader.fieldnames:
            errors.append("追踪矩阵缺少 requirement_id")
        else:
            ids = [r["requirement_id"] for r in reader if r.get("requirement_id")]
            if len(ids) != len(set(ids)):
                errors.append("追踪矩阵存在重复 requirement_id")
if errors:
    raise SystemExit("\n".join(errors))
print("12 阶段独立交付物及治理目录结构检查通过；不代表实际业务验收通过。")
