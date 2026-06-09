# 📋 Microsoft Build 2026 — Comprehensive Source Index & Gap Analysis

> Cross-referenced against [Matt Hansen's Build 2026 List](https://github.com/matthansen0/matts-build-2026-list) (132 announcements as of June 4, 2026)

---

## 🔗 Primary Official Sources

### Tier 1 — Microsoft Official Hubs
| Source | URL | Description |
|--------|-----|-------------|
| **Build 2026 News Hub** | https://news.microsoft.com/build-2026/ | Official landing page for all Build announcements |
| **Build 2026 Live Blog** | https://news.microsoft.com/build-2026-live-blog/microsoft-build-2026-live/ | Real-time coverage and session summaries |
| **Build26-news GitHub Repo** | https://github.com/microsoft/Build26-news | Official structured index — 94KB `news.md` with 134+ extracted statements |
| **Azure Updates** | https://azure.microsoft.com/en-us/updates/ | Filterable list of all Azure service updates |
| **Book of News (OMB Blog)** | https://aka.ms/AA10pe80 | Main developer keynote blog (38 statements) |

### Tier 2 — Hero Blogs (Major Themes)
| Blog | URL | Topic | Statements |
|------|-----|-------|------------|
| Quantum + Discovery | https://aka.ms/AA10vjcq | Majorana 2, Microsoft Discovery | 17 |
| Enterprise Agent Platform | https://aka.ms/AA1188jd | Agent Platform architecture (Jay Parikh) | 22 |
| Windows for Developers | https://aka.ms/Windows-Build2026 | Windows agent platform, MXC, Solara | 42 |
| Microsoft AI Models | http://aka.ms/MAI-Build | MAI model family, Frontier Tuning | 15 |

### Tier 3 — Product-Specific Blogs
| Product Area | URL | Key Topics |
|-------------|-----|------------|
| Azure Cobalt 200 VMs | https://aka.ms/Cobalt200VMs | Arm-based VMs, 50% perf uplift |
| Azure HorizonDB | https://aka.ms/HorizonDB-Build-blog | Enterprise Postgres for AI |
| Web IQ | https://aka.ms/nextgengrounding | AI-native grounding APIs |
| Foundry IQ | https://aka.ms/FoundryIQ | Serverless context retrieval |
| Microsoft Foundry Recap | https://aka.ms/FoundryBuildNews | Hosted agents, Toolboxes, Voice Live |
| Fabric & Databases | https://aka.ms/Azure-Data-Build26 | Rayfin, GPU warehouse, Cosmos DB |
| GPU-Accelerated Warehouse | https://aka.ms/GPUAcceleratedFabricDW | 7x faster, SIGMOD best paper |
| Work IQ APIs | https://aka.ms/MBJ02yr26 | 10 generic MCP tools, Context API |
| GitHub Copilot App | https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/ | Agent-native desktop, canvases |
| Frontier Tuning | https://aka.ms/frontiertuningblog | RL in compliance boundary |
| Surface RTX Spark | https://blogs.windows.com/devices/?p=263819 | 1 petaflop, 128GB unified memory |
| Windows 365 at Build | https://aka.ms/W365Build26Blog | W365 for Agents GA, Dev Box |
| Project Solara | https://aka.ms/ProjectSolaraBuild2026 | Agent-first device platform |
| ASSERT Framework | https://commandline.microsoft.com/assert-written-intent-executable-evals/ | Spec-driven agent evaluation |
| Agent Control Spec | https://commandline.microsoft.com/agent-control-specification-runtime-governance/ | Runtime governance for agents |
| Microsoft Scout | https://aka.ms/ProjectLobster-Blog | First autopilot agent |
| Mayo Clinic AI Model | https://news.microsoft.com/source/?p=24971 | Frontier healthcare AI |
| Responsible AI in Foundry | https://aka.ms/BuildFoundryRAI | ASSERT, ACS, guardrails |
| Majorana 2 | https://aka.ms/m2blog | Quantum chip deep dive |
| Microsoft Discovery | https://aka.ms/MicrosoftDiscoveryBlog | Agentic AI for R&D |

---

## 🟣 Power Platform Sources (Missing from Matt's List)

Matt's list has **zero Power Platform announcements**. These are all net-new additions.

### Official Microsoft Sources
| Source | URL |
|--------|-----|
| **Power Platform Blog (May 2026 Update)** | https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/ |
| **Power Platform 2026 Release Wave 1** | https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/ |
| **Copilot Studio Blog** | https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/ |
| **Power Pages Release Plan** | https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-pages/planned-features |
| **Power Apps Blog** | https://powerapps.microsoft.com/en-us/blog/ |
| **Power Automate Blog** | https://powerautomate.microsoft.com/en-us/blog/ |
| **Power BI Blog** | https://powerbi.microsoft.com/en-us/blog/ |

### Power Apps Announcements
| Announcement | Description | Status |
|-------------|-------------|--------|
| Generative Pages for model-driven apps | AI generates React/TypeScript pages from natural language descriptions | GA (US), expanding globally |
| Code Apps (React/Vue/Blazor) | Pro-code apps run natively in Power Platform with full ALM | GA |
| External code gen tool integration | Build generative pages with GitHub Copilot CLI, Claude Code | GA globally |
| M365 Copilot in model-driven apps | Summarize data, visualize trends, take actions inside apps | GA |
| Power Fx User Defined Types | Custom types for stronger data validation | GA |
| Agent Feed in model-driven apps | Transparency-focused task board for agent/task management | Preview |
| Modernized default UI | Refreshed navigation and theming for model-driven apps | Rolling out |
| Smarter search | Fuzzy-matching search in grids and lookups | GA |

### Power Automate Announcements
| Announcement | Description | Status |
|-------------|-------------|--------|
| Self-healing desktop flows | RPA flows adapt automatically to application UI changes | Preview |
| Copilot Studio-powered actions | AI agents author, optimize, and fix cloud/desktop flows | Preview |
| Object-centric process mining | Deeper analytics into business processes | Preview |
| Restore deleted flows | Recover accidentally deleted cloud flows | GA July 2026 |
| Desktop flow version control | Source control for desktop automation flows | GA May 2026 |
| Schedule desktop flows directly | Run desktop flows on a schedule without cloud triggers | GA May 2026 |
| Video logs for unattended runs | Visual debugging for RPA automation | GA July 2026 |
| Visualize flows as flowcharts | Desktop flows rendered as visual flowcharts | GA July 2026 |
| Python script version alignment | Python scripts updated to current Python versions | GA |

### Copilot Studio Announcements
| Announcement | Description | Status |
|-------------|-------------|--------|
| Computer-using agents GA | Automate websites and desktop apps via UI — first major cloud provider | GA (all geographies) |
| Redesigned workflows experience | Unified visual canvas mixing APIs, approvals, UI tasks, AI steps | GA |
| Real-time voice agents | Voice capabilities via Dynamics 365 Contact Center (NA) | GA (North America) |
| Multi-LLM support for CUA | Supports OpenAI CUA, Claude Sonnet 4.5 for computer-using agents | GA |
| Azure Key Vault credential mgmt | Secure credential storage for computer-using agents | GA |
| Purview audit logging for agents | Compliance audit trail for agent actions | GA |
| Human-in-the-loop governance | Configurable review checkpoints for agent workflows | GA |
| Agent-to-agent communication | Multi-agent orchestration for complex enterprise solutions | Preview |

### Power BI Announcements
| Announcement | Description | Status |
|-------------|-------------|--------|
| Copilot summary shortcuts | AI-driven insight shortcuts in report ribbon and visual header | GA May 2026 |
| Visual calculations & custom totals | Flexible in-report summarization | GA |
| New Get Data experience | Streamlined data import in Power BI Desktop | Preview |
| Conversational Copilot on mobile | Ask plain-language questions, get AI-generated visuals on phone | GA April 2026 |
| Direct Lake calculated columns | Work without full refresh for large datasets | GA |
| Base theme switcher | Better brand consistency in reports | GA |

### Power Pages Announcements
| Announcement | Description | Status |
|-------------|-------------|--------|
| AI agentic site scaffolding | Describe requirements → AI generates Dataverse schema, forms, flows | Preview |
| Copilot CLI & Claude Code plugins | Build, secure, deploy Power Pages sites with AI coding tools | GA |
| Security Agent | AI scans for threats (phishing, DDoS, misconfigurations) | Preview |
| Native deployment pipelines | End-to-end CI/CD for portal promotion | GA |
| Unified authorization | Links web roles and Dataverse security roles | GA |
| Site analytics & server logging | Track page views, form usage, errors in Power Pages Monitor | GA |
| Secure server-side logic | Custom server-side code with data protection | GA |

---

## 🤖 AI Agents & M365 Copilot Sources (Partially in Matt's List)

### Agent 365 Resources
| Source | URL |
|--------|-----|
| **Agent 365 Official Resources** | https://microsoft.github.io/agent-resources/agent365/ |
| **Agent 365 GA Blog** | https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ |
| **Agent 365 Tech Community** | https://techcommunity.microsoft.com/t5/ai-copilot-bg/microsoft-agent-365-resources/ba-p/4179477 |

### Missing from Matt's List — AI & Agents
| Announcement | Description | Source |
|-------------|-------------|--------|
| Microsoft IQ (unified context layer) | Connects Work IQ + Fabric IQ + Foundry IQ + Web IQ | OMB Blog |
| Fabric IQ GA | Shared semantic foundation over structured business data | OMB Blog |
| ASSERT framework | Open-source spec-driven agent evaluation | commandline.microsoft.com |
| Agent Control Specification | Open spec for runtime governance (8 interception points) | commandline.microsoft.com |
| Fireworks AI on Foundry GA | Faster inference with enterprise governance | OMB Blog |
| Microsoft Agent Framework | Provider-neutral agent architecture (open source) | commandline.microsoft.com |
| Agent 365 SDK (free, GA) | Build/onboard/govern agents of any stack | Agent 365 blog |
| Agent 365 for local agents | Observe/govern 20+ types of local agents | OMB Blog |
| Foundry Toolkit for VS Code GA | IDE tooling for agent development | Foundry recap blog |
| Voice Live GA | Unified real-time conversational API | Foundry recap blog |
| Agent Optimizer in Foundry | Converts failures to ranked improvements | Foundry recap blog |
| Copilot Credits | Unified consumption meter for agent tasks | M365 blog |

### Missing from Matt's List — M365 Copilot
| Announcement | Description | Source |
|-------------|-------------|--------|
| Work IQ APIs GA (June 16) | 10 generic MCP tools, Context API, digital workspaces | Work IQ blog |
| Microsoft IQ GA | Unified context layer across GitHub Copilot, Foundry, Copilot Studio | OMB Blog |
| Frontier Tuning in Copilot Studio | RL within compliance boundary for custom model training | Frontier Tuning blog |
| M365 E7 SKU | Bundles Agent 365 + Copilot + Entra Suite | Enterprise announcements |

---

## 🖥️ Windows & Developer Tools (Partially in Matt's List)

### Missing from Matt's List
| Announcement | Description | Source |
|-------------|-------------|--------|
| Coreutils for Windows GA | Linux-like CLI utilities (Rust, from uutils) | Windows blog |
| WSL Containers | Built-in Linux container runtime (CLI + API) | Windows blog |
| Windows Developer Configurations | One-command dev environment setup via WinGet | Windows blog |
| Intelligent Terminal | Context-aware agent integration in terminal | Windows blog |
| Windows Development Skills GA | Structured knowledge for WinUI3 app development | Windows blog |
| Aion 1.0 Instruct | On-device SLM for text intelligence (open weights) | Windows blog |
| Aion 1.0 Plan | 14B parameter reasoning/tool-calling model (in-box) | Windows blog |
| Windows AI APIs expansion | Speech recognition on NPU/CPU, Video Super Res on CPU | Windows blog |
| DGX Station for Windows | 1T parameter desktop AI supercomputer (GB300) | Windows blog |
| Windows post-quantum cryptography | PQC support in TLS, CNG, ADCS | Windows blog |
| Smart App Control expansion | Reputation-based enforcement across millions of devices | Windows blog |
| GitHub Copilot CLI /fleet | Selective task delegation to local models | Windows blog |
| GitHub Copilot SDK GA | Node.js, Python, Go, .NET, Rust, Java SDKs | GitHub blog |
| Copilot code review medium tier | Higher-reasoning model for PR reviews | GitHub blog |
| Microsoft Store updates | Entra ID onboarding, faster certification, real-time analytics | Windows blog |

---

## 📰 Third-Party Comprehensive Roundups

| Source | URL | Coverage |
|--------|-----|----------|
| 4sysops | https://4sysops.com/archives/microsoft-build-2026-product-announcements/ | Full product announcements |
| eWeek | https://www.eweek.com/news/microsoft-build-2026-ai-agent-stack-neuron/ | AI agent stack deep dive |
| Analytics India Magazine | https://analyticsindiamag.com/ai-trends/everything-microsoft-announced-at-build-2026 | Complete announcement list |
| The Neuron | https://www.theneuron.ai/explainer-articles/everything-microsoft-announced-at-microsoft-build-2026-explained/ | Explained announcements |
| EPCGroup Enterprise Recap | https://www.epcgroup.net/blog/microsoft-build-2026-enterprise-recap-key-announcements | Enterprise focus |
| VladTalksTech M365 Recap | https://vladtalkstech.com/microsoft-365/microsoft-365-conference-2026-recap/ | M365 Conference recap |
| A Guide to Cloud | https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/ | AI announcements recap |
| ChatForest Recap | https://chatforest.com/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/ | Windows + Copilot deep dive |
| 365 Mechanix | https://www.365mechanix.com/blogs/2026/power-platform-2026-wave-1-your-complete-guide-to-the-latest-updates/ | Power Platform complete guide |
| CRM Software Blog | https://www.crmsoftwareblog.com/2026/04/microsoft-power-platform-2026-release-wave-1-a-structured-deep-dive/ | Power Platform deep dive |
| Rand Group | https://www.randgroup.com/insights/microsoft/power-platform/microsoft-power-platform-2026-release-wave-1-what-it-means-for-your-business/ | Power Platform business impact |

---

## 📊 Gap Summary

| Category | In Matt's List | Found Missing | Total Known |
|----------|---------------|---------------|-------------|
| 🏗️ Hardware & Infrastructure | ~25 | ~5 | ~30 |
| 🔧 Apps & Development | ~35 | ~15 | ~50 |
| 📊 Data & Analytics | ~30 | ~3 | ~33 |
| 🤖 AI & Agents | ~30 | ~15 | ~45 |
| 🔒 Security & Governance | ~12 | ~5 | ~17 |
| 🟣 **Power Platform** (NEW) | **0** | **~30** | **~30** |
| 🖥️ **Windows & Dev Tools** (NEW) | **0** | **~15** | **~15** |
| **TOTAL** | **132** | **~88** | **~220** |

> **Key Finding**: Matt's list is missing the entire **Power Platform** category (~30 announcements across Power Apps, Power Automate, Copilot Studio, Power BI, and Power Pages) and most **Windows developer platform** announcements (~15 items). These represent significant gaps for enterprise developers.
