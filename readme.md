# 🚀 Matt's List of Build 2026 Azure Announcements

This is a personal collection of announcements and updates from **Microsoft Build 2026**, organized by service category for navigation and reference.

**Last Updated:** June 3, 2026

**🎯 What's Inside:** 100+ announcements across Infrastructure, Apps, Data, AI, and Security with direct links to official documentation and blog posts.

---

## 📋 Table of Contents

- [🏗️ Azure Infrastructure](#-azure-infrastructure)
- [🔧 Azure Apps](#-azure-apps)
- [📊 Azure Data](#-azure-data)
- [🤖 Azure AI](#-azure-ai)
- [🔒 Security & Governance](#-security--governance)

---

## 🏗️ Azure Infrastructure

> *Core infrastructure services, compute, storage, operations, resiliency, and foundational Azure capabilities*

### Key Announcements

- **Compute and hardware:**
    - [Azure Cobalt 200 VMs](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/)  
      *Arm-based VMs optimized for scale-out, Linux-based, agentic AI workloads.*
    - [Cobalt 200 VM series update](https://azure.microsoft.com/updates?id=564451)  
      *Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series preview.*
    - [Guest RDMA for Azure Boost](https://techcommunity.microsoft.com/blog/azurecompute/announcing-preview-of-guest-rdma-for-azure-boost/4524589)  
      *Low-latency RDMA networking inside guest VMs.*
    - [Lasv5 and Laosv5 VMs](https://techcommunity.microsoft.com/blog/azurecompute/announcing-preview-of-new-azure-lasv5-and-laosv5-vms-based-on-the-amd-epyc%E2%84%A2-%E2%80%98tur/4522407)  
      *AMD EPYC Turin storage-optimized VM preview.*
    - [Azure Linux 4.0](https://azure.microsoft.com/updates?id=564543)  
      *Azure Linux 4.0 for VMs and VM Scale Sets.*
    - [Surface RTX Spark Dev Box and DGX Station for Windows](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/)  
      *NVIDIA-powered local AI and agent development hardware.*
    - [Project Solara](https://commandline.microsoft.com/project-solara-build-2026/)  
      *Chip-to-cloud platform for agent-first devices, just-in-time UI, enterprise manageability, and new stationary/portable form factors for agent-driven experiences.*

- **Azure Local, Arc, and edge:**
    - [Small form factor infrastructure](https://techcommunity.microsoft.com/blog/azurearcblog/embed-intelligence-into-physical-systems-with-smaller-form-factor-infrastructure/4524876)  
      *Azure-managed small form factor bare-metal edge infrastructure with Provisioned Machine, Foundry Local, AKS on bare metal, and IoT Operations.*
    - [Foundry Local on Azure Local for sovereign AI](https://techcommunity.microsoft.com/blog/azurearcblog/build-deploy-and-govern-sovereign-ai-with-foundry-local-on-azure-local/4522945)  
      *Sovereign AI, multi-node support, vLLM models, local Microsoft 365 retrieval, and GitHub Enterprise Local preview.*
    - [Foundry Local multi-node inference and vLLM](https://techcommunity.microsoft.com/blog/azurearcblog/scale-on-prem-ai-with-foundry-local-on-azure-local-multi-node-inference-and-vllm/4516692)  
      *Production-scale on-prem AI inference.*
    - [GitHub Enterprise Local](https://techcommunity.microsoft.com/blog/azurearcblog/introducing-github-enterprise-local-preview-devops-for-sovereign-and-private-clo/4523046)  
      *DevSecOps lifecycle on Azure Local for sovereign and air-gapped environments.*
    - [Agentic retrieval in Foundry Local](https://techcommunity.microsoft.com/blog/azurearcblog/unlock-on-prem-productivity-with-agentic-retrieval-in-foundry-local/4523646)  
      *RAG at the edge using local Microsoft 365 data.*

- **Storage and migration:**
    - [Azure Files on macOS with Entra ID](https://techcommunity.microsoft.com/blog/azurestorageblog/secure-modern-access-to-azure-files-on-macos-with-ms-entra-id/4524077)  
      *Identity-based Azure Files access from macOS.*
    - [File share centric management model](https://techcommunity.microsoft.com/blog/azurestorageblog/simpler-scalable-file-share-management-in-azure---now-generally-available/4523035)  
      *Top-level Azure Files resource model with per-share RBAC, encryption, private endpoints, and Bicep/ARM support.*
    - [File share migrations with Azure Copilot Migration Agent](https://techcommunity.microsoft.com/blog/azurestorageblog/file-share-migrations-simplified-with-azure-copilot-migration-agent/4524563)  
      *Agentic SMB/NFS to Azure Files and blob-to-blob migration workflows.*

- **Observability and resiliency:**
    - [What's new in Observability at Build 2026](https://techcommunity.microsoft.com/blog/azureobservabilityblog/what%E2%80%99s-new-in-observability-at-build-2026/4524927)  
      *Azure Monitor rollup for agent observability, SLI/SLO, Prometheus, alerts, OTLP ingestion, OTel, and transformations.*
    - [Azure Monitor Copilot Observability Agent](https://techcommunity.microsoft.com/blog/azureobservabilityblog/azure-monitor-copilot-observability-agent-what%E2%80%99s-new-at-build/4522927)  
      *Expanded investigation entry points, cross-resource analysis, Foundry integration, and shareable investigations.*
    - [Direct OpenTelemetry ingestion](https://techcommunity.microsoft.com/blog/azureobservabilityblog/direct-opentelemetry-ingestion-into-azure-monitor-is-now-generally-available/4524044)  
      *Direct OTLP ingestion for metrics, logs, and traces.*
    - [Monitor AI coding agents with OpenTelemetry](https://techcommunity.microsoft.com/blog/azureobservabilityblog/monitor-ai-coding-agents-with-opentelemetry-in-azure-monitor/4524049)  
      *Observability for GitHub Copilot, Claude Code, and Codex.*
    - [Azure Monitor agent observability](https://techcommunity.microsoft.com/blog/azureobservabilityblog/new-capabilities-to-observe-agents-in-azure-monitor/4524896)  
      *Agent fleet views, automated evaluations, cost breakdown, and traces.*
    - [Monitoring Coverage](https://techcommunity.microsoft.com/blog/azureobservabilityblog/is-your-monitoring-actually-working-whats-new-in-monitoring-coverage/4524619)  
      *Data flow validation and at-scale recommended alerts for VMs and AKS.*
    - [Multi-stage transformations for Azure Monitor DCRs](https://techcommunity.microsoft.com/blog/azureobservabilityblog/is-94-of-your-syslog-just-noise-now-you-can-filter-it-out-before-ingestion-/4524600)  
      *Filter, parse, and aggregate telemetry before ingestion.*
    - [Azure Infrastructure Resiliency Manager](https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/announcing-azure-infrastructure-resiliency-manager-public-preview/4523710)  
      *Resilience workflow across Availability Zones, Advisor, Chaos Studio, Azure Monitor, and Azure Copilot.*
    - [Kubernetes Center security and version insights](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/kubernetes-center-security--ltsout-of-support-version-insights-now-available/4524567)  
      *AKS fleet security posture and version support visibility.*

---

## 🔧 Azure Apps

> *Application development, deployment, integration, SRE agents, and developer platform services*

### Key Announcements

- **Azure Functions and SRE Agent:**
    - [azure-functions-skills](https://devblogs.microsoft.com/azure-sdk/introducing-azure-functions-skills-ai-era-workspace)  
      *Skills, MCP configuration, hooks, and instructions for agent-assisted Azure Functions development.*
    - [Azure Functions Serverless Agents Runtime](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-the-azure-functions-serverless-agents-runtime-preview/4523804)  
      *Markdown-first programming model for AI agents on Azure Functions.*
    - [Go support in Azure Functions](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-go-support-in-azure-functions-preview/4523801)  
      *First-class Go support on Flex Consumption.*
    - [Azure Functions MCP Extension](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-mcp-extension-whats-new-at-build-2026/4524099)  
      *MCP tools, resources, prompts, apps, auth, and schemas for Azure Functions.*
    - [Managed Connectors for Azure Functions](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-managed-connectors-for-azure-functions-preview/4523798)  
      *1,400+ managed connectors as first-class triggers and typed SDKs.*
    - [Azure SRE Agent at Build 2026](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-at-microsoft-build-2026-bringing-agentic-operations-to-the-enter/4524669)  
      *Enterprise SRE Agent releases for VNet integration, managed connectors, permissions, GitHub Enterprise, and private plugins.*
    - [SRE Agent VNet integration](https://techcommunity.microsoft.com/blog/appsonazureblog/vnet-integration-for-azure-sre-agent-preview/4524287)  
      *Run SRE Agent outbound traffic through enterprise network controls.*
    - [SRE Agent managed connectors](https://techcommunity.microsoft.com/blog/appsonazureblog/managed-connectors-for-sre-agent-preview--govern-what-your-agent-can-do/4524840)  
      *Governed connector operations, approvals, parameter policies, and credential isolation.*
    - [SRE Agent tool permissions and hooks](https://techcommunity.microsoft.com/blog/appsonazureblog/shaping-what-azure-sre-agent-does-tool-permissions-and-hooks/4524791)  
      *Allow, ask, and deny rules with hooks for pre-execution policy checks.*
    - [SRE Agent GitHub Enterprise support](https://techcommunity.microsoft.com/blog/appsonazureblog/bring-your-own-github-app-connecting-azure-sre-agent-to-enterprise-repositories/4524673)  
      *BYO GitHub App and GitHub Enterprise access for repository-aware investigations.*
    - [SRE Agent private plugin marketplace](https://techcommunity.microsoft.com/blog/appsonazureblog/private-plugins-with-azure-sre-agent/4523763)  
      *Private plugin marketplaces for reusable runbooks, skills, and operational workflows.*

- **Containers and Kubernetes:**
    - [What's new in AKS at Microsoft Build 2026](https://techcommunity.microsoft.com/blog/appsonazureblog/whats-new-in-azure-kubernetes-service-at-microsoft-build-2026/4524862)  
      *AKS umbrella post covering managed system node pools, Azure Container Linux, AKS on bare metal, Fleet Manager for Arc, Anyscale, and AI Runway.*
    - [AKS on bare metal](https://techcommunity.microsoft.com/blog/appsonazureblog/whats-new-in-azure-kubernetes-service-at-microsoft-build-2026/4524862)  
      *Run AKS on dedicated machines without a hypervisor for NVLink, RDMA, and high-performance networking access.*
    - [Azure Container Apps Sandboxes](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131)  
      *MicroVM-backed sandbox infrastructure for agentic workloads.*
    - [Anyscale on Azure](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-anyscale-on-azure-public-preview-powered-by-ray-on-aks/4523704)  
      *Managed Ray platform running natively on AKS for distributed AI workloads.*
    - [Azure Container Linux on AKS](https://azure.microsoft.com/updates?id=564537)  
      *Container-optimized immutable OS for AKS node pools.*
    - [ACR Artifact Cache deep dive](https://techcommunity.microsoft.com/blog/appsonazureblog/inside-acr-artifact-cache-pull-through-caching-at-scale/4524949)  
      *Pull-through caching architecture for Azure Container Registry.*

- **API Management, Logic Apps, and messaging:**
    - [What's new in Azure API Management at Build 2026](https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-api-management-at-microsoft-build-2026/4524683)  
      *Unified Model API, A2A APIs, MCP/A2A safety, API Center, Anthropic/Vertex AI gateway, token observability, and custom domains.*
    - [Azure API Management Unified Model API](https://azure.microsoft.com/updates?id=562853)  
      *Unified API pattern for multi-model AI applications.*
    - [New AI Gateway capabilities in APIM](https://techcommunity.microsoft.com/blog/integrationsonazureblog/new-ai-gateway-capabilities-in-azure-api-management/4524604)  
      *OpenAI, Anthropic, Vertex AI routing plus MCP and A2A governance.*
    - [MCP Test Console and Git sync in Azure API Center](https://techcommunity.microsoft.com/blog/integrationsonazureblog/mcp-test-console-and-git-repository-synch-in-azure-api-center/4524617)  
      *API Center support for MCP testing and Git synchronization.*
    - [Azure Connector Namespaces](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-connector-namespaces-managed-integration-for-any-azure-compute/4524250)  
      *Managed connectors and MCP servers for Azure compute.*
    - [What's new in Azure Logic Apps at Build 2026](https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-logic-apps-at-microsoft-build-2026/4524685)  
      *Logic Apps Automation, MCP Server, Foundry agent invocation, Knowledge as a Service, and Standard SDK.*
    - [Logic Apps Automation](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%8E%89-automation-just-became-a-team-sport-meet-azure-logic-apps-automation-/4524555)  
      *New Logic Apps SKU with AI-assisted workflow generation and Foundry agent integration.*
    - [Knowledge as a Service for Logic Apps](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%93%A2-announcing-knowledge-as-a-service-for-azure-logic-apps/4524601)  
      *Document-to-knowledge-base capability inside Logic Apps.*
    - [Azure Event Grid at Build 2026](https://techcommunity.microsoft.com/blog/messagingonazureblog/azure-event-grid-powering-iot-and-event-driven-applications-at-scale/4521403)  
      *MQTT v5 Subscription Identifier, 1 MB messages, autoscale, and Stripe events integration.*

- **GitHub and marketplace:**
    - [GitHub Copilot App](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/)  
      *Agent-native desktop app with My Work, worktrees, Agent Merge, canvases, and sandboxes.*
    - [GitHub Copilot App repo](https://github.com/github/app)  
      *Release/download, issues, discussions, and changelog.*
    - [Copilot SDK GA](https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available)  
      *Stable SDK for embedding GitHub Copilot's agentic engine.*
    - [Agent apps for GitHub](https://github.blog/changelog/2026-06-02-extend-github-with-agent-apps)  
      *Marketplace-installed agent apps integrated into GitHub.*
    - [Microsoft Marketplace for apps and agents](https://devblogs.microsoft.com/all-things-azure/build-scale-and-monetize-apps-and-agents-with-microsoft-marketplace)  
      *Build, scale, and monetize apps and agents through Microsoft Marketplace.*

---

## 📊 Azure Data

> *Data storage, analytics, databases, Fabric, and data management services*

### Key Announcements

- **Fabric and data platform:**
    - [Building agentic apps with Microsoft Fabric and Microsoft Databases](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/)  
      *Hero data roundup covering Rayfin, HorizonDB, Fabric IQ, OneLake, PostgreSQL, Cosmos DB, and Database Hub.*
    - [Rayfin](https://aka.ms/rayfin)  
      *Open-source SDK and CLI for enterprise-grade Fabric app backends, moving agent-built apps from prompt to governed production backends in Fabric.*
    - [GPU-accelerated Fabric Data Warehouse](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/)  
      *GPU acceleration built directly into Fabric Data Warehouse with NVIDIA accelerated computing and custom CUDA kernels; early access preview planned for July 2026.*
    - [Database Hub in Fabric](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blogs/Advancing-Databases-for-the-Next-Generation-of-Applications/ba-p/5172237)  
      *Unified control plane for databases in Fabric.*
    - [OneLake catalog in Foundry](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blogs/OneLake-catalog-is-now-natively-available-in-Foundry-Generally/ba-p/5178376)  
      *Native OneLake catalog discovery inside Microsoft Foundry.*

- **PostgreSQL, HorizonDB, SQL, and MySQL:**
    - [Azure HorizonDB](https://techcommunity.microsoft.com/blog/adforpostgresql/azure-horizondb-enterprise-ready-postgres-engineered-for-the-ai-era/4524094)  
      *PostgreSQL-compatible database service engineered for AI-era applications.*
    - [Azure HorizonDB update record](https://azure.microsoft.com/updates?id=563087)  
      *Public preview entry for HorizonDB.*
    - [PostgreSQL Build 2026 roundup](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-new-security-maintenance-and-analytics-features-for-postgresql-at-mic/4524559)  
      *Security, maintenance, analytics, migration, extensions, Grafana dashboards, and tooling updates.*
    - [PostgreSQL workflow in Cursor](https://techcommunity.microsoft.com/blog/adforpostgresql/your-postgresql-workflow-just-found-its-new-home-in-cursor/4524081)  
      *PostgreSQL extension published to Open VSX for AI-native editors.*
    - [Azure SQL TDE with AES keys](https://techcommunity.microsoft.com/blog/azuresqlblog/transparent-data-encryption-in-azure-sql-database-now-supports-aes-keys-public-p/4523240)  
      *AES-256 customer-managed keys for TDE in Azure SQL Database.*
    - [Azure SQL June updates](https://azure.microsoft.com/updates?id=563137)  
      *SQL notebooks and developer tooling updates.*
    - [Azure Database for MySQL quota management](https://azure.microsoft.com/updates?id=563147)  
      *Self-service quota management in Azure Database for MySQL Flexible Server.*

- **Cosmos DB and DocumentDB:**
    - [Cosmos DB Build 2026 roundup](https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/)  
      *MCP Toolkit, Agent Kit, memory, semantic reranking, global secondary indexes, failover, distributed transactions, backup, emulator, and change feed.*
    - [Cosmos DB Agent Kit](https://azure.microsoft.com/updates?id=563022)  
      *Best-practice guidance for AI coding agents building Cosmos DB apps.*
    - [Cosmos DB backup](https://azure.microsoft.com/updates?id=562769)  
      *Vaulted backups for Cosmos DB.*
    - [Cosmos DB all versions and deletes change feed](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-all-versions-and-deletes-change-feed-mode-is-now-generally-available/)  
      *Complete change stream including deletes.*
    - [Cosmos DB change partition keys](https://devblogs.microsoft.com/cosmosdb/change-partition-keys-in-azure-cosmos-db-is-now-generally-available/)  
      *Online repartitioning without stopping writes.*
    - [Cosmos DB Migration Assistant](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-migration-assistant-rdbms-to-nosql-public-preview/)  
      *AI-assisted RDBMS-to-NoSQL migration workflow.*
    - [Cosmos DB integrated embeddings](https://devblogs.microsoft.com/cosmosdb/announcing-the-public-preview-of-integrated-embeddings-in-azure-cosmos-db-build-ai-apps-with-embeddings-that-stay-in-sync/)  
      *Embeddings generated and maintained as items are written.*
    - [OmniVec](https://devblogs.microsoft.com/cosmosdb/introducing-omnivec-an-open-source-embedding-platform-for-ai-apps-on-azure/)  
      *Open-source embedding pipeline platform for Azure data sources.*
    - [DocumentDB MCP Toolkit](https://azure.microsoft.com/updates?id=563112)  
      *MCP access for MongoDB-compatible DocumentDB workloads.*
    - [DocumentDB instant free tier clusters](https://azure.microsoft.com/updates?id=563082)  
      *Near-instant free tier cluster provisioning.*
    - [DocumentDB migration extension](https://azure.microsoft.com/updates?id=563072)  
      *VS Code migration workflow.*
    - [DocumentDB service-managed failovers](https://devblogs.microsoft.com/documentdb/azure-documentdb-general-availability-of-service-managed-failovers)  
      *Automatic regional failover.*
    - [DocumentDB graceful failovers](https://devblogs.microsoft.com/documentdb/graceful-failovers-in-azure-documentdb-now-generally-available/)  
      *Controlled planned failovers.*
    - [DocumentDB change streams](https://devblogs.microsoft.com/documentdb/change-streams-in-azure-documentdb-richer-events-historical-replay-and-multi-node-change-streams-public-preview/)  
      *Richer events, historical replay, and multi-node change streams.*

## 🤖 Azure AI

> *Microsoft Foundry, agents, models, grounding, speech, R&D, and AI application platform capabilities*

### Key Announcements

- **Microsoft agent platform:**
    - [AI alone won't change your business. The system running it will.](https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/)  
      *Microsoft's Build 2026 agent-platform framing: GitHub for build, Microsoft IQ for context, Foundry for runtime, Agent 365 for governance, and Teams/Microsoft 365 for surfacing agents.*
    - [Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)  
      *Agent-optimized APIs for Microsoft 365 context, tools, chat, and workspaces.*
    - [Web IQ](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ)  
      *AI-native grounding APIs built on Bing for fresh web, news, image, and video evidence.*
    - [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)  
      *Always-on personal agent built on OpenClaw with Work IQ context and governed Entra identity.*
    - [Project Lobster is Microsoft Scout](https://www.linkedin.com/pulse/project-lobster-microsoft-scout-omar-shahine-o5bae)  
      *Behind-the-scenes context on the path from Project Lobster to Microsoft Scout.*
    - [Frontier Tuning](https://devblogs.microsoft.com/microsoft365dev/frontier-tuning-teaching-ai-to-work-the-way-you-do/)  
      *Domain-specific model tuning using enterprise data, workflows, and reinforcement-learning environments.*

- **Microsoft Foundry:**
    - [What's new in Microsoft Foundry | Build Edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/)  
      *Foundry Build 2026 overview covering agents, toolboxes, routines, memory, Web IQ, models, guardrails, tracing, and optimization.*
    - [Build and run agents at scale with Microsoft Foundry](https://devblogs.microsoft.com/foundry/agent-service-build2026/)  
      *Deep dive on Foundry Agent Service, hosted agents, Microsoft Agent Framework, Toolboxes, Voice Live, memory, and tracing.*
    - [Hosted Agents in Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=563596)  
      *Container-based runtime for bringing agent code from any framework into Microsoft Foundry.*
    - [Foundry IQ](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/)  
      *Unified knowledge, serverless retrieval, Work IQ, Fabric IQ, Azure SQL, File Search, MCP, and Web IQ knowledge sources.*
    - [Toolboxes and Routines in Microsoft Foundry](https://devblogs.microsoft.com/foundry/toolbox-build-26/)  
      *Governed tools, skills, MCP clients, connectors, and scheduled agent execution.*
    - [Agent Optimizer in Foundry Agent Service](https://devblogs.microsoft.com/foundry/agent-optimizer-build2026/)  
      *Turns production failures into ranked, reviewable agent improvements.*
    - [Agent memory in Foundry](https://devblogs.microsoft.com/foundry/memory-build2026/)  
      *Procedural, user, and session memory for production agents.*
    - [Enterprise agent distribution in Microsoft Foundry](https://devblogs.microsoft.com/foundry/from-building-agents-to-working-with-them-enterprise-agent-distribution-in-microsoft-foundry/)  
      *Publish Foundry agents to Microsoft 365 Copilot and Teams.*
    - [Microsoft Agent Framework](https://commandline.microsoft.com/agent-framework-layered-sdk-loops-workflows-harnesses/)  
      *Provider-neutral agent framework for loops, workflows, harnesses, tools, context, memory, and permissions.*

- **Models, speech, content, and R&D:**
    - [Seven new MAI models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)  
      *Microsoft AI model-family announcement covering reasoning, coding, image, voice, transcription, and Frontier Tuning.*
    - [Mayo Clinic frontier healthcare model partnership](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)  
      *Microsoft and Mayo Clinic are co-creating a frontier healthcare AI model to be made available through Azure Foundry after validation.*
    - [Azure Speech at Build 2026](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-speech-at-build-2026-powering-voice-agents-with-real-time-and-life-like-ex/4524638)  
      *Voice Live, hosted voice agents, speech-to-speech models, WebSocket/WebRTC support, and Foundry speech playground.*
    - [Azure Content Understanding at Build 2026](https://devblogs.microsoft.com/foundry/whats-new-in-azure-content-understanding-at-build-2026/)  
      *Content Understanding in Foundry Tools with agentic mode, analyzers, and workflow integrations.*
    - [Microsoft Discovery GA and Discovery app preview](https://azure.microsoft.com/en-us/blog/announcing-microsoft-discovery-general-availability-and-microsoft-discovery-app-preview/)  
      *Agentic R&D platform for scientific and engineering workflows.*
    - [Majorana 2 and Microsoft Discovery](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/)  
      *Next-generation quantum chip built with the help of Microsoft Discovery's agentic AI.*

## 🔒 Security & Governance

> *Security, identity, governance, compliance, and safe agent operations*

### Key Announcements

- **Agent and model security:**
    - [Securing code, agents, and models across the development lifecycle](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/)  
      *MDASH, Defender/GitHub Code Security, Agent 365 SDK, MXC, Windows 365 for Agents, Purview DLP, and Defender model scanning.*
    - [Agent 365 GA and expanded local/cloud agent management](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)  
      *Observe, govern, and secure local, SaaS, and cloud agents.*
    - [Windows platform security for AI agents](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/)  
      *MXC SDK, process/session isolation, micro-VM roadmap, Linux containers, Windows 365 for Agents, and OpenClaw on Windows.*
    - [Microsoft Execution Containers SDK](https://github.com/microsoft/mxc)  
      *Policy-driven execution layer for agents on Windows and WSL.*
    - [OpenClaw on Windows with Microsoft Execution Containers](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/)  
      *OpenClaw node and gateway run securely on Windows using MXC, with a companion app for setting up claws or connecting to existing ones.*
    - [OpenClaw Windows Node](https://github.com/openclaw/openclaw-windows-node)  
      *OpenClaw node and gateway for Windows.*
    - [Windows 365 at Build 2026](https://techcommunity.microsoft.com/blog/windows-itpro-blog/made-for-developers-and-agents-windows-365-at-build-2026/4519041)  
      *Ready-to-code Cloud PCs and secured execution environments for agents.*

- **Defender, Purview, and database security:**
    - [Start secure, stay secure](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/start-secure-stay-secure-how-microsoft-is-closing-the-gap-from-code-to-runtime/4524580)  
      *Defender for Cloud Build post for MDASH and Defender for Cloud + GitHub Code Security.*
    - [Defender for Cloud hardened images](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/the-end-of-patching-era-for-containers-microsoft-defender-for-cloud-expands-hard/4524798)  
      *Container image hardening as a security baseline.*
    - [Purview sensitivity labels in Azure AI Search](https://azure.microsoft.com/updates?id=563591)  
      *Sensitivity labels flow into Azure AI Search ingestion.*
    - [Purview label auditing in Azure AI Search](https://azure.microsoft.com/updates?id=563267)  
      *Audit events for labels carried alongside indexed documents.*
    - [PostgreSQL Defender security assessments](https://azure.microsoft.com/updates?id=563781)  
      *Continuous security assessment for Azure Database for PostgreSQL.*
    - [PostgreSQL cross-tenant CMK](https://azure.microsoft.com/updates?id=563776)  
      *Cross-tenant customer-managed keys for PostgreSQL Flexible Server.*
    - [Azure SQL TDE with AES customer-managed keys](https://azure.microsoft.com/updates?id=563142)  
      *AES-256 keys for TDE with customer-managed keys.*

---