<p align="center">
  <img src="./Logo.png" width="120" alt="Lawliet OpenClaw Skills Logo">
</p>

OpenClaw-Skills-Lawliet 🛠️
别把 AI 当成高级荧光笔，把它当成你的认知杠杆。 Stop using AI as a high-end highlighter. Start using it as a cognitive lever.

📖 The Manifesto / 宣言
在信息过载的 2026 年，大多数 LLM 沦为了“礼貌的废话生成器”。如果你只想看高果糖浆式的总结，请离开。这里的工具只有一个目的：剥离表象，直抵原子真相。

These tools are built for the few who value logic, physical constraints, and atomic truths over polite, superficial filler. We don't just "chat"; we deconstruct and produce.

⚡ The Infrastructure / 核心底座
1. 🐝 Hive-Commander (The Action-Oriented Swarm)
1+5 分布式生产集群 / Distributed Action Kernel

开发理由 (Why): 单体模型在处理复杂、多维任务（如：同时写代码、测试和文档）时，逻辑密度会随 Context 增长剧烈下降，最终导致“认知崩坏”。

解决问题 (Pain Points): 解决了长文本推理的“降智”问题，以及 AI 无法同时处理多个垂直领域专业任务的局限。

解决思路 (Logic): 采用 1 Master + 5 Workers 的异步并行架构。主控节点负责拆解任务，5 个专家节点在独立的上下文中并行产出。

牛逼之处 (The Edge): 它不仅是“大脑”，更是“工作室”。它内置了 Dev-Mode（架构/代码/测试同步产出）和 Slide-Mode（逻辑/内容/设计同步填充），让 AI 真正具备了工业级的交付能力。

2. 🚦 Meta-Router (The Cognitive Gateway)
高性能调度网关 / High-Performance Performance Router

开发理由 (Why): 随着本地技能库（Skills）的增加，AI 会因为背诵过多的技能说明书而产生“Token 肥胖”，导致推理速度变慢且意图识别混乱。

解决问题 (Pain Points): 解决了“技能越多，AI 越笨”的悖论，节省 80% 以上的无效 Context 消耗。

解决思路 (Logic): 引入 Lazy Loading (按需加载) 机制。通过毫秒级的意图探测，只有在确定需要某个技能时，才将其逻辑挂载到当前对话中。

牛逼之处 (The Edge): 它是整个 Lawliet 军火库的“操作系统内核”。它让你的 Agent 能够挂载成百上千个技能而依然保持瞬时响应，实现真正的“认知零负担”。

🧰 The Arsenal / 认知军火库
3. 🧠 48h-Expert (The Meta-Learner)
领域架构与快速元学习 / Rapid Domain Architecture

开发理由 (Why): 在碎片化时代，人们习惯于碎片化学习，导致认知结构松散，无法建立领域深度。

解决问题 (Pain Points): 解决了“看了很多，但没懂底层逻辑”的问题。

解决思路 (Logic): 基于概念递归逻辑，强制 AI 寻找领域内支撑起 80% 结果的 20% “原子概念”，并绘制出这些概念之间的逻辑依赖图谱。

牛逼之处 (The Edge): 它交付的不是摘要，而是认知地图。它会告诉你：如果你想懂量化交易，你必须先击穿这三个数学模型。它是你 48 小时内降伏一个陌生领域的终极武器。

4. ⚖️ First-Principles (The BS-Detector)
原理审计与“智商税”检测器 / Technical Logic Audit

开发理由 (Why): 营销黑话泛滥。作为产品负责人，必须在 5 分钟内看穿一个所谓的“革命性技术”到底是真的突破，还是在物理边缘摩擦的骗局。

解决问题 (Pain Points): 戳穿那些用形容词堆砌的营销外壳，回归物理常识。

解决思路 (Logic): 强制剥离所有非名词/动词的修饰语，将产品声明简化为物理极限、材料成本和能量守恒等硬指标进行对撞。

牛逼之处 (The Edge): 它是最残酷的审计员。如果某个 3D 打印机宣称的速度违反了其步进电机的物理特性，这个技能会直接给出“逻辑不可行”的判决。它是为追求真相的专业人士准备的智力护身符。

🛡️ Security & Transparency / 安全与权限
"These tools have teeth." 为了实现极致性能，本库需要以下权限：

Python Execution (exec): Hive-Commander 必须运行异步 Python 脚本来驱动并发请求。

Shell Access (bash): Meta-Router 需要调用 ls/grep 实现技能索引自愈。

Cross-Directory Access: 指挥官节点需要读取技能目录来“动态招聘”专家。

🚀 Installation & Usage / 部署与武装
一键全量武装 (One-Click Arming)
Bash
clawhub install hive-commander meta-router 48h-expert first-principles
实战场景 (Action Scenarios)
集群模式: hive: 开发一个带 Web 界面的个人财务管理工具。

元学习: L: 48h 量化交易的底层逻辑。

审计: L: fp 某品牌“自研”高速 3D 打印算法。

Author: Lawliet-ai | License: MIT | Powered by OpenClaw 2026
