# 阶段交付物职责与边界目录 — Stage Deliverables Catalog

> 本清单是文件职责的统一定义。文件存在仅代表模板就绪，不代表产出已经完成。

## 命名规则 Naming Convention

- 阶段目录：`NN-english-slug-中文阶段名/`，示例 `03-business-业务流程/`。
- 成果文件：`english-slug-中文成果名.md`，示例 `business-rules-业务规则.md`。
- `README.md`、`AGENTS.md`、`manifest.json` 等工具约定入口保留标准文件名，在文件标题提供中英文名称。
- 固定英文标识供脚本使用，中文部分面向人员识别；不要随意重命名，正式调整须同步修复引用、索引与 CI。

## 01 产品定位 (strategy)

**阶段职责**：确定建设方向与目标。**门禁**：G1。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [vision-愿景与定位.md](../deliverables/01-strategy-产品定位/vision-愿景与定位.md) | 明确目标用户、产品价值、核心问题与差异化定位 | 不列详细需求、页面或技术选型 |
| [scope-边界与范围.md](../deliverables/01-strategy-产品定位/scope-边界与范围.md) | 界定产品包含、不包含的业务及阶段边界 | 不记录功能级的逐条验收标准 |
| [metrics-指标与目标.md](../deliverables/01-strategy-产品定位/metrics-指标与目标.md) | 定义业务成功、使用效果及衡量口径 | 不替代上线后真实监测结果 |

## 02 需求分析 (requirements)

**阶段职责**：明确建设需求与验收边界。**门禁**：G1。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [stakeholders-角色与干系人.md](../deliverables/02-requirements-需求分析/stakeholders-角色与干系人.md) | 识别业务参与者、职责、利益诉求及沟通边界 | 不等同于最终系统权限配置 |
| [scenarios-业务场景.md](../deliverables/02-requirements-需求分析/scenarios-业务场景.md) | 列出用户在何种条件下完成何种工作及预期结果 | 不代替细化的流程与状态图 |
| [requirements-需求规格.md](../deliverables/02-requirements-需求分析/requirements-需求规格.md) | 为每项需求定义唯一编号、来源、优先级、约束 | 不描述数据库表结构或直接实现代码 |
| [acceptance-criteria-验收条件.md](../deliverables/02-requirements-需求分析/acceptance-criteria-验收条件.md) | 将需求转化为可客观判定的验收条件和反例 | 不等同于测试运行报告 |

## 03 业务流程 (business)

**阶段职责**：定义业务运转机制。**门禁**：G2。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [process-list-流程清单.md](../deliverables/03-business-业务流程/process-list-流程清单.md) | 建立端到端业务流程目录、流程责任人及触发条件 | 不重复描述功能菜单清单 |
| [process-model-流程模型.md](../deliverables/03-business-业务流程/process-model-流程模型.md) | 定义流程节点、分支、角色、输入输出和异常流转 | 不混入页面布局及实现代码 |
| [business-rules-业务规则.md](../deliverables/03-business-业务流程/business-rules-业务规则.md) | 列出判定条件、控制约束、计算口径及业务依据 | 不等同于技术校验实现 |
| [state-model-状态转换.md](../deliverables/03-business-业务流程/state-model-状态转换.md) | 定义合法状态、触发事件、前置条件与状态转换结果 | 不混同于页面按钮显隐状态 |

## 04 领域设计 (domain)

**阶段职责**：确定核心业务概念与约束。**门禁**：G2。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [glossary-术语表.md](../deliverables/04-domain-领域设计/glossary-术语表.md) | 统一领域名词、中文定义、英文术语和同义词 | 不记录物理数据库字段 |
| [domain-objects-领域对象.md](../deliverables/04-domain-领域设计/domain-objects-领域对象.md) | 列明实体、值对象、属性含义、生命周期和业务标识 | 不提前绑定具体数据库技术 |
| [relationships-对象关系与不变量.md](../deliverables/04-domain-领域设计/relationships-对象关系与不变量.md) | 描述对象基数、聚合一致性边界及业务不变量 | 不替代 ER 物理模型 |
| [domain-events-领域事件.md](../deliverables/04-domain-领域设计/domain-events-领域事件.md) | 识别领域事件、发生条件、携带数据和订阅者 | 不等同于消息队列技术配置 |

## 05 功能设计 (functions)

**阶段职责**：组织产品能力与授权。**门禁**：G3。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [function-tree-功能架构.md](../deliverables/05-functions-功能设计/function-tree-功能架构.md) | 按业务能力拆分模块、功能包与唯一功能 ID | 不充当页面布局清单 |
| [function-spec-功能规格.md](../deliverables/05-functions-功能设计/function-spec-功能规格.md) | 逐项描述操作入口、业务动作、规则、状态与异常处理 | 不替代 API 请求参数说明 |
| [permissions-角色权限.md](../deliverables/05-functions-功能设计/permissions-角色权限.md) | 定义角色、数据范围、资源操作及授权决策矩阵 | 不记录用户账号或敏感凭据 |
| [navigation-菜单信息架构.md](../deliverables/05-functions-功能设计/navigation-菜单信息架构.md) | 定义用户导航路径、菜单归属与任务入口 | 不重复记录页面视觉样式 |

## 06 交互原型 (ux)

**阶段职责**：明确界面任务与交互。**门禁**：G3。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [task-flows-用户任务流.md](../deliverables/06-ux-交互原型/task-flows-用户任务流.md) | 建立角色任务、前置条件、操作路径与结果反馈 | 不等同于端到端业务流程 |
| [page-inventory-页面清单.md](../deliverables/06-ux-交互原型/page-inventory-页面清单.md) | 为页面配置唯一编号、业务目标、角色、入口和关联功能 | 不以页面数代替业务功能完成度 |
| [interaction-spec-交互规格.md](../deliverables/06-ux-交互原型/interaction-spec-交互规格.md) | 说明页面布局、字段、按钮、禁用条件、空态和异常提示 | 不替代领域规则的权威来源 |
| [prototype-review-原型评审.md](../deliverables/06-ux-交互原型/prototype-review-原型评审.md) | 记录页面可发现性、信息负担、可用性及评审问题 | 不充当业务验收签署 |

## 07 数据设计 (data)

**阶段职责**：定义数据组织和治理要求。**门禁**：G4。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [logical-model-逻辑数据模型.md](../deliverables/07-data-数据设计/logical-model-逻辑数据模型.md) | 将领域对象映射为逻辑实体、关系与键约束 | 不包含未经确认的生产建表命令 |
| [data-dictionary-数据字典.md](../deliverables/07-data-数据设计/data-dictionary-数据字典.md) | 规定字段含义、类型、是否必填、取值范围、默认值和来源 | 不混入 UI 文案清单 |
| [data-lifecycle-数据生命周期.md](../deliverables/07-data-数据设计/data-lifecycle-数据生命周期.md) | 描述数据创建、变更、归档、删除、保留和审计策略 | 不代替真实数据操作日志 |
| [migration-plan-迁移方案.md](../deliverables/07-data-数据设计/migration-plan-迁移方案.md) | 确定兼容性、迁移步骤、回填、校验与回滚计划 | 不直接执行数据迁移 |

## 08 技术设计 (architecture)

**阶段职责**：落实系统工程实现方案。**门禁**：G4。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [architecture-架构方案.md](../deliverables/08-architecture-技术设计/architecture-架构方案.md) | 定义模块分层、部署单元、依赖关系及技术决策依据 | 不重新定义业务对象和规则 |
| [api-contracts-API契约.md](../deliverables/08-architecture-技术设计/api-contracts-API契约.md) | 定义 API 端点、输入输出、鉴权、错误码与版本约定 | 不替代业务功能规格 |
| [security-nfr-安全非功能要求.md](../deliverables/08-architecture-技术设计/security-nfr-安全非功能要求.md) | 定义安全、性能、可用性、容量、并发及恢复目标 | 不在未经评估时声称符合标准 |
| [integration-集成方案.md](../deliverables/08-architecture-技术设计/integration-集成方案.md) | 规定上下游系统、集成责任、协议、失败重试及幂等性 | 不复制外部系统全部接口源码 |

## 09 开发实现 (implementation)

**阶段职责**：执行编码和开发级验证。**门禁**：G5。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [implementation-plan-实施任务.md](../deliverables/09-implementation-开发实现/implementation-plan-实施任务.md) | 拆分可交付任务，标注依赖、负责人、估算与完成条件 | 不以计划表替代实际交付 |
| [implementation-log-实现记录.md](../deliverables/09-implementation-开发实现/implementation-log-实现记录.md) | 记录实现差异、关联提交、文件范围与设计变更 | 不伪造已实现功能 |
| [unit-test-report-开发自测.md](../deliverables/09-implementation-开发实现/unit-test-report-开发自测.md) | 记录真实执行的构建、单测、静态检查与失败证据 | 未运行时不得报告通过 |

## 10 测试验收 (qa)

**阶段职责**：证明需求符合性并完成业务验收。**门禁**：G5/G6。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [test-plan-测试方案.md](../deliverables/10-qa-测试验收/test-plan-测试方案.md) | 定义测试层次、范围、环境、覆盖策略和准入退出标准 | 不代替具体测试用例 |
| [test-cases-测试用例.md](../deliverables/10-qa-测试验收/test-cases-测试用例.md) | 以需求和功能 ID 列出正常、边界、权限与异常场景 | 不将未执行的用例写成通过 |
| [defects-缺陷与回归.md](../deliverables/10-qa-测试验收/defects-缺陷与回归.md) | 维护缺陷编号、严重程度、复现步骤、责任人与回归证据 | 不在无证据时关闭问题 |
| [uat-用户验收.md](../deliverables/10-qa-测试验收/uat-用户验收.md) | 登记业务代表的试用结果、遗留问题、签字与批准日期 | AI 不得代替用户批准 |

## 11 部署发布 (release)

**阶段职责**：安全部署与运营交接。**门禁**：G6。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [release-checklist-上线检查.md](../deliverables/11-release-部署发布/release-checklist-上线检查.md) | 检查版本、环境、依赖、权限、数据备份及上线条件 | 不代表部署操作已经执行 |
| [deployment-部署手册.md](../deliverables/11-release-部署发布/deployment-部署手册.md) | 提供实际环境部署、配置、验证和故障定位操作步骤 | 不在仓库中存放密钥 |
| [rollback-回滚方案.md](../deliverables/11-release-部署发布/rollback-回滚方案.md) | 描述触发条件、恢复步骤、数据一致性核查和责任人 | 不声称未经演练的回滚已验证 |
| [handover-运维交接.md](../deliverables/11-release-部署发布/handover-运维交接.md) | 明确监控告警、值守职责、故障升级、运维文档和联系人 | 不代替生产监控记录 |

## 12 运营迭代 (operations)

**阶段职责**：基于真实运行数据持续改进。**门禁**：持续评审。

| 成果文件（中英文） | 职责与意义 | 不应承担的内容 |
|---|---|---|
| [operations-metrics-运营指标.md](../deliverables/12-operations-运营迭代/operations-metrics-运营指标.md) | 跟踪上线后的真实业务指标、技术指标、口径与趋势 | 不直接复用立项目标当实际值 |
| [feedback-用户反馈.md](../deliverables/12-operations-运营迭代/feedback-用户反馈.md) | 记录用户反馈来源、影响角色、严重性及事实证据 | 不将反馈直接当作批准的需求 |
| [improvement-backlog-迭代需求.md](../deliverables/12-operations-运营迭代/improvement-backlog-迭代需求.md) | 将运营改进转换为可优先级排序的迭代项及预期收益 | 不直接等同开发任务已排期 |
| [retrospective-复盘报告.md](../deliverables/12-operations-运营迭代/retrospective-复盘报告.md) | 分析阶段目标完成度、根因、改进责任人与跟进验证 | 不隐瞒失败或未完成事项 |

