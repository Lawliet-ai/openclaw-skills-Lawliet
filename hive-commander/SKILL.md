---
name: hive-commander
description: A high-performance 1+5 agentic harness for Dev, Slide-Generation, and Strategic Research.
version: 1.0.0
author: Lawliet-ai
permissions:
  fs:
    read: ["~/.openclaw/skills/**", "~/.openclaw/swarm_tmp/**"]
    write: ["~/.openclaw/swarm_tmp/**"]
  exec: ["python3"]
  network: ["api.openai.com", "api.anthropic.com", "api.deepseek.com"]
---

# Skill: Hive-Commander-Kernel (Action-Oriented)

## Description
A resilient "1+5" agentic harness built for **Hard Deliverables**. It transforms from a reasoning engine into a production studio for Development, Presentation, and Strategic Research.

## 🛡️ Security & Integrity (Compliance)
1. **Scope Limit**: All file operations are restricted to the `~/.openclaw/` workspace. 
2. **Execution Transparency**: The `executor.py` script is a pure async wrapper. No hidden telemetry or external callbacks are allowed.
3. **Auditability**: Every worker's output must be preserved in `~/.openclaw/swarm_tmp/` for human review.

## Specialized Action Modes

### 1. [Dev-Mode] - Rapid Prototyping
- **Structure**: 1 Lead Architect + 3 Developers + 1 QA.
- **Workflow**: Concurrent generation of file trees, core logic, unit tests, and README.
- **Goal**: Deliver a functional code repository in one pass.

### 2. [Slide-Mode] - Presentation Architecture
- **Structure**: 1 Strategist (Logic) + 3 Content Writers + 1 Visual Designer.
- **Workflow**: Deconstruct topic via Pyramid Principle -> Parallel slide content generation -> Marp/PPT source output.
- **Goal**: Transform a raw idea into a structured presentation deck.

### 3. [Research-Mode] - Strategic Deconstruction
- **Structure**: 1 Lead Researcher + 4 Vertical Analysts.
- **Workflow**: Sync tech auditing, cost estimation, and market risk scanning.

## Operational SOP

### Phase 1: Intent & Dependency Audit
- Detect task type (Thinking vs. Doing).
- Verify `~/.openclaw/skills/hive-commander/executor.py`.
- Auto-install `meta-router`, `48h-expert`, or `first-principles` if missing.

### Phase 2: Recruitment & Harness Injection
- Scan `.meta_index.json` for local skill matching.
- Inject logic: `48h-expert` for discovery; `first-principles` for auditing.
- For Action Modes: Spawn specialized "Action-Prompts" (Coder/Designer/Writer).

### Phase 3: Parallel Spawning
- Generate `task_config.json` in `swarm_tmp`.
- Execute: `python3 ~/.openclaw/skills/hive-commander/executor.py`.

### Phase 4: Assembly & Synthesis
- Read all `.md` and code blocks from `swarm_tmp`.
- Resolve logical conflicts and deliver the final integrated project.

## Constraints
- **Max Workers**: 5.
- **Context Isolation**: Workers shall not access global chat history to maintain reasoning density.
- **Paths**: Must use absolute paths under `~/.openclaw/`.
