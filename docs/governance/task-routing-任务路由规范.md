# AI 任务识别与文件路由规范 — Task Routing V1.2

## 运行流程
1. 阅读根目录 AGENTS.md、项目事实源和 manifest.json。
2. 识别任务类型：`new-product`、`new-module`、`change-feature`、`bugfix`、`ui`、`data-change`、`api-change`、`audit`。不确定时先检查上下文；不要随意归入最轻量类型。
3. 执行 `python scripts/task_router.py --type <任务类型>` 查看具体候选文件。
4. 对照现有文件和源码判定需要读取、修改或新增哪些成果；生成路由记录和影响分析。
5. 涉及冻结规则、权限、安全、数据迁移、公共接口时必须获取相应批准；不得凭 AI 自行批准。
6. 修改后运行 `python scripts/governance_check.py` 与相应项目测试，记录实际证据。

## 约束
- 机器路由是**候选文件及最低检查集合**，不代表所有列出的文件都必须修改。
- 跨阶段任务允许多个目录同时更新，但每份成果只允许存入所属阶段目录。
- 若未命中准确路由，使用 `change-feature` 进行影响分析，不得凭空创建新阶段目录。
- 已审批设计的改变必须追踪上游、下游；缺失信息写“待确认”而不编造。
- 未运行测试不得标记通过；模板内元数据存在不构成实质性完成。
- 仅默认检查文档及静态 ID 一致性，**不宣称自动完成语义一致性、业务审批或写入权限阻断**。

## 路由规则配置
`task-routes.json` 是权威机器规则，阶段及文件路径从 `docs/deliverables/manifest.json` 解析，避免重复硬编码。
`docs/governance/templates/task-routing-record-任务路由记录.md` 是每项实际任务的记录模板。
