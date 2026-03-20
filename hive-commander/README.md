# Hive-Commander: Distributed Intelligence Kernel

A production-grade "1+5" asynchronous agentic harness for OpenClaw. Designed for complex research, development, and auditing tasks requiring parallelized reasoning.

### Technical Architecture
- **Orchestration**: Implements a Master-Worker pattern with 5 parallel processing nodes.
- **Session Inheritance**: Automatically propagates API credentials and model configurations from the parent session to child workers, ensuring seamless execution.
- **Dynamic Mounting**: Utilizes `meta-router` for just-in-time skill injection into specialized worker nodes.

### Security Protocols
- **Workspace Isolation**: Operations are strictly restricted to `~/.openclaw/`. No access permitted to system-level sensitive directories (SSH, AWS, etc.).
- **Data Transparency**: All intermediate worker outputs remain accessible in `~/.openclaw/swarm_tmp/` for auditing and manual verification.
- **Zero-Telemetry**: No external data exfiltration; execution is strictly limited to user-defined API endpoints.

### Usage
Trigger the swarm using `hive:` or `swarm:` prefixes.
*Example: `hive: Perform a 5-layer deep audit of the current supply chain compliance protocols.`*

### Dependencies
- `meta-router`: Required for skill discovery and indexing.
- `executor.py`: Required for asynchronous process management.

---
Author: Lawliet | License: MIT
