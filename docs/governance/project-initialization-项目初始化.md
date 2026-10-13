# 新项目初始化指南 — Project Initialization V1.3

## 用途
从本治理模板创建全新的独立项目，不影响原模板仓库、不创建 GitHub 仓库、不推送远程代码。脚本只在本地生成文件；后续 Git 操作需要另行执行。

## 前置条件
- 已克隆 MyProject，安装 Python 3.10 或更新版本。
- `--destination` 为**尚不存在**的新目录，其父目录已存在。
- 新项目名称 `--name` 使用英文标识；`--product` 可使用中文。
- 建议先 `--dry-run` 预览。

## Windows PowerShell 示例

```powershell
cd C:\\developer\\MyProject
python scripts/init_project.py --name equipment-eam --destination "C:\\developer\\equipment-eam" --product "设备资产管理系统" --stack "Java 21 + Spring Boot" --repo-url "https://github.com/<owner>/<repo>" --dry-run
python scripts/init_project.py --name equipment-eam --destination "C:\\developer\\equipment-eam" --product "设备资产管理系统" --stack "Java 21 + Spring Boot" --repo-url "https://github.com/<owner>/<repo>"
```

## 生成结果
复制 `AGENTS.md`、`docs/governance/`、`docs/deliverables/`、`scripts/`、`tests/` 以及 GitHub Actions 检查配置；重新生成项目专用 `README.md` 与 `docs/governance/project-profile.md`，添加 `INITIALIZATION_REPORT.md`。

- 原模板中与工具相关的标准文件名不变。
- 12 阶段及 46 个成果模板保持 DRAFT；需要项目成员逐项设计、审查。
- 初始化过程执行结构校验与单元测试。验证失败会删除**本次刚创建**的目标目录，已有目录永远不覆盖。
- `--no-validate` 可跳过校验，但必须明确报告未验证，默认不推荐。
- 不复制 `.git`、缓存、临时文件、个人配置或模板仓库历史。

## 初始化之后
1. 进入新项目文件夹并检查 README、AGENTS 与 project-profile。
2. 确认真实技术栈、构建/测试命令、审批角色与数据合规要求。
3. 运行 `python scripts/task_router.py --type new-product`。
4. 如需推送 GitHub，在新项目目录内自己执行 `git init`、提交并配置**新仓库**远程。
5. 初始化不代表已有业务功能，也不代表设计门禁通过。

## 限制
脚手架目前提供单项目本地目录初始化，不负责生成 Java/.NET 等业务框架、不自动创建远程仓库、不合并进已有项目，也不代替业务评审。
