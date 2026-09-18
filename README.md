# Earphone Competitive Intelligence Platform

一个面向技术作品集的耳机竞品情报工程示例，展示如何把公开、非结构化资料加工为可验证的产品、BOM、器件供应商和品牌供应链数据。

> 本仓库是从稳定版本导出的无历史、无生产数据工程快照。它不是公司 GitLab 仓库镜像，不包含员工身份、内部地址、部署交接记录、生产配置、历史抓取数据、第三方原始图片或模型缓存。

## 展示重点

- 证据约束的信息抽取：规则优先，可选文本模型补全。
- 实体规范化：产品、品牌、供应商、器件、型号与使用位置。
- 幻觉控制：字段级证据、状态标识、缺失值保留和发布校验。
- 数据产品：产品档案、BOM 对比、器件寻源和品牌供应链视图。
- 工程架构：API、关系数据库、对象存储、后台任务和静态页面导出。
- 测试体系：抽取规则、数据质量、迁移、API 和页面构建测试。

## 代码结构

```text
core/       抽取、清洗、规范化与分析逻辑
server/     API、数据库模型、迁移、对象存储与后台任务
web/        Astro + React 数据产品界面
scripts/    ETL、评估、数据校验和构建命令
tests/      自动化测试
data/       空公开清单；不包含业务数据
docs/       公开架构与通用工程说明
```

架构说明见 [`docs/PUBLIC_ARCHITECTURE.md`](docs/PUBLIC_ARCHITECTURE.md)。

## 本地工程验证

环境要求：Python 3.11+、Node.js 22+。复制 `.env.example` 为本地忽略文件，再根据需要配置通用数据库、对象存储和文本模型接口。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q

cd web
npm ci
npm run build:minio
```

仓库默认没有业务数据，因此产品页面为空是预期行为。交互效果请查看独立的脱敏演示仓库：

- `headphone-component-intelligence`：固定小规模数据和 GitHub Pages 演示。
- 本仓库：工程结构、数据加工代码、测试与架构说明。

## 配置边界

本地和部署配置只从环境变量读取。示例文件只保留空值或无效占位值：

```text
PORTFOLIO_DATABASE_URL
OBJECT_STORAGE_ENDPOINT
OBJECT_STORAGE_ACCESS_KEY
OBJECT_STORAGE_SECRET_KEY
APP_TEXT_MODEL_BASE_URL
APP_TEXT_MODEL_TOKEN
APP_VIDEO_SESSION_FILE
```

真实凭据不得提交到 Git。公开仓库也不包含组织专用的网关地址、服务器路径或 Secret 名称。

## 数据与权利边界

- 不公开历史采集数据、文章全文、完整字幕或来源图片。
- 不公开公司数据库导出、对象存储内容或人工复核表。
- 公开代码仅用于展示工程思路和个人技术能力。
- 第三方网站、产品名称和商标的权利归各自权利人所有。
- 在线演示使用独立的固定脱敏快照，不在公开环境执行定时采集。

## Repository history

The public repository starts with a new Git history. Previous source-control commits, author emails, deployment records, and deleted historical files are intentionally not carried over.
