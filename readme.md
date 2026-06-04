# 🚀 Matt's List of //Build 2026 Announcements

This is a personal collection of announcements and updates at  around **Microsoft //Build 2026**, organized by service category for navigation and reference.

**Last Updated:** June 4, 2026, 8:01 AM (EST)

**Current Total Updates:** 132 announcements

**🎯 What's Inside:** Announcements across Hardware & Infrastructure, Apps & Development, Data & Analytics, AI & Agents, and Security & Governance with direct links to official documentation and blog posts.

---

## 📋 Table of Contents

- [🏗️ Hardware & Infrastructure](#-hardware--infrastructure)
- [🔧 Apps & Development](#-apps--development)
- [📊 Data & Analytics](#-data--analytics)
- [🤖 AI & Agents](#-ai--agents)
- [🔒 Security & Governance](#-security--governance)

---

## 🏗️ Hardware & Infrastructure

> *Core infrastructure services, compute, storage, operations, resiliency, and foundational Azure capabilities*

### Key Announcements

- **Compute and hardware:**
    - [Azure Cobalt 200 VMs](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/)  
      *Arm-based VMs, 50% better performance for AI workloads.*
    - [Confidential Live Migration for Intel TDX confidential VMs](https://techcommunity.microsoft.com/blog/azureconfidentialcomputingblog/announcing-confidential-live-migration-in-azure/4524558)  
      *Private preview enables protected host migration with minimal interruption.*
    - [Guest RDMA for Azure Boost](https://techcommunity.microsoft.com/blog/azurecompute/announcing-preview-of-guest-rdma-for-azure-boost/4524589)  
      *100 Gb/s low-latency Guest RDMA for distributed AI and HPC.*
    - [Lasv5 and Laosv5 VMs](https://techcommunity.microsoft.com/blog/azurecompute/announcing-preview-of-new-azure-lasv5-and-laosv5-vms-based-on-the-amd-epyc%E2%84%A2-%E2%80%98tur/4522407)  
      *Upgrades include: 35% more CPU, 138 TB local storage, and 200 Gbps Bandwidth*
    - [Azure Linux 4.0](https://aka.ms/azurelinux-blog)  
      *Azure Linux 4.0 extends container hosting to general-purpose VMs.*
    - [Surface RTX Spark Dev Box and DGX Station for Windows](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/)  
      *RTX Spark: 1 petaflop, 128 GB memory. DGX Station: 1T parameters locally.*
    - [Project Solara](https://commandline.microsoft.com/project-solara-build-2026/)  
      *Standardizes building, deploying, managing agent-first devices end-to-end.*
    - [Majorana 2 (Microsoft Quantum)](https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor)  
      *Redesigned materials stack aims for more reliable topological qubits.*

- **Azure Local, Arc, and edge:**
    - [Small form factor infrastructure](https://techcommunity.microsoft.com/blog/azurearcblog/embed-intelligence-into-physical-systems-with-smaller-form-factor-infrastructure/4524876)  
      *Azure-managed edge infrastructure runs AI and ops closer to devices.*
    - [Foundry Local on Azure Local for sovereign AI](https://techcommunity.microsoft.com/blog/azurearcblog/build-deploy-and-govern-sovereign-ai-with-foundry-local-on-azure-local/4522945)  
      *Multi-node sovereign AI with local retrieval for regulated orgs.*
    - [Foundry Local multi-node inference and vLLM](https://techcommunity.microsoft.com/blog/azurearcblog/scale-on-prem-ai-with-foundry-local-on-azure-local-multi-node-inference-and-vllm/4516692)  
      *Multi-node vLLM scales on-prem serving to production.*
    - [GitHub Enterprise Local](https://techcommunity.microsoft.com/blog/azurearcblog/introducing-github-enterprise-local-preview-devops-for-sovereign-and-private-clo/4523046)  
      *GitHub Enterprise Local keeps DevSecOps workflows air-gapped.*
    - [Agentic retrieval in Foundry Local](https://techcommunity.microsoft.com/blog/azurearcblog/unlock-on-prem-productivity-with-agentic-retrieval-in-foundry-local/4523646)  
      *On-prem agentic M365 retrieval reduces latency and exposure risk.*

- **Storage and migration:**
    - [Azure Files on macOS with Entra ID](https://techcommunity.microsoft.com/blog/azurestorageblog/secure-modern-access-to-azure-files-on-macos-with-ms-entra-id/4524077)  
      *Entra ID macOS Azure Files removes key auth friction.*
    - [File share centric management model](https://techcommunity.microsoft.com/blog/azurestorageblog/simpler-scalable-file-share-management-in-azure---now-generally-available/4523035)  
      *Share-centric model simplifies per-share RBAC and automation.*
    - [File share migrations with Azure Copilot Migration Agent](https://techcommunity.microsoft.com/blog/azurestorageblog/file-share-migrations-simplified-with-azure-copilot-migration-agent/4524563)  
      *Agent-assisted migrations reduce manual planning.*

- **Observability and resiliency:**
    - [What's new in Observability at Build 2026](https://techcommunity.microsoft.com/blog/azureobservabilityblog/what%E2%80%99s-new-in-observability-at-build-2026/4524927)
    - [Azure Infrastructure Resiliency Manager](https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/announcing-azure-infrastructure-resiliency-manager-public-preview/4523710)
      *Azure Monitor for agent observability and SLI/SLO workflows.*
    - [Azure Monitor Copilot Observability Agent](https://techcommunity.microsoft.com/blog/azureobservabilityblog/azure-monitor-copilot-observability-agent-what%E2%80%99s-new-at-build/4522927)  
      *Copilot investigations shorten incident MTTI.*
    - [Direct OpenTelemetry ingestion](https://techcommunity.microsoft.com/blog/azureobservabilityblog/direct-opentelemetry-ingestion-into-azure-monitor-is-now-generally-available/4524044)  
      *Direct OTLP ingestion removes custom pipeline overhead.*
    - [Monitor AI coding agents with OpenTelemetry](https://techcommunity.microsoft.com/blog/azureobservabilityblog/monitor-ai-coding-agents-with-opentelemetry-in-azure-monitor/4524049)  
      *Observability for AI coding agents tracks quality and latency.*
    - [Azure Monitor agent observability](https://techcommunity.microsoft.com/blog/azureobservabilityblog/new-capabilities-to-observe-agents-in-azure-monitor/4524896)  
      *Fleet views and cost breakdowns for agent operations.*
    - [Monitoring Coverage](https://techcommunity.microsoft.com/blog/azureobservabilityblog/is-your-monitoring-actually-working-whats-new-in-monitoring-coverage/4524619)  
      *Monitoring Coverage prevents silent telemetry gaps.*
    - [Multi-stage transformations for Azure Monitor DCRs](https://techcommunity.microsoft.com/blog/azureobservabilityblog/is-94-of-your-syslog-just-noise-now-you-can-filter-it-out-before-ingestion-/4524600)  
      *Multi-stage transformations cut telemetry noise and cost.*
      *Resilience workflow makes reliability an ongoing practice.*
    - [Kubernetes Center security and version insights](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/kubernetes-center-security--ltsout-of-support-version-insights-now-available/4524567)  
      *Fleet-level AKS security insights reduce upgrade risk.*

---

## 🔧 Apps & Development

> *Application development, deployment, integration, SRE agents, and developer platform services*

### Key Announcements

- **Azure Functions:**
    - [azure-functions-skills](https://devblogs.microsoft.com/azure-sdk/introducing-azure-functions-skills-ai-era-workspace)  
      *Packages skills and MCP config for Functions patterns.*
    - [Azure Functions Serverless Agents Runtime](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-the-azure-functions-serverless-agents-runtime-preview/4523804)  
      *Markdown-first runtime lowers serverless agent barrier.*
    - [Go support in Azure Functions](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-go-support-in-azure-functions-preview/4523801)  
      *First-class Go on Flex Consumption for cloud-native.*
    - [Azure Functions MCP Extension](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-mcp-extension-whats-new-at-build-2026/4524099)  
      *MCP support enables safe agent automation.*
    - [Managed Connectors for Azure Functions](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-managed-connectors-for-azure-functions-preview/4523798)  
      *1,400+ managed connectors reduce integration plumbing.*

- **Azure SRE Agent:**
    - [Azure SRE Agent at Build 2026](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-at-microsoft-build-2026-bringing-agentic-operations-to-the-enter/4524669)  
      *SRE Agent governance enables production operations.*
    - [SRE Agent VNet integration](https://techcommunity.microsoft.com/blog/appsonazureblog/vnet-integration-for-azure-sre-agent-preview/4524287)  
      *VNet integration enforces network controls.*
    - [SRE Agent managed connectors](https://techcommunity.microsoft.com/blog/appsonazureblog/managed-connectors-for-sre-agent-preview--govern-what-your-agent-can-do/4524840)  
      *Governed connectors limit execution blast radius.*
    - [SRE Agent tool permissions and hooks](https://techcommunity.microsoft.com/blog/appsonazureblog/shaping-what-azure-sre-agent-does-tool-permissions-and-hooks/4524791)  
      *Three-mode permissions and hooks add guardrails.*
    - [SRE Agent GitHub Enterprise support](https://techcommunity.microsoft.com/blog/appsonazureblog/bring-your-own-github-app-connecting-azure-sre-agent-to-enterprise-repositories/4524673)  
      *GitHub Enterprise support enables repository-aware workflows.*
    - [SRE Agent private plugin marketplace](https://techcommunity.microsoft.com/blog/appsonazureblog/private-plugins-with-azure-sre-agent/4523763)  
      *Private marketplaces scale approved SRE practices org-wide.*

- **Containers and Kubernetes:**
    - [What's new in AKS at Microsoft Build 2026](https://techcommunity.microsoft.com/blog/appsonazureblog/whats-new-in-azure-kubernetes-service-at-microsoft-build-2026/4524862)  
      *AKS updates signal stronger platform for AI.*
    - [AKS on bare metal](https://blog.aks.azure.com/2026/06/02/aks-baremetal-public-preview)  
      *Bare metal unlocks NVLink and RDMA for GPU workloads.*
    - [Azure Container Apps Sandboxes](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131)  
      *MicroVM sandboxes isolate agentic workloads securely.*
    - [Anyscale on Azure](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-anyscale-on-azure-public-preview-powered-by-ray-on-aks/4523704)  
      *Managed Ray simplifies distributed training and inference.*
    - [Azure Container Linux on AKS](https://aka.ms/azurecontainerlinux-blog)
      *Immutable OS improves consistency and reduces attack surface.*
    - [ACR Artifact Cache deep dive](https://techcommunity.microsoft.com/blog/appsonazureblog/inside-acr-artifact-cache-pull-through-caching-at-scale/4524949)  
      *Pull-through caching reduces latency and upstream risk.*

- **API Management, Logic Apps, and messaging:**
    - [What's new in Azure API Management at Build 2026](https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-api-management-at-microsoft-build-2026/4524683)  
      *APIM adds AI-native model routing and safety controls.*
    - [Azure API Management Unified Model API](https://azure.microsoft.com/updates?id=562853)  
      *One contract across providers reduces switching churn.*
    - [New AI Gateway capabilities in APIM](https://techcommunity.microsoft.com/blog/integrationsonazureblog/new-ai-gateway-capabilities-in-azure-api-management/4524604)  
      *Routes 3 providers with policy-driven governance.*
    - [MCP Test Console and Git sync in Azure API Center](https://techcommunity.microsoft.com/blog/integrationsonazureblog/mcp-test-console-and-git-repository-synch-in-azure-api-center/4524617)  
      *MCP testing and Git sync improve lifecycle governance.*
    - [Azure Connector Namespaces](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-connector-namespaces-managed-integration-for-any-azure-compute/4524250)  
      *Managed integrations standardize security across runtimes.*
    - [What's new in Azure Logic Apps at Build 2026](https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-logic-apps-at-microsoft-build-2026/4524685)  
      *MCP and Foundry position workflows for AI automation.*
    - [Logic Apps Automation](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%8E%89-automation-just-became-a-team-sport-meet-azure-logic-apps-automation-/4524555)  
      *AI-assisted authoring speeds pipeline building.*
    - [Knowledge as a Service for Logic Apps](https://techcommunity.microsoft.com/blog/integrationsonazureblog/%F0%9F%93%A2-announcing-knowledge-as-a-service-for-azure-logic-apps/4524601)  
      *Knowledge as a Service reduces ETL for grounding.*
    - [Azure Event Grid at Build 2026](https://techcommunity.microsoft.com/blog/messagingonazureblog/azure-event-grid-powering-iot-and-event-driven-applications-at-scale/4521403)  
      *1 MB messages, MQTT v5, autoscale for IoT.*

- **GitHub and marketplace:**
    - [GitHub Copilot App](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/)  
      *Agent-native desktop with worktrees enables parallel tasks.*
    - [GitHub Copilot App repo](https://github.com/github/app)  
      *Public repo centralizes releases and feedback loops.*
    - [MAI-Code-1-Flash in GitHub Copilot](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot)  
      *Small-tier coding model rollout expands lightweight coding options in Copilot.*
    - [Copilot SDK GA](https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available)  
      *Copilot SDK GA enables embedding agentic coding.*
    - [Agent apps for GitHub](https://github.blog/changelog/2026-06-02-extend-github-with-agent-apps)  
      *Agent apps reduce custom bots and scripts.*
    - [Microsoft Marketplace for apps and agents](https://devblogs.microsoft.com/all-things-azure/build-scale-and-monetize-apps-and-agents-with-microsoft-marketplace)  
      *Marketplace creates distribution for AI solutions.*

---

## 📊 Data & Analytics

> *Data storage, analytics, databases, Fabric, and data management services*

### Key Announcements

- **Fabric and data platform:**
    - [Building agentic apps with Microsoft Fabric and Microsoft Databases](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/)  
      *Unified Fabric and database roadmap aligns data strategy.*
    - [Rayfin](https://aka.ms/rayfin)  
      *Rayfin moves prototypes to governed Fabric backends.*
    - [GPU-accelerated Fabric Data Warehouse](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/)  
      *GPU acceleration speeds analytics and AI workloads.*
    - [Database Hub in Fabric](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blogs/Advancing-Databases-for-the-Next-Generation-of-Applications/ba-p/5172237)  
      *Database Hub unifies control across engines.*
    - [OneLake catalog in Foundry](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blogs/OneLake-catalog-is-now-natively-available-in-Foundry-Generally/ba-p/5178376)  
      *OneLake catalog in Foundry eases agent grounding.*

- **PostgreSQL, HorizonDB, SQL, and MySQL:**
    - [Azure HorizonDB](https://techcommunity.microsoft.com/blog/adforpostgresql/azure-horizondb-enterprise-ready-postgres-engineered-for-the-ai-era/4524094)  
      *Enterprise PostgreSQL-compatible service for AI patterns.*
    - [Azure HorizonDB update record](https://azure.microsoft.com/updates?id=563087)  
      *Public preview enables early evaluation.*
    - [PostgreSQL Build 2026 roundup](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-new-security-maintenance-and-analytics-features-for-postgresql-at-mic/4524559)  
      *Updates add security, analytics, migration tooling.*
    - [DuckDB extension for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=563766)  
      *DuckDB support in Flexible Server expands in-database analytics options.*
    - [PostgreSQL workflow in Cursor](https://techcommunity.microsoft.com/blog/adforpostgresql/your-postgresql-workflow-just-found-its-new-home-in-cursor/4524081)  
      *PostgreSQL tooling on Open VSX supports AI editors.*
    - [Azure SQL TDE with AES keys](https://techcommunity.microsoft.com/blog/azuresqlblog/transparent-data-encryption-in-azure-sql-database-now-supports-aes-keys-public-p/4523240)  
      *AES customer-managed keys strengthen TDE control.*
    - [Azure SQL June updates](https://azure.microsoft.com/updates?id=563137)  
      *Tooling and notebooks improve query workflows.*
    - [Azure Database for MySQL quota management](https://azure.microsoft.com/updates?id=563147)  
      *Self-service quota management speeds capacity scaling.*

- **Cosmos DB and DocumentDB:**
    - [Cosmos DB Build 2026 roundup](https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/)  
      *Major capabilities ease AI-native workloads.*
    - [Cosmos DB Agent Kit](https://azure.microsoft.com/updates?id=563022)  
      *Agent Kit improves app quality.*
    - [Cosmos DB backup](https://azure.microsoft.com/updates?id=562769)  
      *Vaulted backups improve data loss protection.*
    - [Cosmos DB all versions and deletes change feed](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-all-versions-and-deletes-change-feed-mode-is-now-generally-available/)  
      *Change feed enables audit and replay.*
    - [Cosmos DB change partition keys](https://devblogs.microsoft.com/cosmosdb/change-partition-keys-in-azure-cosmos-db-is-now-generally-available/)  
      *Online partition changes enable repartitioning.*
    - [Cosmos DB Migration Assistant](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-migration-assistant-rdbms-to-nosql-public-preview/)  
      *AI-guided workflows lower modernization complexity.*
    - [Cosmos DB integrated embeddings](https://devblogs.microsoft.com/cosmosdb/announcing-the-public-preview-of-integrated-embeddings-in-azure-cosmos-db-build-ai-apps-with-embeddings-that-stay-in-sync/)  
      *Integrated embeddings reduce pipeline overhead.*
    - [OmniVec](https://devblogs.microsoft.com/cosmosdb/introducing-omnivec-an-open-source-embedding-platform-for-ai-apps-on-azure/)  
      *Open-source embedding pipeline standardizes vectorization.*
    - [DocumentDB MCP Toolkit](https://azure.microsoft.com/updates?id=563112)  
      *MCP Toolkit enables safer agent automation.*
    - [DocumentDB instant free tier clusters](https://azure.microsoft.com/updates?id=563082)  
      *Instant free-tier provisioning speeds evaluation.*
    - [DocumentDB migration extension](https://azure.microsoft.com/updates?id=563072)  
      *Migration extension reduces setup complexity.*
    - [Advanced full-text search in Azure DocumentDB](https://azure.microsoft.com/updates?id=563077)  
      *Fuzzy, proximity, and BM25 search improve hybrid text and vector retrieval.*
    - [DocumentDB service-managed failovers](https://devblogs.microsoft.com/documentdb/azure-documentdb-general-availability-of-service-managed-failovers)  
      *Service-managed failovers automate regional recovery.*
    - [DocumentDB graceful failovers](https://devblogs.microsoft.com/documentdb/graceful-failovers-in-azure-documentdb-now-generally-available/)  
      *Graceful failovers enable planned transitions.*
    - [DocumentDB change streams](https://devblogs.microsoft.com/documentdb/change-streams-in-azure-documentdb-richer-events-historical-replay-and-multi-node-change-streams-public-preview/)  
      *Richer change streams enable event sourcing.*

## 🤖 AI & Agents

> *Microsoft Foundry, agents, models, grounding, speech, R&D, and AI application platform capabilities*

### Key Announcements

- **Microsoft agent platform:**
    - [AI alone won't change your business. The system running it will.](https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/)  
      *AI value comes from full agent systems.*
    - [Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)  
      *Work IQ APIs expose M365 context for automation.*
    - [Computer-using agents, workflows, and real-time voice experiences](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/)  
      *Copilot Studio updates connect UI automation, workflows, and real-time voice in one platform.*
    - [Web IQ](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ)  
      *Web IQ improves agent factuality and recency.*
    - [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)  
      *Always-on personal agent with enterprise governance.*
    - [Project Lobster is Microsoft Scout](https://www.linkedin.com/pulse/project-lobster-microsoft-scout-omar-shahine-o5bae)  
      *Implementation context for Scout's design.*
    - [Frontier Tuning](https://devblogs.microsoft.com/microsoft365dev/frontier-tuning-teaching-ai-to-work-the-way-you-do/)  
      *Domain-specific models fit organizational patterns.*

- **Microsoft Foundry:**
    - [What's new in Microsoft Foundry | Build Edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/)  
      *Maturing platform integrates build and governance.*
    - [Build and run agents at scale with Microsoft Foundry](https://devblogs.microsoft.com/foundry/agent-service-build2026/)  
      *Hosted agents at scale with production tooling.*
    - [Hosted Agents in Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=563596)  
      *Container runtime reduces migration friction.*
    - [Foundry IQ](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/)  
      *Unifies 6+ sources with serverless retrieval.*
    - [Foundry IQ recall improvements for knowledge bases](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-improve-recall-by-up-to-54-with-knowledge-bases/4524852)  
      *Agentic retrieval updates improve recall and reduce token costs in enterprise search.*
    - [Foundry IQ governance and enterprise AI security](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-new-governance-and-enterprise-ai-security-capabilities/4524825)  
      *Adds ACL sync, Purview integration, and private connectivity for governed retrieval workflows.*
    - [Toolboxes and Routines in Microsoft Foundry](https://devblogs.microsoft.com/foundry/toolbox-build-26/)  
      *Standardized tools ease operationalization.*
    - [Browser automation tool with Toolboxes in Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-the-new-browser-automation-tool-with-toolboxes-in-foundry/4522790)  
      *MCP-native browser automation adds live view and intervention controls for hosted agents.*
    - [Domain filter for specialized model discovery](https://azure.microsoft.com/updates?id=563731)  
      *Model catalog domain filters speed discovery of industry-tuned models.*
    - [Agent Optimizer in Foundry Agent Service](https://devblogs.microsoft.com/foundry/agent-optimizer-build2026/)  
      *Converts failures to ranked improvements.*
    - [Agent memory in Foundry](https://devblogs.microsoft.com/foundry/memory-build2026/)  
      *Three memory scopes enable context-aware agents.*
    - [Enterprise agent distribution in Microsoft Foundry](https://devblogs.microsoft.com/foundry/from-building-agents-to-working-with-them-enterprise-agent-distribution-in-microsoft-foundry/)  
      *Distribution to M365 and Teams closes adoption gap.*
    - [Microsoft Agent Framework](https://commandline.microsoft.com/agent-framework-layered-sdk-loops-workflows-harnesses/)  
      *Provider-neutral architecture avoids vendor lock-in.*

- **Models, speech, content, and R&D:**
    - [Seven new First-Party Microsoft AI models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)  
      *Seven new MAI models across reasoning, coding, multimodal.*
    - [Mayo Clinic frontier healthcare model partnership](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)  
      *Mayo Clinic partnership develops healthcare models.*
    - [MAI-Voice-2 in Microsoft Foundry](https://azure.microsoft.com/updates?id=563217)  
      *Public preview introduces multilingual voice cloning and prompting in Foundry.*
    - [Azure Speech at Build 2026](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-speech-at-build-2026-powering-voice-agents-with-real-time-and-life-like-ex/4524638)  
      *Real-time, lifelike voice agents with streaming protocols.*
    - [Voice Live evaluation harness](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluate-before-you-ship-introducing-the-voice-live-evaluation-harness/4523064)  
      *Open-source evaluation pipeline scores multi-turn voice agents before production.*
    - [Text Analytics for Health NextGen Playground](https://azure.microsoft.com/updates?id=563671)  
      *Foundry playground exposes FHIR-aligned health entity extraction for pre-integration testing.*
    - [TextPII NextGen Playground updates](https://azure.microsoft.com/updates?id=564241)  
      *Updated configuration panel improves interactive PII validation workflows.*
    - [Conversational PII NextGen Playground](https://azure.microsoft.com/updates?id=564246)  
      *Conversation-focused PII testing supports transcript-style privacy and compliance scenarios.*
    - [Azure Content Understanding at Build 2026](https://devblogs.microsoft.com/foundry/whats-new-in-azure-content-understanding-at-build-2026/)  
      *Richer analyzers turn content into agent signals.*
    - [Microsoft Discovery GA and Discovery app preview](https://azure.microsoft.com/en-us/blog/announcing-microsoft-discovery-general-availability-and-microsoft-discovery-app-preview/)  
      *Discovery GA enables agentic scientific workflows.*
    - [Majorana 2 and Microsoft Discovery](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/)  
      *AI tooling accelerates deep-tech R&D.*

## 🔒 Security & Governance

> *Security, identity, governance, compliance, and safe agent operations*

### Key Announcements

- **Agent and model security:**
    - [Securing code, agents, and models across the development lifecycle](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/)  
      *Security controls are first-class in AI pipelines.*
    - [Build MDASH / Agentic DevSecOps](https://aka.ms/AgenticDevSecOps)  
      *Build security update on MDASH and agentic DevSecOps workflows for vulnerability discovery and remediation.*
    - [Agent 365 GA and expanded local/cloud agent management](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)  
      *Unified governance across local, SaaS, cloud agents.*
    - [Windows platform security for AI agents](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/)  
      *Windows platform security for local agents.*
    - [Microsoft Execution Containers SDK](https://github.com/microsoft/mxc)  
      *Policy-driven execution enforces least privilege.*
    - [OpenClaw on Windows with Microsoft Execution Containers](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/)  
      *OpenClaw on Windows enables secure deployment.*
    - [OpenClaw Windows Node](https://github.com/openclaw/openclaw-windows-node)  
      *OpenClaw Windows Node lowers setup complexity.*
    - [Windows 365 at Build 2026](https://techcommunity.microsoft.com/blog/windows-itpro-blog/made-for-developers-and-agents-windows-365-at-build-2026/4519041)  
      *Managed Cloud PCs enable secure agent execution.*

- **Defender, Purview, and database security:**
    - [Start secure, stay secure](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/start-secure-stay-secure-how-microsoft-is-closing-the-gap-from-code-to-runtime/4524580)  
      *Code-to-runtime connects developer to runtime security.*
    - [Defender for Cloud hardened images](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/the-end-of-patching-era-for-containers-microsoft-defender-for-cloud-expands-hard/4524798)  
      *Hardened images reduce patching overhead.*
    - [Purview sensitivity labels in Azure AI Search](https://azure.microsoft.com/updates?id=563591)  
      *Labels enable policy-aware retrieval.*
    - [Purview label auditing in Azure AI Search](https://azure.microsoft.com/updates?id=563267)  
      *Auditing creates compliance evidence trails.*
    - [PostgreSQL Defender security assessments](https://azure.microsoft.com/updates?id=563781)  
      *Continuous security assessments for PostgreSQL.*
    - [PostgreSQL cross-tenant CMK](https://azure.microsoft.com/updates?id=563776)  
      *Cross-tenant CMK enables stricter key separation.*
    - [Azure SQL TDE with AES customer-managed keys](https://azure.microsoft.com/updates?id=563142)  
      *AES-256 CMK strengthens encryption governance.*

---

## 📅 Event Information

**Microsoft //Build 2026**  
🌐 *Developer conference announcements roundup*  
📚 *Coverage focused on platform, data, AI, apps, and security updates*

### Summary
Microsoft //Build 2026 highlighted major updates across infrastructure, developer tooling, data and analytics, AI agent platforms, and security governance. This list tracks notable announcements and links directly to source posts and documentation.

---

## 📝 Contributing

This list is maintained by Matt Hansen. Feel free to suggest additions or corrections direct or via PR.

---

## 🔗 Resources

- [Official Microsoft //Build](https://build.microsoft.com/)
- [Azure Updates](https://azure.microsoft.com/updates/)
- [Microsoft Tech Community](https://techcommunity.microsoft.com/)

---

*Last updated: June 4, 2026*
