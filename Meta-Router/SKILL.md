Skill: Meta-Router-Automata (Hardened V2)
[Core Assertion]
System SHALL NOT initiate task execution until the Context-Skill-Alignment is verified. The Router acts as the mandatory kernel gateway.

1. State Integrity Assertions
A1 (Persistence): A hidden state file .meta_index.json MUST exist in the root.

A2 (Sync Policy): If hash(ls -R ~/.openclaw/skills/) changes, or .meta_index.json is null, the system MUST perform an immediate atomic scan.

A3 (Extraction Logic): Indexing is limited to [Folder_Name], [ID], and [Primary_Function]. High-density descriptions MUST be truncated to <128 chars during indexing to prevent token overflow.

2. Dispatching & Routing Assertions
B1 (Explicit Priority): Commands prefixed with ! or matching Shortcut_ID SHALL bypass semantic analysis and trigger immediate mounting.

B2 (Zero-Waste Routing): For ambiguous inputs, the system SHALL execute a keyword-overlap check against the index. FORBIDDEN: Do not mount more than 2 skills simultaneously unless Hive-Commander is invoked.

B3 (Dynamic Injection): Skill mounting MUST be volatile. Once a task is completed (detected by END_OF_WORKFLOW signal), the system SHALL prune the injected Skill metadata from the active context window.

3. Execution Constraints (Hard Limits)
C1 (Latency): Metadata scanning MUST complete within <200ms.

C2 (Memory): The .meta_index.json file size SHALL NOT exceed 4KB. If exceeded, the system MUST implement a "Most-Recently-Used" (MRU) eviction policy for the index.

C3 (Silence): All background indexing and pruning operations SHALL remain invisible to the user unless an I/O_ERROR is encountered.
