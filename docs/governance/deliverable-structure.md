# 阶段交付物目录管理规范

## 职责划分

- docs/governance：通用的治理规则、工作模板及评审约束。
- docs/deliverables：具体项目的 12 阶段独立成果文件。
- docs/deliverables/manifest.json：阶段目录和文件的权威清单。
- 源代码：保留在项目自身已有源码目录。

## 强制约束

1. 先确定任务所属阶段，再写入指定阶段的成果文件。
2. 不同阶段不得共用同一个成果文件；跨阶段只通过稳定 ID 和链接相互引用。
3. 每阶段 README 记录输入、交付物及门禁；每个成果文档必须具备编号、状态、版本、负责人、关联 ID、审批结论。
4. 未填写的文件维持 DRAFT 与「待确认」，不得标记 APPROVED。
5. 变更上游设计时，评估并同步下游受影响阶段及追踪矩阵。
6. 门禁需要实际评审证据；脚本结构通过不表示业务已验收。
7. 文档目录用稳定英文代号，正文和图示说明用中文。

## 状态

DRAFT / IN_REVIEW / APPROVED / SUPERSEDED；阶段门禁使用 NOT_STARTED / IN_PROGRESS / PASS / BLOCKED / WAIVED。未经批准不应自动标记 PASS。

## V1.1 中英文命名强制约束

- 阶段目录格式：`NN-english-slug-中文名称`；成果文件格式：`english-slug-中文名称.md`。
- `README.md`、`AGENTS.md`、`manifest.json` 等保留业界工具约定的英文文件名；文件内标题仍采用中英文双语。
- 每份成果必须在正文写明职责意义、必填内容、不应承担的内容、上下游引用和完成标准。
- 具体职责以 [交付物职责清单](./deliverables-catalog-交付物职责清单.md) 和 `manifest.json` 为准。
- 重命名需要同步 manifest、脚本、引用和跨阶段追踪；严禁仅按名称创建多个含义重复的文件。

## V1.2 AI 任务到文件的自动路由

- 路由权威规则：`task-routes.json`；文件权威路径：`../deliverables/manifest.json`。
- 新任务先执行 `scripts/task_router.py` 获取候选路径，核对现有成果再写入。
- 工具不允许越过既有审批，更不能用结构检查取代对业务规则的人工确认。
- AI 必须在任务报告中说明实改文件与候选文件的差异及原因。
