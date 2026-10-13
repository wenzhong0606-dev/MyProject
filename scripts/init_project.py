"""V1.3 新项目脚手架生成器。只创建本地新目录，不更改模板仓库或远程仓库。"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

TEMPLATE_ROOT = Path(__file__).resolve().parents[1]
INCLUDE = ("AGENTS.md", "docs/governance", "docs/deliverables", "scripts", "tests", ".github/workflows")
EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}
SLUG = re.compile(r"^[a-zA-Z][a-zA-Z0-9_.-]{0,79}$")


def validate_name(name: str) -> str:
    if not SLUG.fullmatch(name) or name in {".", ".."}:
        raise ValueError("项目英文标识只能是字母开头的字母、数字、点、下划线、连字符（最多80位）")
    return name


def gather_files(root: Path) -> list[tuple[Path, Path]]:
    """明确白名单，只复制治理框架、检查脚本与阶段模板。"""
    copied = []
    for item in INCLUDE:
        origin = root / item
        if not origin.exists():
            raise FileNotFoundError("源模板缺失: " + item)
        if origin.is_file():
            copied.append((origin, Path(item)))
            continue
        for f in sorted(origin.rglob("*")):
            if f.is_symlink():
                raise ValueError("模板中存在符号链接，拒绝复制: " + str(f))
            if f.is_file() and not EXCLUDE_DIRS.intersection(f.relative_to(origin).parts) and f.suffix not in EXCLUDE_SUFFIXES:
                copied.append((f, f.relative_to(root)))
    return copied


def create_project(*, name: str, target: Path, product: str, stack: str,
                   repo_url: str, branch: str, dry_run: bool = False,
                   validate: bool = True) -> dict:
    validate_name(name)
    if not product.strip():
        raise ValueError("产品类型不能为空")
    target = target.expanduser().resolve()
    src = TEMPLATE_ROOT.resolve()
    if target == src or src in target.parents or target in src.parents:
        raise ValueError("输出目录不得与模板仓库相同、位于模板内或包含模板仓库")
    if target.exists():
        raise FileExistsError("目标目录已存在，拒绝覆盖: " + str(target))
    if not target.parent.is_dir():
        raise FileNotFoundError("目标父目录不存在: " + str(target.parent))
    files = gather_files(src)
    plan = {"name": name, "target": str(target), "count": len(files),
            "mode": "dry-run" if dry_run else "created",
            "includes": list(INCLUDE), "validation": "not-run"}
    if dry_run:
        return plan
    target.mkdir()
    try:
        for origin, rel in files:
            dest = target / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origin, dest)

        # 此三处都是当前新项目的专属资料，不影响共享治理规范。
        profile = ("# 项目画像 — Project Profile\n\n"
                   f"- 项目名称：{name}\n"
                   f"- 产品类型：{product.strip()}\n"
                   f"- 技术栈：{stack.strip() or '待确认'}\n"
                   f"- 目标仓库：{repo_url.strip() or '待确认'}\n"
                   f"- 默认分支：{branch.strip() or '待确认'}\n"
                   "- 项目状态：新建项目，全部阶段交付模板尚未通过审批\n"
                   "- 业务审批人、合规要求、环境与测试命令：待确认\n\n"
                   "**注意**：不得因模板存在就将阶段标记为已完成。\n")
        (target / "docs/governance/project-profile.md").write_text(
            profile, encoding="utf-8")
        readme = ("# " + name + " — " + product.strip() + "\n\n"
                  "## 项目概况\n\n"
                  f"- 技术栈：{stack.strip() or '待确认'}\n"
                  f"- 代码仓库：{repo_url.strip() or '待确认'}\n"
                  f"- 默认分支：{branch.strip() or '待确认'}\n\n"
                  "## AI 设计开发入口\n\n"
                  "1. 阅读 [AGENTS.md](AGENTS.md)。\n"
                  "2. 阅读 [项目画像](docs/governance/project-profile.md)。\n"
                  "3. 进入 [治理规范](docs/governance/) 和 "
                  "[12阶段独立成果](docs/deliverables/README.md)。\n"
                  "4. 运行 \`python scripts/task_router.py --type new-product\` 识别候选成果。\n"
                  "5. 运行 \`python scripts/governance_check.py\` 校验目录。\n\n"
                  "所有设计文件初始为草案，不得视为已通过业务评审。\n")
        (target / "README.md").write_text(readme.replace("\\`", "`"), encoding="utf-8")
        agents = (target / "AGENTS.md").read_text(encoding="utf-8")
        agents = agents.replace("当前仓库为治理规范仓库，不得虚构业务源码或项目技术栈。",
                                "当前仓库为独立业务项目，应先读取 docs/governance/project-profile.md，未确认的业务事实或技术栈不得猜测。")
        agents += ("\n## 项目初始化约束\n\n"
                   "- 本项目由 MyProject V1.3 初始化，项目特定事实以 docs/governance/project-profile.md 为准。\n"
                   "- 新建项目交付物均为 DRAFT，需经过实际设计及审批方可变更状态。\n"
                   "- 不得把原模板仓库的产品身份或默认仓库地址当作当前项目事实。\n")
        (target / "AGENTS.md").write_text(agents, encoding="utf-8")
        report = ("# 项目初始化报告 — Initialization Report\n\n"
                  f"- 项目：{name}\n- 类型：{product.strip()}\n"
                  f"- 生成时间（UTC）：{datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
                  f"- 复制文件数：{len(files)}\n"
                  "- 12阶段交付物：DRAFT 模板，未经业务验收\n"
                  "- 后续待办：补充审批人、构建/测试命令、技术栈约束和业务目标\n")
        (target / "INITIALIZATION_REPORT.md").write_text(report, encoding="utf-8")
        if validate:
            cmds = [[sys.executable, "scripts/governance_check.py"],
                    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]]
            for cmd in cmds:
                check = subprocess.run(cmd, cwd=target, capture_output=True, text=True, timeout=60,
                                       env={**os.environ, 'INIT_PROJECT_CHILD_VALIDATION': '1'})
                if check.returncode:
                    raise RuntimeError("初始化校验未通过: " + " ".join(cmd) + "\n" + check.stdout + check.stderr)
            plan["validation"] = "passed"
        else:
            plan["validation"] = "skipped"
        return plan
    except Exception:
        shutil.rmtree(target)
        raise


def main():
    parser = argparse.ArgumentParser(description="初始化一个独立软件项目，默认不覆盖任何已有文件")
    parser.add_argument("--name", required=True, help="项目英文标识，如 equipment-eam")
    parser.add_argument("--destination", required=True, help="新项目完整目录；其父目录必须存在")
    parser.add_argument("--product", required=True, help="产品类型或中文产品名称")
    parser.add_argument("--stack", default="", help="技术栈（可选）")
    parser.add_argument("--repo-url", default="", help="新项目仓库地址（可选）")
    parser.add_argument("--branch", default="main", help="新项目分支名称（默认 main）")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不创建文件")
    parser.add_argument("--no-validate", action="store_true", help="跳过验证（不推荐）")
    args = parser.parse_args()
    try:
        result = create_project(name=args.name, target=Path(args.destination), product=args.product,
                                stack=args.stack, repo_url=args.repo_url, branch=args.branch,
                                dry_run=args.dry_run, validate=not args.no_validate)
    except (ValueError, OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        parser.exit(1, f"初始化失败：{exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
