<p align="center">
  <img src="./Logo.png" width="120" alt="Lawliet OpenClaw Skills Logo">
</p>

# OpenClaw-Skills-Lawliet 🛠️

**Stop using AI as a high-end highlighter. Start using it as a cognitive lever.** **别把 AI 当成高级荧光笔，把它当成你的认知杠杆。**

---

## 📖 The Manifesto / 宣言

Most LLM summaries are like high-fructose corn syrup: sweet, but intellectually bankrupt. They tell you what you want to hear, not what is true. These tools exist for one purpose: to transform LLMs from polite parrots into **ruthless deconstruction engines**. 

在信息过载的时代，LLM 沦为了“礼貌的废话生成器”。这里的工具只有一个目的：**剥离表象，直抵原子真相。** 我们不需要复读机，我们需要在物理和逻辑边界上行走的残酷智囊。

---

## ⚡ The Infrastructure / 核心底座

### 1. 🐝 [Hive-Commander](./hive-commander) (The Action-Oriented Swarm)
**1+5 Distributed Production Kernel / 分布式生产集群**

* **The Why (背景):** Single-model reasoning density collapses as context grows. When you ask an AI to code, test, and write docs simultaneously, it chokes.  
    *单体模型在处理多维任务时，逻辑密度会随 Context 增长剧烈下降，最终导致认知崩坏。*
* **The Problem (解决的问题):** It eliminates the "Context Stupidity" of long-form tasks. No more hallucinated code or shallow research.  
    *解决了长文本推理的“降智”问题，以及单线程 AI 无法同时处理多维专业任务的局限。*
* **The Logic (解决思路):** A **1 Master + 5 Workers** asynchronous architecture. The Master deconstructs the mission; the Workers execute in isolated, high-density contexts.  
    *采用主从架构。主控拆解任务，5 个专家节点在独立上下文中并行产出，互不干扰。*
* **The Edge (牛逼之处):** It’s not just a "thinking" tool—it’s a **Production Studio**. With built-in **Dev-Mode** and **Slide-Mode**, it delivers actual codebases and presentation decks in parallel.  
    *它不仅是“大脑”，更是“工作室”。内置开发与 PPT 模式，让 AI 具备真正的工业级交付能力。**牛逼在它能直接帮你把活干了。***

### 2. 🚦 [Meta-Router](./meta-router) (The Cognitive Gateway)
**High-Performance Intent Router / 高性能调度网关**

* **The Why (背景):** "The Skill Paradox"—the more skills you install, the dumber your AI gets because it has to "memorize" every doc before every prompt, leading to **Token Obesity**.  
    *“技能悖论”：技能装得越多，AI 越笨。因为它在对话前要背诵全量说明书，导致响应变慢、意图混乱。*
* **The Problem (解决的问题):** Stops the AI from getting confused by too many instructions. Saves 80% of unnecessary context consumption.  
    *解决了“技能越多，AI 越笨”的悖论，节省 80% 以上的无效 Token 消耗。*
* **The Logic (解决思路):** **Lazy Loading via Intent Detection.** The Router intercepts your query, matches the intent, and mounts only the necessary skill logic.  
    *引入“按需加载”机制。毫秒级意图探测，只有确定需要某技能时，才挂载对应逻辑。*
* **The Edge (牛逼之处):** It’s the **Operating System Kernel** of your arsenal. It allows you to mount 100+ skills with **Zero Overhead**, keeping your Agent sharp and fast.  
    *它是军火库的操作系统内核。让你的 Agent 挂载成百上千个技能而依然保持瞬时响应。**牛逼在它让你的 AI 永远不会变慢。***

---

## 🧰 The Arsenal / 认知军火库

### 3. 🧠 [48h-Expert](./48h-expert) (The Meta-Learner)
**Rapid Domain Mapping / 领域架构与元学习**

* **The Problem:** Fragmented learning leads to superficial understanding. People read summaries but miss the underlying mental models.  
    *碎片化学习导致认知结构松散，无法建立领域深度。*
* **The Logic:** Forces the AI to identify the **Atomic Concepts** (the 20% of core knowledge driving 80% of results) and map their recursive dependencies.  
    *基于概念递归逻辑，强制 AI 寻找支撑领域的“原子概念”，并绘制逻辑依赖图谱。*
* **The Edge:** It delivers a **Cognitive Map**, not a summary. It tells you what you *must* understand to conquer a domain in 48 hours.  
    *交付的是认知地图。它会告诉你：如果你想懂量化交易，你必须先击穿这三个数学模型。**牛逼在它能瞬间让你变成懂行人。***

### 4. ⚖️ [First-Principles](./first-principles) (The BS-Detector)
**Truth Audit & Logic Verifier / 原理审计与“智商税”检测器**

* **The Problem:** Marketing hype is everywhere. We need to know in 5 minutes if a "revolutionary" tech is a breakthrough or a scam.  
    *营销黑话泛滥。我们需要快速看穿一个技术是真的突破，还是在物理边缘摩擦的骗局。*
* **The Logic:** Strips away all adjectives. Re-evaluates claims against **Physical Constants** and **Economic Realities**.  
    *剥离所有修饰语，将声明简化为物理极限、材料成本和能量守恒等硬指标进行对撞。*
* **The Edge:** It is the **Cruelest Auditor**. If a 3D printer's speed claim violates its motor torque limits, the verdict is "Logically Impossible."  
    *它是最残酷的审计员。如果声明违反了物理常识，直接判死刑。**牛逼在它是所有虚假宣传的噩梦。***

---

## 🛡️ Security & Transparency / 安全与权限说明

**"These tools have teeth."** To achieve this level of performance, the arsenal requires specific system permissions:  
这些工具是“带刺”的。为了实现极值的性能，它们需要以下权限：

1.  **Python Execution (exec)**: `Hive-Commander` runs async scripts to drive parallel production. 
2.  **Shell Access (bash)**: `Meta-Router` uses `ls/grep` for self-healing indexing of your skills.
3.  **Cross-Directory Access**: The Commander must "recruit" skills from your local directory to build the swarm.

**Lawliet's Verdict:** I build tools for those who trust logic over generic safety prompts. You can audit every line of code. If you want a "safe" toy, use a highlighter. If you want a harness for your mind, click Allow.  
*我为那些信任逻辑而非通用安全提示的人构建工具。你可以审计这里的每一行代码。如果你想要一个“安全”的玩具，去用荧光笔；如果你想要认知的治理装具，点击允许。*

---

## 🚀 Installation & Usage / 部署与武装

### One-Click Arming / 一键全量安装
```bash
clawhub install hive-commander meta-router 48h-expert first-principles

Action Scenarios / 实战指令
Swarm Mode: hive: Develop a personal finance tool with a Web UI.

Audit Mode: L: fp The authenticity of Brand X's "self-developed" high-speed printing algorithm.

Learning Mode: L: 48h The bottom-layer logic of Quantitative Trading.

Author: Lawliet-ai | License: MIT | Powered by OpenClaw 2026
