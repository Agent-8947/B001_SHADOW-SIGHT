<div align="center">

<img src="logo.png" width="300" alt="Shadow-Sight Logo">

# Shadow-Sight

**Seeing through the digital fog of war.**

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Agent-8947/B001_SHADOW-SIGHT/blob/master/LICENSE)
[![NEXUS](https://img.shields.io/badge/NEXUS-Intelligence_Factory-DC1E1E.svg)](https://github.com/Agent-8947/B001_SHADOW-SIGHT)

---

*<div align="center"> **Seeing through the digital fog of war.** [![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org) [![License](https://img.shields.io/badge/license-MIT*

</div>

## Overview

Shadow Sight is an autonomous multi-layer intelligence pipeline built by the **NEXUS Intelligence Factory**. It ingests a target (domain, company, or individual), searches across multiple intelligence layers, and delivers a structured reconnaissance report — without human intervention.

## Modules

| Module | Description |
|--------|-------------|
| `breach_intel` | NEXUS Module: breach_intel — Breach detection via HIBP k-anonymity API. import h... |
| `domain_intel` | NEXUS Module: domain_intel — Passive OSINT via Python stdlib DNS & SSL.  import ... |
| `endpoint_monitor` | NEXUS Module: endpoint_monitor — HTTP endpoint monitor with concurrent probing. ... |
| `identity_profiler` | NEXUS Module: identity_profiler — Username presence across 15 platforms. import ... |
| `network_recon` | NEXUS Module: network_recon — Subdomain discovery via crt.sh CT logs.  import js... |
| `security_analyzer` | NEXUS Module: security_analyzer Passive OSINT analyzer — IP resolution, HTTPS ch... |
| `shadow_cli` | NEXUS SHADOW SIGHT — Ultimate OSINT Engine Dynamically loads and coordinates all... |
| `web_crawler` | NEXUS Module: web_crawler — Basic Web Crawler (Extracts Title & Links). import u... |

## Quick Start

```bash
# Clone
git clone https://github.com/Agent-8947/B001_SHADOW-SIGHT.git
cd B001_SHADOW-SIGHT

# Install dependencies
pip install -r requirements.txt

# Run the full pipeline
python src/shadow_cli.py example.com
```

## What You Need to Provide

- Full name of a person  (e.g.  John Smith)
- OR  company name  (e.g.  Acme Corp)
- OR  domain / website  (e.g.  acmecorp.com)
- OR  email address  (e.g.  john@acmecorp.com)
- Optional: phone number, city, known aliases

## Requirements

- Python 3.10+
- Windows / Linux / macOS
- Internet connection (for reconnaissance)
- 4 GB RAM minimum

## Architecture

```
┌─────────────────────────────────────────────┐
│              SHADOW CLI (Orchestrator)       │
├─────────┬─────────┬─────────┬───────────────┤
│ Domain  │   SSL   │   Web   │   Security    │
│  Intel  │ Scanner │ Crawler │   Analyzer    │
├─────────┼─────────┼─────────┼───────────────┤
│ Breach  │ Social  │ Entity  │   ... more    │
│  Intel  │Profiler │ Mapper  │   plugins     │
└─────────┴─────────┴─────────┴───────────────┘
         ↓ JSON Report + Logs ↓
```

## Output

All results are saved as structured JSON reports in the `logs/` directory with timestamps.

## Built With

- **NEXUS Intelligence Factory** — Autonomous agent-based code synthesis
- **Python 3.10+** — Core runtime
- **PIL / Pillow** — Logo generation
- **Standard Library** — `ssl`, `socket`, `http.client`, `json`, `threading`

## License

MIT — See [LICENSE](https://github.com/Agent-8947/B001_SHADOW-SIGHT/blob/master/LICENSE) for details.

---

<div align="center">
<sub>Synthesized by <b>NEXUS Agent 11</b> · Validated by <b>Agent 16</b> · Branded by <b>Agent 13</b> · Profiled by <b>Agent 17</b></sub>
</div>
