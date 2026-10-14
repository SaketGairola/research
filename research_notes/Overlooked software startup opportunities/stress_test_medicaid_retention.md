# Stress test: "Coverage retention" software for Medicaid work requirements and 6-month redeterminations (as of Oct 14, 2026)

Scope note: this file covers only gaps left by `consumer_prosumer_admin.md` §4, `healthcare_insurance_finance.md` (Candidate 5) and `regulatory_structural_shifts.md`. Those files already cover the OBBBA basics: the Jul 4, 2025 signing, 80 hrs/month, the Jan 1, 2027 start, the 1-month retro-coverage cut, the Urban Institute's 4.9–10.1M projection and high-risk groups, Fortuna's $4M and $18M raises, and Benefits Data Trust's 2024 shutdown. They are not repeated here except where needed.

Research limits:
- 25 of 25 WebSearch calls were used. The rest of the work used direct fetches.
- These pages could not be accessed (403, Cloudflare or 503): CBPP's vendor-landscape paper, Commonwealth Fund briefs, West Virginia Watch, NPR (Montana), Becker's, Fierce Healthcare, and HRSA's data pages. Facts from those sources come from search snippets and are marked as such.
- Labels: **[Fact]** means observed in a source. **[Inference]** means my interpretation.

---

## 1. Status of the community-engagement requirement (Oct 2026): IFR details, verification, early states, delays, litigation, projected losses

### Takeaway
The rule is in force. The statutory deadline is Jan 1, 2027, the CMS interim final rule took effect Jul 31, 2026, and a federal judge refused to block it on Jul 30, 2026. Nebraska has already been disenrolling people since summer 2026.

Two details in the rule shrink the "collect proof" job this startup would do:
- States must verify ex parte (from data they already hold) first.
- Until Jan 1, 2028, states **may accept a self-declaration under penalty of perjury** when no data is available.

Mandatory documentation, where it is reasonably available, starts only on **Jan 1, 2028**. No good-faith delay approvals were found as of early Oct 2026.

### Cited Findings
**Rule mechanics** (primary source: [CMS IFC overview deck, Jul 2026](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf); [Federal Register 2026-11094, Jun 3, 2026](https://www.federalregister.gov/documents/2026/06/03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals))
- [Fact] Legal basis and dates:
  - The rule is CMS-2454-IFC. It implements SSA §1902(xx), added by §71119 of Public Law 119-21. CMS calls the law the "Working Families Tax Cut" legislation.
  - States must implement by **Jan 1, 2027**, or earlier through a State Plan Amendment or §1115 authority.
  - The rule was effective, and its comments were due, on **Jul 31, 2026**. — [ADvancing States summary, Jun 2, 2026](https://www.advancingstates.org/sites/default/files/Summary%20of%20Interim%20Final%20Rule%20on%20Medicaid%20Community%20Engagement.pdf)
- [Fact] **Ways to comply** in a month:
  - 80 hours of work, community service, a work program or half-time education, in any combination; or
  - monthly MAGI income of at least the federal minimum wage × 80, which is **$7.25 × 80 = $580/month** in 2026 (state and local minimum wages may not be used); or
  - for seasonal workers, an average of at least $580/month over the prior 6 months.
  - States may divide income by $7.25 to impute hours. — [CMS deck, slides 11–13](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] "Work" is defined broadly. It includes in-kind and unpaid work. The preamble says the self-employed, business owners and independent contractors "meet the definition of work." — [ADvancing States summary](https://www.advancingstates.org/sites/default/files/Summary%20of%20Interim%20Final%20Rule%20on%20Medicaid%20Community%20Engagement.pdf)
- [Fact] **Community service rules:** the host organization must provide oversight and must "have a process in place to track the community service completed by individuals, including the type … dates and hours … and a point of contact who can confirm the hours." — [ADvancing States summary](https://www.advancingstates.org/sites/default/files/Summary%20of%20Interim%20Final%20Rule%20on%20Medicaid%20Community%20Engagement.pdf)
- [Fact] **Review (look-back) periods:**
  - At application, the review period is 1, 2 or 3 consecutive months before the application, as the state chooses.
  - At renewal, it is the coverage period ending at renewal. States require 1 or more compliant months and may not dictate which months.
  - Compliance is assessed at every renewal, and states may check more often. — [CMS deck, slides 28–29](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **Verification order:**
  1. Ex parte use of available data is mandatory at application, renewal and any more-frequent checks.
  2. Documentation comes next. **Before Jan 1, 2028, states may require documentation *or* accept a self-declaration under penalty of perjury.** From Jan 1, 2028, states must require documentation wherever it is reasonably available.
  3. Other information must be accepted when no documentation is reasonably available.
  — [CMS deck, slides 32–34](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **Medical frailty:**
  - States check claims and encounter data adjudicated in the prior 12 months, and no older.
  - Self-declaration is allowed through Dec 31, 2027. From 2028 it may be used only once per enrollment period, after which documentation is required.
  - Status is re-verified at least every 12 months.
  - States must keep an auditable list of qualifying diagnoses, and a diagnosis must "significantly impair" the person's ability to perform one or more activities of daily living (ADLs).
  - People in recovery for 5 or more years from a substance use disorder are excluded. — [CMS deck, slides 20–23, 35–36](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **Non-compliance process:** the state sends a notice giving 30 calendar days to show compliance. It must then check eligibility on any other basis, and disenroll no later than the end of the month after the 30 days end. — [CMS deck, slide 38](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **Excluded groups:**
  - parents or caregivers of a child aged 13 or under or of a disabled person;
  - the medically frail;
  - most American Indians and Alaska Natives;
  - veterans with a 100% disability rating;
  - people complying with TANF work rules or in SNAP households subject to SNAP work rules;
  - people in SUD treatment programs;
  - pregnant or postpartum people;
  - former foster youth;
  - inmates.
  The optional short-term hardship exception covers inpatient stays, disaster counties and counties with high unemployment. — [CMS deck, slides 17–19, 25–26](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **Managed care plans:**
  - States may **not** use MCOs, or contractors with financial ties to MCOs, to determine compliance.
  - States **cannot delegate to plans the work of "conduct[ing] tracking or collect[ing] information on work, community service, or education activities"**, or issuing non-compliance notices.
  - Plans *may* do outreach and education, share data (for example on frailty), and refer members to work programs. — [CMS deck, slide 47 (§438.58)](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **State outreach and notices:**
  - States must reach out in the 4th–6th months before compliance begins.
  - Notices go by mail plus at least one other channel (portal, phone or text).
  - States may use MCOs to help with outreach. — [CMS deck, slides 44–45](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
  - STAT reports that states had to notify enrollees by Aug 31, 2026. — [STAT, Jul 30, 2026](https://www.statnews.com/2026/07/30/medicaid-work-requirements-judge-declines-states-request-injunction/)

**Good-faith delay**
- [Fact] How the exemption works:
  - It is granted case by case.
  - Initial approvals run "no longer than 6 months," extensions are possible, and all exemptions expire by **Dec 31, 2028**.
  - States must file quarterly progress reports. — [CMS deck, slide 42](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
  - The IFR's impact analysis assumes 10 states apply and 2 are approved. (search snippet) — [CBPP, "States Need More Time…"](https://www.cbpp.org/research/health/states-need-more-time-to-prepare-for-medicaid-work-requirement)
- [Fact] No reported CMS approval of a delay for any state was found. A Sep 9, 2026 explainer says CMS had not published a list of applicants or approvals. — [The Money Overview, Sep 9, 2026 (low-quality aggregator)](https://themoneyoverview.com/a-state-can-put-off-its-medicaid-work-requirement-until-the-end-of-2028-by-showing-a-good-faith-effort/)
  - **Unverified:** a search summary said Alaska asked for more time and that five governors asked HHS for a delay, citing a Healthcare Dive report of Oct 2. I could not find or confirm the underlying article.

**Early states**
- [Fact] From a KFF survey of 43 states (fielded Jan–Mar 2026), plans for early starts were:
  - **Nebraska**: May 1, 2026, the first state to enforce.
  - **Montana**: Jul 1, 2026.
  - **Iowa**: Dec 1, 2026.
  - **Arkansas**: soft launch Jul 1, 2026, with no disenrollments until Jan 2027.
  - Kentucky: undecided.
  - Most states: Jan 1, 2027. — [KFF, Apr 30, 2026](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/)
- [Fact] **Conflicting Montana date:** an NPR headline reads "Montana starts enforcing Medicaid work requirements on Oct 1. Patients are confused." I could not open the article (503). — [NPR, Sep 30, 2026](https://www.npr.org/2026/09/30/nx-s1-5946766/montana-early-medicaid-work-requirements-patients-confused)
- [Fact] Nebraska before and at launch:
  - The expansion population is about 70,000; Governing says about 72,000.
  - Experts projected 20,000–40,000 coverage losses.
  - The state sent more than 75,000 letters, 38,000 texts and 10,000 emails.
  - The medically-frail code list, over 300 pages, came out a week before launch.
  - No new state staff were hired. — [Healthcare Dive, May 1, 2026](https://www.healthcaredive.com/news/nebraska-medicaid-work-requirements-launch-first-state/818992/); [Governing, Apr 6, 2026](https://www.governing.com/policy/medicaid-work-requirements-squeeze-community-health-centers)
- [Fact] Nebraska results so far:
  - About **200** people were disenrolled in the first round. The Health Center Association of Nebraska reported waits of up to 90 minutes for state staff, and missed callbacks. — [Nebraska Public Media (page dated Jul 31, 2026)](https://nebraskapublicmedia.org/en/news/news-articles/nebraska-becomes-first-state-to-disenroll-medicaid-recipients-under-new-work-requirements/)
  - **More than 1,000** people lost or were denied coverage between May and August 2026, per state figures released Sep 29, 2026. No procedural-versus-substantive breakdown was given. — [Oxfam America / HRW / Nebraska Appleseed, Oct 1, 2026](https://www.oxfamamerica.org/press/nebraskans-losing-coverage-as-medicaid-changes/)

**Litigation**
- [Fact] *Commonwealth of Massachusetts v. Oz* (D. Mass.) was brought by 26 states (24 attorneys general plus 2 governors).
  - It was filed on Jun 29, 2026. — [MN AG, Jun 29, 2026](https://www.ag.state.mn.us/Office/Communications/2026/06/29_Medicaid-Work-Requirements.asp)
  - On **Jul 30, 2026**, Judge Richard Stearns denied a preliminary injunction without prejudice. He wrote that the "timeline was set by Congress in H.R. 1, not by CMS," and called the delegation issues "difficult." He hopes to hold a merits hearing before Jan 1, and the states may renew their request. — [STAT, Jul 30, 2026](https://www.statnews.com/2026/07/30/medicaid-work-requirements-judge-declines-states-request-injunction/); [NC Health News, Aug 8, 2026](https://www.northcarolinahealthnews.org/2026/08/08/judge-rejects-states-bid-to-block-medicaid-work-rules/)
- [Fact] A separate suit by medical organizations, including the American College of Physicians, and some beneficiaries was filed in September 2026. This comes from a search snippet; I did not get the docket or details. — [Fierce Healthcare (snippet)](https://www.fiercehealthcare.com/payers/26-states-sue-cms-over-final-medicaid-work-requirements-rule)

**Projected coverage losses**
- [Fact] CBO (enacted law): **+10M uninsured in 2034**, of which 7.5M come from Medicaid changes. Adding the expiry of enhanced ACA tax credits gives more than 14M. Other coverage cites 10.9M. — [KFF](https://www.kff.org/affordable-care-act/issue-brief/how-will-the-2025-reconciliation-bill-affect-the-uninsured-rate-in-each-state-allocating-cbos-estimates-of-coverage-loss/)
- [Fact] CBO on the **House-passed** work requirement: Medicaid enrollment down 5.2M in 2034, with 4.8M more uninsured. — [FactCheck.org, Jun 2025](https://www.factcheck.org/2025/06/assessing-medicaid-coverage-losses-under-house-reconciliation-bill/)
- [Fact] Urban Institute figures conflict: 4.9–10.1M lose coverage in 2028 per [AJMC, Mar 27, 2026](https://www.ajmc.com/view/5-groups-at-highest-risk-of-losing-medicaid-coverage-under-obbba) (from prior notes), versus "3 to 7 million … by 2028" per [Oxfam, Oct 1, 2026](https://www.oxfamamerica.org/press/nebraskans-losing-coverage-as-medicaid-changes/). The difference probably reflects scope (work requirements with or without 6-month renewals), but this is unconfirmed.

### Inferences
- [Inference] Timing risk is low. Congress set the date, the injunction was denied, and Nebraska is live. The more likely sources of "delay" are state-level good-faith exemptions and states choosing permissive verification, not courts.
- [Inference] **The documentation-collection pain is back-loaded to 2028.** In 2027 a state *may* accept attestation under penalty of perjury when data is missing. In states that do, patient-submitted proof matters less in 2027. A product built mainly on "collect proof of hours" may be early by about a year in those states, while remaining relevant in states that require documentation from day one (unknown which).
- [Inference] The $580/month income test makes compliance easy to prove for anyone with steady W-2 earnings. The hard cases are irregular, cash, gig or self-employed earners, unpaid caregivers who don't meet the exclusion, volunteers, and frail people whose diagnoses aren't in claims data.

### Gaps
- No list of which states accept attestation in 2027 versus requiring documents.
- No confirmed list of states that applied for good-faith exemptions, or decisions on them.
- Montana's actual go-live date and results.
- Arkansas soft-launch compliance data.
- Status of the September ACP suit.
- The Commonwealth Fund and CBPP primaries could not be opened.

---

## 2. What happens to providers financially when patients lose coverage, and unwinding evidence

### Takeaway
Losses are real and documented. In the 2023–24 unwinding, the average health center lost about $595K and spent about 1,600 staff hours on enrollment help. Health centers responded mostly with **their own staff** (84% contacted patients), not purchased software.

The same financial squeeze that creates the need also cuts budgets. NACHC itself lists outreach and other non-billable services as most vulnerable to cuts.

### Cited Findings
- [Fact] **NACHC/GWU unwinding survey** (Jan 2024; 222 health centers; 17% response rate):
  - 23% of health center Medicaid patients were disenrolled, and 74% of those had not re-enrolled.
  - The average revenue loss was **$595,000**, up to $20M at one center.
  - Staff spent an average of **1,600 hours** on patient assistance.
  - 12% of centers cut staff, 11% cut services and 9% limited appointments.
  - **84% contacted patients**, 61% helped them plan other coverage, 56% updated contact information and 54% partnered with community organizations.
  - Patient barriers: 86% did not understand the renewal notice, 69% had trouble with the state website, 63% never received a notice, 56% could not reach the call center, and 44% had portal or login problems. — [NACHC, "Impact of Medicaid Unwinding" (Apr 2024)](https://www.nachc.org/wp-content/uploads/2024/04/NACHC_Impact-of-Medicaid-Unwinding.pdf)
- [Fact] Health center scale and payer mix:
  - **2025 UDS:** 32,746,392 patients across **1,356 reporting organizations**; 47.92% Medicaid/CHIP, 11.63% Medicare and 17.21% uninsured. This is a secondary report of UDS data. — [Medical Daily via inkl (snippet)](https://www.inkl.com/news/health-centers-served-32-7-million-people-last-year-and-their-funding-expires-in-two-months)
  - **KFF (2025 UDS):** about 1,400 organizations operating more than 16,000 sites. Medicaid is **49% of urban and 32% of rural** health center revenue. Section 330 grants are 9% of urban and 12% of rural revenue. — [KFF, Oct 5, 2026](https://www.kff.org/medicaid/rural-and-urban-health-center-patients-and-financing/)
  - Other sources give Medicaid as about 42–43% of operating revenue (Commonwealth Fund / NACHC, via search snippets).
- [Fact] Projections and center-level estimates:
  - **Commonwealth Fund:** about 5.6M health center Medicaid patients could lose coverage, with about **$32B** in revenue losses over 5 years. Governing reports the same figure; some coverage says "over the next decade". — [Governing, Apr 6, 2026](https://www.governing.com/policy/medicaid-work-requirements-squeeze-community-health-centers)
  - **NACHC:** about $7B/yr in higher uncompensated care and operating burden from the whole law. (search snippet; NACHC primary not opened)
  - **Bluestem Health** (Lincoln, NE; about 21,000 patients; lost money two years running): the CEO expects up to 15% of Medicaid patients to lose coverage, costing about $600K/yr.
  - **Community Health Centers of Burlington** (VT): about $3M expected lost revenue. — [Governing, Apr 6, 2026](https://www.governing.com/policy/medicaid-work-requirements-squeeze-community-health-centers)
- [Fact] **NACHC's May 2026 Quick Guide** tells health centers to:
  - "track patient-level Medicaid renewal and reporting dates";
  - have front-desk, eligibility, enrollment, outreach and community health worker staff help patients document and track work hours and submit attestations or third-party confirmations, "especially for self-employed and/or seasonal employees";
  - check whether "EHR, Azara, etc." need changes.
  It also warns that "outreach, and other non-billable support services" are vulnerable to financially driven cuts. — [NACHC Quick Guide, May 2026](https://www.nachc.org/wp-content/uploads/2026/05/20260518HR1-QuickGuide_Final.pdf)
- [Fact] **Hospitals:**
  - Commonwealth Fund (Sep 2025) projects work requirements would cut operating margins in expansion states by **11.7–13.3%** on average, and safety-net hospitals' margins by **25.9–29.6%**. (search snippet; primary returned 403) — [Commonwealth Fund](https://www.commonwealthfund.org/publications/issue-briefs/2025/sep/impact-medicaid-work-requirements-hospital-revenues-margins); [Becker's](https://www.beckershospitalreview.com/?p=310821)
  - In trade-press case studies, hospitals convert self-pay patients to Medicaid through registrars or onsite vendors; a Virginia center found 15–20% of self-pay patients qualified. Contingency-fee levels were **not found** in public sources. — [Relias Media](https://reliasmedia.com/articles/78296-patient-access-capturing-12m-more-in-revenue-convert-self-pays-to-medicaid); [HFMA](https://www.hfma.org/payment-reimbursement-and-managed-care/medicaid-payment-and-reimbursement/8-kpis-for-measuring-medicaid-eligibility-and-advocacy/)

### Inferences
- [Inference] The value at stake per FQHC is meaningful: roughly $0.6M in losses per center in the unwinding and about $0.6M/yr projected at Bluestem. But the unwinding showed FQHCs absorb this mostly with existing outreach and enrollment staff and PCA support, not new vendors. A new tool competes with "our navigators plus Azara plus the state portal."
- [Inference] Hospitals have the clearest existing purchase pattern: self-pay-to-Medicaid conversion vendors on contingency. But that is a retroactive, at-registration job. The new 1-month retro limit weakens back-end conversion, which favors *proactive* retention. Large incumbents (Experian Health; see §4) are already moving into that.

### Gaps
- No primary 2025 Commonwealth Fund dollar figures (403).
- No hospital bad-debt data from the unwinding.
- No FQHC survey on spending for enrollment tools.
- No contingency-fee benchmarks.

---

## 3. Data matching versus patient documentation, and which eligibility vendors are involved

### Takeaway
Most states will rely heavily on data matching. KFF focus groups estimate it can verify 60–80% of enrollees, leaving 20–40% "harder to verify." Deloitte is the incumbent vendor in 16 of the 30 states using existing vendors.

Every major integrator has pledged free or discounted work-requirement modules through 2028. CMS also offers a free, open-source consent-based verification app (Emmy). The "submit to state systems" step is therefore owned by states and their integrators.

### Cited Findings
- [Fact] **KFF state survey** (Apr 30, 2026). Source: [KFF](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/)
  - Existing income data sources states will keep using:

    | Source | States |
    |---|---|
    | SNAP/TANF | 31 |
    | Quarterly wage data | 25 |
    | Equifax Work Number | 25 |
    | Unemployment insurance data | 23 |
    | BENDEX/SDX | 22 |

  - New sources states plan to add:

    | Source | States |
    |---|---|
    | VA benefit data | 11 |
    | Corrections data | 10 |
    | National Student Clearinghouse | 10 |
    | Consent-based W-2 payroll | 8 |
    | **Consent-based self-employment income** | **7** |

  - Look-back and check frequency:
    - 36 states use a 1-month look-back at application; Indiana and Idaho use 3.
    - 34 states use a 1-month look-back at renewal.
    - 34 states check at 6-month renewals; Indiana and New Hampshire check quarterly.
  - 30 states will allow self-attestation of medical frailty if allowed.
  - Only **4 states** plan separate work-requirement portals.
  - Focus groups estimate **data matching could verify 60–80% of enrollees**.
  - **30 states will use existing vendors, with Deloitte the vendor for 16 of them.** No state plans to use only new vendors.
  - Six states plan to use AI: AR, CA, MD, MO, NM and OK.
- [Fact] **CMS fact sheet of vendor pledges** (Jan 29, 2026). Source: [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
  - **Deloitte:** $2M fixed fee per state for core changes, a no-cost first-year Verification Hub, and the GovConnect enrollee-outreach platform.
  - **Gainwell:** $2M implementation including a call center, then **$50 per member per year** for members needing verification.
  - **Maximus:** a Community Engagement Tracking Tool (portal, mobile app, IVR) where members log hours, get third-party verification and apply for exclusions. It is free through 2028 for existing E&E clients.
  - **Accenture:** a community-engagement solution free to partner states through 2028.
  - **Acentra:** a data collection and tracking portal with free licensing through 2028.
  - **Optum:** a shared Community Engagement Module, license-free through 2028.
  - **Cúram/Merative:** community-engagement features at no added cost.
  - **Conduent:** discounted services.
  - **Listed on the GSA schedule but with no pledge details:** Google, Equifax, Experian, TransUnion, ID.me, Truv, GetInsured, Argyle, Healthy Together, Unite Us.
- [Fact] **CMS "Emmy" (Eligibility Made Easy):**
  - A consent-based income verification app, open source at github.com/CMSgov/emmy-app. It is free to use, but states pay for hosting and a payroll-data provider.
  - CMS has worked with 12 jurisdictions: AK, HI, MT, SD, MN, CO, LA, MO, WV, NC, DC and NH.
  - Community-engagement modules are in a one-state pilot.
  - The page does not address self-employment or gig income. — [CMS Emmy page, modified Sep 30, 2026](https://www.cms.gov/medicaid-chip/community-engagement-support/eligibility-made-easy)
- [Fact] **SteadyIQ (Income Passport):**
  - Missouri's social services department (DSS) has used it for about 5 years to verify self-employment, freelance and 1099 income.
  - It now supports Missouri's H.R. 1 work-requirement verification, including hours, job programs, education, volunteering and exemptions (vendor claim). — [PR Newswire, Aug 11, 2026](https://www.prnewswire.com/news-releases/missouri-partners-with-steadyiq-to-implement-hr-1-eligibility-changes-302848012.html)
  - SHVS lists Louisiana's and Alabama's workforce commissions and agencies in Georgia and Nevada as SteadyIQ users for income verification generally. (search snippet) — [SHVS, Nov 2025](https://shvs.org/wp-content/uploads/2025/11/SHVS_Work-Requirements-Compliance-and-Exemptions-Verification_November-2025.pdf)
- [Fact] **Free, nonprofit-built options:**
  - Nava PBC's open-source **OSCER** includes an exemption screener (Demo Day 4 was Jan 14, 2026). — [Nava](https://www.navapbc.com/events/oscer-demo-day-4)
  - Code for America publishes a Work Requirements Implementation Toolkit and supports Maryland. — [Code for America](https://codeforamerica.org/resources/work-requirements-implementation-toolkit/); [Route Fifty, Sep 2026](https://www.route-fifty.com/digital-government/2026/09/maryland-gets-nonprofit-support-implement-new-work-requirements/416173/)
- [Fact] **Funding and costs:**
  - Federal implementation funding is $200M in total, under $2M per state from the equal-share half. Federal match is 90% for system build, 75% for operations and 50% for outreach and application assistance.
  - Georgia Pathways spent $54M on administration in 4.5 years, about two-thirds of its total spending. — [Georgetown CCF, Feb 11, 2026](https://ccf.georgetown.edu/2026/02/11/implementing-costly-medicaid-work-reporting-requirements-who-will-foot-the-bill/)

### Inferences
- [Inference] The documentation residual (20–40% of enrollees) is concentrated in exactly the founder's target groups: self-employed, gig, informal and volunteer. But consent-based gig and bank verification (SteadyIQ, Argyle, Truv, Emmy and Experian Verify; see §4) is being wired in *at the state*. That reduces the need for a provider-side tool to assemble pay stubs.
- [Inference] "Submitting to state systems" is not an open job for a startup. States own intake through their integrators' portals and apps, and the rule bars MCOs from collecting this information on the state's behalf. A provider-side tool can only prepare the patient and route them into the state portal.

### Gaps
- No state-by-state map of who requires documents versus accepting attestation in 2027.
- CBPP's vendor-landscape paper (Feb 2026) could not be opened; it may contain pricing.
- Conduent's, Maximus's and Accenture's state customer lists for this work are unverified.

---

## 4. Competitors and what segment is left open

### Takeaway
Every buyer segment already has a funded or incumbent player:
- MCOs: Fortuna, Findhelp/Uno, Optum.
- FQHCs: Azara and Advocatia, which already markets "work requirement tracking."
- Hospitals: Experian Health, which added income and employment verification on Oct 13, 2026.
- Community-service hour verification: Unite Us, Findhelp.
- States: Deloitte, Gainwell, Maximus and others, plus free CMS, Nava and Code for America tools.

The only thinly covered niches are small non-FQHC Medicaid-heavy providers, clinician-side medical-frailty documentation, and small nonprofits hosting community service. All three are low-budget or embedded in EHRs.

### Cited Findings
- [Fact] **Fortuna Health** (a16z/YC; $4M seed in 2023, $18M Series A in Jul 2025):
  - **Customers:** Highmark Health Options (WV; about 20,000 Medicaid members; "TurboTax for Medicaid"; email, SMS and voice-AI outreach) and Highmark Wholecare, both announced Oct 9, 2026. — [Fortuna blog list](https://www.fortunahealth.com/blog); [West Virginia Watch, Oct 12, 2026 (snippet; page returned 403)](https://westvirginiawatch.com/2026/10/12/digital-system-will-help-some-wv-medicaid-recipients-navigate-coming-work-requirements/)
  - **Reach claim:** Fortuna says it supports payers serving more than 25M Medicaid lives (company claim, snippet).
  - **IFR guide offering:**
    - exemption identification "at scale";
    - "capturing documentation, such as community-service letters, pay stubs, and transcripts";
    - multilingual outreach;
    - state-configured web app.
    — [Fortuna IFR guide](https://www.fortunahealth.com/resources/community-engagement-interim-final-rule)
  - **Provider product:** a dedicated product with a claimed "53%+" enrollment lift (unsourced claim). Pricing is not public. — [Fortuna Providers](https://www.fortunahealth.com/providers)
- [Fact] **Unite Us + Fortuna partnership** (Nov 19, 2025):
  - It verifies community engagement hours through "trusted approvers" with auditable data flowing to state systems.
  - Targets are states, health plans, providers and community organizations.
  - Unite Us says it operates "across 47 states with 2,600+ partners." — [Unite Us press](https://uniteus.com/press/unite-us-and-fortuna-health-partner-to-support-medicaid-members/); [Unite Us CE page](https://uniteus.com/medicaid-community-engagement/)
- [Fact] **Gainwell's CEV platform** (Nov 2025) integrates Argyle (gig, payroll and bank income), Databricks, Findhelp, Fortuna and Unite Us, and claims "automated verification of volunteer hours." — [Unite Us/Gainwell press](https://uniteus.com/press/gainwell-unite-us-partnership/)
- [Fact] **Findhelp** acquired **Uno Health** (benefits enrollment) on Oct 23, 2025. In November 2025 it launched community-engagement verification for "states, payers, and providers." Its referral network is said to be used by 70% of Medicaid MCOs. — [Pulse 2.0](https://pulse2.com/findhelp-buying-uno-health-for-benefit-enrollment-and-social-care-coordination); [Gainwell/Unite Us press](https://uniteus.com/press/gainwell-unite-us-partnership/)
- [Fact] **Azara Healthcare** (FQHC population health and data incumbent):
  - Its homepage banner says it "Closes the Medicaid Coverage Gap for Safety-Net Providers with Addition of Advocatia." It offers benefit screening across more than 1,000 programs and a redetermination product described as "Built to support evolving Medicaid policies, including work requirement tracking and compliance." — [Azara benefit screening (undated, ©2026)](https://www.azarahealthcare.com/benefit-screening)
  - The DRVS redetermination workflow includes "patients due or overdue for redetermination," visit-time alerts, text outreach and navigator worklists.
  - The **California Primary Care Association** used Azara Care Connect across 38 counties and claims 150K+ Medi-Cal enrollments and re-enrollments (Jan 2024–Jun 2025). — [Azara redetermination page](https://www.azarahealthcare.com/outcomes/medicaid-redetermination-solutions)
  - Pricing and health-center count were not disclosed.
- [Fact] **Experian Health** (Oct 13, 2026) added Experian Verify payroll-based income and employment verification (with consumer-permissioned and document fallback) to Patient Financial Clearance "to help streamline Medicaid screening." It explicitly cites the Jan 1, 2027 rules and claims to serve more than 60% of US hospitals. — [Business Wire via FinancialContent, Oct 13, 2026](https://www.financialcontent.com/article/bizwire-2026-10-13-experian-health-integrates-income-and-employment-verification-into-patient-financial-clearance-to-help-streamline-medicaid-screening)
- [Fact] **Optum** sells "eligibility and enrollment assistance" for health-plan members and pledged a state community-engagement module. — [Optum](https://business.optum.com/en/operations-technology/risk-adjustment/member-engagement/eligibility-enrollment-assistance.html); [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
- [Fact] **Maximus** offers a free enrollee-facing portal, app and IVR for logging hours and getting third-party verification (for existing state clients). — [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
- [Fact] **SteadyIQ, Truv, Argyle and Equifax (The Work Number)** provide consent-based or payroll verification sold to states. Equifax's government business is about $800M/yr (snippet). Senators Warren and Wyden wrote to Equifax about profiting from the law. — [Warren/Wyden letter](https://www.warren.senate.gov/imo/media/doc/final_-_warren_wyden_letter_to_equifax_on_plan_to_profit_from_big_beautiful_bill.pdf)
- [Fact] **Benefits Data Trust** closed in 2024 because contract value never covered its costs (see prior notes, [Philadelphia Inquirer, Jun 25, 2024](https://www.inquirer.com/health/benefits-data-trust-bdt-shutting-down-20240625.html)).
- [Fact] Searching "startup Medicaid work requirements app raises seed 2026" found **no new venture-funded entrants** beyond the above.
- [Fact] A low-quality consumer site promotes a "SNAP & Medicaid renewal organizer" product (retireshield.com), which shows consumer-side noise. — [The Money Overview, Oct 3, 2026](https://themoneyoverview.com/12-states-must-run-medicaids-80-hour-work-requirement-by-january-1-and-a-notice/)

| Segment | Who already serves it (evidence above) | Open? (Interpretation) |
|---|---|---|
| State verification/intake | Deloitte (16 states), Gainwell, Maximus, Accenture, Optum, Acentra, Cúram; Emmy; Nava OSCER; CfA | Closed |
| Consent-based income (incl. gig/self-employed) | SteadyIQ, Argyle, Truv, Equifax, Emmy, Experian Verify | Closed |
| MCO member retention | Fortuna (Highmark ×2), Findhelp/Uno, Optum | Closed for a newcomer |
| FQHC redetermination/work-req tracking | Azara + Advocatia (work-req tracking marketed), Fortuna Providers | Mostly closed |
| Hospital patient access | Experian Health (Oct 2026), eligibility conversion vendors | Closed |
| Community-service hour confirmation | Unite Us "trusted approvers," Findhelp, Gainwell | Mostly closed (state-paid) |
| Small non-FQHC Medicaid providers (behavioral health, home health, dental) | No specific evidence found | Possibly open; low budgets |
| Clinician medical-frailty / ADL-impairment attestation | Fortuna guide flags it; EHR-embedded | Possibly open; PHI + EHR heavy |

### Inferences
- [Inference] Integration partnerships (Gainwell + Fortuna + Unite Us + Findhelp + Argyle) mean the "consumer navigator + verification + community service" stack is already bundled into state procurement. A solo entrant would be selling around that bundle, not into it.
- [Inference] Azara is the most damaging finding for the FQHC wedge. It already sits in many health centers' data stack, and NACHC's own guide names it. A standalone tracker would have to beat a feature inside an existing contract.

### Gaps
- Not researched: Propel, Cityblock-like care organizations, TransUnion Healthcare (no work-requirement product found), Harris, MedData, Avant, Change/Optum patient access.
- No pricing for Fortuna, Azara/Advocatia, Unite Us or Findhelp.
- Azara's health-center customer count is not on its site.

---

## 5. Buyer economics: FQHC budgets, MCO incentives, HIPAA/BAA, India-based founder

### Takeaway
- **MCOs** have the clearest motive: Big Five Medicaid enrollment fell 6.5% in a year. They are already buying from Fortuna, and the rule forbids states from delegating hour tracking to them.
- **FQHCs** feel acute pain, but their discretionary budget is shrinking and federal navigator money was cut.
- **Hospitals** buy from incumbents.
- **PHI and offshore-access restrictions** make an India-based solo founder handling patient data a credible deal-breaker for many buyers.

### Cited Findings
- [Fact] **MCO enrollment and exits:**
  - Big Five Medicaid enrollment fell from 36.2M (Jun 30, 2025) to 34.0M (Jun 30, 2026), down 6.5%. UnitedHealth fell 9.5% and CVS/Aetna 2.6%. — [Georgetown CCF, Aug 13, 2026](https://ccf.georgetown.edu/2026/08/13/medicaid-managed-care-the-big-five-in-q2-2026/)
  - Centene expects Medicaid membership to fall about 9% by year-end 2026. It cites states tightening eligibility ahead of work requirements and is exiting Arkansas expansion in 2027. — [Yahoo Finance](https://finance.yahoo.com/healthcare/articles/centene-reaffirms-2026-eps-outlook-050200330.html)
  - Elevance plans more market exits over 12–18 months. — [Georgetown CCF](https://ccf.georgetown.edu/2026/08/13/medicaid-managed-care-the-big-five-in-q2-2026/)
- [Fact] **MCO role limits:** MCOs may do outreach, share data and refer members, but states cannot delegate to them the tracking or collection of work, community service or education information. — [CMS deck, slide 47](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] **FQHC funding:**
  - Federal ACA Navigator grants were cut by about 90% in Feb 2025 for the 31 HealthCare.gov states. — [Georgetown CHIR](https://chir.georgetown.edu/new-administration-plans-to-reinstate-cuts-to-funding-for-aca-outreach-and-enrollment-assistance/)
  - No dedicated 2026 HRSA outreach and enrollment funding was found.
  - Grants are under 20% of health center operating revenue (snippet).
  - NACHC lists outreach and non-billable services as vulnerable to cuts. — [NACHC Quick Guide, May 2026](https://www.nachc.org/wp-content/uploads/2026/05/20260518HR1-QuickGuide_Final.pdf)
- [Fact] **Pricing anchors observed (state-side only):**
  - Gainwell: **$50 per member per year** for members needing verification.
  - Deloitte: **$2M per state** fixed fee.
  - Conduent fraud tool: $2M per state.
  — [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
  - No provider-side or MCO-side pricing was found.
- [Fact] **HIPAA and offshore access:**
  - HIPAA does not ban offshore PHI access, but requires a BAA and safeguards.
  - ACA §6505 bars Medicaid payment to foreign entities for items and services. CMS says it targets services, not administrative support.
  - **Texas's managed care contract bars work or data maintenance outside the US and remote offshore access.** Ohio executive orders bar offshore contracting, including by subcontractors.
  - Some states ban any offshoring of Medicaid data.
  - Medicare Advantage plans need offshore-subcontractor attestations, which flow down to vendors. — [Shumaker, Dec 12, 2025](https://www.shumaker.com/insight/offshoring-patient-data-what-health-care-providers-need-to-know-now/)
- [Fact] **Gainwell precedent:** Bloomberg Law reported Gainwell's contracts require Medicaid data to stay in the US, and that PHI was visible to India-based workers during troubleshooting. — [Bloomberg Law, Dec 11, 2025](https://news.bloomberglaw.com/us-law-week/medicaid-firm-struggles-to-block-patient-data-from-india-workers)

### Inferences
- [Inference] **Right buyer, if any: MCOs pay, and FQHCs feel the pain.** MCOs have a direct revenue motive, since each lost member is lost capitation. But they are served by a16z-backed Fortuna and enterprise vendors, procure slowly, and require security reviews (SOC 2) that a solo founder can't pass quickly.
- [Inference] FQHCs are reachable through about 50 state PCAs and NACHC events. But they are budget-constrained and covered by Azara. The realistic FQHC price point is probably small per-site subscriptions or PCA-level grant-funded deals. This is a hypothesis; no pricing evidence was found.
- [Inference] **Illustrative ceiling, not a market estimate:** 1,356 health center organizations × a hypothetical $6K–$24K/yr = about $8M–$33M/yr if *every* center bought. Realistic penetration against Azara and in-house staff would be a small fraction of that.
- [Inference] **India-based founder:**
  - Credible only if the product never exposes PHI to the founder. That means US-hosted, US-entity, a BAA, no offshore admin access, or ideally a no-PHI or patient-held architecture.
  - Buyers in Texas, Ohio and other states with offshore restrictions, and any MCO, will likely ask about offshore access in security review.
  - Trust and relationship selling to safety-net organizations is also harder remotely, though NACHC and PCA events are US-based and attendable.

### Gaps
- No primary data on FQHC spending on enrollment software.
- Whether HRSA's FY2026 base grants include any outreach and enrollment earmark.
- MCO budgets for retention vendors, and Fortuna's contract values.
- A current state-by-state offshore-restriction list (the 2014 OIG survey is outdated).

---

## 6. Disconfirming evidence (actively trying to kill the idea)

### Takeaway
Litigation does **not** kill the idea, since the injunction was denied. Four other findings come close:
1. Crowding by funded and incumbent players at every buyer layer, plus free government and vendor tools through 2028.
2. States automating 60–80% of verification, plus permitted 2027 self-attestation.
3. The MCO delegation ban on hour tracking.
4. Weak FQHC budgets, combined with PHI and offshore constraints, for this particular founder.

### Cited Findings
- [Fact] The injunction was denied on Jul 30, 2026, so the rule proceeds. — [STAT](https://www.statnews.com/2026/07/30/medicaid-work-requirements-judge-declines-states-request-injunction/)
- [Fact] States will rely mainly on data: 60–80% of enrollees can be verified by data matching, and Deloitte and other integrators are offering cheap or free modules. — [KFF, Apr 30, 2026](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/); [CMS fact sheet, Jan 29, 2026](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
- [Fact] Self-declaration under penalty of perjury is permitted until Jan 1, 2028. — [CMS deck, slides 33–36](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] Incumbents and funded startups are already shipping (Fortuna, Azara/Advocatia, Experian Health, Unite Us, Findhelp/Uno, Optum, Maximus). See §4.
- [Fact] Benefits Data Trust shut down because public contracts did not cover costs. — [Philadelphia Inquirer, Jun 25, 2024](https://www.inquirer.com/health/benefits-data-trust-bdt-shutting-down-20240625.html)
- [Fact] Early Nebraska evidence points to state-side failures: no new staff, 90-minute waits, a frailty list released late, and "unprepared software." — [Nebraska Public Media](https://nebraskapublicmedia.org/en/news/news-articles/nebraska-becomes-first-state-to-disenroll-medicaid-recipients-under-new-work-requirements/); [Oxfam, Oct 1, 2026](https://www.oxfamamerica.org/press/nebraskans-losing-coverage-as-medicaid-changes/)
- [Fact] There are ethical and regulatory sensitivities:
  - Attestations are made under penalty of perjury.
  - Substance use data falls under 42 CFR Part 2, as Fortuna's guide notes. — [Fortuna IFR guide](https://www.fortunahealth.com/resources/community-engagement-interim-final-rule)
  - Equifax's data business drew Senate scrutiny. — [Warren/Wyden letter](https://www.warren.senate.gov/imo/media/doc/final_-_warren_wyden_letter_to_equifax_on_plan_to_profit_from_big_beautiful_bill.pdf)

### Inferences
- [Inference] Much of the coverage loss in Nebraska appears to stem from **state capacity failures**: call centers, notices and code lists. A provider-side tool cannot fix those, and a navigator on the phone can work around them as well as software can.
- [Inference] A product that coaches patients on attestations "under penalty of perjury" carries legal and reputational risk if it is seen as encouraging false claims. It would need careful design (education plus documentation, not answer-steering).
- [Inference] Sales cycles: FQHCs need board and budget approval, and MCOs need procurement and security review. Neither is likely to close within a solo founder's 2–3-month runway. Not evidenced; based on general procurement patterns.

### Gaps
- No direct evidence on FQHC software sales-cycle length.
- No evidence on how many Nebraska losses were caused specifically by documentation failure among self-employed people.

---

## 7. Twenty specific first-customer targets (verifiable entities)

### Takeaway
Prioritize primary care associations (PCAs) and FQHCs in states that are live or early: NE, MT, IA, AR, GA. Next come states with stricter verification (IN, ID, NH) and Emmy-partner states (SD, MN, WV, NC, AK, LA, MO).

**Do not** target Highmark or WV MCOs, which are already Fortuna customers. All websites below were confirmed to resolve on Oct 14, 2026. Whether each target already uses Azara is unknown.

### Cited Findings
**State primary care associations** (organization names confirmed from website titles; state relevance from §1 and §3)
1. Health Center Association of Nebraska — https://www.hcanebraska.org. Live since May 1, 2026, and it publicly reported state-staff delays. — [Nebraska Public Media](https://nebraskapublicmedia.org/en/news/news-articles/nebraska-becomes-first-state-to-disenroll-medicaid-recipients-under-new-work-requirements/)
2. Montana Primary Care Association — https://www.mtpca.org. Early state (Jul 1 or Oct 1) and an Emmy partner.
3. Iowa Primary Care Association — https://www.iowapca.org. Iowa planned to start Dec 1, 2026. — [KFF](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/)
4. Community Health Centers of Arkansas — https://www.chc-ar.org. Soft launch Jul 1, 2026; the state plans to use AI; Centene is exiting expansion in 2027.
5. Kentucky Primary Care Association — https://www.kypca.net. Possible early start (undecided).
6. Georgia Primary Care Association — https://www.gpca.net. Georgia Pathways has been operating since before the federal rule.
7. Indiana Primary Health Care Association — https://www.indianapca.org. Quarterly checks and a 3-month look-back (stricter than the federal minimum).
8. Idaho Community Health Center Association — https://www.idahopca.org. 3-month look-back and stricter state law.
9. Community HealthCare Association of the Dakotas — https://www.communityhealthcare.net. South Dakota is an Emmy partner.
10. West Virginia Primary Care Association — https://www.wvpca.org. Emmy partner. Fortuna is active with WV MCOs, so this is a competitive test.
11. Louisiana Primary Care Association — https://www.lpca.net. Emmy partner, and Elevance is exiting Louisiana Medicaid in 2027.
12. Alaska Primary Care Association — https://www.alaskapca.org. Emmy partner; the reported delay request is unverified.
13. Minnesota Association of Community Health Centers — https://www.mnachc.org. Emmy partner.
14. NC Community Health Center Association — https://www.ncchca.org. Emmy partner.
15. Association for Utah Community Health — https://www.auch.org. Utah's §1115 adult expansion population is subject to the rule. — [CMS deck, slide 9](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)

**FQHCs in early states**
16. Bluestem Health (Lincoln, NE). About 21,000 patients; the CEO projects about $600K/yr in losses. — [Governing, Apr 6, 2026](https://www.governing.com/policy/medicaid-work-requirements-squeeze-community-health-centers). The website did not return a title, so it is unverified.
17. OneWorld Community Health Centers (Omaha, NE) — https://www.oneworldomaha.org
18. Charles Drew Health Center (Omaha, NE) — https://www.charlesdrew.com
19. RiverStone Health (Billings, MT) — https://riverstonehealth.org; and Partnership Health Center (Missoula, MT) — https://www.partnershiphealthcenter.com
20. Primary Health Care (Des Moines, IA) — https://www.phcinc.net; Siouxland Community Health Center (Sioux City, IA) — https://www.slandchc.com; and ARcare (AR) — https://www.arcare.net

**Venues**
- NACHC Partner Conference, **Nov 16–17, 2026**, Kansas City, MO.
- NACHC Policy & Issues Forum, **Feb 8–11, 2027**, National Harbor, MD.
- NACHC Workforce Conference (formerly FOM/IT), **May 25–26, 2027**, Las Vegas.
- Exhibitor options exist. — [NACHC conferences](https://www.nachc.org/conferences/)

### Inferences
- [Inference] PCAs are the best first call. They aggregate 10–60 health centers, run technical assistance on H.R. 1 (NACHC's guide directs centers to them), and sometimes buy tools on members' behalf (CPCA–Azara is the precedent). A PCA can also tell you within one call whether Azara or the EHR already covers the job.
- [Inference] Nebraska is the only state with live disenrollment data. Its PCA and FQHCs are the fastest way to learn which failure modes (documentation versus call center versus frailty coding) actually drive losses.

### Gaps
- Contact names and roles (outreach and enrollment directors) were not collected.
- Missouri PCA's site returned a 429 error and is unverified.
- No information on which targets use Azara, OCHIN Epic or other EHRs.

---

## 8. Narrowest MVP (2–8 weeks, solo non-engineer, AI tools, privacy-constrained) and a 14-day experiment with kill criteria

### Takeaway
If tested at all, build a **no-PHI "proof-packet kit" for navigators**, not a patient tracker:
- state-specific rules;
- an exemption/exclusion screener;
- a self-employed/seasonal income calculator against the $580/month test;
- templated letters for community-service hours and clinician frailty attestations.

It should run in the browser, with nothing stored server-side. Then spend 14 days trying to get PCAs and FQHC outreach leads to commit to a paid pilot, with hard kill criteria.

### Cited Findings (design constraints drawn from sources)
- [Fact] The $580/month income test and the seasonal 6-month average rule. — [CMS deck, slides 11–13](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] Community-service hosts must record type, dates and hours, and give a contact who can confirm. — [ADvancing States summary](https://www.advancingstates.org/sites/default/files/Summary%20of%20Interim%20Final%20Rule%20on%20Medicaid%20Community%20Engagement.pdf)
- [Fact] Provider documentation is acceptable evidence of frailty and must show impairment of ADLs, not just a diagnosis. — [CMS deck, slides 21–23](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf); [Fortuna IFR guide](https://www.fortunahealth.com/resources/community-engagement-interim-final-rule)
- [Fact] NACHC asks health centers to help patients with documentation, "especially for self-employed and/or seasonal employees." — [NACHC Quick Guide](https://www.nachc.org/wp-content/uploads/2026/05/20260518HR1-QuickGuide_Final.pdf)

### Inferences (proposed plan, not evidence)
**MVP (2–4 weeks)**
1. Static web app (for example Next.js or plain HTML/JS built with Claude) hosted in the US, with **no backend and no stored patient data**. Navigators enter de-identified answers during a visit, and the app generates a printable packet the patient keeps.
   - Whether this keeps the vendor outside "business associate" status needs a US health-privacy lawyer's confirmation before any pilot.
2. Rules content for 3–5 states (NE, MT, IA, AR, GA): look-back length, check frequency, attestation versus documentation, hardship options, and links to each state portal. Each rule is sourced and dated.
3. Exemption and exclusion screener mirroring the CMS decision tree (deck slide 30).
4. Self-employed/gig/seasonal calculator: monthly gross minus expenses versus $580, plus the 6-month seasonal average and the evidence checklist.
5. Templates:
   - a community-service hours confirmation letter covering the fields the IFR requires;
   - a clinician frailty attestation that prompts for the ADL-impairment description;
   - a caregiver-exclusion statement.
6. Weeks 5–8, **only if paid**: a US-hosted, BAA-covered due-date tracker that imports a CSV of renewal dates. This needs a US contractor or a HIPAA-eligible platform, and no offshore PHI access.

**14-day experiment**
- **Days 1–3:** build a clickable demo for Nebraska only, and write a one-page "what we learned from Nebraska's first 5 months" brief as a door-opener.
- **Days 2–12:** contact all 20 targets in §7, plus about 20 more health centers in the same states, via email and LinkedIn to O&E, patient-access and CEO staff.
  - Ask for 20-minute calls.
  - Ask: what tools you use now (Azara? Fortuna? EHR?); which failure mode costs the most patients; who owns the budget; whether you'd pay for a 3-month pilot from Jan 2027.
- **Day 10:** attend or arrange meetings around the NACHC Partner Conference if feasible (Nov 16–17 falls after the window, so use it as a follow-up).
- **Days 12–14:** offer a paid pilot (hypothesis: $300–$1,000 per health center per month, or a PCA-level license) and record objections.

**Kill criteria (any one ends it)**
- Fewer than **6 conversations** from about 40 contacts.
- Fewer than **3 of 6** say their current tools (Azara, EHR, Fortuna, state portal) do *not* already cover the job.
- **Zero** verbal commitments to a paid pilot or LOI from at least one PCA or two FQHCs.
- At least **half** of prospects say an India-based vendor or a non-US-hosted/no-BAA tool is a blocker even for a no-PHI kit.
- Prospects consistently identify **state call center or notice failures** as the main cause of loss, which software on the provider side cannot fix.

### Gaps
- No evidence on willingness to pay at any price point. The pilot price above is a hypothesis.
- Legal status of a no-storage, browser-only tool under HIPAA was not verified.

---

## 9. Verdict: advance, advance with conditions, or reject; plus the right buyer and wedge

### Takeaway
**REJECT for the top-five shortlist** (for this founder). The "why now" is verified and durable. But the specific job — tracking who is due, collecting proof, and submitting to the state — is already covered:
- states are automating most verification and may accept attestation through 2027;
- integrators offer free modules;
- CMS offers Emmy for free;
- Fortuna holds MCOs, Azara holds FQHCs and Experian Health holds hospitals;
- the rule bars states from delegating hour tracking to MCOs.

Add PHI and offshore constraints and the Benefits Data Trust precedent, and a solo, India-based, non-engineer founder has no credible edge. **Keep on a watchlist.** Re-test only if 2027 data from the first 6-month cycles shows a large documentation-specific failure mode that incumbents miss.

### Cited Findings (summary of decisive evidence)
- [Fact] The rule is live and court-tested. — [STAT, Jul 30, 2026](https://www.statnews.com/2026/07/30/medicaid-work-requirements-judge-declines-states-request-injunction/)
- [Fact] Data matching is expected to cover 60–80% of enrollees, and Deloitte holds 16 states. — [KFF, Apr 30, 2026](https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/)
- [Fact] Self-attestation is allowed until 2028, and the MCO hour-tracking delegation ban is in the rule. — [CMS deck](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf)
- [Fact] Funded and incumbent players are active. — [Fortuna](https://www.fortunahealth.com/blog); [Azara](https://www.azarahealthcare.com/outcomes/medicaid-redetermination-solutions); [Experian Health, Oct 13, 2026](https://www.financialcontent.com/article/bizwire-2026-10-13-experian-health-integrates-income-and-employment-verification-into-patient-financial-clearance-to-help-streamline-medicaid-screening); [Unite Us](https://uniteus.com/press/unite-us-and-fortuna-health-partner-to-support-medicaid-members/); [CMS vendor pledges](https://www.cms.gov/newsroom/fact-sheets/fact-sheet-pledges-medicaid-technology-companies-support-community-engagement-implementation-related)
- [Fact] Real provider losses (about $595K per FQHC in the unwinding) were absorbed mostly by in-house staff. — [NACHC](https://www.nachc.org/wp-content/uploads/2024/04/NACHC_Impact-of-Medicaid-Unwinding.pdf)
- [Fact] Offshore-PHI restrictions exist in state contracts. — [Shumaker, Dec 12, 2025](https://www.shumaker.com/insight/offshoring-patient-data-what-health-care-providers-need-to-know-now/); [Bloomberg Law, Dec 11, 2025](https://news.bloomberglaw.com/us-law-week/medicaid-firm-struggles-to-block-patient-data-from-india-workers)

### Inferences
- [Inference] **Best buyer, if pursued despite the verdict:** state PCAs, as aggregators, for FQHCs in early or strict states (NE, MT, IA, AR, IN, ID) that do **not** already use Azara's redetermination module. MCOs pay more but are taken and procure slowly.
- [Inference] **Best wedge, if pursued:** a no-PHI "proof-packet kit" for navigators, aimed at the hard-to-verify residual: self-employed/gig/seasonal income against $580, community-service hour letters, caregiver exclusion, and clinician ADL-impairment frailty attestations.
  - The window strengthens on Jan 1, 2028, when documentation becomes mandatory and frailty self-attestation is limited to once.
  - This is a feature an incumbent can copy quickly, not a durable company, so it doesn't justify a top-five slot.
- [Inference] **What would flip the verdict to "advance with conditions":**
  - (a) Nebraska, Montana or Iowa data showing that a large share of terminations are self-employed, caregiver or volunteer documentation failures, *and*
  - (b) at least one PCA or MCO committing to a paid pilot in the 14-day test, *and*
  - (c) a US-based co-founder or contractor to own PHI handling and US sales.

### Gaps
- No primary data yet on *why* Nebraska enrollees lost coverage (procedural versus documentation versus truly non-compliant).
- No competitor pricing.
- No list of states that will require documentation in 2027.
- Search budget was exhausted: CBPP's vendor paper, the Commonwealth Fund primaries and the NPR Montana story could not be read.
