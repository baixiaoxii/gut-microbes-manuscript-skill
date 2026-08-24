# Gut Microbes Manuscript Skill

一个面向 Taylor & Francis 期刊 *Gut Microbes* Research Article 的 ChatGPT/Codex skill。它将作者提供的论文框架、实验结果、方法、图表和参考文献整理为证据可追溯的英文论文，并输出经过版式检查的 Word 文档。

## 主要能力

- 将中文或英文研究材料整理为英文 Research Article。
- 根据近期 *Gut Microbes* 同类型论文提炼章节功能、结果顺序和图表逻辑。
- 支持人体队列、纵向/干预、动物机制和多组学研究的写作模式。
- 建立“实验结果—图表—论文结论”的证据映射。
- 检查微生物组采样、测序、生物信息学、统计学及数据开放信息。
- 区分描述、相关、预测、介导和因果结论。
- 在信息缺失时保留明确的作者输入标记，不补造实验数据或文献。
- 生成 `.docx`，并要求逐页渲染检查后再交付。

## 适用范围

当前版本优先支持 *Gut Microbes* 的实验型 Research Article。Review Article、Rapid Communication、Data Note 及投稿系统自动提交不属于首版的标准流程。

该 skill 是论文组织、写作和投稿前检查工具，不代替作者对数据真实性、作者资格、伦理合规、统计分析和最终投稿内容的责任。

## 目录结构

```text
gut-microbes-manuscript/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-guardrails.md
│   ├── input-contract.md
│   ├── journal-requirements.md
│   ├── microbiome-reporting.md
│   ├── submission-checklist.md
│   └── writing-patterns.md
└── scripts/
    └── audit_evidence.py
```

## 安装

将 `gut-microbes-manuscript` 文件夹作为个人 skill 导入 ChatGPT/Codex。`SKILL.md` 必须位于 skill 文件夹根目录。

如果使用支持个人 skill 的 ChatGPT Work/Codex 环境，也可以把该文件夹放入个人 skills 目录并按照环境提供的安装流程完成验证。

## 使用示例

```text
使用 $gut-microbes-manuscript，根据我提供的论文框架、实验结果表、
Figures 和方法说明，生成一篇 Gut Microbes Research Article 的英文 Word 初稿。
不要补造缺失数据；所有缺失信息使用 AUTHOR INPUT REQUIRED 标记。
```

投稿前检查示例：

```text
使用 $gut-microbes-manuscript 检查这篇论文是否达到 submission-ready 状态，
重点核对结果与结论、微生物组方法、统计报告、伦理声明、数据开放信息和 Word 版式。
```

## 推荐输入

- 论文框架或现有草稿：DOCX、Markdown 或 PDF
- 实验结果：XLSX、CSV、表格或结构化文字
- Figures 与图注
- 完整方法说明
- 参考文献列表、RIS 或 BibTeX
- 作者、单位、伦理、基金、利益冲突、作者贡献和数据开放信息

## 工作流程

1. 识别研究设计和输入文件。
2. 建立结构化 evidence manifest。
3. 审计样本量、方法、统计和结果来源。
4. 建立结果—图表—结论映射。
5. 选择最接近的 *Gut Microbes* 研究论文写作模式。
6. 按 Results、Methods、Discussion、Introduction、Abstract 的顺序写作。
7. 执行证据、报告规范和期刊合规检查。
8. 生成 Word，并逐页渲染检查版式。

## Evidence manifest 审计

skill 内包含一个无第三方依赖的 JSON 审计脚本：

```bash
python gut-microbes-manuscript/scripts/audit_evidence.py evidence.json --mode draft
python gut-microbes-manuscript/scripts/audit_evidence.py evidence.json --mode submission-ready
```

脚本检查：

- 研究问题和研究类型
- 分组及样本量
- 样本采集、提取、测序、生物信息学和统计方法
- 结果编号及图表来源
- 每条结论是否引用真实存在的结果
- 伦理审批和未解决的作者输入标记

## 两种输出模式

### Draft

允许信息不完整，但必须使用：

```text
[AUTHOR INPUT REQUIRED: specific missing item]
```

### Submission-ready

只有在关键方法、结果、声明、引用和 Word 版式检查全部通过后，才能标记为 submission-ready。

## 证据安全原则

该 skill 不得虚构：

- 样本量、P 值、FDR、效应量或置信区间
- 实验条件、方法参数、软件或数据库版本
- 伦理审批、基金、利益冲突、作者贡献或数据登录号
- 文献题目、作者、DOI 或出版信息
- 未完成的验证实验或因果机制

已发表论文只用于学习章节功能、证据顺序、图表逻辑和写作节奏，不复制其具体表述。

## 规则来源与更新

期刊要求以 *Gut Microbes* 最新官方 Instructions for Authors 为最高优先级：

- https://www.tandfonline.com/journals/kgmi20
- https://www.tandfonline.com/journals/kgmi20/about-this-journal

Taylor & Francis 通用稿件与报告规范：

- https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/journal-manuscript-layout-guide/
- https://authorservices.taylorandfrancis.com/editorial-policies/standards-of-reporting/

期刊要求可能更新，因此最终投稿前应重新核对官方作者指南。
