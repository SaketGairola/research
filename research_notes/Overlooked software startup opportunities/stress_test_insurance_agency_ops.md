# Stress test: loss-run request-and-chase for agencies, wholesalers and MGAs, with possible expansion to an AI-plus-offshore "agency back office" (as of Oct 14, 2026)

Scope note: this builds on Candidate 1 (loss-run agent) and Candidate 7 (agency service inbox) in `healthcare_insurance_finance.md`, and on the YC insurance cluster in `investor_theses_and_crowding.md`. It does not repeat these items from those files:
- Big I 37,000 agencies, 9.9 staff, AI use at 46%
- FurtherAI's "7–10 business days" and its $25M Series A
- Appulate's "20 minutes"
- West Bend/CogniSure
- the COI-tracking vendor pricing

New evidence here **contradicts two earlier claims**: that the request step is "under-served", and that it is addressed only by "$29/user/month tools". See the competitor and disconfirming sections.

Method and limits:
- I used all 25 WebSearch calls, plus direct fetches.
- These sources could not be accessed:
  - Coverager (403)
  - insurance-forums.com (403)
  - Reddit (blocked)
  - CNA's loss-run PDF (DNS failure)
  - COVU blog posts (404)
  - California leginfo (403; used public.law instead)
  - Justia (403)
  - the IIABL Louisiana advisory PDF (404)
  - itcvegas.com (DNS failure)
  - the Cogneesol loss-run page (404)
  - the Loss Run Pro podcast page (403)
- G2 and Capterra reviews and agency-owner podcasts were not read.
- "Vendor" marks company-published claims.

---

## 1. How are loss runs requested and delivered today? Portals/APIs vs. email/fax, turnaround, and state statutes

### Takeaway
Agents of record can get loss runs on demand from many carriers today, through carrier portals (Chubb, CNA, ICW, Hallmark) and Applied's Ivans eServicing inside the AMS. The remaining friction is the *prospect* case, where the insured is shopping. That needs a signed authorization from the insured, carrier-specific routing, and chasing.

At least six states set statutory deadlines: CA 10 business days, FL 15 calendar days, KY 20 calendar days, NY 20 days, OK 30 days, LA 30 days (LA unverified). Florida's legislative staff counted about 12 states with such statutes in 2020, not "most states".

### Cited Findings
**Channels and self-service**
- **Chubb:** authorized agents and brokers can pull 3- or 5-year loss runs for "all property, casualty and specialty lines, except risk management and surety business" through the @chubb portal. They can print them or save them to the AMS. — [InsuranceTech (undated, older article)](https://insurancetech.com/chubbandrsquos-online-business-loss-runs-streamline-process-for-agents-and-brokers/d/d-id/1310741d41d.html), via search summary.
- **CNA:** CNA Central lets agents pull loss experience for up to 5 years including the current year. Older periods must be requested by email. — [CNA PDF](https://www-new.cna.com/sites/default/files/assets/25582ffb-aff3-424a-9f7d-55d0b8663831/cna-central-small-business-how-to-access-loss-runs.pdf), via search summary only (direct fetch failed with DNS error).
- **ICW Group:** its agent portal advertises pulling "up to 5 years' worth of loss runs in a single step." — [ICW agent portal](https://icwgroup.com/agents/agent-portal), via search summary.
- **Hallmark (E&S/specialty carrier):** requests go through an online form only, with no email or fax option.
  - Loss runs are released only to "Agency/Broker of Record or Insureds."
  - Turnaround: "Automated processes immediately"; "Manual can take up to 5 days." — [Hallmark loss run request page, accessed Oct 2026](https://www.hallmarkgrp.com/loss-run-request/)
- **Ivans eServicing (Applied):** lets agents request "account status, billing, claims, policy, and loss run information" from carrier partners with one click inside their management system. The page says agents get "complete First Notice of Loss, Endorsements, and Loss Runs." Carrier count and agent pricing are not stated. — [Ivans eServicing page, © 2026](https://www.ivans.com/for-agents/products/ivans-eservicing/)
- **Ivans claims download** (claim notifications, not loss runs): a carrier-side sheet reports "74% of agents receive Claims download." The sheet is dated about 2022. — [Ivans claims download PDF](https://int11.ivans.com/globalassets/all-documents/resources/brochures-data-sheets/ivans/ivans-claims-download_carriers.pdf), via search summary.
- **Florida House staff analysis (Jan 17, 2020):**
  - "Some insurers, especially those providing commercial lines coverage or workers' compensation insurance, have existing loss runs systems that allow their insureds to log into a portal." Others create runs on request "or direct the insureds to obtain such statements from their agents of record."
  - Insureds "seeking new general commercial line policies often request these statements to shop for new insurance."
  - — [FL House analysis CS/CS/HB 269](https://www.flsenate.gov/Session/Bill/2020/269/Analyses/h0269c.COM.PDF)
- **Practitioner guidance (Matt Doman, Loss Run Solutions, a loss-run specialist service; IA Magazine, July 7, 2022):**
  - "Most carriers have specific submission requirements for loss run requests that, if not satisfied, will cause the request to be rejected."
  - Routing depends on policy number, line, state, TPAs, MGAs and M&A.
  - "E&S carriers, including Lloyd's of London, have different instructions."
  - Send a second request "five to 10 business days after the initial request."
  - He calls retrieval "a frustrating and often fruitless chore."
  - — [IA Magazine](https://www.iamagazine.com/?p=6555)
- **Sonant 2026 guide (vendor; updated Aug 14, 2026):** says carriers "typically want" a signed letter of authority before releasing loss runs to a new agent, and to confirm "the correct fax number, email address, or portal." It also claims "Some provide them within 48 hours through their agent portals." — [Sonant](https://www.sonant.ai/blog/loss-run-report)
- **Old practitioner anecdotes (Insurance Journal forum, 2006, dated):**
  - Erie said "up to 72 hours"; one agent reported "2 or 3 weeks"; another reported "two months."
  - Some carriers "will not honor a signed letter on letterhead from a client" and send the prospect back to the current agent.
  - One poster: a delayed request means "THE CLIENT IS SHOPPING!!!!"
  - — [IJ forum thread](https://www.insurancejournal.com/forums/viewtopic.php?p=4250)

**Turnaround data**
- No independent turnaround survey was found.
- FurtherAI's 7–10 business days is already in the prior notes.
- A vendor blog cites "8.3 business days average from request to receipt with manual outreach" and attributes it to an "ACORD 2024 Commercial Lines Process Study." I could not locate or verify that study. — [US Tech Automations, Jun 14, 2026 (vendor)](https://ustechautomations.com/resources/blog/reduce-chase-missing-lossrun-documents-before-quoting-with-automation-2026)
- A podcast host claimed "68% of their clients get loss runs within three business days" using Loss Run Pro. This is a company or host claim, seen via search summary only; the page returned 403. — [Power Producers Podcast episode page](https://no.player.fm/series/power-producers-podcast/the-real-pro-of-loss-runs-with-brenden-corr)

**What agents ask carriers for (Ivans 2026 Agency-Carrier Connectivity Trends; 702 independent agents surveyed April–May 2026)**
- 79% want commercial submission automation.
- 61% want real-time AMS data upload.
- **44% want "automated claims loss-run delivery"**, ranked third.
- 74% name re-keying risk data into multiple carrier portals as their top pain.
- 90% have cut business with a carrier because of submission friction.
- Commercial agencies rely on email (49%) far more than submission-capture software (7%).
- — [Insurance Edge, Aug 25, 2026](https://insurance-edge.net/2026/08/25/us-market-ivans-2026-report-looks-at-carrier-agency-connectivity/)

**State statutes (verified unless marked)**

| State | Citation | Deadline | Scope / who may request | Source |
|---|---|---|---|---|
| California | Ins. Code §679.7 | **10 business days** | Commercial policies subject to §675.5/676.6, excluding professional liability. Request by the insured, or the agent/broker of record "where authorized by the insured." Triggered by cancellation or nonrenewal, a request within 60 days before renewal, insurer downgrade, or conservation. Covers 3 years or the account's tenure. Exempt where the insured has "direct, ongoing access to claims information." | [public.law](https://california.public.law/codes/ca_ins_code_section_679.7) |
| Florida | Stat. §627.444 (effective Jan 1, 2021) | **15 calendar days** | All lines except life. 5 years. Insurer must notify the agent of record. First statement each year is free (per bill analysis). Portal access counts as "provide." | [FL Statutes](https://m.flsenate.gov/Statutes/627.444); [FL House analysis](https://www.flsenate.gov/Session/Bill/2020/269/Analyses/h0269c.COM.PDF) |
| Kentucky | KRS 304.20-100 (effective July 12, 2012) | **20 calendar days** | Commercial P&C. Request by the insured "or the insurer's agent." 5 years. No fee for one statement. "Provide" includes portal access. | [KY Legislature PDF](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=40249) (text extracted locally) |
| New York | Ins. Law §3426(g)(2) | **20 days** | "First-named insured or such insured's authorized agent or broker." Period = coverage period, limited by record-retention rules. | [NY DFS OGC Op. 05-08-12, Aug 16, 2005](https://www.dfs.ny.gov/insurance/ogco2005/rg050812.htm) |
| Oklahoma | 36 O.S. §1204.1 | **30 days** | Loss runs or claims history on written request. | Cited in [FL House analysis, fn. 11](https://www.flsenate.gov/Session/Bill/2020/269/Analyses/h0269c.COM.PDF) (statute itself not fetched) |
| Louisiana | R.S. 22:1214(20) | **30 days** (3 prior policy years); 20 days for more detail | First named insured; P&C | Search summary of an [IIABL technical advisory](https://www.iiabl.com/Information/Pages/Technical/TA%20220%20Loss%20Runs%20and%20Louisiana%20Law.pdf) (PDF returned 404, so **unverified**) |

- In Jan 2020, Florida staff wrote that "approximately 11 other states currently have statutory requirements for insurers providing loss run statements." — [FL House analysis](https://www.flsenate.gov/Session/Bill/2020/269/Analyses/h0269c.COM.PDF)
- That contradicts a vendor claim that "Most states require carriers to provide loss runs within 10 to 30 business days." — [Sonant (vendor)](https://www.sonant.ai/blog/loss-run-report)
- NY DFS issued a separate 2007 opinion on workers' comp loss runs, reportedly allowing a three-year limit. — [NY DFS OGC 07-12-01](https://www.dfs.ny.gov/insurance/ogco2007/rg071201.htm), via search summary.

### Inferences
- These statutes give the right to the **insured**, and to the agent of record or an authorized agent. A competing agent must therefore always route through the insured's signature. That is a coordination step, not a technology gap, and existing tools already handle it with e-sign.
- Several statutes count portal access as "providing" (FL, KY), and California exempts carriers that give ongoing online access. The law is pushing carriers toward self-service. That shrinks the chase problem for agents of record over time.
- Statutory deadlines of 10–30 days give carriers a legal floor, not a ceiling. A product that "chases faster" cannot force a carrier to act before its deadline. What it can do is escalate (DOI complaint) after the deadline passes.

### Gaps
- No list of the roughly 12 statutory states beyond the six above. Texas, Illinois and others were not verified.
- No independent, recent measurement of turnaround by carrier or channel.
- No count of carriers participating in Ivans eServicing loss runs, and no adoption rate.
- No confirmation of which major small-commercial carriers still require email or fax (e.g., Travelers, The Hartford, Liberty Mutual, AmTrust, Erie, NEXT). Their pages were not fetched.

---

## 2. How much staff time and money goes into loss-run chasing and carrier-portal chores?

### Takeaway
Loss-run ordering shows up in job postings as **one line item** in assistant and CSR roles, not as a dedicated job. The cheapest substitute is an offshore VA at about $3.50–$9/hour who does it alongside renewal data gathering and portal checks.

Time per request is around 20–25 minutes, but only vendors claim this. No independent survey quantifies agency hours on loss runs.

### Cited Findings
- **Offshore VA posting (onlinejobs.ph, updated Aug 18, 2026):** "Virtual Assistant – Commercial Insurance." Duties include "Order loss runs and assists with renewal data collection," "request documents from carriers," and "Check carrier portals and report underwriting updates." Uses AMS360. Full time on US hours, paying "$4.00 to $9.00" per hour (also stated as "$3.50 – $9.00/hour"). — [onlinejobs.ph job 1629038](https://www.onlinejobs.ph/jobseekers/job/1629038)
- **US broker postings** list loss runs among many duties (via search summary; pay not shown):
  - Marsh McLennan agency: "Request loss runs based on monthly reports… following up with carriers or wholesalers"
  - Epic Insurance Brokers: "Obtain loss history… Create loss run summaries"
  - USI senior insurance assistant: "Order various reports, loss runs, MVR's and follow-up for their receipt"
  - — [USI posting](https://jobs.usi.com/Jobs/JobDetail/WM-Sr-Insurance-Assistant/28248); [The Muse / Epic posting](https://www.themuse.com/jobs/epicinsurancebrokersandconsultants/commercial-insurance-assistant-0bfd31) (returned 404 on fetch); [MMC posting](https://jofdav.com/jobs/51797754-insurance-associate)
- **Offshore pricing (vendor blog, Jan 26, 2026):**
  - Offshore VAs cost $3–$12/hour for general admin and $6–$15/hour for specialized work.
  - Monthly: Philippines $800–$1,200 (Glassdoor), India $600–$1,100 (AmbitionBox).
  - Insurance tasks listed: endorsements, renewal tracking, claim data collection.
  - — [Global Squirrels](https://globalsquirrels.com/blog/hire-insurance-virtual-assistants-for-agencies-guide/)
- **COVU blog** (an agency-services vendor), via search summary only; the page returned 404 on fetch:
  - Offshore CSR at about $10–$15/hour, against a domestic unlicensed CSR at about $50,000–$55,000 all-in.
  - "Most major carriers limit portal access to appointed agency staff or licensed domestic personnel."
  - — [COVU blog](https://blog.covu.com/?p=2256) (unverified)
- **AMS cost:** Applied Epic is reported at about $150–$200+ per user per month, plus implementation from about $10,000 to $100,000+. — [QuoteSweep AMS comparison 2026 (vendor)](https://www.quotesweep.com/blog/ams-comparison-2026), via search summary.
- **Time per request:** Appulate claims "at least 20 minutes" saved per request (prior notes). A vendor estimates 25 minutes per request, and 360 person-hours a year for a 12-producer agency, labelled as its own illustration. — [US Tech Automations (vendor)](https://ustechautomations.com/resources/blog/reduce-chase-missing-lossrun-documents-before-quoting-with-automation-2026)
- **Volume signal:** Loss Run Pro claims "1M+ quarterly loss run requests" and "7K+ users." — [Loss Run Pro (vendor)](https://lossrunpro.com/)
- **Agency-wide pains:**
  - Big I 2026: hiring is the top challenge (45%) and "multiple carrier interfaces" the top tech challenge (prior notes).
  - Ivans 2026: 74% name re-keying into multiple carrier portals as the top pain. — [Insurance Edge](https://insurance-edge.net/2026/08/25/us-market-ivans-2026-report-looks-at-carrier-agency-connectivity/)

### Inferences
Illustrative arithmetic, using the sourced inputs above; these are not market data:
- **Per-request labor cost:**
  - At 20–25 minutes per request, an offshore VA at $3.50–$9/hour costs about **$1.20–$3.75 per request**.
  - A US CSR at about $24–$26/hour ($50–55K over 2,080 hours) costs about **$8–$11 per request**.
- **Loss Run Pro's effective price:** the $29/user/month Standard tier includes 150 agent-of-record requests a month. At full use that is **under $0.20 per request**.
- **Ceiling for a new entrant:** a per-request price above a few dollars is hard to defend unless it delivers outcomes the incumbents don't, such as hard-to-get E&S, defunct-carrier or TPA loss runs, or guaranteed delivery.
- **Size of the pain:** loss-run chasing looks like a low-value slice of a CSR's day, worth perhaps tens to low hundreds of dollars a month per agency. That is consistent with it being bundled into VA job descriptions. The bigger time sinks agents report are portal re-keying and submissions, which are exactly where the funded players are.

### Gaps
- Not obtained:
  - Indeed or LinkedIn counts of postings mentioning "loss run"
  - US pay for "commercial lines assistant" or "marketing assistant"
  - Reagan Consulting or Agency Performance Partners benchmarks (search returned nothing relevant)
- No published monthly pricing found for insurance-specialist offshore firms. ReSource Pro, Patra, Rely Services and Cogneesol do not publish prices.

---

## 3. Competitors: who automates the request step, and how well?

### Takeaway
The request-and-chase step is **already productized at scale and integrated**:
- **Loss Run Pro** claims 5,000+ carriers and MGAs, 7K+ users, 1M+ requests a quarter, and Epic/AMS360/HawkSoft integrations, at $29/user/month.
- **Appulate LossRunner** claims a 30,000-agency network.
- **Outmarket AI** ($56.5M raised; 300+ agencies) now automates ordering through Loss Run Pro's API on renewal rules (60/90/120 days) and extracts the results.

The back-office expansion faces well-funded AI and services players (Pace, COVU, Covera, Strada, ReSource Pro) and an Applied-controlled platform.

### Cited Findings

| Company | What it does (request step?) | Segment | Pricing | Funding / scale | Source |
|---|---|---|---|---|---|
| **Loss Run Pro** (Missoula, MT) | Request letter on client letterhead with e-sign; "automatically delivered to carriers after signature"; scheduling ("monthly, quarterly or several days before expiration"); tracking; "standardized format"; open API; secure upload; KPI dashboards. Integrations named: Applied Epic, AMS360, HawkSoft. **Yes, request + track.** | Brokers/agents, carriers/MGAs, insurtech platforms (API) | **$29/user/mo** Standard (1–10 users, 150 AOR requests/mo, 25 signature requests/mo); Enterprise undisclosed | Funding not found. Claims 5,000+ carriers & MGAs, 7K+ users, 1M+ quarterly requests, 35+ Top-100 agencies (vendor). Partnered with wholesaler/program manager One80 Intermediaries in May 2023. | [Home](https://lossrunpro.com/); [Product](https://lossrunpro.com/product); [Customers](https://lossrunpro.com/customers); [Insurance Business, May 22, 2023](https://www.insurancebusinessmag.com/us/news/technology/one80-partners-with-insurtech-for-loss-run-software-446671.aspx) |
| **Appulate LossRunner** | Manages carrier contact data ("No need to look this up"), templated letters, electronic signatures, audit trail. **Yes, request.** Follow-ups not described. | Retail agencies | Not public | Appulate: "network of over 30,000 agencies," since 2005 (vendor) | [Appulate LossRunner 101](https://blog.appulate.com/lossrunner-101) (shows Sept 10, 2026; metadata says 2024) |
| **Outmarket AI** | Loss-run extraction and analysis; discrepancy checks; branded Excel exports. **Automated ordering through Loss Run Pro API key with rules "60, 90, or 120 days before renewal"; documents "automatically synced… processed without manual intervention."** COI workflow launched. | Agencies/brokers (300+ agencies; >25% of Top 100, company-reported) | Not public | $34.5M Series B led by SignalFire (Sept 28 / Oct 1, 2026); $56.5M total; 10,000+ active users | [Outmarket blog (Jul 16, 2026 body date)](https://outmarket.ai/blog/outmarket-ai-launches-ai-powered-loss-run-extraction-and-analysis); [Insurance Journal, Oct 1, 2026](https://www.insurancejournal.com/news/west/2026/10/01/887081.htm) |
| **Ivans (Applied)** eServicing | On-demand loss runs, billing, claims and policy data inside the AMS from participating carriers. **Yes, for agent of record.** | Agencies on Ivans-connected AMSs | Not stated | Applied subsidiary | [Ivans eServicing](https://www.ivans.com/for-agents/products/ivans-eservicing/) |
| **Rely Services** (Schaumburg, IL) | Outsourced "Filing loss run requests with previous insurers," report preparation; "Send us the work at the end of your day… completed report… next morning." **Yes, human service.** | Agencies, carriers, brokers, TPAs | Not public; claims "40% or more" savings | "1000+ clients," "ISO27001" seal image (vendor) | [Rely Services](https://www.relyservices.com/loss-runs-processing-services) |
| **Cogneesol** | Loss-run processing; requests, reminders, follow-ups (per search summary; page returned 404). Offices in Mohali and Pune, India; SOC 2 and ISO 27001 badges. | Brokers/agencies | Not public | — | [Cogneesol](https://www.cogneesol.com/loss-runs-processing-services) |
| **FurtherAI** (YC W24) | Processes loss runs on arrival; "does not change the request step" (prior notes) | Carriers, MGAs, brokers | Not public | $25M Series A Oct 2025 (prior notes) | prior notes |
| **Pace** | Agentic operations layer: submission intake including "ACORD forms, and loss runs"; "COI, Policy Change and Endorsement Processing"; FNOL; policy checking | Carriers, MGAs, wholesalers, TPAs, "tech-forward brokers." Customers named: Prudential, Palomar, Convex US, WTW, Newfront | Not public | $10M Series A, Sequoia (Jan 27, 2026). A $46M Series B (May 2026, Thrive and Sequoia) appears only in a search summary and is **unverified**. | [Fortune, Jan 27, 2026](https://fortune.com/2026/01/27/exclusive-pace-raises-10-million-sequoia-enterprise-ai-collides-with-insurance); [withpace.com](https://www.withpace.com/) |
| **COVU** | "U.S.-licensed COVU agents" plus AI ("VERO"); tasks "costed task by task"; COIs, endorsements, renewals; 8 AMS integrations; browser extension. Loss runs not mentioned. | Independent agencies | Not public; company-reported "cost per task ~$4.80" | 50+ agencies, $200M+ premium managed (vendor) | [covu.com](https://www.covu.com/) |
| **Covera** (YC F26) | "AI-native OS for independent P&C agencies" inside the AMS and inbox: submissions, "one click keys every carrier portal," COIs and follow-ups drafted, renewal reminders at 90/60/30 days. Works with Epic, AMS360, QQCatalyst, HawkSoft, EZLynx, Momentum. | Independent agencies | Not public | YC F26, team of 2 | [YC directory via yc-oss](https://yc-oss.github.io/api/companies/all.json) |
| **Strada** (YC S23) | Phone AI agents for servicing, FNOL, quoting, renewals | Carriers, MGAs, brokers | Not public | Funding unclear: about $1–4M across databases, conflicting | [YC](https://www.ycombinator.com/companies/strada); [Caplight](https://www.caplight.com/company/getstrada) |
| **Comulate** | Agency accounting automation (direct bill, cash application) | Large brokers | Not public | $20M Series B (BOND, Workday Ventures), Feb 2025; "8-figure revenues" | [Insurtech Insights](https://www.insurtechinsights.com/comulate-raises-us20-million-in-series-b-funding-to-expand-insurance-accounting-automation/) |
| **Sixfold** | Carrier "AI Underwriter" | Carriers | — | $30M Series B, Jan 2026 (Brewer Lane, Guidewire strategic) | [Insurance Edge, Jan 29, 2026](https://insurance-edge.net/2026/01/29/deals-sixfold-raises-30m-in-series-b-round/) |
| **Kalepa** | Underwriting copilot | Carriers | — | $14M Series A, Sept 2021; $16M total (CB Insights) | [CB Insights](https://www.cbinsights.com/company/kalepa/financials), via search summary |
| **Pibit.ai** (YC W21) | Submission-to-decision underwriting ("CURE") | Carriers, MGAs | — | Team of 116; funding not verified | [yc-oss](https://yc-oss.github.io/api/companies/all.json) |
| **Cytora / Planck / Indio (Applied)** | Cytora: AI risk digitization; Planck: commercial data | Carriers / Applied platform | — | Applied bought Cytora on Sept 9, 2025 (Cytora had raised $41.4M) and Planck for about $300M in July 2024 | [Clickclaims, Sept 9, 2025](https://www.clickclaims.com/2025/09/09/applied-systems-acquires-cytora-to-expand-insurance-ai/); [Coverager](https://coverager.com/?p=227684) via search summary |
| **Zywave, Filepoint** | Document-collection apps: "Can auto-email the carrier"; tracking; no automatic AMS write-back | Agencies | $200–$600/mo (vendor comparison claim) | — | [US Tech Automations (vendor)](https://ustechautomations.com/resources/blog/reduce-chase-missing-lossrun-documents-before-quoting-with-automation-2026) |
| **Mulligan → Insure Stack** (YC W23) | Broker automation: quoting, policy checking, proposals; "acquired in 2026" | Commercial brokers | — | Acquired | [yc-oss](https://yc-oss.github.io/api/companies/all.json) |

- **No YC company description mentions "loss run"**, out of 6,297 companies scanned in yc-oss on Oct 14, 2026. The AI-native commercial brokerages (Harper W25, Fernstone and Casey F25, Panta W26, Acolite Spring 25, Kinro Spring 26) are potential *users*, not competitors. — [yc-oss](https://yc-oss.github.io/api/companies/all.json)
- A search for a startup whose agent sends loss-run requests to carriers *and chases the ones that don't respond* found none besides the Outmarket–Loss Run Pro ordering integration. — search result summary (Oct 14, 2026); [Outmarket](https://outmarket.ai/blog/outmarket-ai-launches-ai-powered-loss-run-extraction-and-analysis)

### Inferences
- The earlier "hidden insight", that funding flows to processing while the request step is neglected, **does not survive**:
  - Loss Run Pro sells request, track and standardize, with AMS integrations and an API.
  - Outmarket ($56.5M) uses that API to automate ordering on renewal triggers.
  - Ivans eServicing covers agent-of-record pulls.
  - Indian and US BPOs sell human request-and-chase.
- The one unclaimed niche is **escalation and chasing of stragglers**: the 10–20% of carriers (E&S/Lloyd's, TPAs, defunct or merged carriers) that don't respond to automated requests. That is a thin, service-heavy slice. Any player above could add it.
- The expansion into an "agency back office" is the most crowded part of insurance AI in 2025–26:
  - Pace and Outmarket together raised over $66M of verified funding.
  - COVU, Covera (YC F26), Strada, ReSource Pro, Patra, Exdion and Quandri are also active (see prior notes for policy checking).

### Gaps
- Not verified: pricing for Appulate, Outmarket, Pace and COVU; funding for Loss Run Pro, Federato, Pibit, Harper and Ascend.
- Not checked this session: Indio's role in loss-run collection, Patra, Reliance Global/5MinuteInsure, Bold Penguin pricing, Tarmika, Semsee, Agentero, Novella.
- No independent user reviews of Loss Run Pro or LossRunner. G2, Capterra and Reddit were not reachable.

---

## 4. Why haven't AMS vendors solved it, and what do agents complain about?

### Takeaway
AMS vendors partly have solved it, for agents of record (Ivans eServicing). They leave the prospect case to partners such as Loss Run Pro, Appulate and Outmarket. Applied, the dominant AMS and owner of Ivans, is actively restricting third-party access to Epic. That is a major platform risk for any startup that needs to write back into the AMS. Direct agent complaints about loss runs could not be gathered from 2025–26 sources.

### Cited Findings
- A vendor comparison says "Applied Epic Tasks" and "Vertafore AMS360 Diaries" provide "Reminder only, no outreach": "They create a human task, not a workflow." — [US Tech Automations, Jun 14, 2026 (vendor)](https://ustechautomations.com/resources/blog/reduce-chase-missing-lossrun-documents-before-quoting-with-automation-2026)
- Vertafore's September 2026 AI announcement for MGAs covers underwriting tools, including a "Change Request Agent" for renewal and endorsement applications. It does not mention loss runs. — [ColoradoBiz](https://coloradobiz.com/vertafore-ai-tools-insurance-underwriting-denver/), via search summary.
- **Applied v. Comulate (Applied's own account):**
  - Applied sued Comulate on Nov 21, 2025, alleging it "created a fake insurance agency to gain unauthorized access to Applied's systems."
  - Feb 11, 2026: the Illinois court granted Applied a preliminary injunction.
  - Mar 5, 2026: the court declined to require Epic integration for Comulate beyond **June 30, 2026**.
  - Apr 21 and May 14, 2026: Comulate's injunction motions were denied.
  - Sept 1, 2026: most of Comulate's motion to dismiss was denied.
  - — [Applied, "Applied v. Comulate"](https://www1.appliedsystems.com/en-us/news/applied-v-comulate)
- Insurance Business reported that the dispute began with "irregular activity detected within Applied's software development kit usage." Comulate called the suit an attempt "to undermine a competitor" and alleges Applied limits data access. — [Insurance Business, Nov 24, 2025](https://www.insurancebusinessmag.com/us/news/technology/applied-systems-sues-comulate-for-alleged-ip-theft-via-fake-agency-front-557615.aspx)
- Applied's ownership of agency-workflow assets:
  - Ivans (Ivans eServicing; the Ivans 2026 report quotes "Michael Streit, president, Applied Systems Carrier")
  - Indio (its news page is mirrored at insight.useindio.com)
  - Planck (2024)
  - Cytora (Sept 2025)
  - — [Insurance Edge](https://insurance-edge.net/2026/08/25/us-market-ivans-2026-report-looks-at-carrier-agency-connectivity/); [Clickclaims](https://www.clickclaims.com/2025/09/09/applied-systems-acquires-cytora-to-expand-insurance-ai/); [Indio mirror](https://insight.useindio.com/en-us/news/applied-v-comulate)
- Complaints found, all older or vendor-authored:
  - "frustrating and often fruitless chore"; requests rejected for format — [IA Magazine, Jul 7, 2022](https://www.iamagazine.com/?p=6555)
  - carriers refusing letters from prospects; 2–3 week delays — [IJ forum, 2006](https://www.insurancejournal.com/forums/viewtopic.php?p=4250)
  - "lost or misplaced" requests — Xceedance (prior notes)
- One80's contract binding leader (May 2023): "loss run reporting is a challenge that many of our clients face." — [Insurance Business](https://www.insurancebusinessmag.com/us/news/technology/one80-partners-with-insurtech-for-loss-run-software-446671.aspx)

### Inferences
- AMS vendors have little reason to build prospect-side loss-run chasing. The AMS has no relationship with the *prior* carrier, and partners already fill the gap.
- Applied has shown it will cut off integrations it does not authorize. A small entrant should assume **no reliable Epic write-back**: email or PDF delivery only, or a sanctioned partner route. That caps the product's stickiness.
- The fact that complaints are old and few is itself weak evidence that the pain is moderate, not acute. It could also simply reflect the access limits of this session.

### Gaps
- No 2025–26 agent quotes from Reddit (r/InsuranceAgent), insurance-forums, Facebook groups, G2 or Capterra. All were blocked.
- No HawkSoft, EZLynx or NowCerts loss-run feature checks.
- Applied's Epic SDK and partner-program terms were not read.

---

## 5. Buyer population and spend

### Takeaway
The population is large: about 37,000 independent agencies (prior notes), roughly 750 WSIA member firms (wholesalers, insurers, associates, service firms), and agency networks with thousands of members. But the spend attributable to loss runs is small, anchored by $29/user/month software and $3.50–$9/hour offshore labor.

AAMGA no longer exists as a separate body; it merged into WSIA in 2017.

### Cited Findings
- WSIA membership "consists of approximately 750 member firms," including "U.S. Wholesale, U.S. Insurance Market, Associate, and Service members," and "tens of thousands of individual brokers." — [WSIA About](https://www.wsia.org/about)
- **AAMGA merged with NAPSLO to form WSIA, effective Aug 1, 2017.** aamga.org now redirects to wsia.org. — [Insurance Business](https://www.insurancebusinessmag.com/us/news/breaking-news/industry-associations-agree-merger-to-become-wsia-74019.aspx); redirect observed Oct 14, 2026.
- Agency networks:
  - **SIAA:** "49 regional Master Agencies," "$18.1 Billion in total written premium" — [siaa.com](https://www.siaa.com/)
  - **Ironpeak** (formerly The Iroquois Group): "3,300+ Members," "$4+ billion" premium with carrier partners in 2025 — [ironpeak.com](https://ironpeak.com/)
  - **Smart Choice:** "over 12,000 independent agencies," "more than $12 billion" premium — [smartchoiceagents.com](https://www.smartchoiceagents.com/)
  - **Renaissance Alliance:** "four geographic regions and 23 states"; member counter not rendered — [renaissanceins.com](https://www.renaissanceins.com/)
- AMS spend: Epic at about $150–$200+ per user per month (see section 2).
- Agency marketing budgets averaged $20,600 in 2026, up from $14,300 in 2024. — [Insurance Journal, Sept 24, 2026](https://www.insurancejournal.com/news/national/2026/09/24/886639.htm)
- MGA premium is about $90B (AM Best 2024, via Vertafore), per prior notes.

### Inferences
- Illustrative arithmetic only. If a commercial-heavy agency sends, say, 20–60 prospect loss-run requests a month (an assumption, not data), the labor saved is worth about $25–$650 a month (offshore to US cost per request, from section 2). Loss Run Pro already sells this for $29 per seat.
- A standalone loss-run product therefore looks like a **sub-$100 to low-hundreds ARPA per month** business, competing against an entrenched $29 product.

### Gaps
- Not found:
  - Big I 2026 revenue-tier distribution and commercial vs. personal mix (the IJ article did not report them)
  - counts of US wholesalers and MGAs beyond WSIA's ~750 firms
  - TMPAA membership
  - agency spend on offshore staff as a share of revenue

---

## 6. Disconfirming evidence

### Takeaway
The disconfirming evidence is strong and mutually reinforcing:
- carriers and Ivans offer self-serve pulls to agents of record
- request-and-chase software already exists at scale
- funded AI platforms are bundling ordering and extraction
- labor substitutes are cheap
- the dominant AMS vendor is hostile to unsanctioned integrations

Agency consolidation is slowing but continuing. I found no direct evidence that PE platforms build in-house loss-run tools.

### Cited Findings
- **Carrier self-serve:**
  - Chubb, CNA, ICW and Hallmark self-serve, Hallmark "immediately" when automated (section 1).
  - FL and KY count portal access as delivery; CA exempts carriers that give insureds ongoing access (section 1).
- **Agent demand for carrier-side automation:** 44% of agents want "automated claims loss-run delivery" from carriers. — [Insurance Edge, Aug 25, 2026](https://insurance-edge.net/2026/08/25/us-market-ivans-2026-report-looks-at-carrier-agency-connectivity/)
- **Software bundling:**
  - Outmarket added Loss Run Pro-powered automated ordering and extraction, and raised $34.5M (Oct 2026).
  - Loss Run Pro integrates with Epic, AMS360 and HawkSoft.
  - Ivans eServicing serves loss runs inside the AMS.
  - (Section 3)
- **Cheap substitutes:** offshore VA job ads bundle "Order loss runs" with renewal work at $3.50–$9/hour. — [onlinejobs.ph](https://www.onlinejobs.ph/jobseekers/job/1629038)
- **Platform risk:** Applied cut Comulate's Epic integration as of June 30, 2026. — [Applied](https://www1.appliedsystems.com/en-us/news/applied-v-comulate)
- **Consolidation (OPTIS, via Insurance Journal, Jan 22, 2026):**
  - 695 agency deals in 2025, down 12% from 787 in 2024.
  - Q4 2025 had 157 deals, the lowest since 2019.
  - Hub had 49 deals and Inszone 45.
  - BroadStreet was the top buyer, but sources conflict on its count: 69 (down 23%) per a search summary of Risk & Insurance and Insurance Business, versus "29, down from 90" in my fetch of the IJ article.
  - Unique buyers fell to 95 from 104.
  - — [Insurance Journal](https://www.insurancejournal.com/news/national/2026/01/21/855124.htm); [Risk & Insurance](https://riskandinsurance.com/insurance-agent-and-broker-ma-deal-count-declines-in-2025/)
- **Offshoring constraint for portal chores:** "most major P&C carrier portals restrict access to agency-employed staff or… personnel holding a P&C license," with periodic access audits. This comes from a vendor blog via search summary and is unverified. CMS bars Marketplace agents and brokers from connecting from outside the US; that is health, not P&C, and comes from a forum repost. — [COVU blog](https://blog.covu.com/?p=2171) (404 on fetch); [insurance-forums](https://insurance-forums.com/community/threads/you-may-not-access-cms-systems-outside-of-the-u-s.110955)
- **Trust and security barriers:** 48% of agencies cite security and privacy as an AI barrier (Big I 2026, prior notes). Only 17% of agents trust AI (Liberty Mutual via IA Magazine, prior notes).

### Inferences
- "Too small a pain" is the most damaging finding. Loss runs rank third among what agents want carriers to automate. They appear as a line item in VA jobs. They are already sold at $29 per seat.
- "Carrier self-serve" and "AMS bundling" erode the agent-of-record case. "Outmarket + Loss Run Pro" erodes the prospect case.
- The India-based human-in-the-loop advantage is not unique. Rely Services, Cogneesol, ReSource Pro, Patra and countless VA agencies already sell it. If carrier portal terms really do restrict non-employee or offshore access, the "carrier-portal chores" expansion carries compliance risk too.

### Gaps
- No evidence either way on PE platforms (Hub, BroadStreet, Inszone, World) building in-house loss-run or back-office tools, or standardizing on Loss Run Pro or Outmarket.
- No carrier agency-agreement text on offshore portal access was read.

---

## 7. Twenty specific first-customer targets or channels (if the founder proceeds despite the verdict)

### Takeaway
Reachable channels exist: state associations in statute states, agency networks, WSIA events, YC AI-native brokerages, and agencies already hiring offshore VAs for loss runs. But several channels (One80, Outmarket's base) are already tied to Loss Run Pro.

### Cited Findings
Targets by type, with verifiable public facts:
1. **IIABCal (California)**: has a "Carrier & Vendor Member Directory" and an "Associate Member Marketplace"; CA has a 10-business-day statute. — [iiabcal.org](https://www.iiabcal.org/); [CA §679.7](https://california.public.law/codes/ca_ins_code_section_679.7)
2. **FAIA (Florida)**: has a "Preferred Providers" list (epayPolicy, Formstack Sign, AskFetch and others); FL has a 15-day statute. — [faia.com](https://www.faia.com/)
3. **Big I New York**: "Support NY" sponsorship (about 35 partners including Applied and HawkSoft); Catalyit free to members; GetLYIT tech sessions Oct 28–29. — [biginy.org](https://www.biginy.org/)
4. **Kentucky Big I affiliate**: KY has a 20-day statute. Association site not fetched (unverified).
5. **Oklahoma Big I affiliate**: 30-day statute. Not fetched (unverified).
6. **Louisiana (IIABL)**: published a loss-run technical advisory (PDF returned 404). — [iiabl.com](https://www.iiabl.com/Information/Pages/Technical/TA%20220%20Loss%20Runs%20and%20Louisiana%20Law.pdf)
7. **SIAA**: 49 master agencies, $18.1B premium. — [siaa.com](https://www.siaa.com/)
8. **Ironpeak** (formerly Iroquois): 3,300+ members. — [ironpeak.com](https://ironpeak.com/)
9. **Smart Choice**: 12,000+ agencies. — [smartchoiceagents.com](https://www.smartchoiceagents.com/)
10. **Renaissance Alliance**: 23 states. — [renaissanceins.com](https://www.renaissanceins.com/)
11. **WSIA Extreme Risk Takers Symposium**, Atlanta, Nov 5–6, 2026. — [wsia.org](http://www.wsia.org/)
12. **WSIA U40 Connect**, Washington DC, Nov 8–10, 2026. — [wsia.org](http://www.wsia.org/)
13. **WSIA 2027 Underwriting Summit** (Mar 21–24, 2027); the 2026 Annual Marketplace ran Oct 11–14, 2026 (San Diego). — [wsia.org](http://www.wsia.org/)
14. **InsurTech Insights USA**, New York, June 9–10, 2027 (7,000+ attendees). — [insurtechinsights.com](https://www.insurtechinsights.com/)
15. **Harper** (YC W25, AI-native commercial brokerage, team of 25), a potential API buyer. — [yc-oss](https://yc-oss.github.io/api/companies/all.json)
16. **Fernstone** (YC F25; "500+ businesses in construction, security, and the trades"). — [yc-oss](https://yc-oss.github.io/api/companies/all.json)
17. **Casey** (F25), **Panta** (W26), **Acolite** (Spring 25, construction), **Kinro** (Spring 26): AI-native brokerages that need prior loss runs on every new account. — [yc-oss](https://yc-oss.github.io/api/companies/all.json)
18. **US agencies posting offshore VA roles that include "Order loss runs"**, e.g., onlinejobs.ph job 1629038 (AMS360 shop). — [onlinejobs.ph](https://www.onlinejobs.ph/jobseekers/job/1629038)
19. **Wholesalers and program managers that distribute tools to retail agents**, the One80 model. One80 already partners with Loss Run Pro, so it is a *competitor channel*. — [Insurance Business, May 2023](https://www.insurancebusinessmag.com/us/news/technology/one80-partners-with-insurtech-for-loss-run-software-446671.aspx)
20. **Online communities**: r/InsuranceAgent, insurance agency owner Facebook groups, insurance-forums.com. These exist, but **access was blocked this session**, so member counts and activity are unverified.

### Inferences
- The best-fit early adopters are the AI-native brokerages (items 15–17). They are tech-forward, onboard many *new* accounts (the prospect case), and buy via API. They may also build in-house or simply use Loss Run Pro's API.
- Statute-state associations (items 1–6) give a credible "know your rights / escalate" message. But associations take sponsorships, not quick pilots.

### Gaps
- Member counts for most state associations, and WSIA directory access terms, were not verified.
- Reagan Consulting, Agency Performance Partners and Catalyit content was not accessed.

---

## 8. Narrowest MVP (2–8 weeks, solo non-engineer with AI coding tools), data-security expectations, and a 14-day experiment with kill criteria

### Takeaway
A narrow, defensible MVP would avoid competing with Loss Run Pro on routine requests. Instead it would be a **"stuck loss-run desk"**: a service that takes only requests outstanding for more than 7–10 days, or for hard carriers (E&S/Lloyd's, TPAs, merged or defunct carriers). It would work them by email, fax and phone with India-based staff, escalate against statutory deadlines, and return a normalized summary.

It is buildable in 2–4 weeks without AMS integration. But the evidence above suggests demand is thin, so the 14-day test should be designed to kill it quickly.

### Cited Findings (inputs to the design)
- **Request mechanics:**
  - The insured's signed authorization is typically needed for a new agent — [Sonant](https://www.sonant.ai/blog/loss-run-report)
  - Carrier-specific requirements cause rejections, and E&S/Lloyd's differ — [IA Magazine, 2022](https://www.iamagazine.com/?p=6555)
  - Hallmark-style web forms accept requests only from the agent/broker of record or the insured — [Hallmark](https://www.hallmarkgrp.com/loss-run-request/)
- **Escalation hooks:** CA 10 business days; FL 15 calendar days; KY and NY 20 days; OK 30 days (section 1).
- **Security expectations:**
  - **NAIC Insurance Data Security Model Law #668:** licensees must contractually require third-party service providers to maintain safeguards and notify breaches.
  - 18 states had adopted it as of 2021, per Faegre Drinker. A third-party site says "24+," undated.
  - NAIC's adoption map is current as of Oct 8, 2026, but its state tally could not be extracted.
  - — [Faegre Drinker, Aug 2021](https://www.faegredrinker.com/en/insights/publications/2021/8/naic-insurance-data-security-model-law-mdl668-update); [NAIC map](https://content.naic.org/sites/default/files/legal-adoption-map-668-idsm.pdf); [Securiti](https://securiti.ai/naic-model-668-overview), via search summary
- **Agent concern:** 48% of agencies cite security and privacy as an AI barrier (Big I 2026, prior notes).
- **Kentucky's statute** bars an agent receiving a loss run from divulging consumer information except under privacy laws. — [KRS 304.20-100](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=40249)

### Inferences (design proposals; not evidence)
**MVP scope (2–4 weeks)**
1. Intake form and email forwarding address: account, prior carriers and policy numbers, signed LOA upload, or e-sign through a hosted e-signature service.
2. Carrier routing sheet for the 50 carriers the first pilots name, with channel, address and requirements. Built by hand by the India team.
3. Outbound email from a dedicated domain, plus an e-fax API and phone calls by staff.
4. Follow-up cadence tied to the insured's state deadline, with a templated DOI-complaint escalation letter for the insured to send.
5. LLM extraction of the returned PDF into a 5-year summary (claims, paid, reserved, open/closed) with human QA. Delivered as PDF and Excel by email.
6. No AMS write-back. This avoids Applied SDK and contract risk.

**Security baseline to pass agency vendor questionnaires**
- MFA and SSO on all tools; encryption at rest and in transit; US-region storage.
- Least-privilege access for India staff, with signed NDAs and background checks.
- No model training on customer data (choose an LLM API with zero data retention).
- Audit log per request; 90-day auto-deletion of documents.
- A written information security program and incident-response plan mapped to Model #668 third-party provisions.
- A data processing agreement.
- SOC 2 Type I is a 6–12-month goal, not an MVP item.

**14-day experiment**
- Days 1–2: one-page offer, "We get your stuck loss runs; pay only per delivered run."
- Days 1–2: list 150 commercial-heavy agencies in CA, FL, NY and KY, the 8 YC AI-native brokerages, and 20 small wholesalers.
- Days 3–10: outreach (LinkedIn, email, association sponsor contacts). Take real requests.
- Days 10–14: measure delivery and willingness to pay.

**Kill criteria (any one kills it)**
- Fewer than 10 of 170 targets reply, or fewer than 5 discovery calls.
- More than 60% of interviewed agencies already use Loss Run Pro, LossRunner, Outmarket, Ivans or portals and describe no residual "stuck" volume.
- Fewer than 3 pilots send at least 20 real stuck requests in total by day 14.
- Median days-to-delivery on stuck requests is no better than the carrier's statutory deadline.
- Fewer than 2 pilots commit to at least $300/month or at least $15 per delivered run. That threshold is the minimum needed to beat offshore VA economics with margin.

**Advance signal**
- At least 3 paying commitments at or above those thresholds.
- Evidence that stuck runs block binding, i.e., lost premium, not just CSR minutes.

### Gaps
- E-fax and e-sign API pricing were not verified.
- Whether carriers accept requests sent by a third-party service (not the agency or the insured) was not verified. That needs testing in the experiment.
- Whether a non-licensed vendor may *call* carriers about a prospect's policy was not legally reviewed.

---

## 9. Verdict: should this advance to a top-five shortlist?

### Takeaway
**REJECT.** That applies both to the standalone loss-run request-and-chase product and to the AI-plus-offshore agency back office. The supposed gap, an under-served request step, is contradicted by evidence:
- Loss Run Pro sells request, chase and standardize at $29 per seat, with AMS integrations and claimed scale of 1M+ requests a quarter.
- Outmarket ($56.5M raised) now automates ordering and extraction on top of it.
- Ivans eServicing and carrier portals self-serve the agent-of-record case.
- Offshore VAs at $3.50–$9/hour already do the residual work.

The expansion path runs into Pace, COVU, Covera, Strada and established BPOs. Applied, the dominant AMS, has just cut off an unsanctioned integrator.

### Cited Findings (summary of decisive evidence)
- Loss Run Pro: $29/user/month; 5,000+ carriers and MGAs; 7K+ users; 1M+ quarterly requests; Epic, AMS360 and HawkSoft integrations (vendor). — [lossrunpro.com](https://lossrunpro.com/)
- Outmarket–Loss Run Pro automated ordering at 60/90/120 days before renewal, plus extraction; $34.5M Series B (Oct 2026). — [Outmarket](https://outmarket.ai/blog/outmarket-ai-launches-ai-powered-loss-run-extraction-and-analysis); [Insurance Journal](https://www.insurancejournal.com/news/west/2026/10/01/887081.htm)
- Ivans eServicing serves loss runs on demand; 44% of agents want carriers to automate loss-run delivery. — [Ivans](https://www.ivans.com/for-agents/products/ivans-eservicing/); [Insurance Edge](https://insurance-edge.net/2026/08/25/us-market-ivans-2026-report-looks-at-carrier-agency-connectivity/)
- Offshore VA roles bundle loss runs at $3.50–$9/hour. — [onlinejobs.ph](https://www.onlinejobs.ph/jobseekers/job/1629038)
- Applied cut off Comulate's Epic integration on June 30, 2026. — [Applied](https://www1.appliedsystems.com/en-us/news/applied-v-comulate)
- Back-office competition: Pace ($10M Series A, Sequoia, Jan 2026), COVU, and Covera (YC F26). — [Fortune](https://fortune.com/2026/01/27/exclusive-pace-raises-10-million-sequoia-enterprise-ai-collides-with-insurance); [covu.com](https://www.covu.com/); [yc-oss](https://yc-oss.github.io/api/companies/all.json)

### Inferences
Reasons, in order of weight:
1. **No unmet gap.** The request step is productized, integrated and cheap.
2. **Low pain ceiling.** Loss runs are a line item for $4–$9/hour VAs and rank third among agents' carrier wishes.
3. **Incumbent and platform risk.** Applied owns Ivans and controls Epic access. Outmarket and Loss Run Pro are already partnered.
4. **Crowded expansion.** The agency back office is a consensus 2026 thesis with $10M–$56M-funded players.
5. **No founder edge beyond India-based ops**, which BPOs and VA firms already provide.

What would overturn this verdict:
- The 14-day test shows a large residual of "stuck" loss runs that block binding, with willingness to pay at or above $15 per delivered run.
- Or AI-native brokerages want a guaranteed-delivery API and won't use Loss Run Pro.

Neither is evidenced today. Treat it, at most, as a low-cost side experiment, not a shortlist candidate.

### Gaps
- No independent measure of residual "stuck" volume after current tools are used.
- No agent interviews or reviews were accessible.
- Loss Run Pro's real performance and churn are unknown, so there could be a quality gap that this research could not detect.
