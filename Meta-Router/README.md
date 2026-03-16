
# Meta-Router: The Cognitive Harness ⚡
# Meta-Router: 认知治理网关

> "The most successful LLM applications are those that treat the LLM as a component within a larger, well-engineered harness." 
> —— Inspired by Mitchell Hashimoto's philosophy of **Harness Engineering**.
> 
> “最成功的 LLM 应用，是那些将大模型视为一个更大、设计精密的‘治理装具’（Harness）中的组件的应用。”
> —— 灵感源自 Mitchell Hashimoto 的 **Harness Engineering** 哲学。

---

### 🧠 The Philosophy / 哲学：为什么需要 Meta-Router？

**The Problem / 痛点:**
Most OpenClaw users fall into the **"Skill Bloat Trap."** They install dozens of skills, thinking it makes the Agent smarter. In reality, it causes **Contextual Noise** and **Token Obesity**. Every query becomes slower, more expensive, and prone to "hallucinated cross-talk" between unrelated skills.
大多数 OpenClaw 用户都会掉进“技能膨胀陷阱”。安装几十个技能并不会让 Agent 变聪明，反而会导致**上下文噪音**和 **Token 肥胖**。每次提问都会变慢、变贵，并且容易在不相关的技能之间产生“幻觉串扰”。

**The Solution / 方案:**
**Meta-Router** is the harness. It is a specialized middleware that manages the LLM’s focus, ensuring it only "sees" the tools it needs for the specific task at hand.
**Meta-Router** 就是那个“治理装具”。它是一个专门的中间件，负责管理 LLM 的注意力，确保它只看到处理当前任务所需的工具。

---

### 🛠️ Core Architecture / 核心架构

Derived from the principles of **Harness Engineering**, Meta-Router operates in three phases:
基于 **Harness Engineering** 原理，Meta-Router 分三个阶段运行：

#### 1. Automated Discovery / 自动发现 (The Scan)
Meta-Router treats your skills directory as a dynamic filesystem. It doesn't wait for manual input; it **observes**. It uses system-level commands to map every `SKILL.md` into a lightweight, high-speed index.
Meta-Router 将你的技能目录视为动态文件系统。它不等待手动输入，而是主动**观察**。它使用系统级命令将每个 `SKILL.md` 映射到轻量级、高速的索引中。

#### 2. Intent Triage / 意图分拣 (The Dispatch)
Instead of loading 50KB of documentation upfront, Meta-Router intercepts your prompt and performs a **semantic triage** against the `.meta_index.json`. 
Meta-Router 不会预先加载 50KB 的文档，而是拦截你的提示词，并针对 `.meta_index.json` 进行**语义分拣**。
- **Lazy Loading**: Only the matched skill is mounted. / **按需加载**：仅挂载匹配的技能。

#### 3. Context Pruning / 上下文修剪 (The Clean-up)
Post-dispatch, Meta-Router explicitly instructs the system to ignore dormant metadata. This preserves your **Attention Window**.
分发后，Meta-Router 显式指令系统忽略不活跃的元数据，从而保护你的**注意力窗口**。

---

### 🚀 Features / 功能特性

* **Self-Healing Index / 自愈索引**: Automatically triggers a re-scan when new skills are detected. / 检测到新技能时自动触发重新扫描。
* **Shortcut Resolution / 快捷调用**: Support for the `L:` (Lawliet) prefix for 100% deterministic routing. / 支持 `L:` 前缀实现 100% 确定性路由。
* **Zero-Overhead Idle / 零开销待机**: Consumes negligible tokens when no specific skill is needed. / 无需特定技能时，消耗的 Token 几乎为零。

---

### 💻 Installation / 安装

```bash
clawhub install meta-router
🛠️ Operational Guide / 使用指南
Initialization / 初始化
To prime the harness for the first time / 首次初始化装具：

"Meta-Router, scan my library."

Automated Usage / 自动化使用
Just ask. The harness handles the rest / 直接提问，装具处理剩余工作：

User: "Analyze this 3D printer's nozzle design."
Router: [Internal Triage: Match found -> Mounting First-Principles Skill] ...

Manual Override / 手动覆盖 (Power User)
L: 48h [Topic] -> Force Meta-Learning mode. / 强制专家学习模式。

L: fp [Topic] -> Force Deconstruction mode. / 强制解构模式。

⚖️ License & Credits / 协议与致谢
Inspiration / 灵感: Conceptually inspired by Mitchell Hashimoto's work on LLM Harnessing.

License / 协议: MIT

Author / 作者: Lawliet

"Innovation is not about adding more; it is about knowing what to exclude."
“创新不在于增加更多，而在于知道剔除什么。”
