"""AI 工程任务路由：只生成候选文件清单，不实施文件改写。"""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ROOT / "docs/governance/task-routes.json"
MANIFEST = ROOT / "docs/deliverables/manifest.json"

def load():
    routes = json.loads(ROUTES.read_text(encoding="utf-8"))["tasks"]
    stages = json.loads(MANIFEST.read_text(encoding="utf-8"))["stages"]
    by_id = {s["id"]: s for s in stages}
    lookup = {(s["id"], a["english"]): f'docs/deliverables/{s["directory"]}/{a["file"]}' for s in stages for a in s["artifacts"]}
    return routes, by_id, lookup

def resolve(task_type):
    routes, stages, lookup = load()
    if task_type not in routes:
        raise ValueError("未知任务类型: " + task_type)
    task = routes[task_type]
    stage_paths = []
    for sid in task["stages"]:
        if sid not in stages:
            raise ValueError("未知阶段: " + sid)
        stage_paths.append(f'docs/deliverables/{stages[sid]["directory"]}/README.md')
    artifacts = []
    for token in task["required"]:
        sid, slug = token.split(":", 1)
        if (sid, slug) not in lookup:
            raise ValueError("未知成果标识: " + token)
        artifacts.append(lookup[(sid, slug)])
    return {"type": task_type, "title": task["title"], "gate": task["gate"],
            "stage_readmes": stage_paths, "candidate_artifacts": artifacts}

def main():
    parser = argparse.ArgumentParser(description="显示 AI 任务涉及的候选阶段和交付文件")
    parser.add_argument("--type", choices=sorted(load()[0]), required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = resolve(args.type)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"任务: {result['title']} ({result['type']})")
        print("门禁: " + result["gate"])
        print("候选阶段:")
        for x in result["stage_readmes"]: print("  " + x)
        print("最低检查成果:")
        for x in result["candidate_artifacts"]: print("  " + x)
        print("注意：以上是候选检查范围，不代表全部必须修改。")

if __name__ == "__main__":
    main()
