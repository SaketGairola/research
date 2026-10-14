# Stress test: a verification and triage layer for receivers of AI-assisted applications (staffing and recruiting first, grant-makers second), as of Oct 14, 2026

Research notes for the report writer. This file covers only the gaps left by `ai_agents_second_order.md` (Candidate 1 "Clean Intake" and Candidate 4 "funder intake triage") and `professional_services_smb.md` (Section 3). It does not repeat the Greenhouse North America benchmark (applications per recruiter +411.8%), the Greenhouse UK/IE/DE AI in Hiring Report (42% of candidates self-report using prompt injection; 86% of recruiters caught or suspected fraud), the Fortune "AI doom loop" coverage, or the RoRI/NIH funder data. All of those are cited in the earlier files.

**Method and limits**
- I used all 25 allowed WebSearch calls. After that I fetched known URLs only.
- These pages could not be read:
  - Gartner's press release (HTTP 403). I used HR Dive's coverage instead.
  - DOJ justice.gov press releases (HTTP 401). Details come from search summaries and secondary coverage, and are flagged where they appear.
  - Staffing Industry Analysts (SIA) news pages and the Ropes/CWS webinar PDF (HTTP 403). Figures from them come from search snippets or from vendors citing SIA, and are flagged.
  - Persona's pricing page (HTTP 403).
  - The CEP AI report (HTTP 404).
- `truely.ai` is a parked domain, so I could not identify "Truely".
- I did not check "Herd", Tezi, Juicebox, Ribbon, Lever, Workday, Socure's or Incode's own hiring products, LinkedIn's fraud data, Reddit, or G2.
- Many statistics below come from vendors that sell fraud detection. Each is labelled.

---

## Q1. How large are candidate fraud and AI-assisted application volume in 2025–2026, and which segments suffer most?

### Takeaway
Candidate fraud is real and measurable, but how large it looks depends heavily on who is counting.
- **Neutral or official sources:** Gartner found 6% of 3,000 candidates admitting interview fraud. The FBI and DOJ say "thousands" of North Korean IT workers are active, and announced new arrests on Oct 13, 2026.
- **Vendor-reported flag rates** are far higher: 11.7% (Crosschq), 23.2% (Huntress using Endorsed), 36% (Checkr resume beta), 39% (Ropes), and 44–47% of *remote IT* applications (Endorsed).

The most-affected segment is **remote software and IT roles, including IT staffing**. Healthcare staffing faces a different, credential-impersonation fraud that is often run by the agencies themselves. The "1 in 4 candidates fake by 2028" figure is a Gartner *forecast*, not a measurement.

### Cited Findings
**Gartner (neutral analyst; survey plus forecast)**
- Gartner (report dated Jul 31, 2025) projects that by 2028 about one in four candidate profiles worldwide could be fake. In a survey of 3,000 job candidates, **6% admitted interview fraud** (impersonating someone, or having someone impersonate them). 39% used AI during applications. Only about a quarter trust AI to evaluate them fairly. 62% are more likely to apply for roles requiring in-person interviews. Analyst Jamie Kohn: "Candidate fraud creates cybersecurity risks that can be far more serious than making a bad hire." — [HR Dive, Aug 8, 2025](https://www.hrdive.com/news/fake-job-candidates-ai/757126/) (Gartner's own release, [gartner.com Jul 31, 2025](https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them), returned 403)

**FBI and DOJ (official)**
- **FBI/IC3 PSA I-101326-PSA (Oct 13, 2026), "North Korean IT Workers Expanding Use of Facilitators, Broadening Recruitment":**
  - North Korean IT workers (ITWs) number in the "thousands", organized in dozens of teams, and North Korea takes an estimated 85–90% of their revenue.
  - They increasingly use US facilitators and laptop farms, now "more farms with fewer laptops" each.
  - They rent aged LinkedIn-type accounts and use stolen identities "often verified through purchased accounts or licenses from identity verification providers".
  - They subcontract work to freelancers in Pakistan, India and Nigeria, and have threatened and extorted former employers.
  - The FBI recommends "identity in depth" across the whole employment lifecycle, and warns **against relying on ban lists or name filtering**, which "can exclude qualified applicants and harm identity theft victims".
  - [IC3 PSA, Oct 13, 2026](https://www.ic3.gov/PSA/2026/PSA261013)
- **DOJ, Oct 13, 2026:** a coordinated announcement of an indictment (grand jury, N.D. Ohio, Oct 1, 2026; 14 indicted; schemes affecting more than 70 US companies), two arrests, searches of laptop farms in Texas ("Operation Lonestar Roundup"), and about 187 devices seized. DOJ lists earlier actions under the same initiative in June 2025, November 2025, April 2026 and May 2026. — [DOJ OPA](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-actions-combat-north-korean-remote-it-worker); [USAO N.D. Ohio](https://www.justice.gov/usao-ndoh/pr/14-indicted-north-korean-remote-it-worker-conspiracy-affecting-more-70-us-companies); [USAO N.D. Texas](https://justice.gov/usao-ndtx/pr/operation-lonestar-roundup-dismantles-north-korean-it-worker-network-used-penetrate-us) (justice.gov returned 401 to my fetcher; details are from search-result summaries)
- **Sentencings, April–May 2026:**
  - April 2026: Kejia Wang and Zhenxing Wang were sentenced to 108 and 92 months. They used the identities of more than 80 Americans to place workers at more than 100 US companies, generating about $5M for North Korea.
  - May 2026: Matthew Knoot and Erick Prince each got 18 months for hosting laptops, in schemes touching about 70 companies and generating $1.2M combined. That brought the total to eight facilitator sentences in five months.
  - [DOJ OPA (Wang)](https://www.justice.gov/opa/pr/two-us-nationals-sentenced-facilitating-fraudulent-remote-information-technology-worker); [Cointelegraph, May 2026](https://cointelegraph.com/news/us-sentences-eight-in-five-months-laptop-farmers-north-korea) (secondary)
- **Staffing firms as conduits:** In January 2025 DOJ charged Erick Ntekereze Prince, owner of the staffing firm Taggcar, and others. The defendants and co-conspirators "obtained work from at least sixty-four U.S. companies" between 2018 and 2024. Taggcar "invoiced a U.S. staffing company eight times" for about $75,709 of work done by a North Korean posing as a US person. Payments from 10 of the companies totalled at least $866,255. — [The Hacker News, Jan 24, 2025](https://thehackernews.com/2025/01/doj-indicts-5-individuals-for-866k.html); [SIA, "FBI arrests staffing firm owners"](https://www.staffingindustry.com/news/global-daily-news/fbi-arrests-staffing-firm-owners-in-north-korean-it-worker-scheme) (SIA page 403; headline only)
- A separate indictment of 14 North Koreans alleges they earned at least $88M (2017–2023) through the Yanbian Silverstar and Volasys Silverstar fronts. — [The Record](https://therecord.media/doj-indicts-14-north-koreans-earning-88-million-at-us-firms)
- The US Treasury says fraudulent workers, mostly in tech, raised nearly $800M for North Korea in 2024. — [Biometric Update, Oct 9, 2026](https://biometricupdate.com/202610/checkr-layers-biometrics-data-analysis-and-fraud-signals-to-catch-fake-candidates) (secondary citation of Treasury)

**Vendor-measured flag rates. All come from companies selling detection; their definitions of "flagged" differ and are not comparable.**
- **Endorsed** (175,000 applications from 2026 across US companies): the share of applications for **US-based remote IT roles** flagged as mid- to high-risk for North Korean IT-worker patterns rose from **11% (Q3 2024) to 44% a year later, and an estimated 47% in the latest quarter**.
  - Common traits of flagged profiles: claimed origins in Texas (26.5%), California and Florida; claimed degrees from the University of North Texas, UT Austin, University of Central Missouri and UT Dallas; first names such as "Sai" and "Michael".
  - The CEO warns that any one trait "should never make an applicant seem suspicious on their own".
  - [Fortune, Sep 1, 2026](https://www.fortune.com/2026/09/01/north-korean-it-worker-remote-job-applications/)
- **Checkr** resume-fraud beta: 36% of applicants triggered review flags, and **half of applicants for technical roles** (software and AI engineers) did. — [Biometric Update, Oct 9, 2026](https://biometricupdate.com/202610/checkr-layers-biometrics-data-analysis-and-fraud-signals-to-catch-fake-candidates)
- **Checkr 2025 Hiring Hoax survey** (3,000 US hiring managers; methodology section empty):
  - 60% caught a candidate misrepresenting experience.
  - **35% say someone other than the applicant took part in a virtual interview.**
  - 31% interviewed someone later found to be using a fake identity.
  - Only 19% are "extremely confident" they would catch a fraudulent applicant.
  - [Checkr, Sep 16, 2025](https://checkr.com/resources/articles/hiring-hoax-manager-survey-2025)
- **Crosschq:** detected fraud in 11.7% of candidates in 2025, up 32% year over year. "Some organizations face fraud rates above 40%". Government, healthcare, financial services and big tech lead. — [Crosschq press release, Nov 18, 2025](https://www.crosschq.com/press/ai-fraud-detection-platform-applicantx)
- **Huntress** (a security company hiring for itself, using Endorsed): **23.2% of applicants** flagged as a fraud risk, Sep–Nov 2025. — [Huntress blog, Feb 20, 2026](https://www.huntress.com/blog/ai-enhanced-candidate-fraud)
- **Ropes** (staffing-focused vendor): "39% of candidates assessed this year showed at least one fraud signal" (2026 Ropes Candidate Fraud Report; no sample size). Its customer results:
  - Swoon flagged 70 of its first 200+ candidates.
  - Mitchell Martin caught 95 fraudulent candidates in three months.
  - At ECLARO, about 20% of candidates who finished an assessment were flagged.
  - [Ropes blog, Aug 20, 2026](https://www.ropes.ai/blog/identity-verification)
- A search snippet of an SIA-hosted Ropes/CWS buyer webinar deck (Sep 10, 2026; PDF returned 403 when fetched) shows:
  - 39.1% of Ropes-screened candidates rated high-risk.
  - Methods: generative-AI assistance 48.5%, remote desktop or proxies 31.3%, identity or document fraud 12.8%.
  - **57% of contingent-workforce buyers rely mainly on their staffing suppliers' screening; 43% use ID-verification technology.**
  - [SIA-hosted PDF](https://www.staffingindustry.com/system/files/2026-09/ropes_americas_buyer_webinar_091026.pdf) (snippet only; not verified)
- **HYPR** (identity vendor), *State of HR Identity Fraud Detection*: 98% of HR leaders have experienced candidate fraud firsthand, and 96% believe they would detect it. No sample size given. — [Help Net Security, Sep 18, 2026](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- **SIA-attributed figures, via other sites only:**
  - "Four in 10" (41%) staffing buyers face candidate-fraud challenges — [StaffingHub, May 12, 2026](https://staffinghub.com/hiring/candidate-verification-ai-resume-fraud-staffing-firms-2026/), citing [SIA](https://www.staffingindustry.com/news/global-daily-news/this-year-may-see-more-candidate-fraud) (403).
  - Identity-related fraud in contingent programs rose from 37% to 54% of companies in one year — [Ropes blog](https://www.ropes.ai/blog/identity-verification) (no date or sample given).

**AI-assisted application volume (new data beyond the earlier Greenhouse figures)**
- Bullhorn says "job seekers and bots are now generating as many as 11,000 applications per minute". No source is given. — [Bullhorn press release, May 28, 2026](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/)
- "Nine in 10 HR workers" reported a surge in low-effort AI-generated applications in 2025 (Resume-Now). — [StaffingHub, May 12, 2026](https://staffinghub.com/hiring/candidate-verification-ai-resume-fraud-staffing-firms-2026/) (secondary; not verified)
- Ashby customer Confluent says about 20% of candidates later archived as fraudulent had already spoken with someone at Confluent before detection was switched on. That share was cut roughly in half after. — [Ashby customer story](https://www.ashbyhq.com/customers/confluent) (search snippet)

**Segments**
- Share of documented hiring-fraud cases: finance 35.45%, IT 30.43%, healthcare 15.41% (Yardstik 2025, via a BridgeView IT blog). — [BrightHire statistics roundup, Sep 25, 2026](https://brighthire.com/blog/candidate-fraud-statistics-2026/) (third-hand; sample not stated)
- **Healthcare staffing.** Fraud here usually involves agency owners placing impostors, not candidates deceiving agencies:
  - Washington, June 2026: a jury convicted a Kent staffing-firm owner on all 11 counts for placing "impostor nurses" using real nurses' stolen credentials. It was the state's first Medicaid-fraud trial on a "leading organized crime" charge. — [SIA](https://www.staffingindustry.com/news/global-daily-news/washington-jury-convicts-staffing-firm-owner-in-nurse-impersonation-scheme) (403; snippet); [KIRO7](https://www.kiro7.com/news/local/kent-man-convicted-using-stolen-nurse-identities-place-impostor-nurses-nursing-homes/E4FZMWOD3JFBPIXJLLQGOC7S4U/)
  - Massachusetts: Blooming Staffing indicted for sending uncertified CNAs to nursing homes and billing more than $300K. — [HealthExec](https://healthexec.com/topics/healthcare-management/legal-news/massachusetts-staffing-agency-owner-indicted-sending-fake-cnas-nursing-homes)
  - Connecticut: NurseSpan placed an untrained person in 18 facilities. — [nurse.org](https://nurse.org/news/fake-nurse-employer-felony-charges)
  - Maryland: an impostor worked at at least 21 facilities. — [DOJ D. Md.](https://www.justice.gov/usao-md/pr/baltimore-county-woman-admits-impersonating-nurses-pleads-guilty-aggravated-identity)
  - 2023: a federal diploma-mill bust involved more than 7,600 fake nursing diplomas. — [ABC7](https://abc7news.com/fake-nursing-degree-diploma-scheme-degrees-sold/12738739/)
- **Offshore and nearshore:** the FBI says ITWs subcontract work to freelancers in Pakistan, India, Nigeria and neighbouring countries. — [IC3 PSA, Oct 13, 2026](https://www.ic3.gov/PSA/2026/PSA261013)

### Inferences
- The fraud is concentrated in **remote, high-salary technical roles**. That is where the largest IT staffing firms and in-house tech recruiting teams operate, and where well-funded vendors are already selling (Q3).
- Healthcare staffing fraud is mostly supply-side: sham agencies and license misuse. The natural buyer there is the *facility* verifying agency staff, not the agency. This is a different product and a different buyer.
- The gap between neutral and vendor figures is large: 6% self-reported interview fraud (Gartner) against 23–47% vendor flag rates. Vendor "flags" are therefore partly suspicion scores, not confirmed fraud. Any startup business case should assume the confirmed-fraud rate sits much closer to the lower figures.

### Gaps
- No primary SIA or ASA survey data was accessible (403). The 41% and 37%→54% figures are second-hand.
- LinkedIn, Lever and Ashby aggregate fraud-rate data were not found.
- I found no fraud rates broken out for staffing-firm applicants versus direct employers.
- I could not verify the arrests, device counts or total-to-date figures in the DOJ Oct 13, 2026 press release.

---

## Q2. What does a fraud incident cost a staffing agency or employer?

### Takeaway
There is **no rigorous per-incident cost figure** for staffing agencies. Lost placement fees and lost client trust are described but never quantified.
- **Employer-side evidence is survey-based:** in a vendor survey, 23% of hiring managers estimate losses above $50K in a year, and 10% above $100K. Resolving an incident takes one to three weeks.
- **Security exposure is the large tail:** in one vendor report, 98% of fraudulent hires already held company credentials when caught.
- **North Korean schemes** generated an average of roughly $17K–$50K in wages per victim company, by my calculation from DOJ figures.

### Cited Findings
- **Checkr survey** of 3,000 US hiring managers (vendor):
  - In the past year, 23% estimate losses above $50,000, 18% estimate $10,000–$50,000, and 10% report losses above $100,000.
  - 29% saw delayed projects, missed revenue or compliance issues tied to fraudulent hires.
  - [Checkr, Sep 16, 2025](https://checkr.com/resources/articles/hiring-hoax-manager-survey-2025)
- **HYPR** (vendor), as reported by Help Net Security:
  - 98% of fraudulent hires had company credentials by the time post-hire fraud was detected.
  - Resolving an incident takes at least one to three weeks, with an average of 2.52 response actions.
  - Third-party security tools detect only 53% of identity-based and AI-driven threats.
  - About 60% of identity-verification and MFA spending is triggered by a breach.
  - [Help Net Security, Sep 18, 2026](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- **Exposure window:** fraudulent hires kept unmonitored network access for an average of 5.73 days after onboarding (HYPR, via Infosecurity Magazine). — [BrightHire roundup, Sep 25, 2026](https://brighthire.com/blog/candidate-fraud-statistics-2026/) (secondary)
- **Generic bad-hire cost:** about $17,000 (CareerBuilder/Harris, 2016). This figure is not specific to fraud. — [BrightHire roundup](https://brighthire.com/blog/candidate-fraud-statistics-2026/); [Benzinga/CareerBuilder](https://www.benzinga.com/node/8711629)
- **What North Korean workers do once inside:** the FBI says they have exfiltrated proprietary data, held stolen code for ransom, released proprietary code, and harvested credentials and session cookies. — [The Hacker News, Jan 24, 2025](https://thehackernews.com/2025/01/doj-indicts-5-individuals-for-866k.html)
- The FBI adds that they now threaten and extort former employers, including death threats and threats to leak data. — [IC3 PSA, Oct 13, 2026](https://www.ic3.gov/PSA/2026/PSA261013)
- **Example scheme revenue:**
  - A Taggcar-linked worker drew a $120,000-a-year salary.
  - Taggcar invoiced a US staffing company about $75,709 for one impostor's work.
  - [The Hacker News](https://thehackernews.com/2025/01/doj-indicts-5-individuals-for-866k.html)
- **Staffing-specific costs:**
  - StaffingHub says a fraudulent placement that fails skills validation "costs more than a replacement" and exposes agencies in healthcare, finance and legal staffing to penalties and liability, but it does not quantify this.
  - It also cites "23% of businesses reported losses over $50,000" without naming a source.
  - [StaffingHub, May 12, 2026](https://staffinghub.com/hiring/candidate-verification-ai-resume-fraud-staffing-firms-2026/)
- **Staffing productivity effects (vendor case studies):**
  - Swoon: interview-to-hire up more than 21% after filtering.
  - Mitchell Martin: submittal-to-hire rate roughly doubled.
  - ECLARO: interview-to-placement 2.5x.
  - [Ropes blog, Aug 20, 2026](https://www.ropes.ai/blog/identity-verification)

### Inferences
- **Calculated, not reported:** DOJ figures imply about $5M across more than 100 companies (≈$50K per company) for the Wang scheme, and $1.2M across about 70 companies (≈$17K per company) for the Knoot/Prince schemes.
  - These are North Korean *revenue* figures, meaning wages paid. They exclude remediation, data loss and extortion.
- **For a staffing agency, the measurable cost is mostly recruiter time and lost credibility on submittals.**
  - Every fake candidate submitted to a client lowers the agency's submittal-to-interview ratio. That ratio is how managed service providers (MSPs) and vendor management systems (VMS) rank suppliers.
  - The Ropes case studies (submittal-to-hire roughly doubled) suggest this is what staffing buyers actually pay to fix. This is my interpretation; I found no independent data.
- **Security exposure is the expensive tail, but it falls mainly on the *client*.**
  - The staffing firm's exposure is contractual and reputational. I found no indemnity or contract data to quantify it.

### Gaps
- No quantified data on placement fees lost to fraud, clawbacks, client terminations of staffing suppliers, or insurance claims.
- No independent (non-vendor) cost-per-incident study.
- IBM's breach-cost figure ($4.88M average, cited by Endorsed) is a generic breach cost, not a hiring-fraud cost.

---

## Q3. Who are the competitors, does anyone detect hidden prompt injection in resumes, and are ATS vendors building this natively?

### Takeaway
This is the most damaging finding for the idea. The space is **crowded, funded and being absorbed into platforms**.
- **ATS vendors have shipped native fraud detection:** Greenhouse (Real Talent with CLEAR), Ashby (Sep 2025), Metaview (included automatically, Apr 2026) and, critically for staffing, **Bullhorn's Verify skill (May 28, 2026)**.
- **Background screeners are moving up-funnel:** Checkr launched a Fraud Detection Suite with Socure biometrics, deepfake detection and *resume fraud detection* on Oct 9, 2026, and sells ID verification for $4.99.
- **Dedicated startups already have staffing logos:** Ropes counts INSPYR Solutions, Randstad Digital and KellyMitchell as customers, and Endorsed counts Korn Ferry.
- **Hidden-text and prompt-injection detection already exists:** hireEZ runs it in production, Greenhouse's Nova by Dweet integration includes it, and an open-source Apache-2.0 defense (ResumeShield) is available.
- The best real-world measurement finds hidden injection in only **about 1% of resumes, declining since 2024**.

### Cited Findings
**ATS-native (platform absorption)**
- **Greenhouse Real Talent + CLEAR:**
  - Partnership announced Jun 12, 2025. Candidates verify with a selfie in MyGreenhouse, and CLEAR runs more than 60 signals (government ID, liveness, device and network metadata).
  - Greenhouse's support documentation says identity verification is "available for Plus and Pro subscription tiers".
  - Real Talent Fraud Detection flags location and IP mismatches, invalid contact details and unusual network activity, and adds a spam blocklist.
  - Greenhouse documentation for this feature does not mention prompt-injection or AI-content detection.
  - [Greenhouse newsroom, Jun 12, 2025](https://greenhouse.com/newsroom/greenhouse-and-clear-announce-partnership-to-enable-candidate-verification); [Greenhouse support, updated Feb 6, 2026](https://support.greenhouse.io/hc/en-us/articles/40966215931291)
- **Ashby:**
  - Launched "the first ATS-integrated fraud detection system" (its own claim). It is released to all customers as an opt-in feature.
  - Signals: device IP, email, phone and the application itself. Bulk re-checks of past applicants are possible.
  - "We provide signals, not verdicts."
  - [Ashby blog, Sep 16, 2025](https://www.ashbyhq.com/blog/all/ashby-launches-the-first-ats-integrated-fraud-detection-system); [Ashby docs](https://docs.ashbyhq.com/candidate-fraud-detection)
  - Incode also publishes an Ashby identity-verification integration. — [Incode developer docs](https://developer.incode.com/docs/ashby) (redirect page only)
- **Metaview:** fraud detection is "available automatically for all Application Review customers", with no setup and no separate tool. It covers identity deception and application automation (mass-apply bots). — [Metaview, Apr 30, 2026](https://content.metaview.ai/fraud-detection/). A snippet mentioning "$60M more, led by Insight Partners" was not verified.
- **Bullhorn (the dominant staffing ATS; 10,000+ customers):**
  - Its May 2026 release says the new **Verify** digital-worker skill "detects and flags authenticity signals" across screening, document verification, onboarding and **assignment check-ins**, working with the Screen skill.
  - Verify is "available now" to Amplify customers. No pricing or technology partner is disclosed.
  - [Bullhorn, May 28, 2026](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/)
  - Bullhorn's marketplace (300+ partners) shows background screeners Asurint and Accurate Background. I found no dedicated candidate-fraud partner in the visible list. — [Bullhorn Marketplace](https://www.bullhorn.com/marketplace) (accessed Oct 14, 2026; partial list)
- **iCIMS ID Verification:** identity checks built into iCIMS, relying on third-party identity services. — [Proof vendor list, updated Jul 15, 2026](https://www.proof.com/blog/top-10-candidate-fraud-and-identity-verification-tools-to-consider-in-2026) (Proof is a competitor and ranks itself first)

**Background screeners moving into fraud**
- **Checkr:**
  - Fraud Detection Suite (Oct 2026): Socure face biometrics with presentation-attack detection and document analysis; deepfake detection; contact and credential checks; online-presence analysis; device and location signals; **resume fraud detection (beta)**.
  - CEO: "A one-time identity check is no longer enough."
  - Acquired Truv (income and employment verification) in August 2026.
  - [Biometric Update, Oct 9, 2026](https://biometricupdate.com/202610/checkr-layers-biometrics-data-analysis-and-fraud-signals-to-catch-fake-candidates)
  - **Public pricing:** Basic $29.99, Essential $59.99 (includes identity verification), Complete $94.99. The **identity-verification add-on costs $4.99 per check** (document review, live selfie, device and location validation). — [Checkr pricing](https://checkr.com/pricing) (accessed Oct 14, 2026)
- **First Advantage (now including Sterling):** Sterling customers order through First Advantage, which markets an identity-check product. — [Sterling](https://sterlingcheck.com/); [First Advantage ID Check](https://fadv.com/id-check/lp/)
- **HireRight and Certn:** screening with basic identity validation. — [Proof list](https://www.proof.com/blog/top-10-candidate-fraud-and-identity-verification-tools-to-consider-in-2026) (vendor-authored)

**Dedicated candidate-fraud vendors**

| Vendor | What it does | Segment | Pricing | Funding / scale | Source |
|---|---|---|---|---|---|
| **Endorsed** (San Francisco) | Scores every applicant on 350–700+ identity signals inside the ATS; Chrome extension (FraudShield); AI Applicant Review add-on; claims 96%+ accuracy and monthly bias audits | Startups to Fortune 500 (logos: Korn Ferry, Huntress, Yahoo, Life360); 27 ATS integrations incl. Greenhouse, Ashby, Lever, iCIMS, Workday; Bullhorn integration unconfirmed | Free trial; **Growth $249 per user per month, annual billing, 3-seat minimum**; Enterprise custom | Liquid 2 Ventures, Pioneer Fund, angels; 10.6M–11M+ applications analysed; round size not found | [endorsed.com](https://www.endorsed.com/) (accessed Oct 14, 2026); [Fortune, Sep 1, 2026](https://www.fortune.com/2026/09/01/north-korean-it-worker-remote-job-applications/); [ExtScope](https://extscope.org/extension/ajjffoajpddpajnogfnoagacmgkhddnc) |
| **Ropes AI** | "Scout" top-of-funnel cross-checks (phone, email, resume, LinkedIn, GitHub); job-specific assessments that detect VPNs, proxies, remote desktops and overlays | **Staffing firms.** Logos: Randstad Digital, Medical Solutions, Swoon, ECLARO, Mitchell Martin, Improving, Talon, ConsultNet, Take2, **INSPYR Solutions**, KellyMitchell, Game7 | Demo only | Not found; ISO 27001 and SOC Type 1 | [ropes.ai](https://www.ropes.ai/); [Ropes blog, Aug 20, 2026](https://www.ropes.ai/blog/identity-verification) |
| **Crosschq ApplicantX** | End-to-end fraud defense: synthetic identities, AI-generated resumes, surge applications, proxies, fake references, deepfakes; "Fraud Suspicion Rating"; API-first plus standalone | Large organisations; partners Workday, SAP, Oracle, Greenhouse, iCIMS, Paradox | Not stated | Not found | [Crosschq, Nov 18, 2025](https://www.crosschq.com/press/ai-fraud-detection-platform-applicantx) |
| **Sardine** | Device, behavioural and network fraud signals applied to applicants: virtual cameras, emulators, remote-access tools, application farms, location spoofing; explainable rules | HR, security and compliance teams | Not stated | Not checked this session | [Sardine](https://www.sardine.ai/candidate-fraud) |
| **BrightHire (part of Zoom)** | Fraud signals across applications, AI screens and live interviews; deepfake detection on Zoom using Zoom's models; no automatic rejection | Tech employers (Duolingo, Canva, Zapier) | Not stated | Part of Zoom | [BrightHire](https://brighthire.com/solutions/candidate-fraud/) |
| **Talview** | Candidate verification (selfie or ID at multiple stages), proctoring, second-camera feed, secure browser, behavioural AI | Employers, IT consulting, exam programmes | Not stated | Not checked | [Talview blog, Dec 17, 2024](https://www.talview.com/blog/detecting-interview-scams-proxy-workers) |
| **Sherlock AI (WeCP)** | Joins Zoom, Teams and Meet interviews to flag AI-assisted cheating, impersonation, deepfakes and proxies | Employers | Not found | No funding found; WeCP is based in Austin and Bangalore | [Capterra](https://www.capterra.co.uk/software/1110423/Sherlock-AI); [IPS News, Apr 4, 2025](https://ipsnews.net/business/2025/04/04/wecp-demonstrates-sherlock-a-new-tool-for-preventing-ai-assisted-cheating-in-remote-interviews/?amp=1) |
| **SEON** | Fraud API used by YC's Work at a Startup job marketplace to screen applicants in real time | Platforms | Not stated | Not checked | [SEON case study](https://seon.io/resources/case-study/y-combinator/) (vendor) |

**Identity-verification infrastructure (the commodity layer)**
- **Persona:** $200M Series D at a $2B valuation (2025), co-led by Founders Fund and Ribbit, aimed at synthetic fraud, deepfakes and verifying "humans and AI agents". — [FinTech Global](https://fintech.global/?p=198974); [Verdict](https://www.verdict.co.uk/newsletters/identity-persona-200m/). Pricing page returned 403.
- **Veriff** self-serve pricing:
  - Essential: $0.80 per verification, $49 monthly minimum.
  - Plus: $1.39, $99 minimum.
  - Premium: $1.89, $209 minimum.
  - Liveness is included in all plans. A 15-day free trial covers 50 sessions.
  - [Veriff pricing](https://www.veriff.com/pricing) (accessed Oct 14, 2026)
- **Others:** CLEAR (Greenhouse), Socure (Checkr), Incode (Ashby), Proof (IAL2, 8,000+ customers), Onfido (Entrust, acquired April 2024) and Trulioo. — [Proof list](https://www.proof.com/blog/top-10-candidate-fraud-and-identity-verification-tools-to-consider-in-2026) (vendor-authored)

**Hidden-text and prompt-injection detection in resumes (yes, it exists)**
- **hireEZ measurement study** (UNC, Duke, ASU, **hireEZ**, UC Berkeley/Dawn Song; arXiv 2605.28999, May 27, 2026). Across **196,682 real resumes**, hidden prompt injections were found in **about 1%**: 1.19% in Applicant Match and 0.91% in the ATS, which the authors call a conservative lower bound.
  - **90.5–95.7% were "data injection"**: hidden skills, experience or job-requirement text with no explicit instruction. Explicit instruction injection is a small minority.
  - The ATS rate was about 0.6–0.8% from 2019 to 2023, peaked around 1.2% in 2024, and **fell to 0.67% by H2 2025**. Applicant Match fell from about 1.5% to about 1.0%.
  - The authors **did not measure whether injections change screening outcomes**.
  - Detector precision was estimated at 86.1% (HCD) and 92.7% (VDA); recall was not measured. General-purpose detectors performed poorly: PromptArmor precision 0.583 and recall 0.070; PromptGuard 0.455 and 0.050.
  - "Both detection methods have been integrated into hireEZ's production systems."
  - [arXiv HTML](https://arxiv.org/html/2605.28999v1)
- **ResumeShield** (single author; Apache 2.0, synthetic data):
  - Naive extraction pipelines were fully vulnerable on a 104-document corpus.
  - Channel separation removed all measured attack success. Filtering reached precision 1.000 and recall 0.944.
  - Every payload that evaded detection was one the attacker had left *visible* (the "concealment dilemma").
  - [arXiv 2609.20188](https://arxiv.org/abs/2609.20188). The page lists v1 as submitted Jul 24, 2026, which conflicts with the 2609 identifier, so the date is uncertain.
- **PhantomLint:** a general detector for hidden LLM prompts in structured documents. — [arXiv 2508.17884](https://arxiv.org/pdf/2508.17884)
- **Greenhouse's Nova by Dweet integration** lists "Hidden content detection — invisible text via tiny font sizes, keyword stuffing, overlapping duplicate text layers". Results are written back to Greenhouse as a note and risk tag. — [Greenhouse support, updated Aug 27, 2026](https://support.greenhouse.io/hc/en-us/articles/46531208072219-Nova-by-Dweet-integration-legacy); [CitedCV, Oct 8, 2026](https://citedcv.com/en/resume-prompt-injection)
- An open, vendor-neutral detection rule for hidden-text prompt injection in user-supplied documents also exists. — [ATR-2026-00515](https://agentthreatrule.org/en/rules/ATR-2026-00515) (not fetched)

### Inferences
- **The "Clean Intake" hidden insight from the earlier notes is largely disproven as a business.**
  - The measured rate is about 1% and falling, and most of it is hidden keyword stuffing rather than instructions.
  - The impact on outcomes is unmeasured, the detection methods are published and open-sourced, and at least two vendors in the hiring stack (hireEZ and Nova/Dweet) already ship it.
  - The Greenhouse "42% of candidates used prompt injection" self-report (UK/IE/DE) is inconsistent with a 1% *observed* rate. Respondents probably interpreted the term loosely. That would make hidden-text detection a **free feature or lead magnet, not a product**.
- **Identity verification is a commodity:** $0.80–$1.89 per check self-serve (Veriff), $4.99 as a Checkr add-on, and bundled at no extra cost to candidates in Greenhouse Plus and Pro. A new entrant cannot charge a premium for it.
- **For staffing specifically, Bullhorn Verify plus Ropes cover the obvious wedge.**
  - Ropes already counts INSPYR Solutions (SIA's #14 IT staffing firm, 2026), Randstad Digital and KellyMitchell as customers.
  - The earlier notes said no funding or revenue evidence existed for startups serving staffing agencies. **That is now contradicted:** Ropes has named staffing customers, and Endorsed is venture-backed with a published $249-per-seat price.
- **Signal-based fraud detection has a data network effect.** Endorsed has scanned more than 11M applications and Sardine operates a device and identity network. A solo newcomer starts with no network data, which is the decisive structural disadvantage.

### Gaps
- No funding amounts found for Ropes, Endorsed (round size), Sherlock/WeCP, Crosschq or Sardine.
- Did not check Lever, Workday, SmartRecruiters, JobDiva, Ceipal or other staffing ATSs for native fraud features.
- Did not check "Herd", "Truely" (domain parked), Tezi, Juicebox or Ribbon. These sourcing or AI-recruiter tools did not appear in fraud-detection results.
- Bullhorn Verify's actual detection methods and price are undisclosed.
- I could not confirm whether Bullhorn Amplify (and so Verify) is bought by small firms or mainly by mid-size and large ones.

---

## Q4. Grant-makers and foundations: volume trends, what grants platforms offer, and whether foundations pay

### Takeaway
I found **no primary data on private-foundation application volume**, and no evidence that foundations pay for AI-flood triage. Public research funders show the flood (covered in earlier notes), and RoRI's prescription is track-record-based shortlisting rather than detection. Grants platforms are adding AI *summaries*, not fraud or AI-flood triage:
- Submittable Smart Summary (in beta in Submittable Next).
- Foundant GLM application summaries.

This segment fails on evidence and should not be part of the wedge.

### Cited Findings
- **RoRI and UCL (Rees & Wilsdon, *Nature* comment):**
  - 12 funders in six countries saw applications rise 17% from 2022 to 2024 and **57% from 2022 to 2025**, with increases ranging from 14% (British Academy) to 142% (MSCA).
  - The authors expect agentic AI to push volume higher in 2026. They advise *against* restricting AI use, and recommend "multi-perspective applicant profiling" and checking whether an applicant's record supports their claims.
  - They name no private foundations and no vendors.
  - [RoRI, Apr 27, 2026](https://researchonresearch.org/could-agentic-ai-topple-grant-funding-systems/)
- **NIH and NSF:**
  - A Northwestern/Kellogg analysis found signs of AI-assisted writing rose sharply from 2023 in NIH and NSF submissions.
  - A *Nature* study reportedly found AI-assisted NIH proposals won at higher rates but scored lower on novelty.
  - [Kellogg NI Institute](https://niinstitute.kellogg.northwestern.edu/press/ai-is-changing-who-wins-research-grants) (search summary only; not fetched)
- **Grants platforms:**
  - Submittable's pricing page lists "automated and multi-stage review tools" and "fraud prevention and security", but no AI review or AI-content features, and shows no prices. — [Submittable pricing](https://www.submittable.com/pricing/) (accessed Oct 14, 2026)
  - A competitor's comparison (Sopact, updated Oct 4, 2026) says Submittable Next has a "Smart Summary" AI application summary in beta, and Foundant GLM offers AI application summaries. — [Sopact](https://www.sopact.com/use-case/submittable-alternatives) (vendor; Sopact sells an AI-first review product)
  - I found no AI-triage claims for Fluxx, SmartSimple or Bonterra.
- **Foundation-specific evidence:**
  - Search results gave only vendor blogs, including an unattributed claim that "only 15 percent of foundations had written guidelines for applicants" (2024).
  - The CEP report URL I tried returned 404.
  - The earlier notes record a Candid 2024 survey, via a blog: about 10% of foundations accept AI-generated proposals and 67% are undecided.

### Inferences
- Foundations' pain is likely real at open-call community, corporate and family foundations, but it is undocumented.
- Grant-management platforms already own the workflow, and are adding AI summaries that will probably grow into triage. This is a forecast, not observed.
- A foundation product would mean selling to slow, small-budget buyers with no proof of willingness to pay. It does not belong in a top-five wedge.

### Gaps
- No Submittable, Candid, Instrumentl, CEP or Chronicle of Philanthropy data on foundation application volume or AI-generated proposals was accessible within the search budget.
- No pricing for Fluxx, SmartSimple or Foundant.
- No evidence of foundations buying fraud or AI-triage tools.

---

## Q5. Buyer population and willingness to pay

### Takeaway
The US has about **27,000 staffing and recruiting companies operating about 54,000 offices** (ASA, 2021 data). Willingness to pay for fraud tooling is **proven at mid and large staffing firms and tech employers**: Ropes logos, Endorsed at $249 per seat with a three-seat minimum (about $9K a year), and Checkr add-ons.

Per-check identity prices set a low ceiling: $0.80–$4.99. I found **no data on staffing firms' screening budget per hire**. Whether the long tail of small IT staffing firms will pay is untested.

### Cited Findings
- **ASA (industry):**
  - About 27,000 US staffing and recruiting companies, operating close to 54,000 offices (2021 data). Temp and contract firms are about 57% of companies and 76% of offices.
  - About 2.2M temp and contract employees worked in an average week in 2024. Staffing companies hired 12.7M temp and contract employees in 2023.
  - Employment mix: industrial 36%, office/clerical 24%, professional/managerial 21%, **engineering/IT/scientific 11%**, **healthcare 8%**.
  - [ASA Staffing Industry Statistics](https://americanstaffing.net/staffing-research-data/fact-sheets-analysis-staffing-industry-trends/staffing-industry-statistics/) (accessed Oct 14, 2026)
- **ASA membership:** nearly 1,250 member companies with more than 15,000 branch offices (end of 2024). "80% of staffing professionals who read ASA publications… are involved in purchasing." — [ASA demographics](https://americanstaffing.net/industry-suppliers/demographics/)
- **SIA 2026 Largest IT Staffing Firms list** (as summarized in search results from firm press releases):
  - 57 US firms, each with at least $100M of 2025 IT staffing revenue, together about **$27.2B, roughly 73% of the market**.
  - Insight Global ranks #2 with about $3.28B. INSPYR Solutions ranks #14 with $468M. Yoh ranks #24. The Judge Group appears on the IT, overall, healthcare and allied-healthcare lists.
  - SIA's overall Largest Staffing Firms list has 214 companies.
  - Sources: [Insight Global](https://insightglobal.com/news/insight-global-ranked-no-2-on-sias-largest-it-staffing-firms-in-the-u-s-for-fifth-consecutive-year/); [INSPYR](https://lifestyle.kbew98country.com/story/282459/inspyr-solutions-listed-14-among-2026-largest-it-staffing-firms-in-the-u-s-by-staffing-industry-analysts/); [Yoh](https://www.yoh.com/resources/news/yoh-recognized-by-staffing-industry-analysts-as-a-2026-largest-it-staffing-firm); [Judge Group](https://www.judge.com/resources/news/the-judge-group-climbs-in-sia-2026-rankings/); [SIA report page](https://www.staffingindustry.com/research/research-reports/americas/largest-it-staffing-firms-in-the-united-states-2025-update) (members only). The 57-firm/$27.2B/73% figures come from a search summary and I did not check them on SIA itself.
- **Bullhorn:** more than 10,000 customers globally. — [Bullhorn, May 28, 2026](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/)
- **Price anchors:**
  - Checkr ID verification $4.99 per check; packages $29.99–$94.99. — [Checkr pricing](https://checkr.com/pricing)
  - Veriff $0.80–$1.89 per verification, with $49–$209 monthly minimums. — [Veriff pricing](https://www.veriff.com/pricing)
  - Endorsed Growth $249 per user per month, 3-seat minimum, annual billing. — [endorsed.com](https://www.endorsed.com/)
  - Individual verifications cost "$30–$80 per verification" (vendor blog estimate). — [Alex](https://www.alex.com/blog/background-screening-cost)
- **Buyer behaviour:** 57% of contingent-workforce buyers rely mainly on their staffing suppliers' screening, and 43% use ID-verification technology. — [SIA-hosted Ropes/CWS deck, Sep 10, 2026](https://www.staffingindustry.com/system/files/2026-09/ropes_americas_buyer_webinar_091026.pdf) (snippet only)
- **Spending triggers:** about 60% of identity-verification and MFA spending is triggered by a breach. — [Help Net Security/HYPR, Sep 18, 2026](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- **SIA treats this as an industry topic:** it ran a webinar titled "Fighting Hiring Fraud at Scale: How Staffing Firms Can Protect Clients and Candidates". — [SIA webinar](https://www.staffingindustry.com/webinars/staffing/thought-leadership/archived/fighting-hiring-fraud-at-scale-how-staffing-firms-can-protect-clients-and-candidates) (not fetched)

### Inferences
- **Size of the long tail (calculated):** $27.2B is about 73% of the market, so total US IT staffing revenue is about $37B and the firms below $100M share about $10B. The number of such firms is unknown.
- **Minimum spend:** Endorsed's entry price works out to about $8,964 a year ($249 × 3 seats × 12 months).
- **Cost of DIY identity checks:** a small firm verifying 1,000 candidates a year with Veriff would pay roughly $800–$1,900 plus monthly minimums.
- **The pricing room for a newcomer is narrow** (my interpretation):
  - It must charge more than commodity identity checks, which are near $1–5.
  - It must still look cheaper than Endorsed or Ropes to small firms.
  - It must justify itself on something other than identity, such as **client-facing proof**, or recruiter time saved.
- **Supplier-side opportunity (hypothesis):** because 57% of buyers lean on suppliers' screening, supplier staffing firms could be pushed into showing evidence of verification. This would create supplier-side demand, but it is a hypothesis, not observed.

### Gaps
- No survey of staffing firms' screening spend per hire, or the share of it going to identity and fraud.
- No count of IT-focused staffing firms below $100M.
- No data on which ATS small IT staffing firms use. Bullhorn's share of small firms is unknown.
- No primary SIA buyer-survey access.

---

## Q6. Disconfirming evidence: bundling, legal risk, detection accuracy, buyer reluctance

### Takeaway
The disconfirming evidence is **strong on five fronts**:
1. **Bundling:** Greenhouse, Ashby, Metaview, Bullhorn and Checkr have all shipped fraud detection in 2025–2026, often at no extra charge.
2. **Legal risk:** a fraud or authenticity score built from outside data may make the vendor a consumer reporting agency under FCRA (the *Kistler v. Eightfold* theory). Scores may also count as an automated employment decision tool under New York City's Local Law 144 or as automated decision-making under Illinois, Colorado and California rules.
3. **Discrimination risk:** fraud "patterns" correlate with national origin. Endorsed's flagged profiles skew to Indian first names and to universities with large Indian student populations, and the FBI warns against name filtering.
4. **Adversarial accuracy:** North Korean workers now buy pre-verified identity-provider accounts, and vendor flag rates are suspicion rates, not confirmed fraud.
5. **Founder fit:** buyers expect SOC 2 or ISO 27001 and network data that a solo founder cannot supply.

### Cited Findings
**Bundling and absorption** (see Q3)
- Greenhouse (Plus and Pro tiers), Ashby (all customers, opt-in), Metaview (automatic), Bullhorn Verify (available to Amplify customers), Checkr Fraud Detection Suite with resume fraud beta, and iCIMS ID Verification. — [Greenhouse support](https://support.greenhouse.io/hc/en-us/articles/40966215931291); [Ashby](https://www.ashbyhq.com/blog/all/ashby-launches-the-first-ats-integrated-fraud-detection-system); [Metaview](https://content.metaview.ai/fraud-detection/); [Bullhorn](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/); [Biometric Update](https://biometricupdate.com/202610/checkr-layers-biometrics-data-analysis-and-fraud-signals-to-catch-fake-candidates)

**FCRA**
- **Kistler v. Eightfold AI** (Contra Costa County Superior Court, filed Jan 20, 2026). The plaintiffs argue that an AI vendor's 0–5 candidate scores, built from LinkedIn, GitHub and other outside data, are "consumer reports" under FCRA and California's ICRAA. If so, the vendor needs employer certifications, accuracy procedures and dispute handling.
  - The case is at an early stage and Eightfold denies scraping.
  - Fisher Phillips advises vendors to "assess whether your tools trigger FCRA obligations".
  - [Fisher Phillips, Jan 26, 2026](https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html)
- **Exposure if FCRA applies:**
  - Employers face disclosure and authorization, pre-adverse-action and adverse-action notice duties.
  - Willful violations carry statutory damages of $100–$1,000 per applicant (15 U.S.C. § 1681n).
  - The risk is concentrated in the *evaluation* step, not sourcing.
  - [ConsumerAttorneys](https://consumerattorneys.com/article/ai-hiring-tools-fcra); [HeroHunt](https://www.herohunt.ai/blog/is-your-ai-sourcing-tool-an-fcra-risk-2026/) (secondary; I did not verify the CFPB guidance they cite)

**State and local AI-hiring rules** (from law-firm and compliance summaries; verify the dates against the statutes)
- **Illinois:** AI-in-employment amendment effective Jan 1, 2026. It prohibits discriminatory effect and ZIP-code proxies, and requires notice.
- **Colorado:** the 2024 AI Act was repealed and replaced by **SB 26-189, effective Jan 1, 2027**. It requires an explanation of an automated decision's role in an adverse decision within 30 days, human review, and data correction.
- **California:** Civil Rights Council automated-decision-system rules have been in effect since Oct 1, 2025. CPPA automated-decision-making rules took effect Jan 1, 2026, with employer compliance for significant decisions from **Jan 1, 2027**.
- **Texas:** TRAIGA took effect Jan 1, 2026. A December 2025 federal executive order seeks to preempt state AI rules but cannot override them by itself.
- Sources: [Masuda Funai](https://masudafunai.com/articles/the-proliferation-of-state-laws-regulating-ai-use-in-employment-decisions); [Brightmine](https://www.brightmine.com/us/resources/hr-compliance/ai-laws-by-state-and-locality/); [Goethena](https://www.goethena.com/post/ai-in-hiring-5-employment-laws-every-hr-team-should-know-in-2027/); [PromptQuorum](https://www.promptquorum.com/power-local-llm/us-state-ai-employment-laws-compliance) (secondary; one older source still lists Colorado as June 30, 2026, which is now superseded)
- **Staffing firms are tracking this:** Eastridge, a staffing firm, publishes guidance for "employers and staffing leaders" on AI discrimination and transparency laws. — [Eastridge](https://www.eastridge.com/blog/navigating-the-new-wave-of-ai-discrimination-and-transparency-laws-what-employers-and-staffing-leaders-need-to-know)
- **NYC Local Law 144:** Endorsed advertises "monthly bias audits… 12x more often than NYC Local Law 144 requires". This shows the market leader treats fraud scoring as within scope of bias-audit expectations. — [endorsed.com](https://www.endorsed.com/)

**National-origin and disparate-impact risk**
- The FBI warns against "relying solely on ban lists or name filtering, which can exclude qualified applicants and harm identity theft victims", and asks employers to "calibrate carefully to limit false positives". — [IC3 PSA, Oct 13, 2026](https://www.ic3.gov/PSA/2026/PSA261013)
- Endorsed's flagged-profile traits include the first name "Sai" and the University of North Texas and University of Central Missouri. Its CEO says no single trait should make an applicant look suspicious. — [Fortune, Sep 1, 2026](https://www.fortune.com/2026/09/01/north-korean-it-worker-remote-job-applications/)

**Accuracy and adversarial dynamics**
- North Korean workers verify stolen identities "through purchased accounts or licenses from identity verification providers". — [IC3 PSA](https://www.ic3.gov/PSA/2026/PSA261013)
- Third-party security tools catch only 53% of identity-based and AI-driven threats. — [Help Net Security/HYPR](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- A valid ID can belong to a real person who is not the one sitting in the interview, so identity checks alone miss most fraud. Identity and document fraud is only 12.8% of the methods Ropes observes. — [Ropes blog](https://www.ropes.ai/blog/identity-verification); [SIA-hosted deck snippet](https://www.staffingindustry.com/system/files/2026-09/ropes_americas_buyer_webinar_091026.pdf)
- Wording-based injection detection falls to 0.889 recall against paraphrases. General-purpose prompt-injection detectors reach recall of only 0.05–0.07 on resumes. — [ResumeShield](https://arxiv.org/abs/2609.20188); [arXiv 2605.28999](https://arxiv.org/html/2605.28999v1)

**Buyer reluctance and requirements**
- 96% of HR leaders believe they would detect fraud. This overconfidence suppresses proactive buying. — [Help Net Security/HYPR](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- Competitors advertise SOC 2 Type II (Endorsed Growth tier) and ISO 27001 plus SOC Type 1 (Ropes), signalling buyer security requirements. — [endorsed.com](https://www.endorsed.com/); [ropes.ai](https://www.ropes.ai/)
- Gartner: 62% of candidates are more likely to apply when interviews are in person. Employers can "fix" fraud with an in-person step rather than software. — [HR Dive, Aug 8, 2025](https://www.hrdive.com/news/fake-job-candidates-ai/757126/)

### Inferences
- **The legal surface grows with the score.** A tool that only *re-verifies continuity* (the same person, checked by the candidate's own selfie, at each stage) and gives no adverse recommendation carries less FCRA and automated-decision risk than one that scores candidates from outside data. That constrains any wedge to "evidence, not verdicts", which is the same positioning Ashby and BrightHire already use.
- **Founder-specific risk** (interpretation, not evidence):
  - An India-based solo founder would be selling a product whose risk signals overlap with Indian-origin candidates, in a market where the FBI names India among subcontracting locations.
  - The founder would also be handling US candidate biometrics and personal data without SOC 2. This adds trust friction on top of the competition problem.
- **The likely incumbent response** to any small-firm traction: Bullhorn bundles Verify into lower tiers, or Checkr pushes its $4.99 add-on through staffing channels. Both already exist, so no new build is needed on their side.

### Gaps
- No legal opinion on whether a candidate-initiated identity re-verification service is a consumer reporting agency.
- EEOC's current stance on AI-hiring guidance was not checked this session.
- No independent accuracy benchmark exists for any commercial candidate-fraud product. All accuracy claims, such as Endorsed's 96%+, are vendor statements.

---

## Q7. Twenty specific first-customer targets (by type or verifiable public information)

### Takeaway
The most reachable early buyers are **IT staffing firms below the SIA top-57 threshold that place remote technical contractors**, plus firms that already write publicly about candidate fraud.
- **Avoid as targets:** the large firms already using Ropes (INSPYR, Randstad Digital, KellyMitchell and others). Use them as reference intelligence instead.
- **Channels:** ASA (about 1,250 members), Bullhorn's marketplace (300+ partners) and background screeners serving staffing firms.
- **Grant-makers:** only two types are listed, because no evidence of willingness to pay exists.

### Cited Findings
The basis for each target follows. The firm descriptions are mine; the evidence is cited.

| # | Target | Type | Why (evidence) |
|---|---|---|---|
| 1 | **BCforward** | IT staffing firm | Publishes on candidate fraud ("AI is changing candidate fraud; it's also changing how companies detect it") — [BCforward](https://www.bcforward.com/ai-is-changing-candidate-fraud-its-also-changing-how-companies-detect-it/) |
| 2 | **KORE1** | IT staffing firm | Publishes IT-staffing market content for 2026 — [KORE1](https://www.kore1.com/top-it-staffing-agencies-us-2026/) |
| 3 | **redShift Recruiting** | Recruiting firm | Published a post on resume prompt injection — [redShift](https://www.redshiftrecruiting.com/career-blog/resume-prompt-injection) |
| 4 | **Eastridge Workforce Solutions** | Staffing firm | Publishes AI-hiring-law guidance for staffing leaders — [Eastridge](https://www.eastridge.com/blog/navigating-the-new-wave-of-ai-discrimination-and-transparency-laws-what-employers-and-staffing-leaders-need-to-know) |
| 5 | **BridgeView IT** | IT staffing firm | Its blog is the conduit for the Yardstik fraud-by-industry data — [BrightHire roundup](https://brighthire.com/blog/candidate-fraud-statistics-2026/) |
| 6 | **Frontline Source Group** | Staffing firm | Its blog is cited for bad-hire cost data — [BrightHire roundup](https://brighthire.com/blog/candidate-fraud-statistics-2026/) |
| 7 | **Yoh** | IT staffing, SIA 2026 #24 | Large; long shot for a solo founder — [Yoh](https://www.yoh.com/resources/news/yoh-recognized-by-staffing-industry-analysts-as-a-2026-largest-it-staffing-firm) |
| 8 | **The Judge Group** | IT and healthcare staffing, on four SIA 2026 lists | Spans IT and healthcare fraud exposure — [Judge](https://www.judge.com/resources/news/the-judge-group-climbs-in-sia-2026-rankings/) |
| 9 | **Prolink** | Staffing, SIA 2026 Largest US Staffing Firms | Named on the 2026 list — [Prolink](https://prolinkworks.com/node/708) |
| 10 | **Insight Global** | IT staffing, SIA #2 | Enterprise; an informational interview only, not a realistic first customer — [Insight Global](https://insightglobal.com/news/insight-global-ranked-no-2-on-sias-largest-it-staffing-firms-in-the-u-s-for-fifth-consecutive-year/) |
| 11 | **Small IT staffing firms acting as subvendors or prime suppliers in chained supply arrangements** | Type | Taggcar, a staffing firm, invoiced a US staffing company for an impostor's work, showing staffing chains are a conduit — [The Hacker News](https://thehackernews.com/2025/01/doj-indicts-5-individuals-for-866k.html) |
| 12 | **Staffing suppliers in MSP/VMS programmes** | Type | 57% of buyers rely mainly on suppliers' screening — [SIA-hosted deck snippet](https://www.staffingindustry.com/system/files/2026-09/ropes_americas_buyer_webinar_091026.pdf) |
| 13 | **ASA member firms in engineering, IT and scientific staffing** | Type and channel | About 1,250 members; IT/engineering is 11% of staffing employment — [ASA](https://americanstaffing.net/industry-suppliers/demographics/); [ASA stats](https://americanstaffing.net/staffing-research-data/fact-sheets-analysis-staffing-industry-trends/staffing-industry-statistics/) |
| 14 | **Asurint** | Background screener on Bullhorn Marketplace (channel or reseller) | Serves staffing agencies — [Bullhorn Marketplace](https://www.bullhorn.com/marketplace) |
| 15 | **Accurate Background** | Background screener on Bullhorn Marketplace (channel) | Listed partner — [Bullhorn Marketplace](https://www.bullhorn.com/marketplace) |
| 16 | **Western Verify / GCheck-type regional screeners** | Channel (screeners serving small employers and staffing) | Publish on fake applicants and staffing screening costs — [Western Verify](https://westernverify.com/resources/blog/the-candidate-isnt-real-ai-fake-applicants-have-arrived-and-small-employers-are-not-exempt); [GCheck](https://gcheck.com/blog/controlling-background-check-costs-in-a-staffing-firm/) |
| 17 | **Security and infrastructure companies hiring remote engineers in-house** (Huntress-like) | Type | Huntress flagged 23.2% of applicants and stacks several vendors — [Huntress](https://www.huntress.com/blog/ai-enhanced-candidate-fraud) |
| 18 | **Small healthcare staffing agencies supplying nursing homes** | Type | Impostor-nurse prosecutions in WA, MA, CT and MD show facility-level demand for credential continuity — [KIRO7](https://www.kiro7.com/news/local/kent-man-convicted-using-stolen-nurse-identities-place-impostor-nurses-nursing-homes/E4FZMWOD3JFBPIXJLLQGOC7S4U/); [HealthExec](https://healthexec.com/topics/healthcare-management/legal-news/massachusetts-staffing-agency-owner-indicted-sending-fake-cnas-nursing-homes) |
| 19 | **Community or corporate foundations running open grant calls** | Type (grant-maker; low priority) | No volume or willingness-to-pay evidence; RoRI public-funder data only — [RoRI](https://researchonresearch.org/could-agentic-ai-topple-grant-funding-systems/) |
| 20 | **University research offices running internal funding rounds** | Type (grant-maker; low priority) | NIH six-application cap and AI-originality rules (earlier notes) create intake-screening work |

**Do not target (existing Ropes customers; use for reference intelligence):** Randstad Digital, Medical Solutions, Swoon, ECLARO, Mitchell Martin, Improving, Talon, ConsultNet, Take2, INSPYR Solutions, KellyMitchell, Game7 Staffing. — [ropes.ai](https://www.ropes.ai/). Also Korn Ferry, an Endorsed customer. — [endorsed.com](https://www.endorsed.com/)

### Inferences
- Targets 1–6 are the best cold-outreach starting points. They have publicly engaged with the topic, which is a cheap signal of pain. Whether any of them already uses Bullhorn Verify, Ropes or Endorsed is unknown, and that is the first discovery question.
- Channel partners (14–16) matter more than direct sales for a solo founder. Small background screeners lack fraud-detection products and could resell a narrow add-on. This is a hypothesis.

### Gaps
- ASA state-chapter and affiliate names were not retrieved.
- Recruiting communities were not checked (Reddit inaccessible in earlier sessions; RecruitingDaily/RecTech communities not searched).
- For targets 1–10, I did not verify company size, ATS used, or whether they already buy fraud tooling.
- No regional association of grantmakers was verified this session.

---

## Q8. The narrowest MVP a solo non-engineer could build in 2–8 weeks, and a 14-day experiment with kill criteria

### Takeaway
If this is tested at all, the narrowest defensible wedge is not a fraud *score*. It is a **"submittal proof pack" for small IT staffing suppliers**: candidate-initiated identity verification at submittal, plus a same-person re-check at interview and at start, plus a hidden-text resume scan. The output is a one-page evidence record the staffing firm can attach to its submittal to the client, MSP or prime vendor.

This avoids scoring with outside data, which is the FCRA and automated-decision exposure. It sells client trust, not detection accuracy, and needs no proprietary data network. Run it **concierge-first for 14 days before building anything**.

### Cited Findings (inputs used in the design)
- **Component costs:**
  - Self-serve identity verification with liveness: $0.80–$1.89 per verification (Veriff), with a 15-day, 50-session free trial. — [Veriff pricing](https://www.veriff.com/pricing)
  - Checkr ID add-on: $4.99, the ceiling a staffing buyer will compare against. — [Checkr pricing](https://checkr.com/pricing)
- **Hidden-text detection** works by comparing rendered against extracted text, plus font-size and colour rules. Open methods are published, including an Apache-2.0 defense. — [arXiv 2605.28999](https://arxiv.org/html/2605.28999v1); [ResumeShield](https://arxiv.org/abs/2609.20188)
- **Lifecycle verification:** the FBI recommends identity in depth across the lifecycle and live-verification friction, and warns against name filtering. — [IC3 PSA](https://www.ic3.gov/PSA/2026/PSA261013). HYPR points to the 90-day gap between hiring and onboarding as a blind spot. — [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/hypr-hiring-fraud-detection-report/)
- **Buyers rely on suppliers' screening (57%).** — [SIA-hosted deck snippet](https://www.staffingindustry.com/system/files/2026-09/ropes_americas_buyer_webinar_091026.pdf)

### Inferences (design; untested hypotheses)

**MVP scope (2–4 weeks with Claude-assisted coding)**
1. **Recruiter interface:** a recruiter pastes a candidate's email and attaches the resume. The candidate receives a link.
2. **Identity at submittal:** the candidate completes a Veriff ID-plus-selfie session through the self-serve API. The tool stores only the verification result and reference IDs, not raw images.
3. **Same-person re-checks:** at the client interview and on day 1, the candidate re-does a selfie or liveness check through a fresh link. The output is a match or no-match against the submittal session, plus device and IP country for each session.
4. **Hidden-text scan:** a PDF/DOCX check (PyMuPDF text-layer against rendered text, plus font-size and colour rules) reports any invisible text verbatim. **No verdict, no score.**
5. **Proof pack:** a one-page PDF and shareable link with timestamps, verification status, re-check results and hidden-text findings, labelled "evidence for human review; not a consumer report or hiring recommendation" (wording subject to counsel review).
6. **Stack:** a simple web app (Next.js or Supabase, or a no-code front end), Veriff API and a Python worker. No ATS integration in v1. Recruiters attach the PDF to the Bullhorn or other ATS record by hand.

**What is deliberately excluded:** scraping LinkedIn or GitHub, any fraud score, any name, school or location heuristics (FCRA, national-origin and FBI-guidance risk), interview deepfake detection (BrightHire/Zoom territory) and grant-maker features.

**Price hypothesis to test:** $8–15 per candidate pack, or $299 a month for up to 50 packs.
- It has to sit above commodity identity-check pricing ($0.80–$4.99) and below Endorsed's roughly $9K-a-year minimum.
- This is a hypothesis, not evidence.

**14-day experiment (concierge; no code beyond the hidden-text script)**
- **Days 1–2:** build a list of 60 US IT staffing firms below $100M revenue (LinkedIn company search; plus targets 1–6 and 11–13 above). Write one outreach script offering a free "submittal integrity audit" of the firm's last 50–100 submitted resumes (hidden-text scan) and 5 free identity re-check packs on live candidates.
- **Days 3–5:** send 60 personalised messages to owners or recruiting heads. Book discovery calls. The four questions are:
  1. Which ATS do you use, and is Bullhorn Verify, Ropes, Endorsed or Checkr already in place?
  2. Has a client, MSP or prime vendor asked you to prove a candidate's identity in the last 6 months?
  3. What did your last fraudulent submittal cost you?
  4. Who signs for tools under $500 a month?
- **Days 6–11:** run the audits manually (founder plus script). Deliver packs using Veriff's free trial sessions.
- **Days 12–14:** ask each engaged firm for a paid pilot (at least $299 for the next month, or a per-pack price) and ask for an introduction to one client or MSP contact. Have one 30-minute call with a US employment or FCRA attorney (budget about $300–500) on whether the pack makes the founder a consumer reporting agency.

**Kill criteria** (any one kills the hiring wedge):
1. Fewer than 6 discovery calls from 60 messages, a reply rate below 10%.
2. In 3 or more of the first 6 calls, the firm already uses Bullhorn Verify, Ropes, Endorsed or a Checkr fraud add-on and calls it "good enough".
3. Hidden text found in fewer than 2% of audited resumes. That is consistent with hireEZ's 1%, and means the scan cannot carry the pitch.
4. Fewer than 2 of 6 firms report a client, MSP or prime *asking* for verification evidence. Without that, the "proof pack" has no external pull.
5. Zero paid pilots at $299 or more, or at $8 or more per pack, by day 14.
6. Counsel advises that the service is a consumer reporting agency requiring an FCRA compliance programme the founder cannot fund. The fallback, pure software run by the staffing firm itself, must then be re-validated.

**Advance signal:** 2 or more paid pilots, plus at least one MSP or prime vendor that says it would *require or prefer* the pack from suppliers. Only that combination would justify building beyond concierge.

### Gaps
- No evidence that MSPs or prime vendors accept supplier-generated verification evidence. This is the central untested assumption.
- Veriff's terms for re-verification against a prior session (face-match continuity) were not checked.
- Legal status of a candidate-initiated verification pack under FCRA, ICRAA and state ADMT rules is unknown.

---

## Q9. Verdict: advance, advance with conditions, or reject? And the most defensible wedge

### Takeaway
**Reject. Do not advance this to the top-five shortlist.**
- The pain is among the best-documented in this research programme (FBI and DOJ actions through Oct 13, 2026; Gartner; multiple vendor datasets).
- Each proposed angle has a specific, evidenced problem:
  - **Prompt-injection detection:** the problem is small (about 1% of resumes, declining) and already productized (hireEZ, Nova/Dweet, open source).
  - **Identity verification:** commoditized at $0.80–$4.99 and bundled into Greenhouse, Ashby and Checkr.
  - **Fraud scoring:** owned by funded, data-rich players (Endorsed, Crosschq, Sardine). It is also legally exposed under FCRA (*Eightfold*), Illinois, Colorado SB 26-189 and California ADMT from 2027.
  - **The staffing-specific wedge** is already occupied by Bullhorn Verify (the default staffing ATS) and Ropes, which counts SIA top-15 and enterprise staffing firms as customers.
  - **Grant-makers:** no willingness-to-pay or volume evidence.
- For a solo, India-based non-engineer, the lack of network data, missing security certifications, and national-origin optics around fraud signals compound the competitive problem.

**Most defensible narrow wedge, if the founder still wants to test:** a concierge "submittal proof pack" for small IT staffing suppliers in MSP/VMS and prime-vendor chains (Q8). Advance it only if the 14-day test produces 2 or more paid pilots *and* external pull from an MSP or prime vendor.

### Cited Findings
- **Platform absorption:** [Greenhouse support](https://support.greenhouse.io/hc/en-us/articles/40966215931291); [Ashby, Sep 16, 2025](https://www.ashbyhq.com/blog/all/ashby-launches-the-first-ats-integrated-fraud-detection-system); [Metaview, Apr 30, 2026](https://content.metaview.ai/fraud-detection/); [Bullhorn, May 28, 2026](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/); [Checkr suite, Oct 9, 2026](https://biometricupdate.com/202610/checkr-layers-biometrics-data-analysis-and-fraud-signals-to-catch-fake-candidates)
- **Staffing-specific incumbent:** [Ropes](https://www.ropes.ai/)
- **Funded dedicated vendor with public pricing:** [Endorsed](https://www.endorsed.com/); [Fortune, Sep 1, 2026](https://www.fortune.com/2026/09/01/north-korean-it-worker-remote-job-applications/)
- **Prompt-injection prevalence and productization:** [arXiv 2605.28999](https://arxiv.org/html/2605.28999v1); [Greenhouse Nova/Dweet](https://support.greenhouse.io/hc/en-us/articles/46531208072219-Nova-by-Dweet-integration-legacy); [ResumeShield](https://arxiv.org/abs/2609.20188)
- **Commodity identity pricing:** [Veriff](https://www.veriff.com/pricing); [Checkr](https://checkr.com/pricing)
- **Legal:** [Fisher Phillips, Jan 26, 2026](https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html); [Masuda Funai](https://masudafunai.com/articles/the-proliferation-of-state-laws-regulating-ai-use-in-employment-decisions)
- **FBI guidance against name filtering:** [IC3 PSA, Oct 13, 2026](https://www.ic3.gov/PSA/2026/PSA261013)
- **Grant-maker evidence limited to public funders:** [RoRI, Apr 27, 2026](https://researchonresearch.org/could-agentic-ai-topple-grant-funding-systems/)

### Inferences
**Why not "advance with conditions"?** A top-five slot should go to opportunities where a capital-light solo founder has a plausible path to defensibility. Here, every layer has a well-resourced owner:
- The ATS layer (Bullhorn, Greenhouse, Ashby).
- The screening layer (Checkr, First Advantage).
- The identity layer (CLEAR, Persona, Veriff, Socure, Incode).
- The dedicated fraud layer (Endorsed, Ropes, Crosschq, Sardine).
- The interview layer (BrightHire/Zoom, Talview, Sherlock).

The only open space, client-facing supplier proof for small firms, rests on an assumption I could not evidence: that MSPs and prime vendors want supplier-generated proof.

**What would reverse the verdict:**
- A primary SIA or MSP source showing buyers are *contractually requiring* supplier identity evidence.
- Evidence that Bullhorn Verify is not available, or not adopted, below the Amplify tier.
- The 14-day test hitting its advance signal.

**Salvage value for the wider report:**
- The hidden-text scanner is a credible free lead magnet or content asset, for example "we scanned N resumes".
- The receiving-side theme, that reviewer hours are the binding constraint, remains valid. It should be pursued in a less-absorbed domain from the earlier notes, such as claims-evidence provenance or funder triage, but only once those show willingness-to-pay evidence.

### Gaps
- Not verified: primary SIA buyer surveys, Bullhorn Verify pricing or tier availability, Ropes and Endorsed funding size, and small-firm adoption of any fraud tool.
- No legal review of the proof-pack concept.
- No practitioner interviews; Reddit, G2 and recruiter communities were not accessed.
- The verdict rests on public product pages and vendor-reported statistics. A discovery sprint could change it if small IT staffing firms turn out to be systematically unserved.
