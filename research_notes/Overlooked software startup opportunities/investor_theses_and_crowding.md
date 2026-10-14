# Investor Theses, Crowded Categories, Thesis-vs-Ground Gaps, and Failed-Startup Opportunities (as of Oct 14, 2026)

Method and access notes, for the report writer:
- The research date is 2026-10-14. Sources marked "(fetched)" were opened and read in full. Sources marked "(search snippet)" were seen only as search-result summaries and should be treated as weaker.
- **The shared WebSearch budget ran out partway through this task.** Coverage of Sequoia (2025–26), Index, Greylock, NFX and Lightspeed, voice-agent crowding, AI recruiting, AI bookkeeping funding, AI security questionnaires, and several failed startups (Olive AI, Convoy) is therefore thin or missing. Each of these is listed under Gaps.
- The YC batch statistics are my own computation over the yc-oss mirror of the YC company directory (https://yc-oss.github.io/api/meta.json, `last_updated` 2026-10-14T02:47Z). The batch files follow the pattern https://yc-oss.github.io/api/batches/winter-2026.json. This mirror is unofficial and covers launched companies only. The keyword classification is approximate, because terms like "agent" and "model" over-match.

---

## Q1. What are YC's current Requests for Startups (2025–2026), and which themes recur?

### Takeaway
YC's RFS lists have moved in 18 months from "vertical AI agents / voice / full-stack AI companies" (2025) to "AI-native services, software for agents, SaaS challengers" (Spring and Summer 2026), and then sharply to the physical world, defense, compliance, trust and consumer (Fall 2026). Five themes recur across editions:
- AI-native service firms that sell outcomes rather than tools
- infrastructure for agents
- government and compliance work
- physical-world and industrial AI
- consumer and education AI

### Cited Findings
**Fall 2026, the current edition (fetched from ycombinator.com/rfs on 2026-10-14).** The page intro reads: "AI is moving into the physical world… includes, for the first time, one from the sitting U.S. Secretary of the Army." It has 13 requests — [YC RFS](https://www.ycombinator.com/rfs):
1. The Primer (Andrew Miklas): an adaptive tutor for reading, writing and arithmetic for young children, "something a parent buys".
2. The Future of American Defense (Daniel P. Driscoll, US Secretary of the Army): "lower the cost per kill", including low-cost interceptors, sensors and drones.
3. A Cloud for Small Software (Pete Koomen). Quote: "Software like this is now very easy to build, but still hard to deploy and share… auth & permissions are hard, and allowing nontechnical users to share arbitrary code is tricky to do securely."
4. Multiplayer AI (Aaron Epstein): live agent sessions that teams can watch, redirect and hand off.
5. Compute at Sea (Francois Chaubard).
6. AI-Powered Consumer Products for 1 Billion People (Raphael Schaad). Claims "the magic can run $1,000 a month in tokens for each user, but that is falling 10x a year."
7. AI for the Aging Population (Max Kolysh). Claims "53 million family members are already doing this work unpaid".
8. New Operating Systems for the Physical World (Charlie Warren): construction, maintenance and fleet; "these industries spend 10 to 100x more on labor than software."
9. The Best Time to Build in Crypto (Nemil Dalal). Notes that crypto prices are down and many builders are leaving.
10. Data for the Real World (Austin Tindle, Diana Hu).
11. Proving You're Human (Max Kolysh). Cites a case where a finance worker wired $25M after a deepfake video call.
12. AI-Native Compliance Infrastructure (Daivik Goel). Quote: "The pain is especially acute for businesses navigating state-by-state licensing, renewal cycles, audits, and regulatory patchwork."
13. Self-Maintaining APIs (Harsha Gaddipati). Quote: "when I worked at AWS, over 30% of our service downtime was due to external api/package changes going unnoticed… like Dependabot but for APIs."

**Summer 2026 (15 requests, per a secondary source dated Apr 28, 2026; paywalled detail not read)** — [The VC Corner](https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas) (fetched):
- AI for Low-Pesticide Agriculture (Garry Tan)
- AI-Native Service Companies (Gustaf Alströmer): insurance, accounting, compliance, healthcare admin
- AI Personalized Medicine
- Company Brain (Tom Blomfield)
- Counter-Swarm Defense (Tyler Bosmeny)
- Dynamic Software Interfaces (Ankit Gupta)
- Electronics in Space
- Hardware Supply Chain (Nicolas Dessaigne)
- Industrial Capabilities in Space (Adi Oltean)
- Inference Chips for Agent Workflows (Diana Hu)
- SaaS Challengers (Jared Friedman): ERP, chip design, supply chain
- Software for Agents (Aaron Epstein)
- Startups That Want to Sell to Huge Companies (Harshita Arora, Brad Flora)
- Supply Chain 2.0 for Semiconductors (Diana Hu)
- The AI Operating System for Companies

**"2026 RFS" published about Feb 4, 2026, probably the Spring 2026 edition. The source does not label the edition** — [TechStartups](https://techstartups.com/2026/02/04/y-combinator-is-out-with-its-2026-request-for-startups/) (fetched):
- Cursor for Product Managers
- AI-Native Hedge Funds
- AI-Native Agencies: "sell finished results, so growth isn't tied to headcount"
- Stablecoin Financial Services
- AI for Government: back-office form processing
- Modern Metal Mills
- AI Guidance for Physical Work
- Large Spatial Models
- Infrastructure for Government Fraud Hunters: False Claims Act cases
- Make LLMs Easy to Train

**Fall 2025 (secondary, Aug 4, 2025)** — [Specter](https://insights.tryspecter.com/yc-requested-startups-fall-2025/) (fetched):
- AI-Native Enterprise Software
- Infrastructure for Multi-Agent Systems
- Retraining Workers for the AI Economy
- The First 10-person, $100bn Company
- Using LLMs Instead of Government Consulting
- Video Generation as a Primitive

**Summer 2025 (secondary, May 12, 2025)** — [VC Cafe](https://www.vccafe.com/2025/05/12/requests-for-startups-2025-part-3/) (fetched):
- Full-stack AI Companies
- More Design Founders
- Voice AI
- AI for Scientific Advancement
- AI Personal Assistant
- Healthcare AI: billing and documentation
- AI Personal Tutor
- Software Tools for Robots
- The Future of Education
- AI Residential Security
- Internal Agent Builder
- AI Research Labs
- AI Voice Assistants for Email
- AI for Personal Finance

**Page navigation.** The YC RFS page lists these editions: Fall 2026, Summer 2026, Spring 2026, Fall 2025, Summer 2025, Spring 2025, Winter 2025, Summer 2024. The applications banner names the next batch as "Winter 2027", with a "November 2" deadline — [YC RFS page HTML](https://www.ycombinator.com/rfs) (fetched).

### Inferences
- **Recurring themes, counted across five editions:**
  - AI-native service firms that sell outcomes appear in 3 of 5: "Full-stack AI companies" (S25), "AI-native agencies" (Spring 2026), "AI-native service companies" (S26).
  - Agent infrastructure and software for agents appears in 4 of 5: Internal Agent Builder (S25), Multi-Agent Infra (F25), Software for Agents (S26), Multiplayer AI and Self-Maintaining APIs (F26).
  - Government, compliance and fraud appears in 4 of 5: AI for Government and Fraud Hunters (Spring 2026), Government Consulting (F25), AI-Native Compliance (F26).
  - Education and tutoring appears in 3 of 5: S25, F25 retraining, F26 Primer.
  - Physical world, defense and hardware appears in 4 of 5, and takes most of the S26 and F26 lists.
  - Consumer AI appears in S25 (assistant, finance, tutor) and returns strongly in F26.
- **Themes that dropped off.** Voice AI (S25) and Healthcare AI documentation (S25) do not reappear in 2026 RFS lists. This fits the crowding evidence in Q4.
- **Fit for a solo non-engineer.** Of the Fall 2026 requests, these are software-only: Cloud for Small Software, Multiplayer AI, Consumer AI, Aging Population (the software parts), Proving You're Human, AI-Native Compliance, and Self-Maintaining APIs.

### Gaps
- I could not retrieve the official text of the Winter 2025, Spring 2025, Fall 2025, Summer 2025, Spring 2026 or Summer 2026 RFS from ycombinator.com, because they render client-side. The lists above come from secondary sources.
- One secondary site (YC Insights) gives a conflicting Summer 2026 list. It was not used.
- The Spring 2025 and Winter 2025 RFS contents were not retrieved at all.

---

## Q2. What did recent YC batches (S25–F26) concentrate on?

### Takeaway
About 75–85% of companies in each batch mention AI. About 35–50% mention agents. Dev-tools and infra keywords hit about 25–30%. The clearest trend is a shift toward industrials and hardware: YC-labeled "Industrials" companies went from about 9–10% of S25 and F25 to about 24–25% of S26 and F26. Meanwhile, YC funded almost no new companies in the consensus-crowded app categories (AI SDR, scribes, SOC 2, generic support agents). It instead clustered heavily in AI-native accounting firms and insurance brokerages.

### Cited Findings
**Batch sizes and YC "industry" labels** (author computation from [yc-oss batch files](https://yc-oss.github.io/api/batches/winter-2026.json); launched companies only; Fall 2026 is probably still filling in):

| Batch | n | B2B | Industrials | Healthcare | Fintech | Consumer |
|---|---|---|---|---|---|---|
| S25 | 166 | 113 (68%) | 15 (9%) | 11 | 9 | 11 |
| F25 | 145 | 90 (62%) | 14 (10%) | 11 | 7 | 16 |
| W26 | 198 | 126 (64%) | 28 (14%) | 15 | 18 | 8 |
| Spring 26 | 193 | 112 (58%) | 25 (13%) | 17 | 21 | 13 |
| S26 | 230 | 117 (51%) | 57 (25%) | 22 | 16 | 10 |
| F26 | 136 | 73 (54%) | 32 (24%) | 8 | 10 | 10 |

— [yc-oss API](https://yc-oss.github.io/api/meta.json)

**Keyword shares of one-liners and descriptions** (author computation, same source; regexes are approximate):

| Keyword group | S25 | F25 | W26 | Spring 26 | S26 | F26 |
|---|---|---|---|---|---|---|
| Any AI term | 85% | 82% | 79% | 82% | 79% | 73% |
| "agent/agentic" | 43% | 42% | 37% | 49% | 34% | 36% |
| Dev-tools/infra terms | 28% | 24% | 31% | 28% | 29% | 27% |
| Robotics/hardware/defense/space terms | 19% | 19% | 24% | 24% | 34% | 32% |
| Voice | 13% | 6% | 9% | 8% | 5% | 7% |

**Independent agent-share estimate.** SylphAI's analysis of 1,632 YC companies from W24 to F26 found:
- Agent-related share by batch: 38.1% in W25, 51.0% in Spring 25, 53.0% in S25, 50.0% in F25, 45.5% in W26, 55.3% in Spring 26. The S26 and F26 samples are tiny (18 and 3 companies).
- Of 228 "CaaS" agent-infrastructure companies, **95 (about 42%) are "Agent Building Platforms"**. Next come orchestration (39), eval/monitoring (37), memory (17), API/SDK (16), auth/identity (8), voice platform (7) and payments (6).

— [SylphAI yc-agent-landscape](https://github.com/SylphAI-Inc/yc-agent-landscape) (fetched; undated, 2026)

**Third-party W26 estimates conflict**, ranging from about 60% to 85% "AI", 33–41.5% agents/agent infra, and 64% B2B. YC has published no official figure — [agentmarketcap.ai](https://agentmarketcap.ai/blog/2026/04/08/yc-w26-batch-78-percent-ai-agent-companies-early-stage-funding), [Quriosity analysis](https://github.com/Quriosity-agent/articles/blob/main/2026-03-23/yc-w26-batch-analysis-85-percent-ai-en.md) (search snippets).

**YC companies in crowded categories, S25–F26** (author keyword scan; names and one-liners from the yc-oss data):
- **AI SDR/outbound:** roughly 0–3 per batch. Examples: Cardinal (W26, "Revenue Agents for GTM teams"), Gojiberry AI (Spring 26).
- **Ambient scribe:** CareSwift (S25, ambulance reports) is the only clinical scribe. None appear after W26.
- **SOC 2/GRC automation:** 0 matches in W26, Spring 26, S26 and F26.
- **Customer-support agents:** 1–5 per batch, mostly niche (airline, e-commerce, contact center).
- **AI-native accounting/finance firms:** a dense cluster:
  - S25: Finto, Magnetic (AI tax prep for CPA firms)
  - F25: Cranston AI (tax for CPA firms), Alder (AR), Zalos
  - W26: FullSeam, End Close, Balance ("Full-Stack AI Accounting")
  - S26: Rational ("First Zero-human Accounting Firm"), Last Accounting Company, Billow AI Labs ("AI-native Accounting Firm that's killing Deloitte"), Luca IQ
- **Insurance:** a dense and growing cluster:
  - Brokerages: Fernstone, Casey (F25); Panta (W26); Kinro (Spring 26); Covera, Ignition Benefits (F26)
  - Carriers and MGAs: Hedge, Mount, Klaimee (Spring 26); Risklytics (S26); Redoubt (F26)
  - Claims and TPA: Veltha (F26 workers' comp TPA), Hesper AI (F26 claims investigator)
  - Others: Qlo (S26, "Legora for commercial insurance carriers"), Verdex (W26)
- **Healthcare billing and prior auth:** Overdrive Health, Janeen (W26); Taiga (Spring 26); LunaBill, Amera (F25).

— [yc-oss batch data](https://yc-oss.github.io/api/batches/summer-2026.json)

**Candidate-adjacent areas look thin in recent YC batches** (author scan, W24–F26):
- Only about 5 loose matches for deepfake/impersonation defense, e.g., Crosslayer Labs (W26) and DeepMark (F26), "a live watermark inside AI voice that survives phone calls".
- Essentially 0 for API breaking-change maintenance (nearest: Quantstruct, W25, stale docs).
- Essentially 0 for multi-state licensing compliance.
- A handful for aging and caregiving: Rhem Labs (F26), Cova (S26, "Financial infrastructure for family caregiving"), Oma Care (W24).

— [yc-oss all companies](https://yc-oss.github.io/api/companies/all.json)

### Inferences
- **What YC is funding right now:** physical-world and industrial companies, and "AI-native services firms" in accounting, insurance and medical billing. It funds little in classic horizontal SaaS app categories. For a solo founder, AI-native accounting firms and insurance brokerages are now crowded within YC itself.
- **Agent-building platforms are the most crowded slice of agent infrastructure** (about 42% of YC agent-infra companies). They are a strong "avoid".
- **Several F26 RFS areas look under-supplied in the directory:** Proving You're Human, AI-Native Compliance/licensing, Self-Maintaining APIs, and the software side of aging. This is consistent with YC writing RFS for gaps. Keyword matching may have missed companies, though.

### Gaps
- No official YC statistics on AI or agent share by batch exist.
- The yc-oss mirror covers launched companies only, so batch counts may be understated. F26 is incomplete.
- Funding totals by YC category were not available.

---

## Q3. What are a16z, Sequoia, Bessemer, Menlo and others saying in 2025–2026?

### Takeaway
The major investor narratives converge on six ideas:
- agents and "systems of action" displacing systems of record
- vertical AI going "multiplayer"
- outcome or services-as-software pricing
- voice agents
- AI-native rebuilds of banking, insurance and industrial infrastructure
- forward-deployed sales into legacy industries

Menlo's demand-side data confirms large and fast-growing spend, concentrated in coding, copilots and healthcare scribes. It also shows that only 16% of enterprise deployments are "true agents".

### Cited Findings
**a16z Big Ideas 2026, Part 1 (Dec 9, 2025)** — [a16z](https://a16z.com/newsletter/big-ideas-2026-part-1/) (fetched):
- Infrastructure: multimodal data chaos (Jennifer Li); AI revives cybersecurity hiring by automating Tier 1 work (Joel de la Garza); agent-native infrastructure (Malika Aubakirova); multimodal creative tools; the AI-native data stack; interactive video.
- Growth: "Systems of record lose ground" (Sarah Wang); "Vertical AI evolves… to multiplayer", with the collaboration layer as the switching cost (Alex Immerman); "Creating for agents, not humans" (Stephenie Zhang); "End of the screen-time KPI", meaning outcome-based ROI measures (Santiago Rodriguez).
- Bio+Health: "Healthy MAUs" (Julie Yoo).

**a16z Big Ideas 2026, Part 2 (Dec 10, 2025)** — [a16z](https://a16z.com/newsletter/big-ideas-2026-part-2/) (fetched):
- American Dynamism: AI-native industrial base, factory renaissance, physical observability, the electro-industrial stack, autonomous labs, and a "data crusade in critical industries".
- Apps:
  - "AI reinforces business models", e.g., Eve's outcome-based legal tools (David Haber)
  - "ChatGPT becomes the AI app store" (Anish Acharya)
  - "Voice agents take up space", from single tasks to full workflows (Olivia Moore)
  - Prompt-free proactive apps (Marc Andrusko)
  - "AI will finally upgrade banking and insurance infrastructure" (Angela Strange)
  - "Forward-deployed motions take AI to the 99%" (Joe Schmidt)
  - A Fortune 500 orchestration layer with "agent supervisors" (Seema Amble)
  - Consumer AI "see me" (Bryan Kim)
  - New model primitives (Kimberly Tan)
  - "AI startups selling to other AI startups", i.e., greenfield customers (James da Costa)

**a16z Big Ideas 2026, Part 3, crypto (Dec 11, 2025)** — [a16z](https://a16z.com/newsletter/big-ideas-2026-part-3/) (fetched). Relevant items include "From KYC to KYA (Know Your Agent)" (Sean Neville), stablecoin on/off-ramps, x402 agent payments, and "The invisible tax on the open web".

**a16z speedrun "14 Big Ideas for 2026" (Dec 18, 2025)** — [speedrun](https://speedrun.substack.com/p/14-big-ideas-for-2026) (fetched). Items include:
- "Multi-player AI will eat single-player AI" (Fareed Mosavat)
- "Pricing will become earned, not negotiated", i.e., outcome bounties (Macy Mills)
- "AI-native marketplaces will work for the buyer" (Sam Shank)
- "Fat AI startups will own the slowest markets", bundling software, data, hardware and human ops (Andrew Lee)
- "The coming consumer AI renaissance": tutoring, therapy, travel (Kenan Saleh)
- "VC will eat PE" (Troy Kirwin)

**Bessemer "State of AI 2025" (Aug 13, 2025)** — [BVP](https://www.bvp.com/atlas/the-state-of-ai-2025) (fetched):
- "Supernovas" reach about $40M ARR in year 1 and about $125M in year 2, at about 25% gross margin ("often negative"), with $1.13M ARR per FTE.
- "Shooting Stars" reach about $3M, $12M, $40M and $103M in years 1–4, at about 60% gross margin.
- The new benchmark is "Q2T3". Bessemer says the five-year trajectory "is not yet proven".
- Theses: systems of action replacing systems of record; memory and context as moats; a narrow wedge; vertical AI in "technophobic" industries; private evals; an M&A wave in vertical software.
- Warnings:
  - Supernova revenue is "vulnerable due to low switching costs or novelty-driven adoption".
  - Competitive intensity is 2–3x higher in promising areas.
  - "Demos can outpace real product value."

**Menlo Ventures "2025 State of Generative AI in the Enterprise" (Dec 9, 2025; survey of 495 US decision-makers)** — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) (fetched):
- Spend: $37B in 2025, up from $11.5B in 2024. Apps took $19B.
- Departmental AI was $7.3B, with coding at $4.0B (55%).
- Vertical AI was $3.5B: healthcare about $1.5B (ambient scribes $600M, up 2.4x), legal $650M, government $350M.
- Horizontal AI was $8.4B: copilots $7.2B, agent platforms $750M.
- 76% of AI solutions are bought rather than built, up from 53% in 2024.
- 47% of AI deals reach production, versus 25% for traditional SaaS.
- 27% of app spend comes via product-led growth (about 40% including shadow AI).
- Startups hold 63% of the app market. By function, startup share is 78% in sales and 91% in finance and ops.
- **Only 16% of enterprise deployments (27% of startup deployments) qualify as true agents.**
- LLM API share: Anthropic 40%, OpenAI 27%, Google 21%.

**Sequoia "Generative AI's Act o1" (Oct 9, 2024; Sonya Huang, Pat Grady)** — [Sequoia](https://www.sequoiacap.com/article/generative-ais-act-o1/) (fetched):
- Models are a "knife-fight"; applications are the most promising layer.
- "Services-as-software": the shift is from seats to outcomes and from the software profit pool to the services profit pool, with a TAM "in the trillions".
- Example: Sierra charges per resolution.

**MIT NANDA "GenAI Divide" (reported Aug 18, 2025)** — [Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) (fetched):
- About 95% of enterprise GenAI pilots show little or no measurable P&L impact.
- Purchased or partnered solutions succeed about 67% of the time; internal builds succeed about one-third as often.
- More than half of GenAI budgets go to sales and marketing tools, but **the largest measured ROI is in back-office automation**: cutting BPO and agency spend.
- Methodology: 150 interviews, 350 surveyed employees, and 300 public deployments.
- Menlo's report explicitly disputes the 95% framing as "boom, not bubble" — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).

### Inferences
- **The consensus investor theses** for late 2025 and 2026 are: agents and systems of action; multiplayer vertical AI (a16z Growth, a16z speedrun and YC F26 all independently); outcome pricing; voice; physical and industrial AI; and banking and insurance infrastructure. Because these are consensus, they are where competition from VC-funded teams is highest.
- **Menlo's split** suggests the money concentrates where workflows are measurable and buyers already exist: coding, copilots, scribes, support. "Agents" as marketed remain mostly fixed workflows.

### Gaps
- **Not accessed because the search budget ran out:** Sequoia's 2025–2026 pieces (e.g., AI Ascent 2025), Index Ventures, Greylock, NFX, Lightspeed, Bessemer State of the Cloud 2026 and Roadmaps, a16z speedrun program terms and priorities, and a16z enterprise or fintech-specific 2026 theses.
- The a16z Bio+Health part of Big Ideas was only partially covered (the Part 1 excerpt).

---

## Q4. Which software categories are crowded or overstated? (feeds "Ideas to avoid")

### Takeaway
Strong evidence of crowding or commoditization exists for six categories:
- AI SDRs (churn and opt-out contracts)
- ambient scribes (Epic shipped a native product in Feb 2026)
- AI customer-support agents (Sierra at $15.8B, Decagon at $4.5B, plus incumbents)
- AI coding tools (negative margins, and model labs competing directly)
- SOC 2 automation (price compression plus Delve's credibility crisis)
- generic agent-building platforms (about 42% of YC agent infra)

Meeting notetakers and PI demand letters are crowded and dominated by a few leaders. Evidence for voice receptionists, AI recruiting, AI bookkeeping and security questionnaires was not gathered.

### Cited Findings

**AI SDRs/outbound**
- 11x raised a $24M Series A (Benchmark, Sep 2024) and a $50M Series B (a16z).
- Ex-employees said 70–80% of customers churned. 11x says current retention is 79%.
- 11x used three-month "break clauses", and one ex-employee said it might report $14M ARR when contracts past the trial totaled about $3M.
- ZoomInfo said the product "performed significantly worse than our SDR employees", and ZoomInfo and Airtable logos were used without permission.

— [TechCrunch, Mar 24, 2025](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/) (fetched)

- Founder Hasan Sukkar stepped down to non-executive chairman in May 2025 — (search snippet summarizing coverage; primary not opened).
- Artisan's CEO cited 250 customers and $5M ARR, and acknowledged customer losses. A claimed GRR below 60% is unverified — (search snippets from competitor blogs; low reliability).
- In recent YC batches only about 0–3 new outbound/SDR companies appear per batch — [yc-oss](https://yc-oss.github.io/api/batches/winter-2026.json).

**Ambient medical scribes**
- Epic made native AI Charting broadly available on Feb 4, 2026. It listens, drafts notes and suggests orders.
- Epic holds 42% of the acute-care EHR market (KLAS).
- Named startups include Abridge (Best in KLAS 2026), Ambience, Suki, Notable, Heidi and DeepScribe. Startups are repositioning toward specialties and adjacent workflows.

— [MedCity News, Feb 5, 2026](https://medcitynews.com/2026/02/ambient-scribe-ai-startups-epic/) (fetched)

- Epic uses Microsoft Dragon technology. Pricing is unpublished; a rumored $80 per provider per month is unconfirmed — [HIT Consultant, Feb 5, 2026](https://hitconsultant.net/2026/02/05/epic-releases-ai-charting-ambient-ai-market-implications/) (search snippet).
- A JAMA study from April 2026 reportedly found about 16 fewer minutes of documentation per 8-hour day and no change in after-hours charting — [beri.net summary](https://www.beri.net/article/best-ambient-ai-scribes-health-systems-abridge-epic-ai-charting-dragon-copilot) (search snippet; the JAMA original was not opened).
- Category spend was $600M in 2025, up 2.4x — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).

**AI customer support agents**
- Sierra reportedly raised $950M in May 2026 at a $15.8B valuation (about $1.6B raised in total) and passed $100M ARR in Nov 2025.
- Decagon was valued at about $4.5B in Jan 2026, with about $481M raised.
- Other competitors: Intercom Fin, Zendesk, Salesforce Agentforce, Ada, Gladly, Parloa.
- Third-party pricing estimates: Decagon about $95K–$590K per year; Sierra in the six figures.

— [Contrary Research](https://research.contrary.com/company/sierra), [Wikipedia: Decagon](https://en.wikipedia.org/wiki/Decagon_(company)) (search snippets; figures not verified against primary press releases)

- Only 1–5 support-agent companies per YC batch, mostly niche — [yc-oss](https://yc-oss.github.io/api/batches/spring-2026.json).

**AI coding agents and IDEs**
- Coding was $4.0B of $7.3B departmental AI spend in 2025 — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).
- Windsurf's gross margins were "very negative". The Mocha founder said "Margins on all of the 'code gen' products are either neutral or negative."
- Cursor repriced to pass through Claude costs, and its CEO apologized.
- Model makers compete directly: Claude Code, OpenAI Codex.

— [TechCrunch, Aug 7, 2025](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/) (fetched)

- Replit's gross margin is about 23% and Lovable's about 35% — [Sacra](https://sacra.com/research/finance-ops-replit-ai-dev-platforms) (search snippet).
- CodeParrot (YC W23, Figma-to-code) shut down in July 2025, with MRR that peaked around $1.5K, as Copilot and Replit expanded — [TechStartups, Dec 9, 2025](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/) (fetched).

**AI meeting notetakers**
- Granola reportedly raised a $125M Series C at a $1.5B valuation. Sources conflict on the date (Mar 2026 vs 2025). YipitData spend panels show "near-zero churn".
- Otter reportedly passed $100M ARR (Mar 2025); its last primary raise was in 2021.
- Fireflies reportedly passed a $1B valuation (Jun 2025).
- Other competitors: Fathom, Read AI, tl;dv, Circleback (YC W24).

— [YipitData](https://www.yipitdata.com/resources/granola-vs-fathom-otter-fireflies-ai-notetaking) (search snippet); the other figures are search-snippet summaries of vendor and aggregator blogs.

- Only 0–4 YC companies per batch in this space — [yc-oss](https://yc-oss.github.io/api/batches/fall-2025.json).

**AI personal-injury demand letters**
- EvenUp raised a $150M Series E at a "$2B+" valuation (about $385M raised in total). Tracxn shows a $3B post-money valuation as of Oct 2025, which conflicts — [EvenUp blog](https://www.evenuplaw.com/blog/evenup-2b-valuation/) (search snippet).
- Supio raised a $25M Series A (Sapphire, 2024), with about $85–91M raised in total and a Thomson Reuters partnership — [Supio press](https://www.supio.com/press/supio-emerges-from-stealth-with-25m-series-a-revolutionizing-legal-tech-for-personal-injury-law-firms) (search snippet).
- YC companies here include Andco (Spring 26, "Agents that build personal injury cases"), Mimos (S25) and Kalinda (S25) — [yc-oss](https://yc-oss.github.io/api/companies/all.json).

**AI legal (general)**
- Legal AI spend was $650M in 2025 — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).
- Clio is valued at $5B — [TechCrunch, May 22, 2026](https://techcrunch.com/2026/05/22/how-vcs-and-founders-use-inflated-arr-to-kingmake-ai-startups/).
- YC S26 includes "Qlo: Legora for commercial insurance carriers", which shows Legora as a reference brand — [yc-oss](https://yc-oss.github.io/api/batches/summer-2026.json).

**SOC 2 / compliance automation**
- Vendr-reported medians: Vanta about $20K, Secureframe about $20K, Drata about $25K per year.
- Entry tiers: Vanta Essentials from $14K on AWS Marketplace; Delve from $12K; Sprinto about $6–10K.
- Add-on frameworks cost about $5–10K each.

— [soc2auditors.org](https://soc2auditors.org/insights/soc-2-software-pricing-comparison/) (search snippet)

- Delve reportedly announced on Mar 24, 2026 that it would arrange no-cost re-audits with an independent AICPA-accredited auditor for active customers, amid "fake audits" allegations — [complies.ai](https://complies.ai/blog/delve-alternatives), [tech-insider](https://tech-insider.org/vanta-vs-drata-vs-delve-compliance-automation-2026/) (search snippets from competitor and secondary sites; primary reporting not verified).
- Zero SOC 2/GRC-automation keyword matches appear in YC W26, Spring 26, S26 or F26 — [yc-oss](https://yc-oss.github.io/api/batches/summer-2026.json).

**Generic agent-building platforms**
- 95 of 228 YC agent-infra companies (about 42%) are "Agent Building Platforms" — [SylphAI](https://github.com/SylphAI-Inc/yc-agent-landscape).
- The whole agent-platform category drew only $750M of enterprise spend in 2025 (about 10% of horizontal AI), and only 16% of enterprise deployments are true agents — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).
- YC's own S25 RFS asked for an "Internal Agent Builder" — [VC Cafe](https://www.vccafe.com/2025/05/12/requests-for-startups-2025-part-3/).
- Tune AI (a GenAI platform with fine-tuning) shut down in 2025 because hyperscalers and open source offered similar features more cheaply, and most users were free — [TechStartups](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/).

**Enterprise "chat with your docs" / RAG**
- Subtl.ai (Hyderabad) shut down in July 2025. It had "no repeatable niche" and every client needed custom work.
- Noogata (enterprise AI analytics, $28M raised) shut down in May 2025 because deals "stuck in pilots".

— [TechStartups](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/)

- YC S26 still asks for a "Company Brain", which is an incumbent-heavy space — [The VC Corner](https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas).

### Inferences

**"Ideas to avoid" verdicts.** Strength of evidence varies, as noted per row.

| Category | Verdict | Basis |
|---|---|---|
| AI SDR | Avoid | Churn, opt-outs, reputational damage, few new YC entrants |
| Ambient scribes | Avoid | Epic native product plus Microsoft; funded leaders |
| AI support agents | Avoid | Multibillion-dollar leaders and incumbents |
| AI coding IDEs/agents | Avoid | Margins, and model labs competing |
| Generic agent builders | Avoid | Crowded; tiny spend relative to supply |
| SOC 2 automation | Avoid | Commoditizing entry price; trust shock |
| Meeting notetakers | Avoid | Leader momentum plus platform bundling (bundling not verified here) |
| PI demand letters | Avoid | EvenUp scale |
| Generic enterprise RAG | Avoid | Failures plus Glean-type incumbents (Glean not verified here) |

- **Why the pattern repeats.** In each case either a system-of-record owner (Epic, Intercom, Salesforce) or a model lab can ship the feature natively, or a winner already holds a large war chest.

### Gaps
- No evidence was gathered (the search budget ran out) for:
  - voice agents for SMB phone answering
  - AI recruiting screeners
  - AI bookkeeping funding (Pilot, Digits, Basis)
  - AI security questionnaires (Conveyor, Vanta Trust Center)
  - Harvey and Legora valuations
  - platform-native notetakers (Zoom, Teams, Meet)
- The Delve allegations rest only on secondary competitor sites. Verify them before citing in a final report.

---

## Q5. What evidence exists on revenue quality in AI applications?

### Takeaway
There is strong evidence that headline AI ARR overstates durable revenue:
- AI-native median gross revenue retention (GRR) is about 40%, and about 23% for products under $50 per month.
- Contracted ARR (CARR) is routinely reported as ARR, sometimes 70% above live revenue.
- 3-month opt-out contracts are common.
- Supernova-type companies run at about 25% (often negative) gross margins, because of inference costs.

The evidence also points to protective factors: price points above $250 per month, annual plans, larger B2B deals, and back-office use cases.

### Cited Findings
**ChartMogul retention study (Dec 10, 2025; about 3,500 companies, with retention measured on those above $250K ARR)** — [ChartMogul report](https://chartmogul.com/reports/saas-retention-the-ai-churn-wave/) (fetched):
- AI-native median GRR is 40% and NRR is 48%. B2B SaaS median NRR is 82%; B2C SaaS median NRR is 49%.
- AI-native GRR by monthly price: above $250 is 70% GRR / 85% NRR; $50–249 is 45% / 61%; under $50 is 23% / 32%.
- AI GRR rose from 27% (Jan 2025) to 40% (Sep 2025).
- Annual plans show 10–20 points higher NRR.
- Caveat: the buckets are about 50 companies each, so results are directional.

**Growth Unhinged commentary on the same data** — [Growth Unhinged](https://www.growthunhinged.com/p/the-ai-churn-wave) (fetched):
- "AI has a tourist problem."
- "3-month opt-out contracts (70-80% opt out)."
- Low-retention companies are about 3x as likely to be shrinking as growing fast.
- a16z's FDE model "trades margin for moat".

**Inflated ARR** — [TechCrunch, May 22, 2026](https://techcrunch.com/2026/05/22/how-vcs-and-founders-use-inflated-arr-to-kingmake-ai-startups/) (fetched):
- Spellbook CEO Scott Stevenson called inflated ARR a "huge scam".
- One VC has seen CARR run 70% above ARR.
- Reported examples: a yearlong free pilot counted as ARR; a "$50M ARR" claim against $42M on the books; a company claiming over $100M ARR when only a fraction came from paying customers.
- Clio's Jack Newton alleges VCs tolerate the practice.

**"Experimental run-rate revenue" (ERR)** as a named concept for volatile, uncommitted AI spend — [Intel Capital](https://www.intelcapital.com/your-ai-revenue-is-not-recurrent/) (search snippet).
- Madrona research reportedly found 77% of enterprises re-evaluate AI vendors every six months or on a rolling basis (search snippet; primary not verified).
- A conflicting benchmark (The SaaS Barometer) reports AI-native median NRR of 132% and GRR of 89%; its methodology differs — [SaaS Barometer](https://thesaasbarometer.substack.com/p/beyond-benchmarks-2025) (search snippet).

**Margins**
- Bessemer: Supernovas about 25% gross margin, "often negative"; Shooting Stars about 60% — [BVP](https://www.bvp.com/atlas/the-state-of-ai-2025).
- Code-gen margins are "neutral or negative" — [TechCrunch](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/).
- YC F26 says power-user consumer AI "can run $1,000 a month in tokens for each user", falling 10x per year — [YC RFS](https://www.ycombinator.com/rfs).

**Pricing shift: seat → usage → outcome**
- Sequoia: seats → outcomes, as in Sierra's per-resolution pricing — [Sequoia](https://www.sequoiacap.com/article/generative-ais-act-o1/).
- a16z: "end of the screen-time KPI" and "AI reinforces business models" (Eve's outcome-based pricing) — [a16z Pt1](https://a16z.com/newsletter/big-ideas-2026-part-1/), [a16z Pt2](https://a16z.com/newsletter/big-ideas-2026-part-2/).
- speedrun: "pricing will become earned" — [speedrun](https://speedrun.substack.com/p/14-big-ideas-for-2026).
- Replit moved from flat-rate to usage-based pricing — [Sacra](https://sacra.com/research/finance-ops-replit-ai-dev-platforms) (search snippet).
- Cursor repriced its heavy users — [TechCrunch](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/).

**Pilot-to-production rate.** Menlo says 47% of AI deals reach production (vs 25% for SaaS). MIT NANDA says 95% of pilots have no P&L impact. These measure different things — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), [Fortune/MIT](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/).

### Inferences
- **Pricing and packaging for the founder** (design implications, not facts): price above $250 per month per account, sell annual contracts, and sell to businesses rather than consumers. Pick workflows where the outcome is countable, so outcome pricing is defensible: verified payment changes, renewed licenses, recovered dollars. Avoid "tourist"-prone prosumer tools.
- **Treat competitor ARR claims with skepticism** when sizing incumbents. The CARR inflation evidence means a "$50M ARR" competitor may be smaller.

### Gaps
- No primary Madrona or a16z churn studies were retrieved.
- No public data on gross margin by AI vertical outside coding was found.

---

## Q6. Which notable startups failed in 2023–2026 with the underlying problem still unsolved?

### Takeaway
Shutdowns rose: Carta counted 966 US shutdowns in 2024 vs 769 in 2023. The verified 2024–2025 failures with problems that persist are:
- Bench: SMB bookkeeping
- Cushion: consumer fee recovery
- Builder.ai: custom software for non-technical businesses
- Noogata and Subtl.ai: enterprise analytics and RAG stuck in pilots
- Humane: an AI device

The failure causes were capital-intensive human-ops models with debt (Bench), sub-scale B2C economics (Cushion), misrepresented AI with human labor behind it (Builder.ai), and pilots that never converted (Noogata). Several of these problems are now targets of YC-funded "AI-native service" firms. That makes them less open, not more.

### Cited Findings
**Shutdown counts**
- Carta: 966 US startup shutdowns in 2024 vs 769 in 2023. AngelList: 364 wind-downs in 2024 vs 233 in 2023 — [TechCrunch, Jan 26, 2025](https://techcrunch.com/2025/01/26/2025-will-likely-be-another-brutal-year-of-failed-startups-data-suggests) (search snippet).
- SimpleClosure's 2025 report says shutting-down companies are "older, have raised more capital" — [BusinessWire, Oct 22, 2025](https://www.businesswire.com/news/home/20251022023911/en). The release returned 403; this is from a search snippet only.

**Bench Accounting** (SMB bookkeeping software plus in-house bookkeepers) — [Wikipedia: Bench Accounting](https://en.wikipedia.org/wiki/Bench_Accounting) (fetched; the article is flagged for promotional content and some citation issues):
- Raised over $100M, including a $60M Series C in 2021.
- On Dec 27, 2024 it told customers the platform would be "immediately inaccessible".
- About 600–650 employees were affected.
- It defaulted on more than $65M of debt and filed for bankruptcy in Canada on Jan 7, 2025, with about $2.8M cash against $65.4M of liabilities.
- Employer.com announced an acquisition on Dec 30, 2024, and Bench was later folded into Employer.com's back-office offerings.
- The number of affected customers is not stated in the source.

**Cushion** (a consumer app that found bank fees and negotiated refunds, later "Plaid for BNPL") — [TechCrunch, Jan 30, 2025](https://techcrunch.com/2025/01/30/fintech-startup-cushion-shuts-down-after-8-years-and-over-20-million-in-funding) (fetched):
- About $21.6M raised; $82.4M post-money valuation in 2022.
- More than 1M consumers onboarded, more than 200K paying customers, and $3M ARR within 10 months.
- Wound down at the end of 2024 because it "didn't reach the scale needed to sustain the business".

**2025 AI shutdowns** — [TechStartups, Dec 9, 2025](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/) (fetched; internal inconsistencies noted):

| Company | Funding | What it did | Why it failed |
|---|---|---|---|
| Builder.ai | About $445M | No-code app development with "Natasha"; work routed to human engineers | Overstated AI and questionable financials. Lender seized cash; insolvency mid-2025 |
| Humane | About $230–241M | AI Pin wearable | Unreliable device; shut Feb 2025. IP and team sold to HP for about $116M |
| Noogata | $28M | Enterprise AI analytics | Deals stayed small or stuck in pilots; shut May 2025 |
| Locale.ai | About $5M | Geospatial analytics | Founder-dependent sales |
| Subtl.ai | About $200K | Enterprise RAG | No repeatable niche, custom work per client; shut Jul 2025 |
| Tune AI | Seed (Accel, Flipkart) | GenAI chat and fine-tuning platform | Commoditized by hyperscalers |
| Wuri (YC W23) | Seed | Visual-novel app, pivoted to enterprise AI wrappers | Pivots and low willingness to pay |
| CodeParrot (YC W23) | $500K | Figma-to-code | Output needed too much cleanup; shut Jul 2025 |
| Astra | Angel | Sales AI assistant | Customers reluctant to share sales data; long cycles |
| Yara AI | Pre-seed | AI mental-health companion | Safety risk; shut Nov 2025 |

### Inferences

**How each problem has changed since the failure (interpretation):**

| Failure | What has changed | Assessment |
|---|---|---|
| Bench | LLMs cut the human-bookkeeper cost per client, so the problem is more solvable. YC's S26 cluster of 4+ AI-native accounting firms plus earlier entrants shows investors see the same thing. | Unsolved but no longer under-contested. |
| Cushion | Voice and agent tech could automate negotiating calls. | The core failure (sub-scale B2C, commission-on-recovery economics) is unchanged, and B2C AI retention is poor (Q5). Low attractiveness. |
| Builder.ai | Coding agents now build small apps cheaply. YC F26 says the unsolved part has moved to deploying, sharing, auth and governance ("A Cloud for Small Software"). | The problem shrank but did not disappear. |
| Noogata, Subtl.ai | The "custom work per client, stuck in pilot" failure mode is the same one MIT NANDA describes. | Lesson for the founder: pick a narrow workflow with a countable outcome. |

### Gaps
- **Not verified in this session:**
  - Olive AI (healthcare admin automation, shut down 2023). The Wikipedia URL returned 404.
  - Convoy (digital freight, shut down Oct 2023). The Wikipedia URL returned 404.
  - Tally (consumer debt, 2024), Forward (CarePods, 2024), Vowel (meetings), Pandion (logistics, Jan 2025), Synapse (BaaS, 2024).
- These are well-known failures but were not sourced here. A follow-up search should confirm them before they appear in the report.
- A Carta 2025 full-year shutdown figure was not found.

---

## Q7. Where do investor theses conflict with ground-level evidence?

### Takeaway
Seven conflicts are well evidenced:
1. The "agents everywhere" narrative versus very few true agent deployments.
2. Front-office budgets versus back-office ROI.
3. Hypergrowth ARR versus 40% median GRR and CARR inflation.
4. "Systems of record lose ground" versus Epic absorbing the scribe layer.
5. "Consumer is back" versus poor B2C AI retention.
6. Coding as the "killer app" versus negative margins and model labs competing.
7. Founder-friendly "AI-native services" theses versus heavy crowding of the same verticals inside YC.

### Cited Findings

**Agents narrative vs. deployment reality**
- Investor side:
  - a16z: "agent-native infrastructure becomes table stakes" — [a16z Pt1](https://a16z.com/newsletter/big-ideas-2026-part-1/).
  - YC RFS on agent infra and multiplayer agents — [YC RFS](https://www.ycombinator.com/rfs).
  - 34–49% of YC companies mention agents (author computation) — [yc-oss](https://yc-oss.github.io/api/meta.json).
  - 55.3% of YC Spring 26 is agent-related — [SylphAI](https://github.com/SylphAI-Inc/yc-agent-landscape).
- Ground side: only 16% of enterprise deployments are true agents, and agent platforms drew $750M of $37B — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).

**Where budgets go vs. where ROI shows up.** More than half of GenAI budgets go to sales and marketing, but the biggest measured ROI is back-office BPO and agency replacement — [Fortune/MIT](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/). Meanwhile:
- Menlo reports 78% startup share in sales AI — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).
- 11x churn and break clauses — [TechCrunch](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/).

**Hypergrowth benchmarks vs. revenue quality**
- Investor side: Bessemer's Supernova benchmark of $40M then $125M ARR — [BVP](https://www.bvp.com/atlas/the-state-of-ai-2025).
- Ground side:
  - AI-native median GRR of 40% — [ChartMogul](https://chartmogul.com/reports/saas-retention-the-ai-churn-wave/).
  - CARR up to 70% above ARR — [TechCrunch](https://techcrunch.com/2026/05/22/how-vcs-and-founders-use-inflated-arr-to-kingmake-ai-startups/).

**"Systems of record lose ground" vs. a system of record absorbing the AI layer**
- Investor side: Sarah Wang, a16z — [a16z Pt1](https://a16z.com/newsletter/big-ideas-2026-part-1/). Bessemer's "systems of action" thesis — [BVP](https://www.bvp.com/atlas/the-state-of-ai-2025).
- Ground side: Epic, with 42% of acute EHR, shipped native AI Charting and put startup scribes on notice — [MedCity](https://medcitynews.com/2026/02/ambient-scribe-ai-startups-epic/).

**"Consumer is so back" vs. B2C retention**
- Investor side: YC F26 consumer RFS — [YC RFS](https://www.ycombinator.com/rfs); a16z speedrun "consumer AI renaissance" — [speedrun](https://speedrun.substack.com/p/14-big-ideas-for-2026).
- Ground side: B2C SaaS median NRR is 49%, and AI products under $50 per month have 23% GRR — [ChartMogul](https://chartmogul.com/reports/saas-retention-the-ai-churn-wave/). Cushion failed despite more than 200K paying users — [TechCrunch](https://techcrunch.com/2025/01/30/fintech-startup-cushion-shuts-down-after-8-years-and-over-20-million-in-funding).
- Counter-evidence: Granola's reported "near-zero churn" — [YipitData](https://www.yipitdata.com/resources/granola-vs-fathom-otter-fireflies-ai-notetaking) (search snippet).

**Coding as the first "killer use case" vs. margins.** Menlo puts coding at $4.0B — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/). TechCrunch reports neutral-to-negative margins and model makers competing — [TechCrunch](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/).

**Forward-deployed sales vs. economics.** a16z promotes FDE motions into legacy verticals — [a16z Pt2](https://a16z.com/newsletter/big-ideas-2026-part-2/). The same playbook is described as one that "trades margin for moat" — [Growth Unhinged](https://www.growthunhinged.com/p/the-ai-churn-wave).

**YC's own investment mix is shifting away from pure software.** Industrials went from 9% (S25) to 25% (S26) — [yc-oss](https://yc-oss.github.io/api/batches/summer-2026.json). The F26 RFS opens with "AI is moving into the physical world" — [YC RFS](https://www.ycombinator.com/rfs).

### Inferences
- **Where real gaps may sit for a solo, capital-light founder:**
  1. Back-office workflows with measurable dollar outcomes that are still handled by people or BPO. This is where MIT finds ROI, but investor and YC attention concentrates on a few verticals (accounting, insurance, medical billing).
  2. Trust and verification problems created by AI itself: deepfake impersonation and agent identity. YC and a16z both call for this, and the YC directory shows few companies.
  3. "Plumbing" problems that AI coding has made newly salient: deploying and sharing small software, and API drift.
- **YC's pivot toward hardware and defense may lower competition** from YC-funded teams in some pure-software B2B niches. This is speculative.

### Gaps
- No customer-complaint datasets were gathered (G2 reviews, Reddit or HN threads) to test buyer satisfaction category by category.
- No primary adoption surveys of SMBs, as opposed to enterprises, were found. Most data (Menlo, MIT) is enterprise and US-only.

---

## Q8. Candidate startup opportunities emerging from the gaps and failures (5–8)

### Takeaway
Seven candidates are outlined below. None reaches "high" confidence on the evidence gathered here, because the search budget ran out before ground-level customer evidence could be collected for each. They are hypotheses for the stress-test phase.

The strongest evidence of a real, growing, dollar-denominated problem supports C1 (impersonation-proof payment-change verification) and C2 (elder-fraud protection via institutions), using FBI IC3 data. C3–C7 rest mainly on YC and a16z RFS text plus failure analogues.

### Cited Findings
**FBI IC3 2024 report** — [FBI IC3 2024 Annual Report](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf) (fetched and extracted):
- Total reported losses were $16.6B, up 33% from 2023, across 859,532 complaints.
- Business Email Compromise accounted for $2,770,151,146 (21,442 complaints). Prior years: $2.95B in 2023 and $2.74B in 2022.
- People over 60 filed 147,127 complaints (up 46%) with $4.885B in losses (up 43%). Their BEC losses alone were $385M.
- The IC3 PSA list includes "Criminals Use Generative Artificial Intelligence to Facilitate Financial Fraud" (Dec 3, 2024) and "Business Email Compromise: The $55 Billion Scam" (Sep 11, 2024).

**Trustpair** — [Trustpair](https://trustpair.com/) (fetched Oct 14, 2026):
- Vendor bank-account validation, continuous monitoring, and payment-file checks.
- Claims 600+ clients; covers enterprise and mid-market.
- Connectors for SAP, Oracle, Coupa, Ivalua and Kyriba; "up to $1M liability" coverage.
- Pricing is not public.
- The site announces "Basware Completes Acquisition of Trustpair" (acquisition date not verified).

**Carefull** — [Carefull](https://www.getcarefull.com/) (fetched Oct 14, 2026):
- Fraud and scam monitoring for older adults and families, with ScamCheck and Trusted Contacts.
- $29.99 per month for a two-person membership.
- Distributed as a benefit through Edward Jones, Synovus, MassMutual, Osaic and several credit unions.
- The B2B page cites "$64 Billion annually in elder fraud and money mistakes" (Carefull's own claim).

**Harbor Compliance** — [Harbor Compliance](https://www.harborcompliance.com/) (fetched Oct 14, 2026):
- Multi-state entity registration, licensing and tax registration, offered as managed service, SaaS (License Manager, Compliance Navigator AI), or a hybrid.
- Targets accounting, AEC (architecture, engineering, construction), law firms and nonprofits.
- Most pricing is quote-based; one listed price is a $99 per year Texas registered agent.

**YC F26 RFS text** for Proving You're Human, AI for the Aging Population, AI-Native Compliance Infrastructure, Self-Maintaining APIs, A Cloud for Small Software and Multiplayer AI is quoted in Q1 — [YC RFS](https://www.ycombinator.com/rfs).

**YC directory coverage near the candidates** — [yc-oss](https://yc-oss.github.io/api/companies/all.json):
- Deepfake and impersonation: DeepMark (F26), Crosslayer Labs (W26).
- Aging: Rhem Labs (F26), Cova (S26), Oma Care (W24).
- Internal tools and small software: Vybe (Spring 25, "Secure internal apps. Built by AI"), Olive (W25), Floracene (S26, HIPAA internal tools), Floot (S25, "app platform inside Claude and ChatGPT").
- API drift: none found; nearest is Quantstruct (W25).
- Licensing: none found.

### Inferences

All candidate content below is the author's interpretation unless a citation is attached. "Unverified" marks claims from general knowledge that were not checked in this session.

#### C1. Impersonation-proof vendor bank-change and payment-request verification for US SMB and mid-market AP
- **Problem and painful step:**
  - An AP clerk gets a "please update our bank details" or "urgent wire" request by email, phone, or now a cloned voice or video.
  - The control is a manual call-back to a number on file. It fails when the attacker controls the email thread or impersonates a known voice.
  - The YC F26 RFS cites a $25M deepfake-video wire — [YC RFS](https://www.ycombinator.com/rfs).
  - BEC losses were $2.77B in 2024 — [IC3](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf).
- **User:** AP specialist. **Budget-holder:** controller or CFO. Possible co-payers are cyber insurers and outsourced accounting firms.
- **Current workaround:** call-back procedures, dual approval in AP tools, and enterprise tools like Trustpair built around SAP, Oracle and Coupa — [Trustpair](https://trustpair.com/).
- **Hidden insight (hypothesis):**
  - The market frames this as a deepfake-detection problem, which is an arms race and technically hard.
  - For payments it is really a cryptographic-provenance and workflow problem: proving the request came from the known vendor via a channel the attacker does not control.
  - Enterprise-grade tools focus on ERP-scale customers. QuickBooks, Xero and Bill.com-scale firms may be underserved. This is unverified, and AP platforms may already embed checks.
- **Why now:** voice and video cloning is cheap (YC F26 RFS, Oct 2026); IC3's GenAI fraud PSA (Dec 3, 2024); 60+ BEC losses of $385M in 2024.
- **Product sketch, 2–8 week MVP:**
  - A vendor-facing verification link, with identity plus bank-ownership check via a third-party account-verification API (pricing unverified).
  - Every bank change is logged with an attestation.
  - An integration with QuickBooks Online or Xero that flags unverified changes before payment runs.
  - A "verified vendor" badge reusable across buyers.
- **Expansion path:** a network of pre-verified vendors (a network effect); payment-request verification for exec impersonation; data for cyber-insurance underwriting; a "KYA"-style verification for AI agents initiating payments (a16z "From KYC to KYA" — [a16z Pt3](https://a16z.com/newsletter/big-ideas-2026-part-3/)).
- **Competitors:**
  - Trustpair: enterprise and mid-market; 600+ clients; no public pricing; now part of Basware per its site — [Trustpair](https://trustpair.com/).
  - Eftsure: the site could not be fetched (redirect loop). From general knowledge it is Australia-origin and expanding to the US — unverified.
  - Others from general knowledge, all unverified: Nametag (helpdesk identity verification), Pindrop (call-center voice authentication), and AP suites such as Bill, Tipalti and Ramp with built-in vendor checks.
- **Why incumbents haven't captured it (hypothesis):** enterprise vendors sell ERP-integrated, high-ACV deals; SMB AP platforms treat it as a feature. No one may own the cross-company verified-vendor network for SMBs. This is unverified.
- **First 10 customers:**
  - US fractional-CFO and outsourced-accounting firms, each managing many SMB AP ledgers; one firm can bring 10+ clients.
  - Cyber-insurance brokers who want controls evidence.
  - An India-based founder can sell remotely via LinkedIn and CPA communities, but SOC 2 or similar trust credentials will be asked for early.
- **Disconfirming evidence:**
  - Category consolidation (Basware buying Trustpair) suggests the feature gets absorbed into AP suites.
  - Bank-side account-verification services could commoditize the check (not researched).
  - SMB willingness to pay is unknown.
  - BEC losses were flat across 2022–2024 ($2.74B, $2.95B, $2.77B), which does not show explosive growth in this specific loss line.
- **Confidence: Medium-low.** The problem's size is well evidenced. SMB-segment demand, willingness to pay and the competitive map are not.

#### C2. Elder-fraud and impersonation protection distributed through credit unions, community banks and advisors (B2B2C)
- **Problem:**
  - Older adults are targeted by impersonation scams (grandparent and voice-clone calls, tech support, investment).
  - Adult-child caregivers find out after the money is gone.
  - 60+ losses were $4.885B in 2024, up 43% — [IC3](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf).
  - YC cites 53M unpaid family caregivers — [YC RFS](https://www.ycombinator.com/rfs).
- **User:** an older adult plus an adult-child "trusted contact". **Budget-holder:** a credit union, community bank or wealth advisor, as a member benefit or retention tool. The family pays only as a fallback.
- **Current workaround:** bank fraud teams react after the fact; families monitor manually; Carefull charges $29.99 per month or is offered via partners such as Edward Jones and credit unions — [Carefull](https://www.getcarefull.com/).
- **Hidden insight (hypothesis):**
  - Investors pitch consumer AI for aging. Retention data says direct-to-consumer AI subscriptions churn badly: B2C NRR is 49%, and products under $50 per month have 23% GRR — [ChartMogul](https://chartmogul.com/reports/saas-retention-the-ai-churn-wave/).
  - The durable buyer is the institution that eats reimbursement, complaint and deposit-attrition costs.
  - The product wedge is real-time "pause and verify" before an out-of-pattern transfer, which links to YC's "Proving You're Human".
- **Why now:** voice cloning; the IC3 elder-fraud surge; YC F26 explicitly requests aging products and human-verification products.
- **Product sketch:** a family "verification circle" (a safe-word or callback protocol); a scam-check assistant via SMS or WhatsApp; and optional read-only transaction alerts via account aggregation, with a white-label portal for the institution.
- **Expansion path:** caregiver coordination (appointments, bills, documents); estate and "LegacyKit"-type records; insurer and Medicare Advantage distribution.
- **Competitors:**
  - Carefull: $29.99 per month; bank, credit-union and advisor distribution — [Carefull](https://www.getcarefull.com/).
  - EverSafe and Aura family plans: unverified.
  - YC Rhem Labs (F26, home-care tech for aging parents) and Cova (S26, caregiving finance) — [yc-oss](https://yc-oss.github.io/api/companies/all.json).
- **Why incumbents haven't captured it (hypothesis):** bank fraud tooling is enterprise-scale and transaction-focused rather than family-workflow-focused. Carefull shows the B2B2C channel works, which is both validation and competition.
- **First 10 customers:** small US credit unions, which often buy through CUSOs and leagues (channel unverified), and independent RIAs with older clients. Vendor-risk reviews will be heavy for an India-based solo founder.
- **Disconfirming evidence:** an established competitor already holds the exact channel; financial-institution sales cycles are long; consumer-protection and privacy compliance (GLBA etc.) is a burden (not researched).
- **Confidence: Low-medium.** The problem is strongly evidenced. Distribution fit for this founder is weak.

#### C3. "Dependabot for APIs": neutral agent that detects third-party API changes and opens fix PRs
- **Problem:** breaking changes and deprecations from Stripe, Twilio, Shopify and others go unnoticed until something breaks. The YC partner says over 30% of downtime he saw at AWS came from unnoticed external API or package changes (single-person anecdote) — [YC RFS](https://www.ycombinator.com/rfs).
- **User:** engineering lead at a 5–100 person SaaS company. **Budget-holder:** CTO. An alternative buyer is the API provider, who pays to push migrations.
- **Current workaround:** reading changelogs, Dependabot or Renovate version bumps (which do not handle semantic API behavior; general knowledge), and pinned API versions.
- **Hidden insight (hypothesis):** the provider side, not the customer side, may be the better buyer. API vendors lose revenue and goodwill when customers fail to migrate. "Install Stripe's update agent" is the YC framing.
- **Why now:** coding agents (Claude Code, Devin) have normalized giving third parties codebase access (YC RFS claim).
- **Product sketch:** a GitHub app plus a changelog-monitoring corpus; an LLM maps changes to code usages and opens draft PRs.
- **Competitors:** none found in YC; nearest is Quantstruct (W25, docs). Dependabot and Renovate (free; unverified detail) and SDK generators such as Stainless and Speakeasy (unverified) are adjacent.
- **Disconfirming evidence:** GitHub, Cursor or Claude Code could ship this as a feature; customer willingness to pay is unproven; it is technically demanding for a non-engineer founder.
- **Confidence: Low.** Demand evidence is a single anecdote from the RFS author. Founder-skill fit is poor.

#### C4. AI-native licensing and renewal operations for multi-state regulated SMBs (pick one vertical)
- **Problem:** businesses operating across states must track and renew licenses, registrations and filings that differ by jurisdiction. YC's RFS quotes "slow, fragmented, and expensive, often requiring dedicated legal teams" — [YC RFS](https://www.ycombinator.com/rfs).
- **User:** operations or compliance manager. **Budget-holder:** COO or CFO.
- **Current workaround:** spreadsheets, outside counsel, and managed services such as Harbor Compliance, whose pricing is mostly by quote — [Harbor Compliance](https://www.harborcompliance.com/).
- **Hidden insight (hypothesis):** most "compliance AI" money went to SOC 2/security frameworks (crowded, per Q4). Jurisdictional licensing is a different, less glamorous workflow. It is document-heavy and deadline-driven, and suits an AI-plus-human-ops service, which the India-based founder could run cost-effectively.
- **Product sketch:** a license inventory built from uploaded documents, a jurisdiction rules knowledge base, deadline tracking, auto-filled renewal forms, and a human filer for state portals.
- **Competitors:** Harbor Compliance (managed and SaaS; AEC, law, accounting, nonprofits) — [Harbor Compliance](https://www.harborcompliance.com/). AgentSync (insurance producer licensing) and CSC/CT Corporation are unverified. No YC companies were found — [yc-oss](https://yc-oss.github.io/api/companies/all.json).
- **First 10 customers:** depends on the vertical, which is unselected. Candidates include multi-state home-services or contractor firms, telehealth or staffing firms, and fintech money transmitters (the last is regulatory-heavy).
- **Disconfirming evidence:** there is no ground-level demand evidence beyond the RFS; the incumbent offers both software and managed service; regulatory error liability is a risk.
- **Confidence: Low** until a vertical is chosen and customer interviews are done.

#### C5. Outcome-priced "AI-native back office" replacing offshore BPO work in an un-crowded vertical (India-advantaged)
- **Evidence for the pattern:**
  - MIT: the largest GenAI ROI comes from cutting BPO and agency spend, while budgets skew to the front office — [Fortune/MIT](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/).
  - Menlo: 91% startup share in finance and ops AI — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/).
  - YC Spring 2026 and S26 ask for AI-native agencies and service firms — [TechStartups](https://techstartups.com/2026/02/04/y-combinator-is-out-with-its-2026-request-for-startups/), [VC Corner](https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas).
  - speedrun: "Fat AI startups will own the slowest markets" — [speedrun](https://speedrun.substack.com/p/14-big-ideas-for-2026).
- **Founder advantage (hypothesis):** a founder in India can staff human-in-the-loop quality control cheaply and understands BPO delivery.
- **Crowding warning:** YC already funds dense clusters in accounting firms, insurance brokerages and TPAs, and medical billing — [yc-oss](https://yc-oss.github.io/api/batches/summer-2026.json). Bench's collapse shows the risk of a capital-intensive, human-heavy services model financed with debt — [Wikipedia: Bench](https://en.wikipedia.org/wiki/Bench_Accounting).
- **Needed next:** identify a back-office workflow that is (a) currently outsourced to BPOs by US SMBs, (b) has a countable outcome, and (c) has fewer than about 3 YC or venture entrants. This could not be done here because the search budget ran out.
- **Confidence: Medium on the pattern, Low on any specific vertical.**

#### C6. "A cloud for small software": governed hosting and sharing for AI-built internal tools in non-technical SMB teams
- **Problem:** "Software like this is now very easy to build, but still hard to deploy and share… auth & permissions are hard" — [YC RFS](https://www.ycombinator.com/rfs).
- **Failure analogue:** Builder.ai (about $445M; "AI" app development actually done by human engineers) shows demand for custom software from non-technical businesses. The building step is now handled by coding agents — [TechStartups](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/).
- **Competitors:** YC companies Vybe (Spring 25), Olive (W25), Floracene (S26) and Floot (S25) — [yc-oss](https://yc-oss.github.io/api/companies/all.json). Replit, Lovable, Retool, Glide and Vercel are unverified, but Replit and Lovable reportedly run on thin margins — [Sacra](https://sacra.com/research/finance-ops-replit-ai-dev-platforms) (search snippet).
- **Disconfirming evidence:** many well-funded builders already host apps; platform risk from Anthropic and OpenAI app surfaces ("ChatGPT becomes the AI app store" — [a16z Pt2](https://a16z.com/newsletter/big-ideas-2026-part-2/)); security of sharing arbitrary code is hard.
- **Confidence: Low.** It is crowded and needs infrastructure depth.

#### C7. Vertical "multiplayer" agent workspace for a multi-party workflow
- **Thesis convergence:**
  - YC F26: "Multiplayer AI" — [YC RFS](https://www.ycombinator.com/rfs).
  - a16z: "Vertical AI evolves… to multiplayer", where the collaboration layer is the switching cost — [a16z Pt1](https://a16z.com/newsletter/big-ideas-2026-part-1/).
  - speedrun: "Multi-player AI will eat single-player AI" — [speedrun](https://speedrun.substack.com/p/14-big-ideas-for-2026).
- **Possible wedge (hypothesis):** a multi-party workflow where one side has adopted AI and the counterparties have not. Examples: commercial insurance placement (broker, carriers, insured), where YC's many AI-native brokerages could be users, or freight tendering.
- **Disconfirming evidence:** this is a consensus thesis among the most active investors (high competition); no ground evidence of buyer demand was gathered; model labs are adding shared and group features (not verified here).
- **Confidence: Low.**

**Cross-cutting suggestion for the stress-test phase:**
- C1 and C2 have the best "problem is real, growing, dollar-denominated" evidence and fit an MVP buildable in 2–8 weeks.
- C5 has the best investor-vs-ground divergence but needs a specific vertical.
- C3, C6 and C7 are investor-pulled more than customer-evidenced.

### Gaps
- **Not collected for any candidate:** customer complaints, review-site data, interviews, or SMB adoption surveys.
- **Competitor gaps:**
  - Competitor pricing was obtained only for Carefull ($29.99 per month) and partially for Harbor Compliance.
  - Trustpair, Eftsure, Nametag, Pindrop, EverSafe, Aura, AgentSync, Stainless, Speakeasy, Replit, Lovable and Retool pricing and weaknesses were not verified.
  - "At least 3 competitors with public pricing" is not met for any candidate.
- **Data gaps:**
  - The IC3 2025 annual report (likely published in spring 2026) was not retrieved, so 2025 BEC and elder-fraud trends are unknown.
  - Market sizes for C3–C7 were not found and should not be estimated without sources.
- **Next searches (the search budget is exhausted for this run; the user can continue in a follow-up):**
  - "Trustpair Basware acquisition date"
  - "Eftsure US pricing"
  - "Nacha 2026 fraud monitoring rule"
  - "Carefull funding"
  - "credit union elder fraud vendor"
  - "AgentSync funding pricing"
  - "API breaking change monitoring startup"
  - "Olive AI shutdown 2023"
  - "Convoy shutdown 2023"
  - "AI receptionist funding 2026"
  - "Harvey valuation 2026"
  - Sequoia, Index, Greylock, NFX and Lightspeed 2026 AI theses
