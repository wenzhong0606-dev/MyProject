# MyProject — AI 软件产品设计与开发治理规范

本仓库是跨项目复用的 AI 软件工程治理规范仓库，当前不包含业务系统源码。

## 使用方式
1. AI 首先读取根目录 `AGENTS.md`。
2. 依照 `docs/governance/product-lifecycle.md` 选择适用流程。
3. 使用 `docs/governance/design-gates.md` 完成阶段质量审查。
4. 记录任务计划、验证结果、设计冲突与遗留问题。

默认分支：`main`。技术栈、业务模块、审批人均须基于具体项目确认，不得臆造。

## 独立阶段成果目录

所有 12 阶段的独立产出文件集中在 [docs/deliverables](docs/deliverables/README.md)。每阶段拥有独立目录、交付清单、文件模板和评审要求。

## 中英文阶段交付物规范

阶段目录与成果文件采用英文稳定标识 + 中文含义的双语命名。详见 [12 阶段成果目录](docs/deliverables/README.md) 和 [46 份成果职责说明](docs/governance/deliverables-catalog-交付物职责清单.md)。

## V1.2 AI 任务自动路由

- [任务路由执行规范](docs/governance/task-routing-任务路由规范.md)
- [机器可读路由映射](docs/governance/task-routes.json)
- [任务路由记录模板](docs/governance/templates/task-routing-record-任务路由记录.md)

示例：`python scripts/task_router.py --type new-module` 或 `python scripts/task_router.py --type ui --json`。

工具返回需要检查的候选阶段、文件和质量门禁；最终需要修改哪些文件，应以实际影响分析为准。

## V1.3 新项目初始化 — Project Initialization

[完整操作指南](docs/governance/project-initialization-项目初始化.md)。

```powershell
python scripts/init_project.py --name equipment-eam --destination "C:\\developer\\equipment-eam" --product "设备资产管理系统" --stack "Java 21 + Spring Boot" --dry-run
python scripts/init_project.py --name equipment-eam --destination "C:\\developer\\equipment-eam" --product "设备资产管理系统" --stack "Java 21 + Spring Boot"
```

要求目标目录尚不存在，父目录已存在。工具复制治理规则和独立成果模板，重新生成项目画像，并运行基础校验；不会创建远程仓库。
