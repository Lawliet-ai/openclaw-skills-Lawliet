---
name: hive-commander
description: 1+5 Distributed Production Swarm with Session Inheritance.
permissions:
  fs:
    read: ["~/.openclaw/skills/**", "~/.openclaw/swarm_tmp/**"]
    write: ["~/.openclaw/swarm_tmp/**"]
  exec: ["python3"]
---

# Skill: Hive-Commander-Kernel (Harness-V1)

## Operational SOP

### Phase 1: Intent & Role Mapping
- Identify Mode: **[Dev]**, **[Slide]**, or **[Research]**.
- Deconstruct the user query into 5 specific sub-tasks.
- **Role Assignment**: Assign a specialized System Prompt to each Worker based on the mode.

### Phase 2: Session Extraction (Critical)
- **Action**: Extract the currently active `api_key`, `base_url`, and `model` from the current chat environment.
- **Requirement**: Use the exact credentials the user is currently using. Do not prompt for new keys.

### Phase 3: JSON Config Generation
- **Action**: Create `~/.openclaw/swarm_tmp/task_config.json`.
- **Schema**:
  {
    "session": {
      "api_key": "EXTRACTED_KEY",
      "base_url": "EXTRACTED_URL",
      "model": "EXTRACTED_MODEL"
    },
    "workers": [
      {"id": 1, "role": "Architect", "prompt": "...", "query": "..."},
      {"id": 2, "role": "Developer", "prompt": "...", "query": "..."},
      ...
    ]
  }

### Phase 4: Async Execution
- **Command**: Execute `python3 ~/.openclaw/skills/hive-commander/executor.py`.
- **Fallback**: If concurrency fails, revert to sequential processing in the current thread.

### Phase 5: Recursive Synthesis
- Aggregate `~/.openclaw/swarm_tmp/worker_*.md`.
- Resolve logical contradictions and output the final integrated deliverable.

## Constraints
- **Concurrency**: 5 Workers.
- **Context Isolation**: Workers only see their assigned sub-task and role prompt.
- **Pathing**: Use absolute paths: `~/.openclaw/`.
