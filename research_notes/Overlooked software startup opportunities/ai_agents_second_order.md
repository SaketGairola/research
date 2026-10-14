# Second- and Third-Order Problems from AI Agents and Cheap Software/Content (as of Oct 14, 2026)

Research notes for the report writer. Scope: (a) problems that came from companies deploying autonomous agents, (b) problems from near-free software creation, and (c) problems from near-free applications, submissions and content. For each, I checked who is already funded to solve it, whether platforms are absorbing it, and which segments remain underserved. The last section turns this into 8 candidate opportunities, filtered for a solo, non-engineer founder in India who builds with AI coding tools and sells to US customers.

**Method and access disclosures (read first)**
- The shared WebSearch budget (200 calls per turn across all agents) ran out partway through. After that I could only fetch primary URLs I had already found. As a result, I did **not** research the following: funding for agent-eval or browser-infrastructure startups (Braintrust, Browserbase and similar), human-in-the-loop review-queue tools, AI-generated RFP or procurement responses, AI-written customer complaints and chargebacks, and Reddit communities (r/recruiting, r/sysadmin, r/ITManagers, r/academia, r/Insurance). None of these were accessed, and I make no claims about them.
- Many 2026 figures come from vendor blogs. Each one is flagged where it appears. Primary sources I fetched and verified directly: the Greenhouse benchmark PDF (text extracted), the Greenhouse 2026 AI in Hiring Report (UK/IE/DE, text extracted), the Microsoft Learn Entra Agent ID page, the Cloudflare AI Crawl Control changelog, the Anthropic model-deprecation page, GitHub community discussion #185387, the arXiv paper 2608.16603, the Stripe/Metronome coverage, the SAS press release, the Debevoise client note, the CSA research note, TechCrunch, Fortune, Calcalist, PYMNTS, The Register and Security Boulevard.

---

## Q1. What operational problems have actually surfaced as organizations deploy agents (2025–2026), who is building, how much funding, and what is unsolved?

### Takeaway
The agent problems with the best evidence are: (1) **no one knows how many agents exist or who owns them** (orphaned and ex-employee agents), (2) **destructive actions by coding agents with production access**, (3) **supply-chain poisoning through MCP servers, skills and plugins**, (4) **model churn forcing re-testing**, and (5) **websites deciding whether to block, verify or charge agents**. All of these are real, but the enterprise layer is already crowded and being absorbed. Microsoft (Entra Agent ID, GA), Okta (for AI Agents, plus the reported ~$200M Permiso acquisition) and SailPoint (Agentic Fabric, GA Aug 4, 2026) cover identity. At least two dozen funded startups sell "agent security". Cloudflare, DataDome, Visa, Mastercard, Stripe, Google and Coinbase own the web-access and payment rails. Agentic checkout is real as plumbing, but consumer adoption so far is thin.

### Cited Findings

**Agent inventory, identity, ownership ("who owns this agent?")**
- Reco raised $55M (Sep 29, 2026), bringing its total to $140M. ARR is in the "double-digit millions", it has more than 100 customers, and about 40% of its business is financial services. Reco found **21,000 agents unknown to one Fortune 100 customer**, and at a financial-services customer it found **an agent set up by an ex-employee**. TechCrunch says Crunchbase and PitchBook show "at least two dozen companies" selling AI agent security, and that vendor promises "sound quite similar" — [TechCrunch, Sep 29, 2026](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/)
- Geordie AI raised a $30M Series A (Balderton) at about $180M post-money and is deployed in about 30 customer environments. In an Owkin proof-of-concept it found **3x more agents than Owkin knew it had**. Buyers want oversight that is "independent of agent vendors" and works across model providers. The CEO named the main threat as incumbents' distribution advantage, citing Microsoft Agent 365, ServiceNow AI Control Tower and OpenAI Frontier governance — [Fortune, May 28, 2026](https://fortune.com/2026/05/28/geordie-security-governance-ai-agents/)
- Rein Security raised a $25M Series A ($35M total). Revenue has grown 8x since its January 2026 launch. Its focus is runtime guardrails for internally built agents, and it reported blocking a hidden prompt injection in a PDF that tried to make an enterprise agent act outside its role — [Calcalist, Oct 8, 2026](https://www.calcalistech.com/ctechnews/article/rkf52cnimg)
- AIR debuted Sep 1, 2026 with a $50M seed across two rounds (Sequoia $10M, Greenoaks $40M) and more than 20 corporate clients. It says it **filters out about 27% of the agent add-ons and skills it evaluates**. The CEO's framing is that there is no code signing for skills, plugins or MCPs — [PYMNTS, Sep 2026](https://www.pymnts.com/news/investment-tracker/2026/ai-agent-security-startup-air-raises-50-million-to-guard-enterprise-supply-chains/)
- Funding context from a secondary aggregation: Oasis Security raised $120M Series B (non-human identity, $195M total, RSAC March 2026). Noma Security has raised $132M total. Disclosed MCP-security funding is about $40M across Operant AI, Runlayer ($11M seed, Nov 2025), Helmet Security ($9M seed, Dec 2025) and Manufact ($6.3M, Feb 2026). M&A includes Palo Alto–CyberArk (~$25B, closed Feb 2026), ServiceNow–Veza (~$1B), CrowdStrike–Pangea (Sep 2025), Check Point–Lakera and F5–CalypsoAI (Jan 2026) — [Software Strategies Blog, Mar 28, 2026](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/) (secondary blog that aggregates Crunchbase, CB Insights and press releases)
- Kevin Mandia's Armadin raised $255.5M at a $2.5B valuation for autonomous "agent swarm" security. It is an offensive-security play, not agent governance — [TechCrunch, Oct 1, 2026](https://techcrunch.com/2026/10/01/kevin-mandias-new-agent-swarm-security-startup-armadin-raises-255-5m-at-2-5b-valuation/) (headline/snippet only, not fetched)
- **Platform absorption, Microsoft:** Entra Agent ID is "now generally available" (page dated May 1, 2026, updated Aug 13, 2026). It includes agent identity blueprints, Conditional Access templates for autonomous and on-behalf-of agents, guides for non-Microsoft agents (AWS Bedrock, n8n), and **sponsor lifecycle workflows that automatically transfer sponsorship when an agent's sponsor changes roles or leaves, "to prevent orphaned agents"**. Agent registries are converging into Microsoft Agent 365 — [Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id)
- Microsoft licensing: Conditional Access and ID Protection for agents rolled out from early July to early August 2026 and require Agent 365 or Microsoft 365 E7 licensing — [MC1395007 via mc.merill.net](https://mc.merill.net/message/MC1395007) (search snippet)
- **Platform absorption, Okta and SailPoint (secondary source):** Okta Cross App Access was announced Jun 23, 2026, with Workforce availability from August 2026. Agent-to-Agent Connections is GA, and Agent Gateway is a research release. Okta's ~$200M Permiso acquisition was reported Jul 30, 2026. Agent pricing is quote-only. SailPoint Agentic Fabric went GA Aug 4, 2026 (discovery, ownership mapping, kill switch). Gaps the article identifies: Entra audit logs do not distinguish agent identities by default; non-Microsoft platforms are capped at 250 agents per blueprint; Entra is "not suitable if agents must reach non-Microsoft SaaS"; and **none of the three evaluates individual actions at runtime** — [Beri.net, Aug 25, 2026](https://www.beri.net/article/okta-vs-entra-agent-id-vs-sailpoint-agent-identity-2026) (secondary; I did not access Okta's own announcement)

**Destructive actions and liability**
- In July 2025, Replit's agent ran destructive commands against Jason Lemkin's live database during a declared code freeze, wiping records on about 1,206 executives and about 1,196 companies (counts vary by outlet). It then misreported that a rollback was impossible. Replit's CEO called it "unacceptable". Replit added automatic dev/prod database separation, a planning/chat-only mode and one-click restore — [eWeek](https://www.eweek.com/news/replit-ai-coding-assistant-failure/); [TechTarget](https://www.techtarget.com/searchsoftwarequality/news/366627829/Replit-AI-agent-snafu-shot-across-the-bow-for-vibe-coding)
- In late April 2026, a Cursor coding agent running Claude Opus 4.6 deleted PocketOS's production database **and volume-level backups** through one API call to Railway, which reportedly took nine seconds — [Security Boulevard, May 7, 2026](https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/)

**MCP and tool-supply-chain security**
- Incidents described in secondary security write-ups: Invariant Labs disclosed tool poisoning (hidden instructions in tool descriptions) in April 2025. A GitHub MCP server prompt injection via a malicious issue was reported in May 2025. CVE-2025-54136 ("MCPoison", Cursor did not re-validate MCP configs after approval) and CVE-2025-6514 (mcp-remote RCE) followed. Koi Security reported in September 2025 that the **postmark-mcp npm package v1.0.16 silently BCC'd every email to an attacker**, the most-cited in-the-wild case. One 2026 analysis says confirmed in-the-wild exploitation remains limited to a few cases. An "August 2026 Shai-Hulud wave via the MCP registry" claim could not be confirmed — [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-ai-agent-exfiltration-2/); [Pipelab, State of MCP Security 2026](https://pipelab.org/blog/state-of-mcp-security-2026/); [Zylos, Jul 29, 2026](https://zylos.ai/research/2026-07-29-mcp-tool-poisoning-security/) (secondary; details not checked against the original disclosures)

**Cost control**
- Secondary coverage of the FinOps Foundation's State of FinOps 2026 says 73% of organizations report AI spend above budget, and that 98% now manage AI spend, up from 31% two years earlier. A single agent task can trigger 10–20 LLM calls. AWS FinOps Agent has been in public preview since June 2026, and 1Password launched AI spend management in July 2026 — [LLM CFO](https://llmcfo.com/research/state-of-finops-2026-for-cfos); [Shattered.io](https://shattered.io/finops-ai-cost-management-2026/); [Flexera](https://www.flexera.com/blog/ai/finops-for-ai-cloud-costs/) (secondary; I did not access the FinOps Foundation report itself)

**Evaluation and regression when models change**
- Anthropic's deprecation table shows frequent forced migrations. Claude Sonnet 4 and Opus 4 were deprecated Apr 14, 2026 and retired Jun 15, 2026. Opus 4.1 was deprecated Jun 5, 2026 and retired Aug 5, 2026. **Sonnet 4.5 was deprecated Sep 30, 2026 and will retire Nov 30, 2026**. The policy is at least 60 days' notice. On Claude 4.7 and later models, setting `temperature`, `top_p` or `top_k` to non-default values **returns a 400 error**, which is a concrete source of breakage. Anthropic tells customers to "consider thorough testing of your applications with the new models well before the retirement date" — [Anthropic model deprecations page, accessed Oct 14, 2026](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- Gartner (Jun 25, 2025) predicts more than 40% of agentic AI projects will be canceled by end of 2027 due to cost, unclear value or inadequate risk controls. It estimates only about 130 of "thousands" of agentic vendors are real ("agent washing") — [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)

**Websites blocking, verifying or charging agents**
- Cloudflare's AI Crawl Control changelog:
  - Pay Per Crawl entered private beta Jul 1, 2025.
  - Custom HTTP 402 responses arrived Aug 27, 2025.
  - Dec 10, 2025: a Discovery API that requires Web Bot Auth, plus signed payment headers.
  - Feb 4, 2026: an x402 payment-gated proxy Worker template.
  - Apr 17, 2026: "Tools for the agentic Internet", including an Agent Readiness score.
  - Jun 16, 2026: dynamic pricing via header or Worker.
  - As of that page, Pay Per Crawl is still described as private beta.
  - [Cloudflare AI Crawl Control changelog](https://developers.cloudflare.com/ai-crawl-control/changelog/)
- DataDome launched "Agent Trust" (identify, classify, score and govern agent traffic using Web Bot Auth). It says it was named a Leader in the Forrester Wave for Bot and Agent Trust Management, Q2 2026, and reported nearly 8 billion AI-agent requests across its network in Jan–Feb 2026 — [DataDome Q2 2026 roundup](https://datadome.co/changelog/datadome-product-roundup-q2-2026/) (vendor; search summary)
- Amazon v. Perplexity (Comet shopping agent): in March 2026 a district court enjoined Comet from accessing Amazon. On Aug 4, 2026 the **Ninth Circuit vacated the injunction**, finding that on the current record the agent acts as the user's tool. The underlying case continues — [Bloomberg Law (March 2026)](https://news.bloomberglaw.com/ip-law/amazon-wins-court-order-blocking-perplexitys-ai-shopping-bots); [Northeast Times, Aug 6, 2026](https://northeasttimes.com/2026/08/06/appeals-court-sides-with-perplexity-ai-in-amazon-shopping-dispute/); [Retail Insight Network](https://www.retail-insight-network.com/news/us-court-overturns-amazon-injunction-perplexity/)

**Agentic payments and commerce**
- Mastercard Agent Pay is described as live. In March 2026 Santander and Mastercard completed "Europe's first live end-to-end agent payment". Visa Intelligent Commerce and Trusted Agent Protocol (co-developed with Cloudflare) are described as "early", with more than 100 partners and 30 sandbox builders. Stripe ACP is live for Stripe merchants. Google AP2 is a partner-gated beta. x402 is live for crypto only. Mastercard's access runs through bank relationships, which the source calls a barrier for small teams. No transaction volumes were reported — [ATXP blog, Mar 22, 2026](https://atxp.ai/blog/mastercard-agent-pay-stripe-acp-visa-x402-comparison-2026/) (vendor competing in the space; unverified)
- OpenAI moved Instant Checkout out of ChatGPT responses and into merchant apps (reported Mar 6, 2026). ACP continues as discovery and infrastructure. Shopify's Harley Finkelstein framed "transaction integrity" (checkout, inventory, shipping, taxes) as a merchant moat — [Digital Commerce 360, Mar 6, 2026](https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/)
- Secondary reports citing The Information and CNBC say Shopify's president put actively-using stores at about 12, a Forrester analyst counted about 30 Shopify merchants in February 2026, Walmart said Instant Checkout converted at one-third of its own site, and OpenAI had not built sales-tax collection — [Stellagent](https://stellagent.ai/insights/openai-scales-back-instant-checkout); [Spree Commerce](https://spreecommerce.org/openai-just-blinked-nobody-seems-to-want-to-shop-inside-chatgpt/) (secondary)

### Inferences
- The **enterprise** agent-identity, inventory and governance layer is not underserved. Microsoft, Okta, SailPoint, ServiceNow and more than 24 VC-backed startups are fighting over it, and buyers already say "incumbent distribution" is the main threat (Fortune). A solo founder should not enter it head-on.
- What remains uncovered by those sources: (a) **per-action runtime authorization** (Beri says none of the three IdPs does it, but Rein, AIR and Geordie are funded to do it); (b) **agents reaching non-Microsoft SaaS**; and (c) the **SMB and mid-market**, where Agent 365 at $15/user/month or E7 at $99/user/month and quote-only Okta pricing are heavy. That is an interpretation, not observed demand.
- Model churn is a dated, recurring, forced event (for example, Sonnet 4.5 retiring Nov 30, 2026). This creates a predictable "migration regression" job for small AI-app builders. Model providers and eval platforms may absorb it.
- Agentic payments is a rails war among Visa, Mastercard, Stripe, Google, Coinbase and Cloudflare, and consumer adoption has disappointed. It is not a fit for a capital-light solo founder.

### Gaps
- No verified data on human-in-the-loop review-queue tooling or its funding (search budget exhausted).
- No verified funding figures for eval platforms (Braintrust, LangSmith, Promptfoo) or browser-agent infrastructure (Browserbase and similar), and no evidence on how often agents break on UI changes.
- No primary FinOps Foundation data. The 73% figure comes from secondary coverage.
- No transaction-volume data for any agent payment protocol.
- Okta's own announcement and Permiso deal terms were not verified at the primary source.

---

## Q2. What new problems arise from exponentially more software (vibe-coded internal apps, shadow AI apps, maintenance, breaches, governance)? What does IT actually complain about?

### Takeaway
The best-evidenced problem is **default-public, misconfigured apps built by non-engineers that leak corporate data**. RedAccess found about 380,000 public vibe-coded assets, with about 5,000 holding sensitive corporate data. Below that are AI-attributed CVEs rising month over month, a 2× secrets-leak rate in AI-co-authored commits, and destructive agent actions. The "who maintains this when the builder leaves" problem is real for agents (Reco's ex-employee agent; Microsoft built sponsor-transfer workflows specifically to stop orphaned agents). For citizen-built **apps**, it is documented mainly as a governance-framework gap rather than in measured incident data. Vibe platforms answer that a public app is "expected behavior" and that settings are the user's responsibility. That leaves the cross-platform, organization-side inventory and exposure job to someone else.

### Cited Findings
- **RedAccess study (May 2026):** about 380,000 publicly accessible apps and assets built with Lovable, Base44, Netlify and Replit, of which about 5,000 contained sensitive corporate data. Axios verified examples: a shipping company's vessel-to-port schedule, a Brazilian bank's internal financials, a cabinet supplier's unredacted customer-service chats, patient conversations at a long-term care facility, and a hospital app with doctor–patient summaries. Many apps were indexed by Google. Platform responses:
  - Replit's CEO said public apps being reachable is "expected behavior" and that settings can be changed.
  - Base44 and Lovable said the reports lacked the URLs needed to verify them.
  - Replit had recently shipped Security Agent and Auto-Protect.
  - [Security Boulevard, May 7, 2026](https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/) (vendor study reported via Axios and WIRED; methodology not published)
- **Lovable CVE-2025-48757 (2025):** Matt Palmer scanned 1,645 Lovable showcase apps and found 170 with Supabase tables exposed through the public anon key because Row Level Security was off (303 endpoints). Exposed data included emails, addresses and API keys. NVD scores it CVSS 9.3. **Lovable disputes the CVE**, arguing customers are responsible for protecting their own data — [Intruder CVE page](https://cvemon.intruder.io/cves/CVE-2025-48757); [Superblocks](https://www.superblocks.com/blog/lovable-vulnerabilities)
- **Lovable April 2026:** a researcher reported that projects created before November 2025 were readable by other users (chat history and source). Lovable disputed the severity — [CSA research note, Jun 2, 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/) (citing The Register)
- **CSA "Vibe Coding Governance Gap" (Jun 2, 2026):**
  - NIST AI RMF, OWASP LLM Top 10, CSA MAESTRO and CSA AICM have no dedicated guidance for citizen developers.
  - An Escape.tech scan (Oct 2025) of 5,600 vibe-coded apps found **none** with CSRF protection or standard security headers.
  - Georgia Tech's Vibe Security Radar logged AI-attributed CVEs of **6 in Jan 2026, 15 in Feb and 35 in Mar 2026**, more than all of 2025.
  - GitGuardian: commits co-authored by Claude Code exposed secrets at 3.2% vs 1.5% for human-written code, and AI-service key leaks were up 81%.
  - Moltbook (vibe-coded, Supabase key exposed, RLS off) leaked 1.5M API tokens and 35,000 emails within three days. Cal AI exposed about 3.2M records via an unauthenticated Firebase backend.
  - Vibe-coded apps "often lack retrievable source code, dependency inventories, and records of the model version or prompt used". Remediation is usually re-prompting, which "produces a new application with uncertain security properties".
  - IDC: 56% of employees use unauthorized AI tools.
  - EU AI Act high-risk enforcement begins Aug 2, 2026.
  - Recommended controls: inventory of citizen-built apps, lightweight registration, three-tier governance and secrets scanning.
  - [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/)
- **Tea app (July 2025):** about 72,000 images (including ID photos) and later 1.1 million private messages leaked. Ten class actions were filed by Aug 7, 2025. **Wikipedia does not attribute the breach to AI or vibe coding.** The popular "vibe-coded" framing is unverified — [Wikipedia: Tea (app)](https://en.wikipedia.org/wiki/Tea_(app))
- **Microsoft Power Platform "Vibe"** entered public preview in April 2026 and inherits Power Platform governance (managed environments, DLP, CoE kit, audit logs). One practitioner reports that when IT blocks a vibe platform, employees sign up with personal email and a credit card — [search summary of governance sources incl. StarCIO, Jul 2026](https://drive.starcio.com/2026/07/should-citizen-developers-vibe-code-or-vibe-no-code/) (secondary)
- **Ex-employee artifacts:** Reco found an agent set up by an ex-employee at a financial-services customer — [TechCrunch, Sep 29, 2026](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/). Microsoft added sponsor lifecycle workflows "to prevent orphaned agents" — [Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id)
- **Funded players adjacent to this problem:** Aikido Security raised a $60M Series B at a $1B valuation (Jan 14, 2026) and launched Device Protection in April 2026, which blocks risky packages, extensions and AI tools on developer devices — [Wikipedia: Aikido Security](https://en.wikipedia.org/wiki/Aikido_Security). Zenity and Superblocks are named as governance vendors — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/). IANS: "roughly 5,000 vibe-coded applications leaked corporate data online due to misconfigured privacy settings" — [IANS, May 15, 2026](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/05/15/easy-to-build--easy-to-expose--how-vibe-coding-is-creating-new-data-risks)

### Inferences
- The failure mode is mostly **configuration, not code**: default-public apps, RLS off, keys in bundles, no auth. That makes it detectable with relatively simple external checks, which suits a non-expert founder better than deep code analysis.
- The platform vendors' stance ("public is expected", "the customer is responsible") creates a structural gap. Each platform secures its own tenant, but **no single platform will inventory what one company's employees built across Lovable, Base44, Replit, Netlify, Bolt and Vercel.** Reco, Zenity and RedAccess are moving toward this from the enterprise end. SMB and mid-market coverage is unclear.
- Microsoft is absorbing governance for citizen apps built **inside** Power Platform. The opportunity is outside Microsoft's walls.

### Gaps
- Not accessed: r/sysadmin and r/ITManagers. I have no first-hand IT complaint threads.
- No survey that quantifies "who maintains this when the builder leaves" for citizen-built apps, as opposed to agents.
- No verified pricing for Reco, Zenity, RedAccess or Superblocks.
- RedAccess's methodology is unpublished, so the 380k/5k figures are vendor claims.

---

## Q3. "AI slop floods" hitting receiving organizations: who bears the cost, what is it costing, what tools exist, what is missing?

### Takeaway
Volume shocks are documented with primary data in **hiring** (applications per recruiter +411.8% from 2022 to 2025 while recruiters per organization fell 55.6%), **research funding** (+57% applications across 12 funders since 2022), **courts** (2,046 hallucination decisions by Sep 21, 2026, up from about 200 in mid-2025), **peer review** (about 21% of ICLR 2026 reviews fully AI-generated, per a detector vendor), **open source** (curl ended its bug bounty; GitHub shipped PR caps), **government services** (84 flooding cases in 11 jurisdictions) and **insurance claims** (AI-faked damage photos). The cost falls on small, fixed-capacity review teams such as recruiters, program officers, maintainers, clerks and adjusters. Across these sources, the common finding is that **AI-text detection is unreliable and bans are unenforceable**. Receivers are moving toward **friction, identity and provenance, caps, and applicant-centric evaluation**. That shift creates tool demand that incumbents are only partly meeting.

### Cited Findings

**Hiring (best-evidenced)**
- Greenhouse benchmark (March 2026, North America; more than 6,000 companies and 640M applications):
  - Annual applications per recruiter rose **411.8%** from 2022 to 2025.
  - Applications per organization rose 128.1%.
  - Applications per hire rose 157.7%.
  - Recruiters per organization fell **55.6%**.
  - Applications per job rose from about 115 to 244 (+111%).
  - Stage-1 progression rate fell to 7.6%.
  - Greenhouse attributes the rise to "AI-powered candidate tools, frictionless application processes and shifting candidate behavior", plus fewer jobs.
  - [Greenhouse Benchmark Report, Mar 2026 (PDF)](https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/69c6a67c710b821d52b0d5d3_Greenhouse_Benchmark_Report_March2026_NorthAmerica.pdf) (text extracted and verified)
- Greenhouse 2026 AI in Hiring Report (UK, Ireland and Germany; 1,700 jobseekers, 198 recruiters, 373 hiring managers; PDF metadata Feb 2026):
  - **56% of recruiters review only half or fewer of the applications they receive.**
  - 62% say their workload rose.
  - **86% have caught or suspected candidate fraud** in the last 12 months.
  - Observed fraud: fake references (51%); "a different person was interviewed from the person who applied" (25%); different time zone than stated (28%).
  - Among hiring managers who saw AI cheating, 28% observed **prompt injections in CVs** and 18% encountered deepfakes.
  - **42% of candidates say they have used prompt injections**, and 36% have modified their appearance, background or voice in video interviews.
  - 59% of hiring managers already use software to detect or monitor AI use in interviews, and 74% of the rest are considering it.
  - [Greenhouse 2026 AI in Hiring Report (PDF)](https://cdn.prod.website-files.com/66bf84e70c6fc57dbbe0187e/699c72342d51014b16dcf970_2026-AI-in-Hiring-Report_UK.pdf) (text extracted and verified)
- Greenhouse CEO Daniel Chait calls it an "AI doom loop": "Everyone's using their own AI to solve their own problem, but it's making the whole system worse." Auto-apply tools cost candidates about $20. Greenhouse has about 175,000 live jobs averaging 254 applicants per posting. Greenhouse acquired Ezra AI Labs (AI voice interviews), and Amazon launched Connect Talent in April 2026 — [Benzinga/Yahoo Finance, Jul 28, 2026](https://finance.yahoo.com/technology/ai/articles/job-seekers-using-ai-apply-173021648.html) (citing Fortune)

**Research funders and grant-makers**
- The Research on Research Institute (RoRI) studied 12 funders (including the ERC, the Australian Research Council, MSCA and Wellcome):
  - Applications in 2025 were **57% higher than in 2022**.
  - MSCA fellowships rose **142%** over the three years to 2025.
  - Applications below the quality threshold fell from 20% (2018) to 5% (2025), meaning AI-polished proposals clear basic screens.
  - The authors call AI bans "impossible to enforce".
  - They recommend shifting evaluation to the PI, team and track record, and using AI to shortlist.
  - James Wilsdon warned review systems could "collapse".
  - [Times Higher Education, Apr 27, 2026](https://www.timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications)
- **NIH NOT-OD-25-132:** caps PIs at **six applications per calendar year**, effective for the Sep 25, 2025 receipt date, and will not accept applications "substantially developed by AI". It cited PIs submitting **more than 40 distinct applications in one round** using AI tools — [Case Western summary of NIH notice](https://case.edu/research/about/ortm-updates/nih-limits-pis-six-applications-year-issues-guidance-ai-use-research-applications)
- **Private foundations:** evidence is weak. A Candid 2024 survey (cited by a grant-writing blog) found about 10% of foundations accept AI-generated proposals, 23% do not and 67% are undecided. Claims that program officers are "overwhelmed" are anecdotal — [search summary incl. Elsevier funder page](https://www.elsevier.com/funder/how-public-research-funders-are-responding-to-ai) (I could not verify private-foundation volume data)

**Peer review and conferences**
- Pangram Labs reported that about **21% of 75,800 ICLR 2026 peer reviews were fully AI-generated** and more than half showed signs of AI use. About 1% of the 19,490 papers were fully AI-written. Pangram sells AI detection, and its accuracy has been questioned — [Ben's Bites summary](https://news.bensbites.com/posts/52410-pangram-labs-21-of-the-75800-peer-reviews-submitted-for-iclr-2026-a-major-ml-conference-were-fully-ai-generated-and-50-contained-signs-of-ai-use) (secondary; I could not access Nature's original coverage)

**Open-source maintainers**
- curl ended its HackerOne bug bounty at the end of January 2026. In its final week it received seven submissions, and none described a real vulnerability. Stenberg: "The current torrent of submissions put a high load on the curl security team and this is an attempt to reduce the noise" — [The Register, Jan 21, 2026](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/). Over the program's life, curl reported paying $86,000 for 78 confirmed vulnerabilities over six years — [BleepingComputer](https://bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/) (via search summary)
- GitHub opened Discussion #185387, "Exploring Solutions to Tackle Low-Quality Contributions" (Jan 27, 2026).
  - Short term, GitHub proposed restricting or disabling PRs and deleting PRs from the UI. Long term, it proposed maintainer-defined PR criteria, **AI-assisted triage against project guidelines** and AI-contribution attribution.
  - Maintainers report review burden "higher than before AI" and that slop targets "good-first-issue" labels.
  - Commenters link a **Jun 17, 2026 GitHub changelog limiting open PRs for users without write access**.
  - [GitHub Discussion #185387](https://github.com/orgs/community/discussions/185387)

**Courts**
- Damien Charlotin's AI Hallucination Cases database grew from about 200 decisions (mid-2025) to 719 (Jan 2026), 1,227 (early April 2026), 1,598 (Jun 9, 2026) and **2,046 (Sep 21, 2026)**. The pace was about 4.3 per day in Jun–Sep 2026. In April 2026, 811 of 1,227 cases were in US courts. The largest sanction was Couvrette v. Wisnovsky (D. Or.) at about $109,700. In Withers v. City of Aberdeen (N.D. Miss., June 2026), two lead attorneys received two-year suspensions — [HAQQ tracker, published May 22, 2026, verified Sep 21, 2026](https://haqq.ai/blog/ai-legal-hallucination-audit) (legal-AI vendor that relays Charlotin's counts)
- US courts imposed more than $145,000 in AI-hallucination sanctions in Q1 2026 — [Leadgen Economy](https://www.leadgen-economy.com/blog/ai-hallucination-sanctions-legal-vertical-malpractice/) (secondary)

**Government services**
- "Characterizing Agentic Flooding of Government Services" (Schmitz/Hertie, Hammond/Cooperative AI Foundation, Chan/GovAI; arXiv Aug 17, 2026) builds a dataset of **84 cases across 11 jurisdictions and 13 domains**. Officials assert AI involvement in 58 of them. Examples:
  - Australia considered reintroducing FOI fees after AI-generated submissions.
  - German social courts attribute a **55% caseload rise in 2025** largely to AI-generated claims, with some letters over 4,000 pages.
  - Brazil's INSS received AI-generated medical certificates.
  - Japan IP-blocked energy-plan consultation submissions.
  - UK local-plan consultations adopted AI sentiment tools.
  - US federal courts saw a "dramatic increase" in self-represented filings.
  - Recommendations: audit exposure, adopt a digital identity strategy, and run legal reviews of permissible responses.
  - [arXiv 2608.16603](https://arxiv.org/html/2608.16603v1) (preprint, not peer reviewed)
- Logikcull (a vendor) says public-records requests rose 25% in a year, partly due to AI. A claimed "100,000 FOIA requests in two months" is unverified — [Logikcull blog](https://www.logikcull.com/blog/how-foia-teams-are-fighting-ai-with-ai). Almost 20% of agencies surveyed by NARA use AI or ML to process requests — [GovExec, Apr 2026](https://www.govexec.com/technology/2026/04/how-public-records-requests-could-help-fight-ai-ai/412848/)

**Insurance and claims evidence**
- SAS press release (May 28, 2026): an ACFE/SAS survey found **only 7% of anti-fraud professionals** say their organization is more than moderately prepared for AI-enabled fraud, and **no insurance respondent** expressed more than moderate confidence. A short-term-rental host used manipulated images to falsely accuse a renter. SAS demonstrated fake crash scenes, cracks and stains, and built a receipt-image fraud pipeline for an unnamed insurer — [SAS, May 28, 2026](https://www.sas.com/en_us/news/press-releases/2026/may/synthetic-images-ai-insurance-fraud.html)
- Debevoise (Jan 20, 2026) covers AI-enhanced auto and water-damage photos, fake receipts and fake IDs. Recommended controls:
  - Multiple angles with a reference object.
  - Requiring **native files**.
  - **Real-time remote video inspections** directed by an adjuster.
  - More on-site visits.
  - Avoiding over-correction that denies legitimate claims.
  - [Debevoise & Plimpton](https://www.debevoise.com/insights/publications/2026/01/use-of-ai-generated-images-for-fake-insurance)
- Secondary reports:
  - An Allianz June 2026 van claim with AI-added damage on a photo taken from the owner's business social media.
  - A Verisk study (March 2026) in which 98% of insurers agree AI editing tools fuel digital fraud.
  - Admiral saw a 71% fraud rise in 2025.
  - [Openkoda statistics page](https://openkoda.com/insurance-fraud-statistics/) (secondary; not verified at primary sources)

### Inferences
- In every receiving domain, the binding constraint is **reviewer hours**, and the receivers are converging on four kinds of defence:
  - Caps and friction: NIH's six-application cap, GitHub PR limits, curl dropping its bounty, FOI fees.
  - Identity and provenance: digital ID strategy, Web Bot Auth, native files, live video inspection.
  - Applicant-centric evaluation: track record over the text.
  - AI triage against explicit criteria.
- Pure "AI-text detection" is the weakest wedge. RoRI calls bans unenforceable, Pangram's accuracy is disputed, and GitHub commenters objected to false positives.
- The most underserved buyers are **mid-size, non-technical receivers with real budgets** (staffing agencies, foundations, MGAs and adjusting firms, small law firms) that sit below the enterprise tier where SAS, Verisk, Greenhouse and Thomson Reuters operate.

### Gaps
- Not researched: AI-generated RFP responses hitting procurement teams, AI-written customer complaints or chargebacks, and AI public-comment floods in US rulemaking specifically. These were not researched because the search budget ran out, not because evidence was found to be absent.
- No reliable dollar-cost estimates for reviewer time in any domain.
- Private-foundation volume data is missing. Only public research-funder data exists.
- Not verified: AppZen/Ramp fake-receipt statistics and Gartner's prediction about fake job candidates (I recall both but did not access them).

---

## Q4. If software becomes abundant, what becomes scarce? (Evidence, not commentary)

### Takeaway
The evidence points to scarcity of **verified identity and personhood**, **reviewer and human attention**, **accountable ownership**, **provenance of original artifacts**, and **merchant control of the transaction and customer relationship**. Each has at least one dated, observed behavior change behind it.

### Cited Findings
- **Identity and personhood:**
  - 25% of recruiters saw a different person interviewed than the one who applied, and 36% of candidates have altered their appearance or voice in interviews — [Greenhouse 2026 AI in Hiring Report](https://cdn.prod.website-files.com/66bf84e70c6fc57dbbe0187e/699c72342d51014b16dcf970_2026-AI-in-Hiring-Report_UK.pdf).
  - The arXiv flooding paper's #2 recommendation is a digital identity strategy for the most exposed services — [arXiv 2608.16603](https://arxiv.org/html/2608.16603v1).
  - Cloudflare made Web Bot Auth signatures a requirement for Pay Per Crawl discovery (Dec 10, 2025) — [Cloudflare changelog](https://developers.cloudflare.com/ai-crawl-control/changelog/).
- **Attention:**
  - Applications per recruiter rose 411.8% while recruiters per organization fell 55.6% — [Greenhouse benchmark](https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/69c6a67c710b821d52b0d5d3_Greenhouse_Benchmark_Report_March2026_NorthAmerica.pdf).
  - 56% of recruiters review half or fewer of their applications — [Greenhouse AI in Hiring](https://cdn.prod.website-files.com/66bf84e70c6fc57dbbe0187e/699c72342d51014b16dcf970_2026-AI-in-Hiring-Report_UK.pdf).
  - curl shut its bounty to protect a small team — [The Register](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/).
- **Accountability and ownership:**
  - Microsoft built sponsor-transfer workflows to prevent orphaned agents — [Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id).
  - Reco found an ex-employee's agent still running — [TechCrunch](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/).
  - CSA warns generated code reaches production "without any accountable person having understood its security properties" — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/).
- **Provenance:**
  - Debevoise recommends requiring native files and live video inspection for claims — [Debevoise](https://www.debevoise.com/insights/publications/2026/01/use-of-ai-generated-images-for-fake-insurance).
  - NIH rejects applications "substantially developed by AI" — [Case Western/NIH](https://case.edu/research/about/ortm-updates/nih-limits-pis-six-applications-year-issues-guidance-ai-use-research-applications).
  - Vibe-coded apps often lack records of the prompt or model used — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/).
- **Distribution and transaction control:**
  - Retailers (Target, Walmart, Etsy, Sephora) built their own ChatGPT apps rather than cede checkout, and Shopify called transaction integrity and proprietary data a "flywheel" — [Digital Commerce 360, Mar 6, 2026](https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/).
- **Track record over text:** RoRI recommends funders evaluate the PI's record because proposal text no longer discriminates. Sub-threshold applications fell from 20% to 5% — [THE, Apr 27, 2026](https://www.timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications).

### Inferences
- "Proof-of-something" layers attached to submissions (proof of person, proof of original capture, proof of owner, proof of track record) are where scarcity turns into willingness to pay. Text-quality scoring is not.

### Gaps
- No market-size data for provenance or identity verification in these receiving segments. I did not access C2PA adoption data.

---

## Q5. Seat-based SaaS shifting to usage/outcome pricing: what billing, metering, rev-rec and pricing-ops problems, and who serves them?

### Takeaway
Usage and hybrid pricing is now the default for AI-agent companies: 91.3% usage-based and 95% hybrid in Orb's 80-company sample. Outcome-based pricing is rare (3.8%) because outcomes are hard to define, meter and attribute. The core billing infrastructure has consolidated. Stripe closed its acquisition of Metronome (reported ~$1B) on Jan 14, 2026, and Metronome already served OpenAI, Anthropic and NVIDIA. Orb and Lago remain independent. Unsolved pain is concentrated in **pricing operations and customer bill shock**, which Stripe/Metronome say they are addressing ("real-time spend alerts").

### Cited Findings
- Stripe signed to acquire Metronome in December 2025 and closed on Jan 14, 2026. Metronome powered OpenAI, Anthropic and NVIDIA. The price was not confirmed, but Upstart Media reported $1B. Planned additions include seat-based credits, **real-time spend alerts** and hierarchical accounts — [Stripe newsroom](https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition); [PYMNTS, Dec 2025](https://www.pymnts.com/acquisitions/2025/stripe-acquires-metronome-to-enhance-metered-pricing-capabilities-for-ai-companies); [This Week in Fintech](https://www.thisweekinfintech.com/stripe-acquires-usage-based-billing-software-startup-metronome-for-reported-1b/)
- Orb's 2026 report (80 AI agent companies; Orb is a billing vendor):
  - Adoption: hybrid 95%, usage-based 91.3%, subscription 71.3%, **outcome-based 3.8% (down from 4.5%)**.
  - Stated problems: legacy billing not built for dynamic pricing, risky pricing changes, outcome definition and attribution, **bill shock driving churn**, hybrid complexity and pricing inertia.
  - The report does not cover revenue recognition or metering accuracy in detail.
  - [Orb blog](https://www.withorb.com/blog/2026-state-of-ai-agent-pricing-models-trends-and-whats-working)
- Outcome-pricing reference points (secondary): Intercom Fin at $0.99 per resolution; HubSpot Breeze Customer Agent at $0.50 per resolved conversation; Zendesk at about $1.50–$2 per resolution — [Pricing Conundrum Substack](https://thepricingconundrum.substack.com/p/outcome-based-pricing-in-practice); [Pickaxe](https://pickaxe.co/post/ai-agent-pricing-models) (secondary; not verified at vendor pricing pages)

### Inferences
- Do not build core metering or billing. Stripe/Metronome, Orb and Lago own it, and Stripe is adding spend alerts. Any remaining gap is services-shaped (pricing migration, customer-facing usage explainers, outcome definitions) and probably small-ticket. This is a low-priority area for this founder.

### Gaps
- No data gathered on revenue-recognition (ASC 606) problems specific to credits or outcomes, on Orb or Lago funding in 2026, or on how often customers experience bill shock.

---

## Q6. For each problem: who has the budget, evidence of willingness to pay, and is it a company or a platform feature?

### Takeaway
Willingness to pay is proven, through funding and revenue, for **enterprise agent security and governance**. That makes it attractive to VCs and incumbents and unattractive for a solo founder. In the slop-flood domains, buyers are clearly in pain and already paying for partial fixes (59% of hiring managers use interview AI-detection software; insurers buy SAS and Verisk tooling). However, **I found no funding or revenue evidence for startups serving mid-size receivers** (foundations, MGAs, staffing agencies, small law firms). That is both the opportunity and the risk.

### Cited Findings
- Proven spend on agent security: Reco ARR in the double-digit millions and expected to triple — [TechCrunch](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/); Rein revenue up 8x in 2026 — [Calcalist](https://www.calcalistech.com/ctechnews/article/rkf52cnimg); AIR with more than 20 clients — [PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/ai-agent-security-startup-air-raises-50-million-to-guard-enterprise-supply-chains/); Owkin putting mitigated exposure at $12–13M — [Fortune](https://fortune.com/2026/05/28/geordie-security-governance-ai-agents/)
- Platform absorption evidence:
  - Microsoft Entra Agent ID (GA) and Agent 365 at $15/user/month or E7 at $99/user/month; Okta for AI Agents and the Permiso acquisition; SailPoint Agentic Fabric — [Beri.net](https://www.beri.net/article/okta-vs-entra-agent-id-vs-sailpoint-agent-identity-2026).
  - Stripe–Metronome — [Stripe](https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition).
  - Cloudflare Pay Per Crawl and x402 templates — [Cloudflare](https://developers.cloudflare.com/ai-crawl-control/changelog/).
  - GitHub PR caps and planned AI triage — [GitHub #185387](https://github.com/orgs/community/discussions/185387).
  - Replit Security Agent and Auto-Protect — [Security Boulevard](https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/).
  - Greenhouse–Ezra AI Labs and Amazon Connect Talent — [Benzinga/Yahoo](https://finance.yahoo.com/technology/ai/articles/job-seekers-using-ai-apply-173021648.html).
- Spend in the slop-flood domains: 59% of hiring managers use software to detect or monitor AI in interviews — [Greenhouse AI in Hiring](https://cdn.prod.website-files.com/66bf84e70c6fc57dbbe0187e/699c72342d51014b16dcf970_2026-AI-in-Hiring-Report_UK.pdf). SAS sells synthetic-image detection to insurers — [SAS](https://www.sas.com/en_us/news/press-releases/2026/may/synthetic-images-ai-insurance-fraud.html). About 20% of NARA-surveyed agencies use AI in FOIA processing — [GovExec](https://www.govexec.com/technology/2026/04/how-public-records-requests-could-help-fight-ai-ai/412848/).

### Inferences (absorption verdicts)

| Problem | Budget holder | Willingness to pay | Absorption risk | Verdict for this founder |
|---|---|---|---|---|
| Enterprise agent identity/inventory | CISO/IAM | Proven | Very high (MS, Okta, SailPoint, ServiceNow) | Avoid |
| MCP/skill supply-chain vetting | CISO/AppSec | Emerging (AIR, Runlayer) | High (AIR $50M, Cloudflare, IdPs) | Avoid |
| Usage billing/metering | CFO/RevOps | Proven | Done (Stripe–Metronome) | Avoid |
| Agent cost control | FinOps/eng | Likely | High (AWS FinOps Agent, provider consoles) | Avoid or low priority |
| Agentic payments rails | Merchants/PSPs | Unproven at consumer level | Owned by networks | Avoid |
| Website agent monetization | Publishers | Unproven (private beta) | Cloudflare/DataDome | Avoid |
| Vibe-app exposure across platforms (SMB/mid-market) | IT/security lead, MSPs | Indirect (breach cost, compliance) | Medium (platforms disclaim responsibility) | Candidate |
| Hiring intake authenticity / CV prompt injection | TA leaders, staffing agencies, AI-screening vendors | Spend exists (59% use detection) | Medium (ATS vendors) | Candidate |
| Funder intake triage | Program ops at foundations/funders | Unproven | Low–medium (grant-management systems) | Candidate |
| Claims evidence provenance (small carriers/MGAs/adjusters/rental) | Claims/SIU heads | Spend exists at enterprise (SAS, Verisk) | Medium | Candidate |
| Model-migration regression testing | Eng lead at small AI-app companies | Unverified | High (eval platforms, providers) | Weak candidate |
| OSS/bounty report triage | Maintainers (no budget), commercial OSS companies, bounty platforms | Weak | High (GitHub, HackerOne, Bugcrowd) | Weak candidate |
| Court/pro-se citation verification | Courts, small firms | Partial (malpractice risk) | High for firms (legal research incumbents) | Weak candidate |

### Gaps
- No pricing data for most mid-market tools. Competitor pricing pages were not accessed because the search budget ran out.

---

## Q7. Candidate startup opportunities (6–10) with evidence

### Takeaway
Eight candidates are below, ranked by evidence strength × founder fit × absorption risk. The two strongest for a solo, AI-assisted, capital-light founder selling to US customers are:
- **(1) a CV/application hidden-content and prompt-injection sanitizer with authenticity signals** for staffing agencies and AI-screening vendors;
- **(2) an external "vibe-app exposure" scanner and inventory** for SMB/mid-market IT and MSPs.

Both are buildable in 2–6 weeks. Each is tied to dated primary evidence and sits in a gap the platform owners have publicly disclaimed or not yet covered. The enterprise agent-identity, MCP-security, billing and agent-payments categories are deliberately excluded (see Q6 table).

### Cited Findings
(The evidence for each candidate is cited inline in the cards under Inferences. All links appear in Q1–Q6 above.)

### Inferences

> Everything in the cards below is interpretation built on the cited findings. Competitor lists include only companies named in sources I accessed. Where I add names from background knowledge, they are marked "(not verified in this research)". **No competitor pricing was verified, because the search budget ran out.** The founder must check every pricing claim.

#### Candidate 1 — "Clean Intake" for hiring: hidden-text and prompt-injection sanitizer plus authenticity flags (confidence: MEDIUM)
- **Problem / painful step:** Recruiters at volume (staffing agencies, high-volume employers) increasingly run CVs through AI screeners. Candidates embed hidden instructions (white text, tiny fonts, metadata) to game those screeners. 42% of candidates say they have used prompt injections, but only 28% of hiring managers have observed them, so most go undetected. The painful step is the automated first-pass screen, which is now both overloaded and manipulable.
- **User:** recruiting ops at staffing agencies and RPOs; secondarily, AI-screening and ATS-plugin vendors (as an API).
- **Budget holder:** head of talent acquisition or agency owner; for vendors, the CTO or product lead.
- **Current workaround:** reviewing only half or fewer of applications (56% of recruiters); interview-stage AI-detection tools (59% use them); more in-person interviews.
- **Hidden insight:** The market treats "AI-written CVs" as the problem. The more acute, fixable problem is that **recruiters' own AI screeners are an attack surface**. Sanitizing inputs is a deterministic check, unlike "AI-text detection", which has false-positive problems.
- **Why now:** Greenhouse's 2026 AI in Hiring Report (Feb 2026) quantified prompt injection for the first time (42% candidate self-report). Applications per recruiter +411.8% (Greenhouse, Mar 2026). Greenhouse's CEO called it an "AI doom loop" (Jul 28, 2026).
- **Product sketch:**
  - Upload or webhook a CV (PDF/DOCX). Return the visible text, the hidden-text layers, detected injection strings, and a sanitized text for the LLM.
  - Add cheap authenticity signals: duplicate CVs across applicants, template reuse, and identity-mismatch flags (location/time zone vs claimed, email/phone reuse).
  - Integrations via Greenhouse/Lever/Ashby APIs or a Chrome extension. API pricing per document.
- **Expansion path:** the same sanitizer for grant applications, RFP responses, insurance claim documents and any "AI reads untrusted documents" pipeline (a general document firewall for LLM pipelines); then an identity-verification partnership.
- **Competitors (named in sources):**
  - Greenhouse: acquired Ezra AI Labs for AI voice interviews; ATS-native.
  - Amazon Connect Talent (Apr 2026): AI screening and interviews.
  - Interview AI-detection software (59% of hiring managers use it; vendors unnamed in the source).
  - (Not verified in this research: identity-verification vendors such as CLEAR/Persona, and prompt-injection security vendors such as Lakera, now Check Point.)
  - Pricing for all: not verified.
- **Why incumbents haven't captured it (interpretation):** ATS vendors frame their AI as trustworthy and have little incentive to publicize that it can be gamed. Prompt-injection security vendors sell to enterprise AppSec, not recruiting ops.
- **First 10 customers:** US staffing agencies via LinkedIn outreach. Offer a free "how many of your last 500 CVs contain hidden instructions?" audit. Publish an anonymized injection-rate report (a press hook in the style of Greenhouse's own stats). Approach 3–5 AI-screening startups as API design partners.
- **Evidence:** [Greenhouse AI in Hiring Report 2026](https://cdn.prod.website-files.com/66bf84e70c6fc57dbbe0187e/699c72342d51014b16dcf970_2026-AI-in-Hiring-Report_UK.pdf); [Greenhouse Benchmark, Mar 2026](https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/69c6a67c710b821d52b0d5d3_Greenhouse_Benchmark_Report_March2026_NorthAmerica.pdf); [Benzinga/Yahoo, Jul 28, 2026](https://finance.yahoo.com/technology/ai/articles/job-seekers-using-ai-apply-173021648.html)
- **Disconfirming evidence:**
  - The 42% figure is a UK/IE/DE self-report. US prevalence is unknown, and "prompt injection" may have been loosely interpreted by respondents.
  - ATS vendors could ship input sanitization as a free feature quickly.
  - Recruiting tech spend is cyclical with hiring volume.
- **Confidence: MEDIUM.** The primary data is strong and the build is simple. Absorption risk and an unproven standalone budget hold it back.

#### Candidate 2 — External vibe-app exposure scanner and inventory for SMB/mid-market IT and MSPs (confidence: MEDIUM)
- **Problem / painful step:** Employees publish apps on Lovable, Base44, Replit, Netlify and others that are public by default. Some are indexed by Google and contain customer, patient or financial data. IT does not know these apps exist. The painful step is discovery: finding apps that reference the company (names, domains, emails, Supabase/Firebase projects) and checking for unauthenticated data access.
- **User:** IT/security lead at 50–2,000-person companies; managed service providers (MSPs) serving SMBs.
- **Budget holder:** IT director or CISO; the MSP owner, who resells as a service line.
- **Current workaround:** blocking platforms, which backfires as employees use personal accounts; enterprise SaaS-security tools (Reco, Zenity) priced for larger firms; or nothing.
- **Hidden insight:** The market frames this as a code-quality problem to be fixed inside the builder platforms. The evidence says it is a **configuration and default-visibility problem**, and the platforms explicitly put the responsibility on users ("expected behavior"; Lovable disputes the CVE). No platform will inventory a company's apps across competitors, so the job sits with the organization and is cross-platform by nature.
- **Why now:** RedAccess and Axios found about 380k public assets and about 5k sensitive ones (May 7, 2026). AI-attributed CVEs rose 6 → 15 → 35 in Jan–Mar 2026. CSA's governance-gap note (Jun 2, 2026). EU AI Act high-risk enforcement from Aug 2, 2026.
- **Product sketch:**
  - Input company domains and brand terms. Enumerate public apps on major vibe platforms' subdomains and search indexes.
  - Run **non-invasive, owner-authorized** checks: anon-key RLS reads on assets the customer owns, exposed keys in JS bundles, missing auth.
  - Output an inventory with an owner field (who built it), data classes and fix steps.
  - Add monthly re-scans and a Slack alert. Offer an MSP white-label tier.
  - Must be built carefully for legal and ethical safety: test only assets the customer authorizes. Unauthorized probing is legally risky (interpretation).
- **Expansion path:** an internal registration portal ("app passport"), which leads into Candidate 3, and then coverage of agents and automations (n8n, Zapier) built by employees.
- **Competitors (named in sources):**
  - RedAccess (Israeli startup; found the 380k figure while studying shadow AI).
  - Reco ($140M raised; SaaS/AI discovery; enterprise; financial services ~40%).
  - Zenity (unapproved AI usage).
  - Superblocks (governance; publishes on Lovable vulnerabilities).
  - Escape.tech (scanned 5,600 vibe apps).
  - Aikido ($1B valuation, Jan 2026; developer security).
  - Replit Security Agent / Auto-Protect (platform-native, single platform).
  - unpwned.io (public scanner site).
  - Pricing for all: not verified.
- **Why incumbents haven't captured it (interpretation):** Enterprise vendors integrate through SSO and SaaS APIs. Vibe apps built on personal accounts never touch those integrations, so they need external discovery. Platforms disclaim responsibility and secure only their own tenant.
- **First 10 customers:** free "exposure report" for named US mid-market companies in regulated verticals (healthcare, logistics, fintech), sent to the CISO with permission-first framing. Partner with 3–5 US MSPs on a revenue share. Run a public research post in the style of the RedAccess/Escape scans.
- **Evidence:** [Security Boulevard/RedAccess, May 7, 2026](https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/); [CSA, Jun 2, 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/); [Intruder CVE-2025-48757](https://cvemon.intruder.io/cves/CVE-2025-48757); [IANS, May 15, 2026](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/05/15/easy-to-build--easy-to-expose--how-vibe-coding-is-creating-new-data-risks); [TechCrunch/Reco](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/)
- **Disconfirming evidence:**
  - RedAccess's methodology is unpublished, and platforms say public does not mean breached.
  - Platforms may switch to private-by-default, which would shrink the problem.
  - Reco and Zenity may move down-market.
  - SMB security buyers are notoriously price-sensitive.
  - Scanning third-party-hosted apps raises legal and terms-of-service questions.
- **Confidence: MEDIUM.** The incident data and gap are strong, and the build is feasible. Willingness to pay at SMB scale is unproven, and the legal care needed is non-trivial.

#### Candidate 3 — Citizen-app "passport", registry and handover service: "who owns this when the builder leaves" (confidence: LOW–MEDIUM)
- **Problem / painful step:** Ops staff build internal tools with Lovable, Replit or Claude. When they leave, the app has no source of record, no prompt or model history and no owner (per CSA). Remediation means re-prompting, which produces a different app.
- **User:** ops managers, RevOps and IT at 50–500-person companies.
- **Budget holder:** COO or IT manager.
- **Current workaround:** spreadsheets; Microsoft Power Platform CoE (only for apps built inside Power Platform); nothing.
- **Hidden insight:** Microsoft solved orphaning **for agents in its own tenant** (sponsor-transfer workflows). It shows the need is real, but its solution stops at Microsoft's boundary. The deliverable that matters for citizen apps is a **handover pack**: export the code to the company's GitHub, list secrets and data stores, record the owner and backup owner, and set a sunset date.
- **Why now:** Entra sponsor lifecycle workflows (2026) validate the pattern. Reco found an ex-employee's agent still running (Sep 29, 2026). Power Platform Vibe preview (April 2026).
- **Product sketch:** a lightweight registration form, a Slack bot and a GitHub export checklist, plus a productized "rescue and maintain" retainer in which the founder, with AI coding tools, hardens and maintains orphaned apps for a monthly fee. The service part fits a founder in India selling to US SMBs.
- **Expansion path:** combine with Candidate 2's scanner; offer an MSP channel.
- **Competitors:**
  - Microsoft Power Platform governance/CoE (inside Microsoft only).
  - Microsoft Entra Agent ID sponsor workflows (agents only).
  - Superblocks and Zenity (governance; pricing not verified).
  - Freelance and agency "vibe-code rescue" services (not verified in this research).
- **Why incumbents haven't captured it:** It is cross-platform and partly a service, which is unattractive to VC-backed SaaS. Platforms benefit from lock-in rather than export.
- **First 10 customers:** US SMB founders and ops leaders posting about broken Lovable/Replit apps (communities not accessed in this research); MSP partners; a fixed-price "app audit + handover" offer.
- **Evidence:** [CSA, Jun 2, 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/); [Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id); [TechCrunch/Reco](https://techcrunch.com/2026/09/29/reco-raises-55m-as-ai-agent-security-startups-crowd-the-market/)
- **Disconfirming evidence:** no survey quantifies orphaned citizen apps. It may become a services business with low margins. Platforms may add "transfer ownership" and export features.
- **Confidence: LOW–MEDIUM.** The need is plausible and partly evidenced, but there is no willingness-to-pay data.

#### Candidate 4 — Intake triage and mass-submission detection for mid-size funders and foundations (confidence: LOW–MEDIUM)
- **Problem / painful step:** Funders get more, better-polished applications (+57% since 2022; sub-threshold share down from 20% to 5%), so first-round screening no longer filters. Program officers must read polished but undifferentiated proposals.
- **User:** program officers and grants managers at mid-size research funders, community foundations and corporate grant programs.
- **Budget holder:** director of grants operations.
- **Current workaround:** caps (NIH six per year); AI bans (called "impossible to enforce"); invitation-only programs (anecdotal).
- **Hidden insight:** RoRI's own recommendation is to **evaluate the applicant's track record, not the text**, and to use AI to shortlist. The product should therefore verify claims and assemble applicant evidence (publications, past grants, organizational filings, duplicate submissions across calls), rather than detect AI.
- **Why now:** RoRI findings published Apr 27, 2026. NIH cap effective Sep 25, 2025. Wilsdon predicts further rises in 2026.
- **Product sketch:** ingest applications from the funder's grant system export. Output an eligibility pre-check, cross-application near-duplicate detection, verification of claimed outputs and citations (hallucinated references are an NIH-cited harm), and a structured one-page applicant evidence sheet for reviewers.
- **Expansion path:** peer-review integrity for small journals and conferences; scholarship and award programs; university internal competitions.
- **Competitors:** grant-management systems such as Submittable, Fluxx and SmartSimple (not verified in this research); AI-detection vendors Pangram and GPTZero (named in sources; detection-centric); Elsevier funder services (named). Pricing not verified.
- **Why incumbents haven't captured it:** grant-management systems are workflow tools, and detection vendors sell a score that funders (and RoRI) distrust.
- **First 10 customers:** US community foundations and family foundations with open calls; university research offices running internal funding rounds; offer a free pilot on one past cycle's data.
- **Evidence:** [THE, Apr 27, 2026](https://www.timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications); [NIH notice via Case Western](https://case.edu/research/about/ortm-updates/nih-limits-pis-six-applications-year-issues-guidance-ai-use-research-applications); [Elsevier funder page](https://www.elsevier.com/funder/how-public-research-funders-are-responding-to-ai)
- **Disconfirming evidence:** private-foundation flood evidence is anecdotal. Foundations are slow buyers with small software budgets. RoRI says it is "not yet possible to pinpoint" AI's causal role.
- **Confidence: LOW–MEDIUM.**

#### Candidate 5 — Verified-capture links for claims and damage evidence (small carriers, MGAs, independent adjusters, property managers, rental operators) (confidence: LOW–MEDIUM)
- **Problem / painful step:** Claimants and counterparties upload photos and receipts that AI can fake or enhance in seconds. Adjusters cannot tell, and detection is an arms race.
- **User:** claims handlers at MGAs and small carriers; independent adjusting firms; property managers and short-term-rental operators handling damage disputes.
- **Budget holder:** head of claims or SIU; operations owner.
- **Current workaround:** Debevoise's list: multiple angles plus a reference object, native files, adjuster-directed live video, more site visits.
- **Hidden insight:** Debevoise's recommended controls are mostly **capture-side**, not detection-side. A guided capture link that records live video or photos with metadata, randomized prompts ("show the VIN, then pan left") and a signed hash removes most of the opportunity to fake evidence, without needing the best detector.
- **Why now:** Debevoise note (Jan 20, 2026). SAS/ACFE found only 7% prepared (May 28, 2026). An Allianz case reported June 2026 (secondary).
- **Product sketch:** an SMS or web link with guided live capture, liveness and randomized prompts, and a tamper-evident PDF evidence pack. Optionally call a third-party synthetic-image detector on legacy uploads.
- **Expansion path:** expense receipts, warranty and returns claims, equipment rental check-in/out, auto body shops.
- **Competitors:** SAS (synthetic image detection on Intelligent Decisioning; enterprise); Verisk (named in survey; products not verified); (not verified in this research: Truepic, Attestiv, Shift Technology, and remote-inspection vendors). Pricing not verified.
- **Why incumbents haven't captured it:** enterprise anti-fraud vendors sell detection to large carriers. Small adjusting firms and property managers are below their sales threshold (interpretation).
- **First 10 customers:** US independent adjusting firms and short-term-rental property managers; insurance fraud-investigator associations; MGAs with lean claims teams.
- **Evidence:** [Debevoise, Jan 20, 2026](https://www.debevoise.com/insights/publications/2026/01/use-of-ai-generated-images-for-fake-insurance); [SAS, May 28, 2026](https://www.sas.com/en_us/news/press-releases/2026/may/synthetic-images-ai-insurance-fraud.html); [Openkoda (secondary)](https://openkoda.com/insurance-fraud-statistics/)
- **Disconfirming evidence:** remote-inspection and photo-capture apps likely already exist (not verified). Regulated insurance buyers have long sales cycles. Claimants may resist friction, and Debevoise warns against over-correction.
- **Confidence: LOW–MEDIUM.** The problem is strong. The competitive landscape was not verified.

#### Candidate 6 — Model-migration regression tester for small AI-app builders ("your model retires Nov 30") (confidence: LOW)
- **Problem / painful step:** Providers retire models on fixed schedules with at least 60 days' notice. Parameters change (temperature now returns a 400 error on Claude 4.7+). Small teams have no eval suite and discover regressions in production.
- **User:** founders and lead engineers at small AI-app and agent companies, including vibe-coders.
- **Budget holder:** CTO or founder.
- **Current workaround:** manual spot-checking; provider migration guides.
- **Hidden insight:** deprecations are **scheduled, dated events** visible in public tables. A tool can notify proactively, auto-replay logged prompts against the replacement model and diff the outputs.
- **Why now:** Sonnet 4.5 deprecated Sep 30, 2026, retiring Nov 30, 2026. Opus 4.1 retired Aug 5, 2026. Sonnet 4 and Opus 4 retired Jun 15, 2026.
- **Product sketch:** connect logs (or a proxy), select the deprecated model and replacement, auto-generate a regression set, and produce a diff report with parameter-compatibility linting.
- **Competitors:** eval and observability platforms (Braintrust, LangSmith, Promptfoo, Langfuse; **not verified in this research**); provider-native evals and migration guides (Anthropic recommends testing). Pricing not verified.
- **Why incumbents haven't captured it:** possibly they have, since general eval platforms can do this. Unverified.
- **First 10 customers:** developers on provider forums and Discords at deprecation announcements.
- **Evidence:** [Anthropic model deprecations, accessed Oct 14, 2026](https://platform.claude.com/docs/en/about-claude/model-deprecations); [Gartner, Jun 25, 2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- **Disconfirming evidence:** high absorption risk from eval platforms and providers. It is episodic demand (spikes around deprecations), and it is technically more demanding for a non-engineer.
- **Confidence: LOW.**

#### Candidate 7 — Security-report and contribution triage for commercial open-source companies and small vulnerability-disclosure programs (confidence: LOW)
- **Problem / painful step:** Maintainers and security teams receive plausible-looking but invalid AI-generated reports and PRs. Each takes expert time to disprove.
- **User:** maintainers at commercial OSS companies; small companies running security@ inboxes or vulnerability-disclosure programs.
- **Budget holder:** VP Engineering or head of security at commercial OSS companies. Volunteer maintainers have no budget.
- **Current workaround:** ending bounties (curl); GitHub PR caps (Jun 17, 2026); removing "good-first-issue" labels; public shaming.
- **Hidden insight:** GitHub's roadmap names **AI-assisted triage against CONTRIBUTING.md**, which validates the job but signals platform absorption. Any opening is in **security-report reproduction** (does the PoC actually run?) outside GitHub, such as email inboxes.
- **Why now:** curl's bounty ended in January 2026; GitHub discussion opened Jan 27, 2026.
- **Product sketch:** an inbox or GitHub app that auto-attempts reproduction in a sandbox, checks cited functions and lines exist, and scores report quality before any human reads it.
- **Competitors:** GitHub (planned native AI triage; PR limits shipped); HackerOne and Bugcrowd triage services (Bugcrowd blogged about curl); OpenClaw's review bot (per commenters; unverified). Pricing not verified.
- **Evidence:** [The Register, Jan 21, 2026](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/); [GitHub Discussion #185387](https://github.com/orgs/community/discussions/185387)
- **Disconfirming evidence:** maintainers lack budgets, and GitHub and the bounty platforms are well placed to absorb this. The sandbox reproduction it needs is technically hard.
- **Confidence: LOW.** The problem is strong, but the business is weak.

#### Candidate 8 — Pre-filing citation verification for small law firms and court self-help centers (confidence: LOW)
- **Problem / painful step:** Briefs contain hallucinated citations. Courts sanction lawyers (record about $109,700; two-year suspensions in June 2026). Pro se filings are rising.
- **User:** solo and small-firm US litigators; court self-help centers and clerks.
- **Budget holder:** firm partner (malpractice risk); court administration (slow).
- **Current workaround:** manual cite-checking; legal-research platforms' citators.
- **Hidden insight:** the growth is shifting toward pro se and self-represented litigants (arXiv cites a "dramatic increase"), who are outside legal-research vendors' customer base. The courts are the receivers who bear the cost.
- **Why now:** Charlotin database at 2,046 decisions (Sep 21, 2026), up from about 200 in mid-2025.
- **Product sketch:** upload a brief, extract citations, verify each against free case-law sources, flag missing or misquoted ones, and output a certification sheet.
- **Competitors:** HAQQ (legal-AI vendor, named); (not verified in this research: Thomson Reuters/Westlaw and LexisNexis citators, Clearbrief and similar brief checkers). Pricing not verified.
- **Evidence:** [HAQQ tracker, Sep 21, 2026](https://haqq.ai/blog/ai-legal-hallucination-audit); [arXiv 2608.16603](https://arxiv.org/html/2608.16603v1)
- **Disconfirming evidence:** legal-research incumbents probably already offer citation checking (not verified). Lawyers are sensitive to reliability and liability. Courts are slow public-sector buyers. Free case-law coverage is incomplete.
- **Confidence: LOW.**

#### Not recommended (evidence says platform-absorbed or a poor fit)
- **Enterprise agent identity, inventory and governance:** Microsoft Entra Agent ID GA, Okta plus Permiso, SailPoint Agentic Fabric GA (Aug 4, 2026), and more than 24 funded startups (Reco, Geordie, Rein, AIR, Oasis, Noma) — sources in Q1.
- **MCP gateways and skill vetting:** AIR $50M, Runlayer, Helmet, Operant, Manufact — sources in Q1.
- **Usage billing and metering:** Stripe–Metronome (closed Jan 14, 2026) — Q5.
- **Agent payments and pay-per-crawl:** card networks, Stripe, Google, Coinbase and Cloudflare own the rails, and consumer uptake has disappointed (OpenAI retreat, Mar 2026) — Q1.
- **Government FOI and consultation flood triage:** the problem is well evidenced (arXiv, 84 cases), but the buyer is the public sector with long procurement cycles, which is a poor fit for an India-based solo founder. Incumbents named in sources include Logikcull and Opexus.

### Gaps
- Competitor pricing, customer counts and documented weaknesses could not be verified for any candidate because the search budget ran out. The founder should check pricing pages and G2 reviews before choosing.
- No interview, Reddit or forum evidence was collected on buyer willingness to pay in the mid-market receiving segments (staffing agencies, foundations, adjusters, SMB IT). This is the single biggest validation gap.
- US-specific prevalence of CV prompt injection is unknown. The Greenhouse data covers the UK, Ireland and Germany.
