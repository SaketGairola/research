# Stress test: (A) impersonation-proof vendor bank-change verification for US SMB/mid-market AP, and (B) an IBM i "system dossier" (AI plus Indian IBM i developers), as of 14 Oct 2026

Method and access notes (read first):
- This file builds on two earlier notes and does not repeat them: `investor_theses_and_crowding.md` (IC3 2024 BEC figures, Trustpair basics, first C1 sketch) and `it_msp_security_data.md` (Fortra 2026 skills figure of 69%, IBM Bob basics, IN-COM tool landscape, PromptedDev and Virtutem framing). It covers only the gaps those notes left.
- I used all 25 allowed WebSearch calls. Everything after that came from direct fetches of known URLs, plus curl and pdftotext on the PDFs.
- Primary documents read in full: the FBI IC3 2025 Annual Report (PDF), the AFP 2026 Key Highlights (PDF), Nacha's rule pages, IBM's Bob announcement and pricing pages, and the Fresche X-Analysis AI brief (PDF).
- **Could not access:**
  - the full AFP 2026 report (members only, or $295);
  - the Fortra 2026 survey page (HTTP 403);
  - Eftsure's site (redirect loop);
  - BILL help pages (403; content came only from search snippets);
  - At-Bay's BusinessWire release (403);
  - bloop.ai (503).
- **Not researched at all:** Mobilize.Net/Asymbix, Kyndryl, the Infosys/TCS/HCL IBM i practices, Bluestone, Medius, Coupa supplier onboarding, Paymode-X and Nuvei.
- "Search summary" means the claim came from a search-result digest and the page itself was not fetched. Treat those claims as lower confidence.
- The facts are under **Cited Findings**. My interpretation is under **Inferences**.

## A1. How large and how fast-growing is vendor/BEC payment fraud (IC3 2025, AFP 2026, insurer claims), and how much of it involves deepfakes?

### Takeaway
BEC is still large and grew modestly in 2025: $3.05B reported to IC3, up 10%, with complaints up 15.5%. The AFP says 74% of organizations were hit by BEC, mostly through fake vendor or executive payment-change requests. The "deepfake" part, however, is small in every primary source. AI-linked BEC was about $30M (about 1% of BEC losses), and deepfake attempts were reported by 7% of organizations that experienced fraud. Insurer data shows funds-transfer-fraud frequency and severity *falling* in 2025.

### Cited Findings
**FBI IC3 2025 Annual Report** (PDF metadata: created 16 Apr 2026) — [IC3 2025 report](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf):
- Overall: 1,008,597 complaints and $20.877B in losses, up 26% from 2024.
- BEC was the #2 cyber-enabled fraud by loss: $3,046,598,558 across 24,768 complaints. This compares with $2,770,151,146 (21,442 complaints) in 2024 and $2,946,830,270 in 2023.
- My arithmetic: BEC losses rose 10.0% and complaints rose 15.5%. Average loss per complaint fell from about $129.2K to about $123.0K.
- AI section: IC3 received 22,364 complaints with AI-related information, with $893,346,472 in losses. "In 2025, businesses reported losses over $30 million to BEC scams involving AI." The AI table shows BEC at $30,256,592, which is about 1% of BEC losses (my calculation). IC3 also notes that "Voice cloning can also be used to request wire payment."
- People aged 60+ lost $568,048,472 to BEC in 2025, versus $385,001,099 in 2024.
- Recovery (IC3 Recovery Asset Team, Financial Fraud Kill Chain):
  - Domestic: 3,574 incidents, with $507,042,623 frozen.
  - International: 326 incidents, with $171,970,560 frozen.
  - IC3 says that in the past most kill-chain cases were BEC, but in 2025 it saw a rise in Tech Support and Account Takeover cases.

**AFP 2026 Payments Fraud and Control Survey** (press release 14 Apr 2026; 465 treasury practitioners surveyed in January 2026) — [AFP press release](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags); [AFP Key Highlights, hosted by sponsor Truist, Apr 2026](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf):
- 76% of organizations experienced attempted or actual payments fraud in 2025, versus 79% in 2024 and 80% in 2023.
- BEC affected 74% of organizations in 2025, "a significant increase from 2023 and 2024." The AFP says "Fraudsters primarily impersonate vendors or executives to request changes to payment instructions."
  - A separate "sources of fraud" table shows "BEC/Fraudulent email" at 70% overall, 72% for organizations under $1B revenue, and 75% for those at or above $1B. This differs from the 74% headline; it is probably a different question.
- 39% of organizations "continue to receive genuine emails that have been intercepted by fraudsters."
- Other figures from the same table:
  - "Manipulated ACH or wire transfer instructions": 33% overall.
  - Vendor or third-party compromise: 13%.
  - "Deepfake attempt (e.g., voice and/or video swapping, 'deep voice'…, vishing)": **7% overall, 5% under $1B, 8% at or above $1B**.
- In 2025, 30% of organizations were targeted by fraudulent phone calls. The AFP lists "Attempts to change bank account details" and "Vendor and customer impersonation" as phone tactics.
- Conclusion text: "Deepfake technology has not yet had a widespread direct impact on payment systems."
- Smaller firms: 48% of organizations under $1B that experienced fraud incurred a loss, and 24% of those recovered nothing. For organizations at or above $1B, the figures were 66% and 19%.
- Only 17% use AI to fight payments fraud.
- Respondent anecdotes:
  - A vendor's mailbox was taken over. Its fake invoices passed "all approval steps," and a bank-change request "was entered into the system before Treasury could confirm the same."
  - In another case, "AP called the number on the email to confirm the banking details," which is a call-back done wrongly.

**Insurer claims data:**
- Coalition 2026 Cyber Claims Report, covering 2025 (published 5 Mar 2026) — [Coalition](https://www.coalitioninc.com/announcements/2026-cyber-claims-report):
  - BEC plus funds transfer fraud (FTF) made up 58% of incidents.
  - FTF was 27% of claims, with frequency down 18% and severity down 14%, to an average of $141K.
  - BEC frequency rose 15%, but severity fell 28%, to an average of $27K.
  - 52% of FTF claims started as BEC.
  - Coalition clawed back $21.8M (average recovery $202K).
  - Businesses with more than $100M in revenue had claim frequency five times higher than smaller ones.
  - A separate claims-report page says 71% of FTF claims resulted directly from social engineering — [Coalition claims report page](https://www.coalitioninc.com/en-gb/claims-report) (search summary).
  - Average claim severity across all types fell 19% to about $116K — [Reinsurance News](https://www.reinsurancene.ws/coalition-report-finds-sharp-rise-in-ransomware-demands-as-most-businesses-refuse-to-pay/) (search summary).
- At-Bay ("Why we built InsurSec packages", 30 Jan 2026) — [At-Bay](https://www.at-bay.com/articles/why-we-built-insursec-packages/):
  - Nearly 60% of At-Bay cyber claims involve ransomware or financial fraud.
  - The average amount transferred in a fraud incident was $286K in 2024, and the largest exceeded $5M.
- A secondary summary claims that At-Bay recovered $56M in 2025, and that recovery happened 70% of the time when reported within 3 days but under 30% after 14 days. I could not verify that these come from At-Bay's 2026 report — [Digitrendz](https://digitrendz.blog/?p=172852) (search summary).

**Deepfake and vendor-impersonation cases:**
- The most-cited case is still Arup (January 2024): a finance employee made 15 transfers totalling about $25.6M after a deepfake *executive* video call. It was executive impersonation, not vendor impersonation — [Coretelligent blog](https://www.coretelligent.com/blog/the-deepfake-cfo-problem-what-voice-cloning-fraud-means-for-your-approval-processes/) (vendor blog, search summary).
- A targeted search found **no documented court case or press-reported case of a cloned *vendor* voice redirecting AP payments in 2025–2026**. Pages describing that scenario are vendor blogs with hypothetical examples, e.g., a "paving contractor… $340,000 draw" — [CallSphere blog](https://callsphere.ai/blog/a-cloned-voice-asks-accounts-payable-to-change-the-paving-contractor-s).

### Inferences
- The problem is real and money-denominated. However, the threat that pays is **ordinary email-based vendor impersonation and vendor-mailbox takeover**, not deepfakes. Pitching "deepfake-proof" leads with the smallest slice of losses: about 1% of IC3 BEC losses, and 7% of fraud-hit organizations.
- Average per-incident losses ($123K per IC3 BEC complaint; $141K for Coalition FTF; $286K for At-Bay) are big enough to justify a control. But falling FTF frequency and severity at Coalition suggests existing controls and recovery are improving, not collapsing.

### Gaps
- The full AFP 2026 report (paywalled) was not read, so the breakdown of BEC by payment method (ACH credit vs wire) and by revenue band below $1B is missing.
- Beazley claims data was not retrieved, and At-Bay's 2026 InsurSec report itself was not accessed.
- No US small-business-specific BEC loss series was found. IC3 does not break BEC down by victim company size.

## A2. How are vendor bank changes verified today, and is there a forcing function (Nacha 2026 rules, cyber-insurance conditions)?

### Takeaway
The default control is a call-back to a number on file, and almost every AFP respondent already uses it and rates it effective. The genuinely new forcing function is **Nacha's Phase 2 fraud-monitoring rule (effective 22 Jun 2026)**. It requires every non-consumer business that originates ACH payments, regardless of volume, to have risk-based processes to catch payments induced by "False Pretenses" (BEC and vendor impersonation). Insurance adds pressure through low social-engineering sublimits and call-back conditions. However, neither the rule nor the insurance conditions require a software product.

### Cited Findings
**Current controls (AFP 2026, percent of organizations)** — [AFP Key Highlights](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf):
- "Established policies to verify changes to invoices, bank deposits and contact details": 96% implemented; 58% rate it very effective and 33% effective.
- "Verifying fund transfer requests by calling an authorized contact at the payee organization using a phone number from official records, not from email": 94% implemented; 63% very effective and 31% effective.
- Senior sign-off above a threshold: 94%.
- Shared passcodes for wires: 42%.

**Nacha fraud-monitoring rules:**
- Phase 1 took effect 20 Mar 2026 for ODFIs (the originator's bank) and large originators (2023 ACH volume of 6M or more). Phase 2 rules "become effective on June 19, 2026," and parties should comply "no later than June 22, 2026" — [Nacha new rules](https://www.nacha.org/newrules).
- Phase 2 applies to "all non-Consumer Originators, TPSPs and TPSs" not covered by Phase 1, **with no volume threshold** — [Nacha Phase 2 page](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2). The rule:
  - requires "risk-based processes and procedures… reasonably intended to identify Entries suspected of being unauthorized or authorized under False Pretenses," reviewed at least annually;
  - defines False Pretenses as "the inducement of a payment by a Person misrepresenting (a) that Person's identity, (b) that Person's association with or authority to act on behalf of another Person, or (c) the ownership of an account to be credited," with BEC, vendor impersonation and payroll impersonation as examples;
  - gives "change controls regarding payment information and instructions for vendor and payroll payments" as an example control;
  - does **not** require entries to be screened one by one, and does **not** change how liability is allocated.
- The AFP flags the same rollout for treasury teams — [AFP Key Highlights](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf).
- Ramp already uses the rule in marketing: "Starting June 22, your bank will require fraud monitoring, vendor verification, and audit trails." Ramp also says "No single tool can" guarantee compliance — [Ramp AP fraud prevention page](https://ramp.com/ap-fraud-prevention) (fetched 14 Oct 2026). Ramp's description of the requirements goes further than Nacha's own text.

**Insurance conditions:**
- Social-engineering endorsements on crime policies "condition coverage on the policyholder having followed specified verification procedures," such as call-back to a known number, dual authorization, or "verifying vendor banking changes through an independent channel." Insurers may deny claims if these were skipped. Sublimits are commonly "$25,000 to $250,000" — [National Law Review / Ward and Smith, 7 Jul 2026](https://natlawreview.com/article/social-engineering-fraud-and-your-crime-policy-why-your-insurer-may-deny-claim-and).
- Brokers "now ask for higher limits" on social engineering. A $50K crime sublimit "can create a false sense of security." "Callback provisions verify payment-change requests before money moves" — [Insurance Business Canada, 10 Aug 2026](https://www.insurancebusinessmag.com/ca/news/professional-liability/brokers-are-asking-for-higher-social-engineering-fraud-limits-585525.aspx) (Canadian carrier Trisura).
- At-Bay's InsurSec premium credit is tied to an approved MDR (managed detection and response) solution. Its page does not mention any payment-verification tool being required or rewarded — [At-Bay, 30 Jan 2026](https://www.at-bay.com/articles/why-we-built-insursec-packages/).

**Bank-side account validation:**
- Early Warning's Payment Chek/Verify Payment includes Account Owner Authentication ("Validates that the individual being inquired upon can transact on the account") — [Early Warning product brief, Aug 2024](https://www.earlywarning.com/sites/default/files/2024-09/PaymentChek%20Product%20Brief%20202408-%20name%20updated.pdf) (search summary).
- Bank of America offers corporate clients Account Validation, supported by Early Warning, for pre-payment checks on vendors and contractors — [BofA, 28 Oct 2021](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2021/10/bofa-launches-account-validation-to-assist-clients-with-fraud-pr.html) (search summary).
- A Los Angeles County education office bulletin tells districts to check vendor EFT-change requests against Early Warning data — [LACOE bulletin](https://www.lacoe.edu//Portals/0/zBulletins/6707.pdf) (search summary).

### Inferences
- Nacha Phase 2 is a real "why now," and it reaches every US business paying vendors by ACH. But the rule is risk-based. A written policy, a call-back to a number on file and an approval log probably satisfy it for a small business. Banks (ODFIs) and AP platforms are the natural carriers of the compliance message, and Ramp already is one. A new vendor would be selling a "nice to have" on top of a call that costs nothing.
- Insurance call-back conditions push buyers toward a *documented procedure*, not toward a particular tool. I found no carrier that requires or discounts a payment-verification product. A possible wedge is evidence that the call-back was done properly, e.g., a timestamped record. That is a feature, not a company.
- The AFP's 94% call-back adoption is from treasury practitioners, a sample that skews toward larger firms (an inference from the sample; the full breakdown was not accessible). Adoption among firms with 10–200 employees may be lower, but I found no source measuring it.

### Gaps
- No primary carrier policy wording was retrieved (e.g., Coalition, Chubb or Travelers social-engineering endorsements).
- No data on what share of US SMBs actually do call-backs.
- No information on how ODFIs are enforcing Phase 2 on small business clients, e.g., whether banks are mandating tools or charging for account validation.

## A3. Competitors (segment, pricing, funding): is there a real US SMB/mid-market gap?

### Takeaway
There is little gap left. SMB AP platforms bundle vendor-bank verification and fraud screening, and Ramp includes "automated fraud checks" even on its **free** plan. Mid-market and enterprise are served by specialists that back their verification with $1M guarantees or indemnification (Eftsure, Trustpair, PaymentWorks). The category is consolidating: Basware closed its Trustpair acquisition on 5 Oct 2026, and TPG and Corpay took AvidXchange private in Oct 2025. Even the long tail of Xero users already has bank-change alert apps at about AUD 9/month. The thinnest remaining gap is BILL users, because BILL's documented control is a vendor confirmation email that does not block payment.

### Cited Findings
**SMB AP platforms:**
- **Ramp:**
  - Free plan: "$0/mo/user" with "Automated fraud checks." Plus: "$15/mo/user" plus a platform fee — [Ramp pricing](https://ramp.com/pricing) (fetched 14 Oct 2026).
  - Ramp's "Fraud Prevention Agent reviews every AP transaction against 60 signals." Its page headline is "Vendor banking verified before payment" — [Ramp AP fraud prevention](https://ramp.com/ap-fraud-prevention).
  - ACH ownership verification "checks account-holder information for a vendor's bank account" through bank connection or documents. Vendor edits stay pending until approval workflows finish. It does "not guarantee against fraud" — [Ramp support: vendor verification](https://support.ramp.com/vendor-verification).
- **BILL:**
  - AP and AR plans cost $49, $65 or $89 per user per month, plus custom Enterprise pricing. The pricing page lists "Automatic W-9 collection and verification," with no fraud or payment protection line. "Dual control" is listed only for Enterprise — [BILL pricing](https://www.bill.com/pricing) (fetched 14 Oct 2026).
  - After a manual bank change, BILL emails the vendor to confirm. The confirmation "isn't required to schedule payments" — [BILL help: confirm manual vendor bank change](https://vendorpayhelp.bill.com/hc/en-us/articles/360056648731) (search summary; direct fetch returned 403).
  - BILL's vendor bank-account API endpoints are MFA-protected — [BILL developer docs](https://developer.bill.com/hc/en-us/articles/209610646) (search summary).
- **Tipalti:** AP plans start at $99/month. The pricing page lists "Fraud detection," "Built-in fraud and compliance" and tax-ID validation, but does not show which plan includes them — [Tipalti pricing](https://tipalti.com/pricing/).
- **Zip** (procure-to-pay; 21 May 2026): Bank Account Verification "queries verification providers to confirm the account exists, is open, and belongs to the named account holder." US checks run against bank data networks with an RTP micro-deposit fallback, and international checks go through J.P. Morgan. It is an opt-in add-on; no price is published — [Zip blog](https://zip.com/blog/payment-risk-insights-bank-account-validation).
- **AvidXchange:** TPG and Corpay closed the take-private in Oct 2025 at about $2.2B. Corpay took about 34% for about $550M — [BusinessWire, Oct 2025](https://www.businesswire.com/news/home/20251014818572/en/Corpay-and-TPG-close-AvidXchange-Acquisition) (search summary). Corpay publishes vendor-verification content — [Corpay blog](https://www.corpay.com/en-LU/resources/blog/vendor-verification-banking-validation) (search result only).

**Specialists:**
- **Trustpair:**
  - "600+ enterprise customers. Zero fraud." Quote-only pricing, including a "Custom Access" tier with "Up to $1M liability." It has 20+ native connectors (SAP, Oracle ERP Cloud, Coupa, Kyriba, Ivalua and others); QuickBooks, NetSuite and Sage Intacct are not listed. US office in New York — [Trustpair pricing](https://trustpair.com/pricing/) (fetched 14 Oct 2026).
  - Basware completed the acquisition on 5 Oct 2026 ("first agreed in August"). Trustpair "will keep operating as an independent business." Basware has "over 6,500 customers globally" — [FinTech Global, 5 Oct 2026](https://fintech.global/2026/10/05/basware-completes-acquisition-of-trustpair/).
- **Eftsure:**
  - Pricing scales with "annual expenditure and the number of new vendors onboarded monthly." The "Eftsure Guarantee" provides "up to $1 million" if a verified payment is lost to social engineering, for customers signing after 10 Mar 2025 — [Eftsure pricing](https://eftsure.com/pricing) (search summary; direct fetch failed with a redirect loop).
  - US reference customer: the City of Milwaukee uses Eftsure for vendor onboarding and verification — [City of Milwaukee](https://city.milwaukee.gov/Comptroller/Vendor-Onboarding-and-Verification-Using-Eftsure) (search result).
- **PaymentWorks:**
  - Positions itself as "the secure front door to your ERP." "ACH payments are INDEMNIFIED by PaymentWorks… Additional $3M coverage is available."
  - Claims a "network of 1.5M+ authenticated payees" and "$325M" of fraud stopped.
  - Its case studies are higher-education and public-sector bodies (University of Tennessee, Cabarrus County, City of Vista). Partners listed include JPMorgan, Wells Fargo, BMO and Chubb. No pricing — [PaymentWorks](https://www.paymentworks.com/) (fetched 14 Oct 2026).
- **Trustmi:** $17M Series A (Jul 2023) — [TechCrunch, 26 Jul 2023](https://techcrunch.com/2023/07/26/trustmi-lands-17m-to-scale-its-payments-fraud-prevention-tech).
- **Creednz:** about $7M total funding — [CB Insights](https://www.cbinsights.com/company/creednz) (search summary).
- A search for 2026 seed or Series A rounds in vendor-payment fraud found none (search summary). This is consistent with consolidation rather than new entry, but is not conclusive.

**Account-verification infrastructure:**
- **Plaid:** "Identity Match: Match bank account ownership" is "Included" on Pay as You Go ("unlimited usage, no commitments upfront"). No per-call prices are published — [Plaid pricing](https://plaid.com/pricing/).
- **Early Warning and banks:** see A2.

**Long-tail and Xero apps:**
- **VendorAlert:** "When a contact's bank details change in Xero, alert the people you choose." AUD 9 per month per organization; listed July 2026; one review — [Xero App Store](https://apps.xero.com/us/function/payments/app/vendoralert).
- **XBert** alerts on contact bank changes for Xero, MYOB and QuickBooks Online — [XBert help](https://support.xbert.io/en/articles/11069292-contact-bank-account-changed) (search summary).

**Deepfake and impersonation-defense entrants** (crowding on the "AI impersonation" framing):
- **imper.ai:** about $22M Series A, led by Redpoint and Battery, after a $6.5M seed six months earlier. Real-time impersonation checks across Zoom, Teams, Slack, WhatsApp and Google Workspace — [Calcalist, 4 Dec 2025](https://www.calcalistech.com/ctechnews/article/rk9nmmjgbl).
- **Kibu:** $10.5M seed, with "quorum consensus for approvals like wire transfers." Targets defense contractors and family offices. Byline May 2026; page metadata says Aug 2026 — [TAMradar](https://www.tamradar.com/funding-rounds/kibu-seed-10-5m).
- **GetReal Security:** $17.5M Series A in 2025 — [SecurityWeek](https://www.securityweek.com/getreal-security-raises-17-5-million-to-tackle-gen-ai-threats/amp/) (search summary).

### Inferences
- **Why incumbents haven't "served" the segment: they have.** SMBs that pay through Ramp get this free. Mid-market ERP users have Eftsure, Trustpair, PaymentWorks and Zip. Xero micro-businesses have AUD 9/month alert apps. Two segments look thinly protected:
  1. **BILL users.** The control is a confirmation email that does not block payment, and dual control is Enterprise-only. But BILL can close this in a product cycle, and MFA-protected bank endpoints may limit what a third-party app can read. The latter is inferred from a search snippet.
  2. **Businesses paying straight from a bank portal or QuickBooks with no AP tool.** Their bank, now obliged under Nacha Phase 2, is the natural provider, through Early Warning-style validation.
- Incumbents make **financial guarantees**: up to $1M at Trustpair and Eftsure; ACH indemnification plus $3M optional cover at PaymentWorks. A solo founder cannot match these, and buyers may now expect them.
- **Willingness-to-pay signals are weak** for a standalone SMB tool. The closest price anchors are free (Ramp Free), bundled (BILL $49–89/user, with no fraud line item) and AUD 9/month (VendorAlert).

### Gaps
- Not verified: Medius, Coupa Supplier Portal/onboarding, Paymode-X (Bottomline), Bottomline's own vendor-verification pricing, Nuvei (probably not relevant, since it is a merchant acquirer), and Melio/QuickBooks Bill Pay vendor verification.
- Eftsure's US pricing and US customer count are unknown. Trustpair's acquisition price is undisclosed.

## B1. How large is the IBM i installed base, and how bad is the skills gap?

### Takeaway
No official current count exists. The best estimates are **about 100,000–150,000 companies worldwide**: IBM said "at least 100,000… could be as high as 300,000" in 2018, and IT Jungle estimated 120,000–150,000 in 2020. The US share is unknown. Skills overtook security as the #1 concern (69%) in Fortra's 2026 survey, and 73% of respondents run in-house-written applications, which is exactly the code that goes undocumented.

### Cited Findings
- **Installed-base estimates** (all IT Jungle; search summaries, not fetched individually):
  - "just north of 100,000" (2010) — [IT Jungle 2010](https://www.itjungle.com/tfh/tfh101810-story01.html).
  - IBM said "over 150,000 companies in more than 115 countries" (2012) — [IT Jungle 2012](https://itjungle.com/tfh/tfh080612-story02.html).
  - Steve Will (IBM) in 2018: "at least" 100,000, "could be as high as 300,000" — [IT Jungle, 23 May 2018](https://www.itjungle.com/2018/05/23/ibm-i-finds-a-youthful-swagger-down-in-texas/).
  - "anywhere from 120,000 to 150,000 unique IBM i shops" — [IT Jungle, 10 Feb 2020](https://www.itjungle.com/2020/02/10/the-state-of-the-ibm-i-installed-base-part-1/).
  - IT Jungle's 2022 analysis used a dataset of about 20,000–30,000 actual customers, which it called the active part of the base — [IT Jungle, 14 Feb 2022](https://www.itjungle.com/2022/02/14/the-state-of-the-ibm-i-base-2022-part-one/).
- **Fortra 2026 survey** (315 respondents, fielded late 2025):
  - Skills 69% (up from 60% in 2025), security 64%, application modernization 62%, HA/DR 47%.
  - The AI concern figure differs by source: **42% per IT Jungle versus 47% per TechChannel**.
  - 73% use in-house-written applications.
  - Sources: [IT Jungle, 2 Feb 2026](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/); [TechChannel, 27 Jan 2026](https://techchannel.com/skills-gap/fortra-survey-2026/).
- IBM's counter-narrative from Steve Will: "It's relatively easy to take a computer professional and teach them how to do things on IBM i." He also points to Bob as a tool that helps "anybody who's smart and wants to learn it" — [IT Jungle, 2 Feb 2026](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/).
- **Vendor claims on retirement:**
  - "Over 72% of IBM i developers are over 50" (citing a 2025 Procern analysis); about 18,000 retirements per year versus about 3,600 replacements; about 30 open full-time RPG roles nationwide — [VIRTUTEM playbook, 2026](https://www.virtutem.com/rpg-developer-retirement-playbook/) (a managed-services vendor; figures unverified).
  - The average RPG developer is "mid-to-late fifties" — [Profound Logic, 31 Mar 2026](https://www.profoundlogic.com/ibm-i-staffing-cliff-developer-retirement-agentic-coding/) (vendor).
  - ASNA projected an average RPG programmer age of 70 by 2025 — [ASNA white paper](https://www.asna.com/es/white-paper/ibm-i-crisis-decade) (vendor projection).

### Inferences
- The buyer population is large in absolute terms but unmeasured. The "active" pool of perhaps 20,000–30,000 companies is the realistic reach. I do not know how many are US mid-market manufacturers, distributors or insurers.
- The skills pain is well evidenced. Whether it turns into *documentation* spending, rather than hiring, training, managed services or Bob, is the open question.

### Gaps
- No current US count of IBM i companies, and no industry split (manufacturing, distribution, insurance). The Fortra demographics page returned 403.
- No source found on how many mid-market insurers run policy or claims systems on IBM i.

## B2. What do IBM (Bob / watsonx Code Assistant for i), partner tools and AI startups already do? Who captures business intent, not just code structure?

### Takeaway
In 2026 the gap the earlier note identified ("nobody documents business intent") closed substantially:
- IBM's **Bob Premium Package for i** went GA in June/July 2026, starting at USD 40. It explains RPG and COBOL and generates technical documentation.
- **Fresche X-Analysis AI** (brief dated Jan 2026) markets "AI-Powered Code Analysis: Extract and document business rules."
- **ARCAD Discover** adds AI documentation.
- Most damaging: on 10 Aug 2026, **Profound Logic launched an "IBM i Documentation Service"**, a managed engagement producing "technical" and "business-facing documentation." That is close to candidate B as specified.

What none of them explicitly advertises is **structured interviews with the retiring person** reconciled against code. Only Hypercubic does that ("HyperTwin"), and only for mainframes.

### Cited Findings
**IBM Bob, Premium Package for i:**
- IBM announced general availability on 9 Jul 2026 — [IBM announcement](https://www.ibm.com/new/announcements/introducing-the-ibm-bob-premium-package-for-i). TechChannel reported a GA date of 24 Jun 2026 — [TechChannel, 26 May 2026](https://techchannel.com/artificial-intelligence/ibm-bob-premium-package-for-i-release-date/). The sources conflict on the exact date.
- Capabilities per IBM:
  - works on live systems ("read, write and compile code");
  - explains complex RPG and COBOL and "creates technical documentation";
  - generates RPG, CL, COBOL and DDS;
  - converts fixed-format RPG to free-format;
  - generates unit tests;
  - offers a database mode.
- A customer said Bob "was able to list and label all the inputs/outputs and file structures" in large undocumented programs.
- IBM's page does **not** name business-rule extraction, application discovery or data-flow analysis.
- TechChannel adds that the package includes skills for "Creating technical documentation from source code," and curated documentation going back to the System/36 era.
- Pricing — [IBM Bob pricing](https://www.ibm.com/products/ai-coding-agent/pricing) (fetched 14 Oct 2026):
  - Premium Package for i "Starting at USD 40."
  - Plans: Pro from $20, Pro+ from $60, Ultra from $200 "per instance," with 50, 180 and 1,000 Bobcoins respectively.
  - Bobcoins are valued at $0.50 each, per TechChannel.
- A third-party blog claims Premium includes "business rule extraction" and "modernization planning" modes — [Nick Litten blog](https://www.nicklitten.com/ai-for-legacy-rpg-pros-cons-and-how-ibm-bob-closes-the-skills-gap/) (search summary; not confirmed by IBM).

**Fresche X-Analysis AI** (solution brief, PDF dated 12 Jan 2026) — [Fresche brief](https://freschesolutions.com/wp-content/uploads/2025/09/solution-brief-x-analysis-ai-01-2026.pdf):
- Features: "AI-Powered Code Analysis: Extract and document business rules and logic from RPG, COBOL, and Synon applications," plus automated documentation, impact analysis, data-model extraction and quality metrics.
- Positioning: "Understand Business Logic: Use AI to extract and document critical business rules and processes, improving collaboration between IT and business teams."
- Fresche says it is trusted by "2,200+ companies."
- No price is published. A search summary says X-Analysis is now sold by annual subscription with a free trial — [X-Analysis Advisor page](https://freschesolutions.com/products/x-analysis-advisor-2/) (search summary); [trial page](https://go.freschesolutions.com/try-the-x-analysis-suite-free) (fetched; no terms).

**ARCAD Discover** ("Global application analysis with an AI interface"): features listed are "Automated Documentation," "Embedded and Secure AI" and "Multi-Technology." No pricing, and no business-rule detail on the page — [ARCAD](https://www.arcadsoftware.com/arcad/news-events/arcad-press-articles/arcad-discover-global-application-analysis-with-an-ai-interface/) (page links an IT Jungle article from 10 Feb 2025).

**Profound Logic:**
- "IBM i Documentation Service" (10 Aug 2026), described as "a managed engagement" — [Profound Logic blog](https://www.profoundlogic.com/blog/ibm-i-documentation-service-capturing-tribal-knowledge/):
  - CoderFlow is configured "inside a customer's own environment" with "real access" (compiling, querying DB2 schemas).
  - Deliverables are technical documentation (purpose, logic paths, data structures, dependencies, edge cases) plus "business-facing documentation" for non-RPG readers.
  - The customer's developers review and extend the output.
  - Interviews are not mentioned, and pricing is not published.
- Profound's earlier piece (31 Mar 2026) pitches agents that "identify business rules, map dependencies, and generate documentation" while veterans can still validate — [Profound Logic](https://www.profoundlogic.com/ibm-i-staffing-cliff-developer-retirement-agentic-coding/).
- Its site offers CoderFlow, "Profound AI" (described as a "gift" to the community) and AI Foundations training — [Profound Logic home](https://www.profoundlogic.com/).

**VIRTUTEM** (IBM i/Infor LX managed services for North American manufacturers and distributors):
- Offers a "complimentary IBM i staffing risk review."
- Says Bob can document RPG programs "in hours rather than weeks," but that Bob "is not designed to map institutional knowledge across an entire environment."
- Recommends documenting "one critical process per month" — [VIRTUTEM](https://www.virtutem.com/rpg-developer-retirement-playbook/).

**Mainframe-focused AI and services firms** (none mention IBM i or RPG on their home pages):
- **Hypercubic:** "agentic AI platform for mainframe operations and modernization." HyperDocs documents "COBOL programs, data flows, dependencies, and business logic." **HyperTwin** captures how engineers "debug and operate legacy systems" and targets "Experts about to retire." It reports "$5.3 million in seed funding, led by CIV" — [Hypercubic](https://www.hypercubic.ai/).
- **Swimm** has pivoted to agentic modernization *services*: "Fixed price per stage"; deliverables include "extracted business logic"; "On-premise deployment… air-gapped"; SOC 2/ISO 27001; mainframe COBOL/JCL/PL/I — [Swimm](https://swimm.io/).
- **Mechanical Orchard** (Imogen) "rewrites legacy systems into modern, cloud-ready code"; its testimonials come from Fortune 20/100/500 companies — [Mechanical Orchard](https://www.mechanical-orchard.com/).
- **CloudFrame** does COBOL-to-Java, and its Atlas product produces knowledge graphs plus "BRDs & HLDs" — [CloudFrame](https://www.cloudframe.com/).
- **TSRI** offers automated conversion and "UML code-level documentation" for government and enterprise; RPG is not listed — [TSRI](https://tsri.com/).
- **Astadia** ("now part of Amdocs") covers mainframe technologies; IBM i is not listed — [Astadia](https://www.astadia.com/).

### Inferences
- **"AI documents what the code does" is now commoditized** on IBM i. Bob costs from USD 40, X-Analysis AI is sold to a 2,200-company base, ARCAD bundles it, and Profound sells it as a done-for-you service. A new entrant cannot win on generating documentation.
- **Residual whitespace**, inferred from what vendors do *not* advertise:
  1. structured capture of the retiring person's tacit operational knowledge (why rules exist, year-end and EDI quirks, manual workarounds), reconciled with code and marked as verified or unverified;
  2. a price and format suitable for small shops with 1–5 IBM i staff, which may not buy Fresche or Profound engagements (unverified, since neither publishes prices);
  3. vendor neutrality, i.e., not a lead-in to a conversion sale.
  Hypercubic's HyperTwin shows the interview/operations-capture idea is fundable on mainframes, and it or Profound could move into it on IBM i.
- Bob at USD 40 is as much a **cost input** for a service business as a competitor. A dossier team can run Bob or Claude inside the customer's environment.

### Gaps
- Not verified: Mobilize.Net/Asymbix, Kyndryl, Infosys/TCS/HCL IBM i practices, Bloop (503), Bluestone, and any IBM i-specific AI startup.
- No prices for X-Analysis AI, ARCAD Discover, or the Profound Documentation Service.
- No independent accuracy benchmarks of Bob or X-Analysis on RPG business-rule extraction.

## B3. How do mid-market IBM i shops buy, and what do they pay for consultants (US and India)?

### Takeaway
IBM i shops buy through long-standing IBM business partners and IBM i-focused MSPs (IBM cited 200+ in 2014). US contract RPG work is advertised at roughly $48–75/hour, mostly $55–65. Offshore India IBM i roles are posted at $14–22/hour by the same US staffing firms. The India labour advantage is therefore real but **already used by incumbents and staffing firms**.

### Cited Findings
**Buying channel:**
- IBM's Doug Balog said there were "more than 200 MSPs focused on i" and "a shift of i clients looking to go to MSPs." The IBM i MSP business is "almost entirely" IBM business partners. One example is KS2 Technologies (Texas, about 80 mostly small IBM i customers) — [IT Jungle, 10 Nov 2014](https://www.itjungle.com/2014/11/10/tfh111014-story02/) (dated).
- Customers may pick or switch their IBM business partner — [IT Jungle, 2009](https://itjungle.com/fhg/fhg120909-story03.html) (search summary).
- Fresche and Profound both sell into this channel, and VIRTUTEM is an Infor partner offering IBM i managed services — [VIRTUTEM](https://www.virtutem.com/rpg-developer-retirement-playbook/).

**US contract rates (advertised postings, 2025–2026):**
- San Diego: $48–60/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/california/job-488137).
- Woonsocket, RI (senior, claims platform): $60–75/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/rhode-island/job-504418/).
- Remote US: $60–65/hr — [Remotive/American IT Systems](https://remotive.com/remote/jobs/software-development/as-400-rpg-developer-5734788).
- Keller, TX: $55–60/hr — [SkillUp listing](https://explore.skillup.org/all/open-jobs/e59153e2ab5466883a881b310418f96ffeb9726d) (search summary).
- UK median RPG contract rate: about £450/day — [ITJobsWatch](https://www.itjobswatch.co.uk/contracts/uk/rpg.do).
- VIRTUTEM claims senior RPG pay of about $105K versus $125K+ for .NET developers — [VIRTUTEM](https://www.virtutem.com/rpg-developer-retirement-playbook/).

**India offshore rates:**
- Offshore RPG programmer (2026): $18–22/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/texas/job-558346/).
- iSeries developer, India/Hyderabad (2025): $14–17/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/pennsylvania/job-426597); [Insight Global](https://jobs.insightglobal.com/find_a_job/georgia/job-395755).
- All of these are search summaries of postings, not rate surveys.

### Inferences
- A useful anchor, my arithmetic from the postings above: two weeks (80 hours) of a US contract RPG developer at $60/hr costs about $4,800, versus about $1,600 at $20/hr offshore. A fixed-fee dossier for a bounded scope therefore has room in roughly the low thousands of dollars. That is a hypothesis to test, not observed willingness to pay.
- Because buying runs through trusted partners, **partnering with IBM i MSPs and business partners as a white-label "documentation bench"** may beat selling direct. The partner already holds system access and trust. Several partners (Profound, Fresche) are now competitors, though, so the targets are the smaller MSPs and ERP-specific partners.

### Gaps
- No 2024–2026 data on IBM i MSP counts or channel share. No published prices for any IBM i documentation engagement.
- No data on how IBM i *insurers* buy, as distinct from manufacturers and distributors.

## Both candidates: buyer population, willingness-to-pay signals, why incumbents haven't served, credibility barriers for an unknown India-based solo vendor

### Takeaway
Candidate A has a larger and newly regulated buyer population. But willingness to pay for a standalone tool is undercut by free and bundled features, and trust requirements are severe: it touches bank details, buyers expect guarantees, and verification links can look like phishing. Candidate B has a smaller, older and more conservative population. But it has a hard deadline (retirements), a service-shaped deliverable where India costs and AI tools matter, and trust can be borrowed through IBM i partners. Its incumbents moved into the space in 2026.

### Cited Findings
**Candidate A:**
- Buyer population: every US "non-Consumer Originator" of ACH is under Nacha Phase 2 from 22 Jun 2026 — [Nacha](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2).
- Willingness-to-pay signals:
  - Ramp Free includes automated fraud checks — [Ramp pricing](https://ramp.com/pricing).
  - VendorAlert charges AUD 9/month — [Xero App Store](https://apps.xero.com/us/function/payments/app/vendoralert).
  - Specialists bundle $1M guarantees or indemnification — [Trustpair](https://trustpair.com/pricing/); [Eftsure](https://eftsure.com/pricing) (search summary); [PaymentWorks](https://www.paymentworks.com/).
  - Loss sizes justify a control: FTF averages $141K at Coalition and $286K at At-Bay — [Coalition](https://www.coalitioninc.com/announcements/2026-cyber-claims-report); [At-Bay](https://www.at-bay.com/articles/why-we-built-insursec-packages/).
  - Insurance sublimits of $25K–$250K leave firms under-insured — [National Law Review, 7 Jul 2026](https://natlawreview.com/article/social-engineering-fraud-and-your-crime-policy-why-your-insurer-may-deny-claim-and).

**Candidate B:**
- Buyer population: roughly 100,000–150,000 IBM i companies worldwide (estimate), with about 20,000–30,000 "active" — [IT Jungle 2020](https://www.itjungle.com/2020/02/10/the-state-of-the-ibm-i-installed-base-part-1/); [IT Jungle 2022](https://www.itjungle.com/2022/02/14/the-state-of-the-ibm-i-base-2022-part-one/).
- Willingness-to-pay signals:
  - Profound and Fresche have productized documentation, and VIRTUTEM offers a free staffing-risk review as lead generation — sources in B2.
  - US contract rates of $48–75/hr — sources in B3.
  - No prices found for documentation services.

### Inferences
- **Credibility barriers, candidate A:**
  - A solo India-based company asking US vendors to enter bank details through its link looks exactly like the fraud it claims to stop.
  - US finance teams will ask for SOC 2, a US entity, insurance and a guarantee.
  - The core check (account ownership) depends on Plaid, Early Warning or bank data, so there is no data moat.
- **Credibility barriers, candidate B:**
  - IBM i shops guard their source code.
  - The answer is to deliver *inside the customer's environment* (as Profound does) or through their MSP, under NDA, with a US entity.
  - Offshore India IBM i work is already common (Insight Global India postings), so "India-based" is normal in this market rather than disqualifying. The founder's lack of IBM i expertise is the larger barrier.
- **Why incumbents haven't served the segment:**
  - For A, they have; see A3.
  - For B, until 2026 the tool vendors sold conversion and ALM. They are now moving down into documentation (Fresche AI, Bob, Profound service). The only segment possibly left uncovered is very small shops plus interview-based tacit-knowledge capture.

### Gaps
- No primary willingness-to-pay data (interviews, pricing pages, win/loss) exists for either candidate. Reddit and LinkedIn were not accessed.

## Disconfirming evidence (actively trying to kill each candidate)

### Takeaway
Candidate A fails several kill tests: the core control is cheap and already near-universal, the feature is free inside the leading SMB AP tool, the "deepfake" thesis is about 1% of losses, and incumbents offer financial guarantees. Candidate B survives but is badly wounded. Its central insight ("nobody documents business intent") was contradicted in 2026 by IBM, Fresche and especially Profound's done-for-you service. What survives is a narrower wedge: interview-based knowledge capture for small shops, delivered with or through partners.

### Cited Findings
**Against candidate A:**
1. 94% of AFP respondents already verify through call-back to an official number, and 63% rate it "very effective." 96% have bank-change verification policies — [AFP Key Highlights](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf).
2. Deepfake share is small: 7% of fraud-hit organizations reported a deepfake attempt (AFP), and AI-linked BEC losses were about $30.3M of $3.05B (IC3) — [AFP](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf); [IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf).
3. Coalition saw FTF frequency fall 18% and severity fall 14% in 2025 — [Coalition, 5 Mar 2026](https://www.coalitioninc.com/announcements/2026-cyber-claims-report).
4. Ramp Free includes "Automated fraud checks." Ramp, Zip (May 2026) and Tipalti bundle verification — [Ramp](https://ramp.com/pricing); [Zip](https://zip.com/blog/payment-risk-insights-bank-account-validation); [Tipalti](https://tipalti.com/pricing/).
5. Consolidation: Basware–Trustpair (5 Oct 2026) and TPG/Corpay–AvidXchange (Oct 2025) — [FinTech Global](https://fintech.global/2026/10/05/basware-completes-acquisition-of-trustpair/); [BusinessWire](https://www.businesswire.com/news/home/20251014818572/en/Corpay-and-TPG-close-AvidXchange-Acquisition).
6. Incumbents offer guarantees and indemnification: up to $1M at Trustpair and Eftsure, and indemnified ACH at PaymentWorks — sources in A3.
7. The Nacha rule is risk-based, requires no per-entry screening and does not change liability. It does not mandate a tool — [Nacha](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2).
8. Well-funded entrants own the "AI impersonation" framing: imper.ai (about $22M Series A), Kibu ($10.5M seed), GetReal ($17.5M) — sources in A3.

**Against candidate B:**
1. Profound Logic's IBM i Documentation Service (10 Aug 2026) is a near-identical managed offering from a long-established IBM i vendor — [Profound Logic](https://www.profoundlogic.com/blog/ibm-i-documentation-service-capturing-tribal-knowledge/).
2. Fresche X-Analysis AI already markets AI business-rule extraction to "2,200+ companies" — [Fresche brief, Jan 2026](https://freschesolutions.com/wp-content/uploads/2025/09/solution-brief-x-analysis-ai-01-2026.pdf).
3. IBM Bob Premium Package for i (GA Jun/Jul 2026, from USD 40) "creates technical documentation" — [IBM](https://www.ibm.com/new/announcements/introducing-the-ibm-bob-premium-package-for-i); [IBM pricing](https://www.ibm.com/products/ai-coding-agent/pricing).
4. IBM frames the skills gap as solvable by training plus Bob, which weakens the urgency of documentation-only spend — [IT Jungle, 2 Feb 2026](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/).
5. Offshore India IBM i labour at $14–22/hr is already sold by US staffing firms, so it is not a unique advantage — [Insight Global](https://jobs.insightglobal.com/find_a_job/texas/job-558346/).
6. Hypercubic already builds retiring-expert capture (HyperTwin) for mainframes with $5.3M seed funding and could extend to IBM i — [Hypercubic](https://www.hypercubic.ai/).
7. The market size is unmeasured, and the buyer base is shrinking or ageing (estimates only) — [IT Jungle 2020](https://www.itjungle.com/2020/02/10/the-state-of-the-ibm-i-installed-base-part-1/).

### Inferences
- A's kill tests are structural: a free substitute, a bundled substitute, and a trust requirement the founder cannot meet. B's kill tests are competitive: well-placed incumbents. Competitive kill tests can sometimes be routed around by segment, here small shops, or by channel, here partnering with MSPs.

### Gaps
- No customer-voice evidence (reviews, forums) was gathered for either candidate in this run. Reddit was previously blocked, and the search budget is exhausted.

## First-customer targets for the stronger candidate (B): 20 verifiable channels

### Takeaway
Below are 20 named, verifiable places to find first IBM i buyers: COMMON plus the 19 US local IBM i user groups COMMON lists. Additional partner targets follow. These are *channels* to reach IT managers at member companies. Individual company names were not verified in this run.

### Cited Findings
**Target #1, COMMON (the national IBM i user association):**
- NAViGATE at IBM TechXchange, 26–29 Oct 2026, Atlanta. COMMON's own listing elsewhere gives 26–30 October.
- iPOWER 26, 17–18 Nov 2026.
- Source: [COMMON](https://www.common.org/).

**The 19 US local user groups listed by COMMON** — [COMMON LUG directory](https://www.common.org/lug/local-user-groups/):

| # | Group | Location | Website |
|---|---|---|---|
| 2 | Orange County Educational Advancement Network (OCEAN) | Costa Mesa, CA | https://ougsc.memberclicks.net/ |
| 3 | Fairfield Application System User Group | Wilton, CT | http://www.fasug.org/ |
| 4 | Omni Users Group | Oak Brook, IL | http://www.omniuser.org/ |
| 5 | STATUS | Ft. Wayne, IN | http://www.statususer.org/ |
| 6 | Kentuckiana Small Systems Association | Louisville, KY | http://www.kssa.net/ |
| 7 | Southeast Michigan iSeries Users Group | Rochester, MI | http://www.semiug.org/ |
| 8 | West Michigan IBM i Users Group | Grand Rapids, MI | http://www.wmsug.net/ |
| 9 | QUSER | St. Paul, MN | http://www.quser.org/ |
| 10 | Gateway/400 Group | St. Louis, MO | http://www.gateway400.org/ |
| 11 | New Hampshire Midrange Users Group | Peterborough, NH | https://www.nhmug.org/ |
| 12 | Midrange Users Group of Western New York | Buffalo, NY | http://www.mugwny.org/ |
| 13 | Long Island Systems Users Group (LISUG) | Syosset, NY | http://www.lisug.org/ |
| 14 | TriState Midrange Users Group | West Chester, OH | http://www.tsmug.org/ |
| 15 | New England Midrange Users Group | Harrisville, RI | http://www.nemug.com/ |
| 16 | IMUG Midrange Users Group | Nashville, TN | http://www.imugtn.org/ |
| 17 | Metro Midrange Systems Association | Irving, TX | http://www.metromidrange.org/ |
| 18 | Greater Salt Lake Midrange User Group | Salt Lake City, UT | (no URL listed) |
| 19 | Mid-Atlantic Group of IBM i Collaborators (MAGIC) | Virginia Beach, VA | http://www.magic-ug.org/ |
| 20 | Wisconsin Midrange Computer Professional Association | Elm Grove, WI | http://www.wmcpa.org/ |

**Alternate and partner targets (verifiable but not counted in the 20):**
- KS2 Technologies: a Texas IBM i business partner and MSP serving mostly small IBM i shops, as of 2014 — [IT Jungle](https://www.itjungle.com/2014/11/10/tfh111014-story02/).
- VIRTUTEM: Infor LX/BPCS managed services for North American manufacturers and distributors; a possible partner or competitor — [VIRTUTEM](https://www.virtutem.com/rpg-developer-retirement-playbook/).
- Companies posting US RPG contract roles through staffing firms (e.g., the Insight Global San Diego and Woonsocket, RI postings), which signal current staffing pain — [Insight Global](https://jobs.insightglobal.com/find_a_job/california/job-488137).

### Inferences
- The best first pitch is a talk offer to user-group program chairs ("What breaks when your last RPG developer retires: a 30-minute risk triage"), followed by an offer of a fixed-scope pilot to attendees.
- The Midwest and Great Lakes groups (IL, IN, KY, MI, MN, MO, OH, WI) likely skew toward manufacturing and distribution. This is an inference from geography and was not verified.
- Small IBM i MSPs (like KS2) are the white-label channel. Avoid pitching Profound and Fresche partners, who now compete.

### Gaps
- Member counts and meeting calendars for each group were not checked. The midrange.com mailing lists, LinkedIn IBM i groups and r/IBMi were not accessed in this run.
- AFP chapters and AP communities were not compiled, because A is rejected.

## Narrowest MVP (2–8 weeks, solo non-engineer with AI coding tools) and a 14-day experiment with kill criteria

### Takeaway
For B, do **not** build a documentation tool, since Bob, X-Analysis and ARCAD exist. Build a **"Retirement Risk Dossier" service-plus-pipeline** for one bounded scope (e.g., the top 25 programs or one business process). It combines Claude-structured interview capture with code cross-referencing, and a contract IBM i developer validates every rule. Run the 14-day experiment *before* building most of it. For A, if the founder still wants to test it, a 14-day kill test is included, but the evidence says reject.

### Cited Findings
- Cost inputs:
  - IBM Bob Premium Package for i starts at USD 40 — [IBM pricing](https://www.ibm.com/products/ai-coding-agent/pricing).
  - Offshore IBM i developers are posted at $14–22/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/texas/job-558346/).
  - US contract RPG costs $48–75/hr — [Insight Global](https://jobs.insightglobal.com/find_a_job/rhode-island/job-504418/).
- Trust patterns from incumbents:
  - Profound runs its tooling "inside a customer's own environment" — [Profound Logic](https://www.profoundlogic.com/blog/ibm-i-documentation-service-capturing-tribal-knowledge/).
  - Swimm offers air-gapped, on-premise deployment and "Fixed price per stage" — [Swimm](https://swimm.io/).
- Content model: document "one critical process per month," covering what it does, what breaks it, and what cannot change — [VIRTUTEM](https://www.virtutem.com/rpg-developer-retirement-playbook/). Record SME sessions and have an IBM i developer validate AI output because tools "can be confidently wrong" — PromptedDev, cited in the earlier note `it_msp_security_data.md`.

### Inferences
**B — narrowest MVP (my design; prices are hypotheses to test, not market data):**
- **Scope:** one business process (e.g., order-to-invoice or month-end close) or the 25 riskiest programs.
- **Inputs:**
  1. A source export: the customer or their MSP runs a provided script to copy RPG/CL/DDS members to stream files, or IBM Bob or Claude is run inside the customer's VPN so no code leaves.
  2. A job scheduler listing (WRKJOBSCDE or the third-party scheduler's export).
  3. 2–3 recorded 60–90 minute sessions with the retiring developer, using a structured question bank (period-end jobs, EDI partners, magic constants, "what do you fix by hand", "what must never be touched").
- **Pipeline (buildable with Claude Code in 2–4 weeks):**
  - Parse source with simple pattern rules (CALL/CALLP, F-specs and file usage, hard-coded constants, date and period logic).
  - Build a program and call inventory.
  - Have an LLM summarize each program and align transcript statements to programs and files.
  - Output an HTML/PDF dossier containing:
    - a **business-rule register** (rule; code location; interview evidence; confidence; "verified by [developer] on [date]");
    - a **calendar-risk list** (year-end and period-end jobs);
    - an **integration map** (EDI, FTP, external files);
    - a **"what breaks if…" page**.
- **Human layer:** one contract IBM i validator (India, about $15–25/hr range per postings) checks every rule marked high-impact. The founder runs interviews and project management.
- **Offer to test:** a fixed-fee pilot. My hypothesis is about $2,500–$5,000 for the bounded scope, anchored on 80 hours of US contractor time (about $4,800). Delivery is under NDA by a US LLC, with a data-deletion attestation, and run in the customer's or MSP's environment where required.

**B — 14-day experiment:**
- Days 1–3:
  - Recruit one experienced IBM i validator, ideally US-based or ex-US, as advisor or contractor.
  - Produce a sample dossier from public RPG code and a mock interview.
  - Publish a one-page offer.
- Days 2–10:
  - Email program chairs of the 19 LUGs offering a talk.
  - Contact 10–15 small IBM i MSPs and business partners with a white-label offer.
  - Send 100–150 LinkedIn messages to IT managers whose profiles list IBM i/AS400/RPG.
- Days 5–14: run discovery calls, ask for a paid pilot, and ask what they already use (Bob, X-Analysis, Profound, nothing).
- **Kill criteria (stop if any is true at day 14):**
  1. Fewer than 8 discovery calls with IBM i decision-makers or MSP owners.
  2. Fewer than 3 calls confirm a named key-person departure within 24 months *and* no existing documentation tool or service in use.
  3. At least 50% of qualified calls say Bob, X-Analysis or Profound already covers the need.
  4. Zero prospects willing to grant code access (directly or via their MSP) under NDA for a paid pilot, or to sign an LOI.
  5. No MSP or partner willing to co-deliver a pilot.
- **Continue criteria:** at least 2 paid pilots at or above $2,500, or 1 paid pilot plus 1 MSP letter of intent.

**A — optional 14-day kill test (only if the founder insists):**
- Target BILL users and businesses without an AP tool, pitching a "Nacha False-Pretenses evidence pack": a documented call-back workflow plus a timestamped log.
- **Kill if:**
  - fewer than 10 of 40 SMB controllers or fractional CFOs report having no call-back or verification beyond what BILL or Ramp provides; or
  - none will pay $50 or more per month; or
  - their bank already offers account validation.
- The prior evidence (Ramp Free, AFP 94% call-back adoption, VendorAlert at AUD 9/month) makes passing unlikely.

### Gaps
- The extraction script and the in-environment deployment approach have not been validated with a real IBM i shop or MSP. Whether customers will let any third party run AI on their source is the key unknown.
- No evidence was found on fixed-fee price acceptance for IBM i documentation.

## Verdicts

### Takeaway
- **(A) Vendor bank-change / payee verification for US SMB and mid-market AP: REJECT.**
- **(B) IBM i system dossier: ADVANCE WITH CONDITIONS.** It is the stronger of the two but low-to-medium confidence. It is materially weakened by Profound Logic's August 2026 documentation service, Fresche X-Analysis AI and IBM Bob for i. It should take the last shortlist slot only if the 14-day experiment passes.

### Cited Findings
**Reasons for rejecting A:**
- The core control is near-universal and rated effective: 94% use call-backs and 63% rate them "very effective" — [AFP](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf).
- The feature is free or bundled in SMB AP tools — [Ramp pricing](https://ramp.com/pricing); [Zip](https://zip.com/blog/payment-risk-insights-bank-account-validation).
- Specialists offer $1M guarantees or indemnification and are consolidating into suites — [Trustpair](https://trustpair.com/pricing/); [PaymentWorks](https://www.paymentworks.com/); [FinTech Global](https://fintech.global/2026/10/05/basware-completes-acquisition-of-trustpair/).
- The deepfake share of losses is about 1% — [IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf).
- The Nacha Phase 2 forcing function is real but risk-based and tool-agnostic — [Nacha](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2).

**Reasons for advancing B only with conditions:**
- The skills pain is #1 (69%) and code is mostly in-house (73%) — [TechChannel](https://techchannel.com/skills-gap/fortra-survey-2026/).
- The labour-cost and tool-cost structure suits an India-based service: $14–22/hr offshore versus $48–75/hr US, and Bob from USD 40 — sources in B3 and B2.
- Incumbents are now present — [Profound Logic](https://www.profoundlogic.com/blog/ibm-i-documentation-service-capturing-tribal-knowledge/); [Fresche](https://freschesolutions.com/wp-content/uploads/2025/09/solution-brief-x-analysis-ai-01-2026.pdf); [IBM](https://www.ibm.com/new/announcements/introducing-the-ibm-bob-premium-package-for-i).

### Inferences
**Conditions for B:**
1. **Reposition** from "AI documentation" (commoditized) to "retiring-expert knowledge capture plus validated runbook," aimed at small IBM i shops and delivered with or through small MSPs.
2. **Recruit IBM i credibility** (an advisor or validator with a verifiable US IBM i track record) before outbound selling.
3. **Use a no-code-exfiltration delivery model**: run in the customer's or MSP's environment, under NDA, through a US entity.
4. **Pass the 14-day kill criteria** above.
5. **Re-check monthly** whether Profound or Fresche publish low fixed-fee pricing, or whether Hypercubic extends to IBM i. Either would remove the remaining wedge.

**For A:** the only defensible residue is a feature (call-back evidence logging for BILL or bank-portal users), not a venture-scale company for this founder. Do not shortlist it.

### Gaps
- Both verdicts rest on desk research without customer interviews.
- B's verdict is the more sensitive to missing data: prices of Profound and Fresche services, the share of very small IBM i shops, and whether shops will let outsiders run AI on their source. These are exactly what the 14-day experiment is designed to answer.
