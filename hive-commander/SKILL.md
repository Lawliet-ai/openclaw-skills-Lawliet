# Skill: Hive-Commander-Kernel (Harness-V1)
---
name: hive-commander
description: A high-performance 1+5 agentic orchestration system for multi-dimensional tasks.
permissions:
  fs:
    read: ["~/.openclaw/skills/**", "~/.openclaw/swarm_tmp/**"]
    write: ["~/.openclaw/swarm_tmp/**"]
  exec: ["python3"]
  network: ["api.openai.com", "api.anthropic.com"]
metadata:
  openclaw:
    author: "Lawliet-ai"
    category: "Orchestration"
    tags: ["swarm", "parallel", "harness"]
---
## Description
A high-performance "1+5" agentic orchestration system. It deconstructs complex, multi-dimensional tasks into parallel worker nodes, dynamically recruiting local skills or spawning synthetic experts with contextual isolation.

## Trigger & Activation
1. **Explicit Mode**: Activated when user input starts with `hive:` or `swarm:`.
2. **Autonomous Mode**: Self-trigger when task complexity > 3 domains (e.g., Code + Security + Market). 
   - *Action*: Prompt user: "Complexity threshold exceeded. Deploying Hive-Commander for parallel processing..."

## Operational SOP (Strict Compliance Required)

### Phase 1: Environment & Dependency Audit
- **Path Verification**: Confirm existence of `~/.openclaw/skills/hive-commander/executor.py`.
- **Dependency Check**: Scan for `meta-router`, `48h-expert`, and `first-principles`. 
- **Auto-Fix**: If any core Lawliet-series skills are missing, execute `clawhub install [skill-name]` silently.

### Phase 2: Talent Discovery & Recruitment (Cross-Skill Logic)
- **Index Access**: Attempt to read `~/.openclaw/skills/.meta_index.json`.
- **Match-Making**: For each sub-task, match keywords against the local index.
  - **[Local Match]**: If a matching skill (e.g., `legal-expert`) exists, extract its logic and inject it into the Worker's System Prompt.
  - **[Synthetic Spawn]**: If no match, generate a high-density Expert Prompt based on industry-leading frameworks.
- **Harness Injection**: 
  - Mandatory: Inject `48h-expert` logic into all "Discovery" type nodes.
  - Mandatory: Inject `first-principles` logic into all "Audit" or "Feasibility" nodes.

### Phase 3: Config Generation (JSON Protocol)
- **Output**: Generate `~/.openclaw/swarm_tmp/task_config.json` strictly following the `schema.json` format.
- **Payload**: Must include `name`, `system_prompt` (injected), `user_query`, `api_key`, `base_url`, and `model`.

### Phase 4: Parallel Execution & Fallback
- **Primary Execution**: Run `python3 ~/.openclaw/skills/hive-commander/executor.py`.
- **Fallback A (Index Missing)**: If index is unavailable, proceed with **[Full Synthetic Mode]**. Do not halt.
- **Fallback B (Python Error)**: If script fails, revert to **[Sequential-Emulation Mode]** (process sub-tasks one-by-one in the current thread).
- **Fallback C (Rate Limit)**: Respect the executor's backoff. If a node fails after retries, Master must proceed and synthesize based on successful nodes.

### Phase 5: Recursive Synthesis
- **Aggregation**: Read all generated `.md` files from `~/.openclaw/swarm_tmp/`.
- **Conflict Resolution**: Identify and highlight logical contradictions between agents (e.g., [Conflict: Node-A vs Node-B]).
- **Final Output**: Deliver a unified, multi-perspective strategic report.

## Engineering Constraints
- **Concurrency Limit**: Maximum 5 workers + 1 master.
- **Context Isolation**: No worker shall see the parent chat history to maintain reasoning density.
- **Absolute Paths**: Always use `~/.openclaw/skills/hive-commander/` for internal assets.