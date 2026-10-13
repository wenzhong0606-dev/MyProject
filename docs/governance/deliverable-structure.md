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
