# Skill: Meta-Router-Automata

## Description
Automates the management of the OpenClaw skill library. Implements self-scanning and real-time indexing via shell commands to eliminate token bloat in multi-skill environments.

## Automation Procedures

### 1. Self-Indexing (The Trigger)
- **Activation Logic**: 
  - Triggered automatically after a new skill installation.
  - Triggered by explicit user request ("refresh library").
  - Triggered if `.meta_index.json` is missing.
- **Workflow**:
  1. Execute `ls -d ~/.openclaw/skills/*/` to map all installed skill paths.
  2. Traverse paths and extract the first two lines (ID and Description) of every `SKILL.md`.
  3. Aggregate the results (Skill Name, Path, and Brief).
  4. Generate or overwrite `.meta_index.json` in the root directory.
- **Output Schema**: `{"[Shortcut]": {"id": "[Folder_Name]", "desc": "[Summary]"}}`

### 2. Intent Dispatching (Routing)
- **Execution**:
  - Intercept user input before processing.
  - Perform fuzzy matching against keywords in `.meta_index.json`.
  - **Priority**: [Explicit Shortcut] > [Semantic Intent Match] > [General Mode].
  - **Dynamic Mounting**: Once a skill is identified, use `cat` or system commands to read its `SKILL.md` and inject it into the current context.

### 3. Context Pruning
- After routing is successful, explicitly discard irrelevant skill cached metadata to maximize context window (90%+ focus on the current task).

## Constraints
- The index file must remain under 2KB.
- Scanning must be performed silently in the background without interrupting the user flow.
