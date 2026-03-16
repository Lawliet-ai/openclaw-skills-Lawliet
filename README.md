<p align="center">
  <img src="./Logo.png" width="120" alt="Lawliet OpenClaw Skills Logo">
</p>

# OpenClaw-Skills-Lawliet 🛠️
## 别把 AI 当成高级荧光笔，把它当成你的认知杠杆。
## Stop using AI as a high-end highlighter. Start using it as a cognitive lever.

![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-orange)
![Version](https://img.shields.io/badge/Version-1.0.0--latest-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

### 📖 The Manifesto / 宣言

**大多数 LLM 生成的总结就像高果糖浆——甜，但没营养。如果你只想看废话复读，别来这。**

这里的工具只有一个目的：把 LLM 从复读机变成能够进行“底层解构”的残酷智囊。这些技能是我为那些比起礼貌的表层废话，更看重深层逻辑、物理硬约束和原子真相的人准备的认知杠杆。

**Most LLM summaries are brain-dead filler.** High-fructose corn syrup for the mind. Sweet, but intellectually bankrupt. This repo is not for people who want easy answers; it's for people who want the atomic truth.

---

### ⚡ Core Infrastructure / 核心底座 (Must Install)

#### **[Meta-Router: 自动化认知网关](./Meta-Router/README.md)**
这是整个 Lawliet 军火库的“操作系统内核”。

* **为什么要装？** 技能装得越多，AI 越慢。因为它每次对话前都要背诵几万字的技能说明。这叫“认知污染”。
* **它怎么工作？** * **自动索引**：安装新技能后，它会自动扫描并生成不到 1KB 的快速检索表。
    * **按需加载 (Lazy Loading)**：禁止 AI 遍历全量文档。只有检测到对应意图时，才挂载特定技能，节省 80% 以上的 Token。
    * **路由拦截**：像网关一样拦截你的输入，实现“毫秒级”技能分发。
* **Why this?** Stop feeding the LLM 10k tokens of skill docs per prompt. This meta-skill implements an "Index-then-Load" architecture. It monitors your environment, builds a silent cache, and prunes context to maximize reasoning speed.

---

### 🧰 The Arsenal / 认知军火库

| Skill / 技能 | Description / 简介 |
| :--- | :--- |
| **[48h-Expert](./48h-expert)** | 48 小时内建立领域的底层认知图谱。拒绝摘要，只要思维模型。 / Build a domain mental map in 48h. |
| **[First-Principles](./first-principles)** | 撕掉营销黑话，用物理定律审视产品真相。 / Strips away marketing fluff to find atomic truths. |

---

### 🚀 Installation / 部署与武装

#### **一键安装所有核心技能**
```bash
clawhub install meta-router 48h-expert first-principles

使用说明 (Usage)
初始化：安装后，对你的 Agent 说：Refresh library。

自动化路由：正常提问，Meta-Router 会自动帮你选择最合适的工具。

显式强制调用 (Shortcut)：

L: 48h [领域名] -> 瞬时切换到专家学习模式。

L: fp [产品名] -> 瞬时切换到第一性原理拆解模式。

Bash
# Example / 示例
L: 48h 量化交易的底层逻辑 (Quant Trading Bottom-layer Logic)
L: fp 某品牌 3D 打印机的自研高速算法 (Specific high-speed algorithm verdict)

Usage Guide
Initialization: After installation, simply tell your Agent: Refresh my skill library.

Automated Routing: Just ask a question. Meta-Router will intercept your intent and dispatch the correct tool silently.

Explicit Force-Call (Shortcuts): Use the L: prefix for 100% precision.

L: 48h [Topic] -> Instant activation of Meta-Learning mode.

L: fp [Product/Tech] -> Instant activation of First-Principles Deconstruction.

Bash
# Examples
L: 48h The bottom-layer logic of Quantitative Trading
L: fp Efficiency verdict of Brand X's "Self-developed" high-speed 3D printing algorithm
