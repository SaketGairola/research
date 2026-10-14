# Stress Test: (A) Governance for Vibe-Coded Apps Built by Non-Engineers vs (B) Multi-Tenant Copilot Oversharing Cleanup for MSPs (as of 14 Oct 2026)

Method and access notes (read first):
- Research date: 14 Oct 2026. I used all 25 permitted WebSearch calls, then switched to direct fetches only.
- These notes build on two earlier files:
  - `it_msp_security_data.md`: Q4 (Copilot) and Q7 (vibe apps), candidate cards 1–2.
  - `ai_agents_second_order.md`: Q2, candidate cards 2–3.
- I did not repeat what those files already cover: RedAccess's 380k/5k figures, the CSA governance-gap note, CVE-2025-48757, the Replit and PocketOS database deletions, the Microsoft blueprint basics, Syskit pricing, and Nudge's $750/mo floor. Where my findings **contradict** those notes, I say so.
- **Could not access:**
  - crt.sh: certificate-transparency search returned HTTP 502 twice.
  - Microsoft's Copilot Business product page: HTTP 503.
  - Rencore blog: 404.
  - Inforcer pricing page: 404.
  - A Spanish article relaying a Retool survey: 403.
  - Netskope site search: content truncated.
  - Reddit: not attempted, because the earlier session found it blocked.
- I found no Netskope or Zscaler primary documentation on vibe-coding platforms.
- Many sources are vendor pages and are flagged as such. "Observed" means a cited source states it. Everything under **Inferences** is my interpretation.

---

## A1. How widespread is citizen-built app publishing (platform usage, enterprise plans, surveys)?

### Takeaway
Usage is large and growing fast:
- Lovable reports $600M annualized revenue (Sep 2026) and 1M new projects a week.
- Replit was valued at $9B (Mar 2026).
- Wix says Base44 reached about $100M ARR by Mar 2026, and it is driving Wix's growth.

Every major platform now sells Business or Enterprise tiers with SSO. However, **I found no reliable survey measuring how many SMB or mid-market employees publish apps without IT's knowledge.** The only figure found (60% of builders evade IT, attributed to Retool) is unverified.

### Cited Findings
- **Lovable** (TechCrunch headlines):
  - "Lovable's annualized revenue crosses $600M as vibe coding takes off" (24 Sep 2026).
  - "Lovable confirms new $13.3B valuation, raises another $400M" (12 Aug 2026).
  - "Lovable says it has hit $500M in annualized revenue, with 1 million new projects a week" (9 Jun 2026).
  - "Lovable says it added $100M in revenue last month alone, with just 146 employees" (11 Mar 2026).
  - Source: [TechCrunch Lovable tag page, accessed 14 Oct 2026](https://techcrunch.com/tag/lovable/) (headlines only; article bodies not read).
  - **Conflicting estimate:** Panto's third-party "triangulation" gives 2026 ARR of only $22M–$38M and 420k–650k MAU — [Panto](https://www.getpanto.ai/blog/lovable-statistics) (search summary). This is far below Lovable's own statements as reported by TechCrunch. Treat Panto as unreliable.
- **Replit:**
  - "Replit snags $9B valuation 6 months after hitting $3B" (11 Mar 2026); "Replit hits $3B valuation on $150M annualized revenue" (10 Sep 2025); Visa invested (28 May 2026). Source: [TechCrunch Replit tag page](https://techcrunch.com/tag/replit/) (headlines only).
  - Replit says it has users at 85% of Fortune 500 companies, and self-serve Enterprise purchases up to $200,000 opened in May 2026 — [Superblocks blog (competitor-authored)](https://www.superblocks.com/blog/replit-enterprise).
  - A Sacra estimate of about $525M annualized revenue in April 2026 is search-snippet only and unverified — [Sacra](https://sacra.com/chat/h/bc47d079-fd4d-4750-8241-36983b058cf9/).
- **Base44 / Wix:**
  - Wix management said Base44 reached roughly $100M ARR, with enterprise-sized organizations adopting it "via self-serve channels" and "no sales team" (Q4 call, Mar 2026) — [Yahoo Finance / Wix Q4 call](https://finance.yahoo.com/news/wix-com-q4-earnings-call-165003576.html) (search summary).
  - Wix Q2 2026 revenue was $563.1M (+15% YoY), with Base44 driving much of the growth — [Ynet](https://www.ynetnews.com/business/article/bkqk6tylzg) (search summary).
  - Sacra *estimates* $200M ARR and 10M users by Aug 2026 — [Sacra](https://sacra.com/c/base44/) (estimate, not Wix-confirmed).
- **Plan structure (shows enterprise intent):**
  - Lovable Business: from $50/mo for 100 credits; Pro: from $25/mo — [Lovable subscription plans](https://docs.lovable.dev/introduction/subscription-plans).
  - Replit Core: $20/mo; Pro: $100/mo; Enterprise: custom — [Replit pricing](https://replit.com/pricing).
  - Base44 Starter through Elite: $16–$160/mo; Enterprise: custom — [Base44 pricing](https://base44.com/pricing).
  - Bolt Pro: $25/mo; Teams: $30/member/mo; Enterprise: custom — [Bolt pricing](https://bolt.new/pricing).
- **Surveys (weak):**
  - A Spanish-language article attributes to Retool that "60% of builders evade IT" and "only 5% of CTOs see the apps their team creates". I could not open it (403) and did not find the original Retool report — [Ecosistema Startup](https://ecosistemastartup.com/?p=114732) (search snippet only; **unverified**).
  - A 2022 ServiceNow survey (UK/IE) found 53% of employees would build their own apps given low-code means. It is dated — [ERP Today](https://erp.today/benefits-of-low-code-app-development-still-flying-under-the-radar-according-to-servicenow-research/) (search summary).

### Inferences
- The *supply* of citizen-built apps is real and large: about 1M new Lovable projects a week, and Base44 adopted self-serve by enterprise-sized orgs. Wix's "no sales team" self-serve enterprise adoption shows these apps enter companies bottom-up, often on individual or team plans rather than IT-procured Enterprise contracts.
- None of the usage figures splits *company-internal* apps from consumer or hobby projects. The share that holds company data inside SMBs is **unknown**.

### Gaps
- No primary survey quantifies SMB or mid-market employees publishing apps without IT approval. The Retool figure is unverified.
- No Bolt or Vercel v0 usage figures were found. Replit 2026 revenue is unverified.

---

## A2. New incidents and exposures in 2025–2026 (beyond those in the prior notes)

### Takeaway
New incident evidence keeps arriving:
- A Lovable-hosted exam app exposed 18,697 user records (Feb 2026).
- Wiz found an auth bypass that let attackers into *private, SSO-only* Base44 enterprise apps (Jul 2025).
- RedAccess's follow-up says more than 2,000 of its 5,000 "corporate" apps held sensitive data.

In every case, the platform's position is the same: the scan was available, and fixing it is the user's job.

### Cited Findings
- **Lovable exam app, 27 Feb 2026:**
  - 18,697 user records exposed (14,928 unique emails; 4,538 student accounts; 10,505 "enterprise users"; 870 with full PII).
  - 16 vulnerabilities, 6 of them critical. RLS and role checks were missing, and an inverted auth function let unauthenticated users in.
  - The researcher's support ticket was "closed without a response". He argued that "a basic security scan of showcased applications would have caught every critical finding."
  - Lovable's CISO said every project gets a free pre-publish scan but implementing fixes "is up to the user".
  - Source: [The Register, 27 Feb 2026](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/). HN discussion: 140 points, 35 comments — [HN item 47182659](https://news.ycombinator.com/item?id=47182659).
- **Base44 auth bypass (Wiz, published 29 Jul 2025):**
  - Exposed `auth/register` and `auth/verify-otp` endpoints let an attacker who knew only the app_id create a verified account on a *private* app, "bypass[ing] all given authentication controls" including SSO-only access.
  - Affected enterprise apps used for internal chatbots, knowledge bases and HR/PII.
  - Fixed in under 24 hours. Base44 "found no evidence that any customer was impacted."
  - Source: [Wiz](https://www.wiz.io/blog/critical-vulnerability-base44).
- **RedAccess follow-up:** of about 5,000 apps that "looked corporate", "more than 2,000 of those held sensitive corporate, operational, or personal data". Exposed apps "often granted admin access by default to anyone with the URL" — [The Hacker News, 29 May 2026](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html). This is "a contributed piece from one of our valued partners", i.e., RedAccess marketing.
- **HN community attention is low.** The Wired story on RedAccess was submitted three times and got 6, 4 and 3 points. "Show HN: Scan vibe coded apps for security vulnerabilities" got 1 point — [HN Algolia query, accessed 14 Oct 2026](https://hn.algolia.com/api/v1/search?query=vibe%20coded%20apps%20exposed&tags=story).

### Inferences
- The Base44 case matters for the "governance" thesis. Even apps that IT *did* put behind SSO were exposed by a platform bug, so platform-level controls are not a full answer.
- The pattern of incidents found by researchers, not owners, suggests the owning organizations had no inventory. This is consistent with the thesis, but it is an inference.

### Gaps
- No incident was found where an **SMB or its MSP** was publicly identified as the victim, or where a regulator acted. Breach-cost data specific to vibe apps is absent.

---

## A3. What the platforms themselves now offer for governance (absorption risk)

### Takeaway
**Platforms are absorbing in-workspace governance fast, but only for apps built inside a company workspace and mostly behind Enterprise pricing.**
- Lovable now has a workspace Security Center, PII detection, publishing controls, scheduled deep scans, audit logs, Aikido/Wiz connectors and a pre-publish scan on every plan.
- Replit shipped audit logs, org-wide settings and an Admin API (Aug 2026).
- Vercel lets every plan protect all deployments.

No platform inventories apps employees built on **personal accounts** or on **competing platforms**.

### Cited Findings
- **Lovable:**
  - **Every plan:** a basic scan on every publish (10–15 seconds) checks configuration, schema, RLS, auth gaps and sensitive data exposed to the internet. Admins can block publishing on critical issues. A deep AI scan takes 2–4 minutes. Enterprise admins can schedule deep scans weekly or monthly. Auto-fix is opt-in. Source: [Lovable blog, 1 Jun 2026](https://lovable.dev/blog/how-lovable-protects-your-apps-automatically).
  - **Business and Enterprise:** SSO and the Security Center (workspace-wide code, dependency, secrets and scan coverage). Source: [Lovable enterprise docs](https://docs.lovable.dev/introduction/lovable-for-enterprise).
  - **Enterprise only:**
    - SCIM.
    - "Restrict external publishing" to admins or owners, and disabling public preview links.
    - A pre-publish block on unresolved PII findings.
    - A custom publishing domain.
    - Audit logs (about 90 days).
    - EU inference.
    - Aikido AI-pentest and Wiz SCA/SAST connectors.
    - Source: [Lovable enterprise docs](https://docs.lovable.dev/introduction/lovable-for-enterprise).
  - **Plan matrix:** SSO and Security Center on Business+; "Publishing controls", audit logs, SCIM and scheduled scans on Enterprise only — [Lovable subscription plans](https://docs.lovable.dev/introduction/subscription-plans).
  - **Workspace Insights (23 Jun 2026, Enterprise):** one table of "every project, its publish status, and risk signals", plus a count of "externally published apps" and PII detection — [Create With (secondary)](https://www.createwith.com/tool/loveable/updates/lovable-launches-workspace-insights-for-enterprise-governance-and-security).
- **Replit:**
  - "Govern Replit at scale" (16 Aug 2026, Enterprise) announced:
    - audit logs with more than 50 events streamed to a SIEM (30-day default retention);
    - org-wide, lockable Workspace Settings, starting with model and provider controls;
    - an Admin API beta (usage, workspace, member, project data);
    - a Compliance API.
    - Source: [Replit blog](https://replit.com/blog/new-enterprise-governance-tools).
  - **Conflict:** a competitor blog says Replit Enterprise admins can "prohibit public apps, require private deployments, and mandate security scans" — [Superblocks](https://www.superblocks.com/blog/replit-enterprise). Replit's own 16 Aug 2026 post does **not** mention those controls, so treat them as unconfirmed.
  - Replit's pricing page lists SSO/SAML only on Enterprise — [Replit pricing](https://replit.com/pricing).
- **Base44:** SSO and "advanced security controls" only on Enterprise. The FAQ says users can "keep your apps and websites private, share with your team, or publish to the web". No default visibility or scanner is listed — [Base44 pricing](https://base44.com/pricing).
- **Bolt:** SSO, audit logs and "data governance & retention policies" only on Enterprise. No security scanning is mentioned — [Bolt pricing](https://bolt.new/pricing).
- **Vercel (v0 deploys to Vercel):**
  - "All Deployments" protection (preview and production) is available on all plans.
  - IdP-based "Passport" and Trusted IPs are Enterprise only.
  - Password protection costs $20/month per project on Pro.
  - Team-wide protection defaults can be set.
  - Source: [Vercel docs, updated 15 Sep 2026](https://vercel.com/docs/deployment-protection).
- **Platform domains are on the Public Suffix List.** `lovable.app`, `lovableproject.com`, `base44.app`, `bolt.host`, `replit.app`, `netlify.app`, `vercel.app` and `v0.build` are listed, submitted by each vendor's security team — [Public Suffix List, fetched 14 Oct 2026](https://publicsuffix.org/list/public_suffix_list.dat).

### Inferences
- **The in-workspace governance feature is being absorbed.** A company that buys Lovable Business or Enterprise, or Replit Enterprise, gets inventory, scanning and publishing controls from the vendor. A third-party product that duplicates this for one platform is a feature, not a company.
- **What platforms will not absorb:**
  1. Apps built on employees' personal or free accounts (outside the company workspace).
  2. A cross-platform view (Lovable + Replit + Base44 + Bolt + Vercel + Netlify).
  3. Ownership and handover when the builder leaves.

  Platforms have no commercial incentive to report on apps outside a paying workspace, or to help export apps. This is interpretation, consistent with Wix's self-serve adoption and Lovable's "up to the user" stance.
- **SMB fit:** Lovable puts publishing controls and audit logs behind custom-priced Enterprise, and Base44 and Bolt put SSO there too. A 50-person firm is unlikely to buy those tiers, which leaves SMBs reliant on defaults (inference; SMB tier mix not measured).

### Gaps
- Default visibility for new apps on each platform (public vs private) was not verified from primary docs for Base44, Bolt or Replit.
- I could not confirm whether Replit Enterprise can ban public apps (sources conflict).

---

## A4. Competitors (pricing, funding) and whether SASE/CASB, platforms or MSP tools will absorb this

### Takeaway
The enterprise end is occupied:
- RedAccess sells "Shadow Builders Security — Govern Vibe-Coded Apps".
- Escape raised $18M for attack-surface management and DAST.
- Wiz and Aikido are embedded inside Lovable.
- Nudge does shadow-AI discovery at $5 per mailbox per month.

**MSP tooling is also starting to absorb shadow-AI *usage* discovery** (CIPP's Shadow AI report, Augmentt "AI & SaaS discovery"). The builder-side scanner market looks tiny: Vibe App Scanner earns about $856 MRR from 34 subscriptions. No competitor found specifically sells *cross-platform inventory, exposure and handover for SMBs via MSPs*. That is either the gap or a sign that nobody pays for it.

### Cited Findings
- **RedAccess:**
  - An "agentless, session-layer security platform" giving "SSE-grade visibility and governance at the session itself, across any browser, any device, including unmanaged ones" — [THN partner piece, 29 May 2026](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html).
  - The homepage lists a "Shadow Builders Security" use case ("Govern Vibe-Coded Apps"). It shows no pricing, no MSP program and no funding; CTAs are demo or free report — [Red Access](https://www.redaccess.io/) (vendor).
  - Funding: **not found**.
- **Escape:**
  - Products: AI pentesting, business-logic DAST, external network pentest and attack surface management.
  - Pricing is custom ("scoping pricing to your environment"). Sold through AWS Marketplace and "20+ channel partners".
  - No vibe-app product SKU; only a research article.
  - Source: [Escape pricing](https://escape.tech/pricing).
  - $18M Series A on 10 Mar 2026 — [TipRanks](https://www.tipranks.com/private-companies/escape) (search summary; single-sourced).
- **Nudge Security:**
  - Shadow AI and SaaS discovery, AI agent discovery, OAuth risk, playbooks. Its FAQ says pricing is "$5 per mailbox per month".
  - Has partner and deal-registration links, but no program details.
  - **No mention of vibe-coding or apps employees build.**
  - Source: [Nudge Security](https://www.nudgesecurity.com/) (vendor).
- **Zenity:** homepage is about AI-agent security (Surface / Enforce / Protect). It does not mention vibe-coding platforms, Power Platform or pricing — [Zenity](https://zenity.io/) (vendor).
- **Retool:**
  - Says governance (access controls, audit logs, permissions) is "inherited automatically by every app on the platform", versus per-project in Lovable. Claims more than 10,000 organizations — [Retool competitor page](https://retool.com/competitor/lovable) (vendor).
  - Publishes a Lovable→Retool migration guide: export the React app, then "governance applies automatically" — [Retool](https://retool.com/resources/migrate-lovable-app-to-retool) (search summary).
- **Superblocks:** "From $100/seat/month", with an on-prem agent, SSO, RBAC and audit logs — [Superblocks](https://www.superblocks.com/blog/replit-enterprise) (vendor).
- **Wiz and Aikido:** available as Lovable Enterprise connectors ("Aikido AI pentest and Wiz SCA/SAST") — [Lovable enterprise docs](https://docs.lovable.dev/introduction/lovable-for-enterprise).
- **Builder-side scanner traction:** Vibe App Scanner (founded Dec 2025):
  - Go plan $19/mo, Pro $39/mo.
  - **MRR $856 from 34 active subscriptions**; all-time revenue $5,646.
  - "Verified with" Stripe, updated 13 Oct 2026.
  - Source: [TrustMRR](https://trustmrr.com/startup/vibe-app-scanner).
  - Its Show HN got 1 point — [HN item 46577230](https://news.ycombinator.com/item?id=46577230).
- **Free open-source building blocks exist:**
  - "supashield", a CLI to test Supabase RLS policies — [HN 45607925](https://news.ycombinator.com/item?id=45607925); [GitHub](https://github.com/Rodrigotari1/supashield).
  - "KeyLeak Detector" — [HN 45786192](https://news.ycombinator.com/item?id=45786192); [GitHub](https://github.com/Amal-David/keyleak-detector).
- **MSP tooling moving into shadow AI:**
  - **CIPP v10.6.0** release notes describe a Shadow AI "reporting and executive report". They note detection gaps because much AI use happens in the browser, and a browser-based method is planned for the next release — [newreleases.io CIPP v10.6.0](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0) (release roughly Jul 2026; the page says only "3 months ago").
  - CyberDrain claims "9000+ active MSPs" — [CyberDrain CIPP](https://cyberdrain.com/products/cipp/) (vendor).
  - Augmentt's "Discover" product covers "AI & SaaS discovery" for MSPs — [Augmentt](https://www.augmentt.com/) (vendor).
- **SASE/CASB limits:** a RedAccess-authored piece argues CASB "can't separate custom apps on a platform's subdomains from the platform itself", and that SSE "sees traffic to the platform's domain but lacks application-level context" — [THN partner piece](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html) (vendor argument, not independent). **I found no Netskope or Zscaler primary documentation on vibe-coding platforms** (search returned nothing; Netskope site search was truncated).
- **Outside-in discovery feasibility test (14 Oct 2026):**
  - Cert Spotter's CT API refused every platform domain I tried: "Cannot search lovable.app because it is not beneath an eTLD available for public registration". The same applied to base44.app, netlify.app, replit.app and vercel.app — [Cert Spotter API](https://api.certspotter.com/v1/issuances?domain=lovable.app).
  - crt.sh returned 502 on all attempts, so **I could not determine whether these platforms issue per-app certificates (enumerable) or wildcards (not enumerable).**

### Inferences
- **Who will absorb what:**
  - Shadow-AI *usage* discovery (an employee signed up for Lovable) is becoming a checkbox in MSP tools (CIPP, Augmentt) and SaaS-security tools (Nudge). That is a feature, not a wedge.
  - In-workspace *governance* is being absorbed by the platforms (A3).
  - Enterprise *session-layer* control is RedAccess's pitch.
  - The unabsorbed residue is **(i) an inventory of apps actually published, including from personal accounts and across platforms; (ii) data-exposure verification of those apps; (iii) ownership and handover.** The first two are hard outside-in.
- **The prior notes' "scan certificate-transparency logs" recommendation is weaker than assumed.** Platform suffixes are on the PSL, a major CT search vendor blocks enumeration beneath them, and wildcard certificates (unverified) would hide app names entirely. Inside-out discovery (client-authorized identity logs, mailbox signup notices, employee self-registration) is more realistic for a solo founder.
- The tiny revenue of Vibe App Scanner ($856 MRR after about 10 months) is the closest observable willingness-to-pay data point. It is **disconfirming for a builder-facing scanner**, though not decisive for an MSP- or IT-facing inventory product, which has a different buyer.

### Gaps
- No pricing found for RedAccess, Escape, Zenity, Noma, Reco, Wiz, Netskope, Zscaler or Retool.
- RedAccess funding not found.
- Microsoft Power Platform CoE and Power Platform "Vibe" were not re-checked; see prior notes.
- Whether Lovable, Base44 and Replit apps get individual TLS certificates is unverified (crt.sh down).

---

## B1. Microsoft's Copilot deployment blueprint and SharePoint Advanced Management (SAM) bundling: status Oct 2026

### Takeaway
Microsoft has made the "hidden insight" in the prior notes free. **SAM, included with any Copilot license (one licensed user unlocks it), now provides:**
- **site attestation policies**, where site owners confirm necessity, ownership, membership, permissions and sharing, with read-only or archive enforcement;
- **site access reviews** delegated to owners of overshared sites;
- site ownership policies, "Everyone except external users" (EEEU) insights, permission-state reports, Restricted Content Discovery (RCD) and AI insights.

The owner-attestation loop that the prior notes called the paid gap is native, per tenant.

### Cited Findings
- **Blueprint:**
  - "Secure & Governed Data Foundation for Microsoft Copilot" (ms.date 6 May 2026, updated 18 Aug 2026) has three pillars: remediate oversharing, set up guardrails, meet regulations.
  - It states SAM "is included with your Microsoft Copilot license."
  - It provides PDF and PowerPoint downloads and links the free Microsoft Zero Trust Assessment.
  - Source: [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance).
- **SAM features included with Copilot licenses**, per the table for "Enterprise and business commercial customers… *Microsoft Copilot (WW)*":
  - site ownership policy, active mode;
  - inactive-site policy;
  - **site attestation policy**, active mode;
  - content management assessment;
  - block-download policy;
  - Restricted Access Control and Restricted Content Discovery;
  - sharing-links reports;
  - EEEU insights;
  - permission-state reports;
  - **site access review for all reports**;
  - change history.

  Sensitivity-label reports require E5. Source: [Microsoft Learn, SAM features in Copilot licenses, updated 18 Aug 2026](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license).
- **Site attestation detail:**
  - Owners or admins are asked whether the site "is still needed and whether its ownership, membership, permissions, and sharing settings remain appropriate".
  - Cadence is 3, 6 or 12 months.
  - After three monthly notifications, enforcement can be "Read-only access" or "Archive".
  - Emails can be customized, and a CSV report is produced per run.
  - Up to 10,000 sites per CSV scope.
  - Source: [Microsoft Learn, updated 19 Aug 2026](https://learn.microsoft.com/en-us/sharepoint/request-site-attestations).
- **SAM also lists** "Initiate site access reviews to delegate the process of reviewing DAG reports to site owners of overshared sites" and AI insights on reports — [SAM overview, updated 18 Aug 2026](https://learn.microsoft.com/en-us/sharepoint/advanced-management).
- **Licensing conflict:**
  - The SAM prerequisites page lists base subscriptions as Office 365 E3/E5/A5, Microsoft 365 E1/E3/E5/A5 and government plans. It **does not list Microsoft 365 Business plans**, yet says "at least one user… assigned a Microsoft Copilot license" unlocks SAM Copilot features — [Microsoft Learn, SAM prerequisites](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-prerequisites).
  - The features page explicitly covers "business commercial customers" — [features page](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license).
  - Fusion Computing, an MSP for 10–150-employee firms, says SAM is "included with a paid Copilot licence" and uses it in client engagements — [Fusion Computing](https://fusioncomputing.ca/microsoft-365-copilot-oversharing-canadian-smb/).
- **Microsoft 365 Lighthouse (MSP multi-tenant console):**
  - "Copilot insights" (Sep 2024) shows Copilot usage, license assignment, recommended customers and deployment progress for recommended enablement tasks.
  - The what's-new log (last entry May 2025; page updated Apr 2026) shows **no oversharing or SharePoint-permission feature**.
  - Source: [Lighthouse what's new](https://learn.microsoft.com/en-us/microsoft-365/lighthouse/m365-lighthouse-whats-new).

### Inferences
- **This contradicts the prior notes' candidate card**, which named "owner attestations, exception tracking and client-ready evidence" as the paid gap. Owner attestation, delegated access review and enforcement are now native and free with Copilot.
- What remains outside Microsoft:
  1. **Multi-tenant aggregation** for MSPs (Lighthouse lacks oversharing views).
  2. **Client-presentable before/after reporting.**
  3. Remediation labor.

  Items 1 and 2 are addressed by competitors (B3).

### Gaps
- No Microsoft roadmap item was found for adding oversharing to Lighthouse. Absence of evidence is not evidence of absence.
- The SAM base-license conflict for Business Standard and Premium tenants is unresolved from primary text.

---

## B2. Copilot adoption and SMB SKU pricing

### Takeaway
Microsoft reports over 30M paid M365 Copilot seats as of its FY26 Q4 (reported 30 Jul 2026), up from 15M in January. It has also pushed SMB pricing down: Copilot Business is $21/user/month (≤300 seats), and permanent bundles started 1 Jul 2026 at $23.50 (Business Standard) and $32 (Business Premium). **No SMB-specific seat count exists**, and Nov 2025 reporting described SMB uptake as mostly pilots.

### Cited Findings
- **Seat counts:**
  - Nadella: "We now have over 30 million paid Microsoft 365 Copilot seats" (FY26 Q4). No SMB breakdown — [UC Today, 30 Jul 2026](https://www.uctoday.com/unified-communications/microsoft-365-copilot-passes-30-million-paid-seats-as-cloud-and-ai-growth-power-record-quarter).
  - Earlier: 15M paid seats among 450M M365 commercial subscribers (Jan 2026) — [Directions on Microsoft, 29 Jan 2026](https://www.directionsonmicrosoft.com/blog/microsoft-claims-15-million-paid-m365-copilot-seats) (search summary). 20M at FY26 Q3 — [No Jitter](https://nojitter.com/ai-automation/microsoft-365-copilot-hits-20-million-paid-seats) (search summary).
  - A third-party estimate puts paid seats at about 6.6–6.7% of paid commercial seats (search summary; unverified).
- **Copilot Business price:**
  - "$21 per user per month, effective December 1, 2025, for customers on any Microsoft 365 Business plan", down from $30, for ≤300 employees. Uptake is early, "most customers still in pilots or using the tool with a small subset of employees", with data governance among the cited challenges — [Computerworld, 19 Nov 2025](https://www.computerworld.com/article/4093224/).
  - Pax8 terms:
    - $21 annual/annual, with an $18 promo from 1 Dec 2025 to 31 Dec 2026.
    - $25.20 monthly/monthly.
    - "Up to 300 users and no seat minimum".
    - Source: [Pax8 blog, updated 8 Jul 2026](https://www.pax8.com/blog/?p=5825). Its bundle table has internal inconsistencies (Business Premium listed at $23 standard vs $32 promo).
- **Permanent bundles from 1 Jul 2026:**
  - Business Standard + Copilot Business: $282/user/year.
  - Business Premium + Copilot Business: $384/user/year.
  - Business Basic + Copilot Business: $252/year (25% promo through 31 Dec 2026).
  - 1–300 seats, annual commitment.
  - Source: [Sherweb, 16 Jun 2026](https://www.sherweb.com/blog/microsoft-ecosystem/microsoft-updates-msps-june-2026).
  - Corroborated as $23.50 and $32.00 per user per month by a New Jersey MSP — [Strategic Micro Systems, 5 Jun 2026](https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/).
  - **Conflict:** a Collab365 summary of a 28 May 2026 Microsoft announcement says the plan "folds the AI assistant into existing Business Standard and Premium licences", with prices not released — [Collab365, 29 May 2026](https://spaces.collab365.com/posts/microsoft-bundles-copilot-into-its-small-business--zz6N8Y). The partner sources describe *new bundled SKUs at higher prices* rather than Copilot added to existing licenses. The partner pricing is more specific and corroborated.

### Inferences
- Demand for readiness work should rise as bundles make Copilot the default SMB upsell. However, **each Copilot-licensed SMB tenant also gets SAM's oversharing toolkit free.** The same event that creates demand also ships Microsoft's remedy.
- The installed base in SMB is unknown. If SMB clients mostly run small pilots (Computerworld), MSP readiness projects may be small, one-off and services-led.

### Gaps
- No Microsoft-reported SMB or Copilot Business seat count.
- No primary Microsoft page for bundle prices (product page returned 503).
- No data on partner incentives that pay MSPs for Copilot deployment or readiness.

---

## B3. Is there truly no multi-tenant, MSP-priced oversharing product? (Answer: there are several)

### Takeaway
**The premise is false.** At least six products sell multi-tenant or MSP-oriented Copilot readiness and oversharing tooling:
- **CIPP:** open source, "9000+ active MSPs" claimed. It has a Copilot readiness report and a SharePoint Sharing Report that can invalidate links.
- **Orchestry Starter:** $2,499/tenant/year, multi-tenant, with a Copilot Readiness Dashboard that flags oversharing.
- **Cloudiway AI Readiness Assessment:** a full white-label MSP program; SOC 2 Type II and ISO 27001.
- **Inforcer:** multi-tenant, with Copilot Readiness Assessments.
- **AvePoint Elements:** multi-tenant, MSP-focused.
- **CoreView:** multi-tenant, with SharePoint oversharing controls.

Syskit, which the prior notes said had no MSP offering, has a partner program and a "Copilot readiness" use case, though without published MSP terms.

### Cited Findings
- **CIPP v10.6.0** (around Jul 2026):
  - "the copilot readiness report" in the dashboard.
  - A new "Copilot and AI section" (pin chat, block content, enable or disable Copilot).
  - A "SharePoint Sharing Report" showing "how much of your data in your tenant has been shared", link counts and top sharers, with the ability to "invalidate links that should not be shared".
  - Purview, apps-with-access and auto-labeling "coming soon".
  - Source: [newreleases.io](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0).
  - Open source; "9000+ active MSPs" — [CyberDrain](https://cyberdrain.com/products/cipp/) (vendor claim; hosted pricing not shown).
- **Orchestry Starter (formerly Beacon):**
  - "read-only Microsoft 365 reporting and governance platform for partners and MSPs".
  - Manages multiple customer tenants from one interface.
  - A **Copilot Readiness Dashboard** with readiness score, and recommendations flagging "broken permission inheritance, oversharing, inactive sites, and missing sensitivity labels".
  - Source: [Orchestry Starter](https://www.orchestry.com/starter).
  - Price: "Starting at $2,499 per tenant/year", unlimited users; Professional $4,999 and Enterprise $7,499 per tenant/year; free trial — [Orchestry pricing](https://www.orchestry.com/pricing).
- **Cloudiway AI Readiness Assessment:**
  - 100+ checks across 19 risk categories: anonymous links, "Everyone" shares, broken inheritance, dormant guests, admins without MFA, external forwarding.
  - OAuth "read-only delegated permissions"; "No data stored".
  - Claims "SOC 2 Type II" and ISO 27001.
  - "Full white-labeling for MSPs".
  - Pricing is quote-only.
  - Source: [Cloudiway product page](https://cloudiway.com/products/ai-readiness-assessment) (vendor).
  - Its MSP program pitches client pricing of a "Paid Audit: $5K–$15K per engagement" and "Risk Remediation: $15K–$40K" — [Cloudiway MSP program](https://cloudiway.com/ai-readiness-msp-program/) (vendor; aspirational, not market data).
- **Cloudiway's own comparison (5 May 2026)** lists:
  - AvePoint: "Multi-tenant management for large enterprises and MSPs", white-label "Limited", "Subscription, mid-to-high".
  - Varonis: "No MSP white-label model", "Enterprise subscription, high".
  - Concentric AI: "Per-user subscription, mid-to-high".
  - Native Microsoft: "findings scattered across 5+ portals", "Reports not client-presentation ready".
  - PowerShell + ScubaGear: "8 to 10 days of senior consultant time per tenant".
  - Source: [Cloudiway blog](https://cloudiway.com/blog/ai-readiness-assessment-platforms-comparison-2026/) (vendor ranks itself).
- **Inforcer:** "single dashboard for managing policies and compliance across multiple Microsoft 365 tenants", plus Copilot Readiness Assessments on six pillars. Request-pricing only — [Inforcer, Nov 2025 (updated 2026)](https://www.inforcer.com/insights/microsoft-365-copilot-business-copilot-for-the-smb).
- **AvePoint Elements:** "multi-tenant management, baseline enforcement, and delegated admin". An MSP case study used Workspace Management and Risk Management to review permissions and fix overshared Teams before a Copilot rollout. No price — [AvePoint MSP page](https://avepoint.com/solutions/scale-msp-growth).
- **CoreView:** multi-tenant "centralized management"; "Stop SharePoint oversharing before it becomes a breach". No price — [CoreView MSP](https://www.coreview.com/msp).
- **Syskit:** a partner program with a "Copilot readiness" use case. No MSP terms published — [Syskit partners](https://www.syskit.com/partners/).
- **Augmentt:** multi-tenant baselines and drift (CIS/NIST/SCuBA), MSP-branded reports. **No Copilot readiness or oversharing feature stated** — [Augmentt](https://www.augmentt.com/).
- **Microsoft Marketplace consulting offers:** Invero sells a "2-Week Assessment" with a tenant-wide oversharing Power BI dashboard — [Microsoft Marketplace](https://marketplace.microsoft.com/nb-no/product/invero.copilot_readiness?country=CA) (search summary).
- **Prevalence claims (vendor, unverified):** Rencore reports 15–30% of SharePoint content shared more broadly than intended across 200+ tenants — [Rencore](https://hub.rencore.com/blog/copilot-readiness-oversharing) (search snippet; page returned 404 on fetch).

### Inferences
- Even at the micro-tenant end, CIPP is free or low-cost and already used by many MSPs (vendor claim). It now covers Copilot readiness and link cleanup, which removes the "price gap" for MSPs managing 10–50-seat clients.
- Orchestry's $2,499/tenant/year works out to about $208/tenant/month (my arithmetic). That is steep for a 10-seat client, but CIPP and native SAM undercut it. A new entrant would be squeezed between free (Microsoft, CIPP) and established, credentialed vendors (Cloudiway SOC 2/ISO, AvePoint).

### Gaps
- Pricing not found for Cloudiway, Inforcer, AvePoint Elements, CoreView, Rencore, Liongard or Nerdio. Liongard and Nerdio were not checked (budget).
- No independent review comparing these tools.

---

## B4. What MSPs charge for Copilot readiness and oversharing work, and how they deliver it

### Takeaway
Published prices range from **$2,500 flat** (solo consultant) to **$6,500–$10,500** (3–5 week readiness), and up to a vendor-pitched $5K–$15K audit. One MSP estimates **40–60 IT-hours over 30 days for a 50-seat tenant** using **only native Microsoft tools** (SAM, Purview). The money is in services, not tool subscriptions.

### Cited Findings
- **Creative Data Concepts:** Copilot readiness covering an oversharing audit, label design, permissions triage and remediation, guest review, and a Purview baseline. Takes 3–5 weeks; "$6,500–$10,500", "Tiered by data volume and complexity" — [Creative Data Concepts](https://creativedata.net/services/copilot-readiness) (location not stated).
- **Justin McKelvey:** AI Readiness Assessment "$2,500 flat", two weeks, credited against an install within 90 days; AI Team Rollout from $4,500. He advises: "Price the readiness job as a fixed scope with a defined end" — [Justin McKelvey, 5 Oct 2026](https://justinmckelvey.com/blog/ai-for-msps).
- **Fusion Computing (Toronto; clients with about 10–150 employees):**
  - Five phases: Inventory, Classify, Triage, Remediate, Lock.
  - A 50-seat tenant takes **40–60 IT-hours over 30 calendar days**, of which inventory is 8–12 hours. A 65-user engagement's inventory took 9 hours.
  - Tools are **SAM and Purview**; "Scripts or third-party tools: None named". Price not stated.
  - Source: [Fusion Computing](https://fusioncomputing.ca/microsoft-365-copilot-oversharing-canadian-smb/).
- **Other MSPs:**
  - Strategic Micro Systems (Parsippany, NJ; "AI-first managed IT") recommends a permissions audit before Copilot but lists no price — [StMicro, 5 Jun 2026](https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/).
  - Aldridge (managed IT) offers a "Copilot AI Readiness Self-Assessment" but no price — [Aldridge](https://aldridge.com/microsoft-lowers-copilot-pricing-for-small-and-midsize-businesses/).
- **Rollout delays (secondary):** a Gartner survey (June 2025, 132 IT leaders) reportedly found 40% of organizations delayed Copilot rollout by three months or more — relayed by [MyWorkDrive](https://www.myworkdrive.com/blog/microsoft-365-copilot-oversharing) (search summary; primary not seen).

### Inferences
- At $6,500–$10,500 per project and 40–60 hours of labor, the MSP's cost is **labor**, not tooling. A tool saving, say, 10 hours would be worth a few hundred dollars per project. That is within reach of CIPP (free) and Orchestry, and below the threshold that makes MSPs switch tools (inference).
- An India-based founder's real advantage here might be **white-label remediation labor** (a services business). That is a different candidate and is not evaluated here.

### Gaps
- No survey of MSP readiness pricing. Leadership Through Data's reported £2.50/user (UK) appeared only in a search summary without a usable URL, so it is excluded.

---

## C1. Both candidates: who pays, how much, buying process, willingness to pay, why incumbents haven't served the segment

### Takeaway
- **For B**, the buyer (MSP owner) is real and already paying, but for *services*. Tool budgets are crowded by free Microsoft features, free CIPP and credentialed specialists.
- **For A**, the buyer is undefined:
  - SMB owners don't know the problem exists.
  - MSPs have no evidenced client demand.
  - Enterprise security teams buy from RedAccess, Wiz or platform Enterprise tiers.

  The only hard willingness-to-pay data point (Vibe App Scanner, $856 MRR) is weak and on the builder side.

### Cited Findings
- **MSP tool price envelope:**
  - Orchestry Starter: $2,499/tenant/year — [Orchestry pricing](https://www.orchestry.com/pricing).
  - Nudge: $5/mailbox/month — [Nudge](https://www.nudgesecurity.com/).
  - Prior notes: RevSync $299–$599/mo; per-tech PSA pricing $89–$209 — `it_msp_security_data.md` Q1.
- **MSP service prices:** $2,500 to $10,500 per readiness project ([McKelvey](https://justinmckelvey.com/blog/ai-for-msps); [Creative Data Concepts](https://creativedata.net/services/copilot-readiness)).
- **Builder-side vibe-app scanner:** 34 subscriptions, $856 MRR — [TrustMRR](https://trustmrr.com/startup/vibe-app-scanner).
- **Platforms' enterprise go-to-market:**
  - Wix says enterprise-sized organizations adopt Base44 self-serve with "no sales team" — [Yahoo Finance](https://finance.yahoo.com/news/wix-com-q4-earnings-call-165003576.html) (search summary).
  - Replit opened self-serve Enterprise for contracts up to $200,000 — [Superblocks](https://www.superblocks.com/blog/replit-enterprise).
- **Microsoft's channel:** SMB Copilot bundles are sold through CSP partners on annual terms ([Sherweb](https://www.sherweb.com/blog/microsoft-ecosystem/microsoft-updates-msps-june-2026)). Pax8 offers "client readiness assessment" resources ([Pax8](https://www.pax8.com/blog/?p=5825)).

### Inferences
- **B, buying process:** the MSP owner or vCIO picks tools through peer groups and distributor marketplaces (Pax8), and expects a free trial (Orchestry, Augmentt and CIPP all offer free or trial access). The sale is to a tool-saturated buyer whose evaluation baseline is "what CIPP or SAM already shows". Incumbents *have* served this segment; the premise "incumbents haven't served it" fails.
- **A, buying process:** there is no established budget line. The likeliest path is MSP security add-ons, priced per client per month, after a triggering incident or a cyber-insurance or compliance question. Incumbents haven't served SMBs because:
  - enterprise vendors price for CISOs;
  - platforms only see their own paying workspaces;
  - MSP tools currently detect *usage*, not *published apps* (inference).

  Whether SMBs will pay is **unverified**.

### Gaps
- No interviews or forum evidence (Reddit not accessed) on MSP willingness to pay for either product. No cyber-insurance questionnaire evidence asking about citizen-built apps.

---

## C2. Trust and credential barriers for an unknown India-based solo vendor (admin consent, SOC 2, Microsoft partner status)

### Takeaway
- **B needs tenant-wide SharePoint and Graph read access** in client tenants. That is the highest-trust request in the M365 ecosystem. Competitors advertise SOC 2 Type II and ISO 27001 (Cloudiway).
- Publisher verification is free and has no stated country restriction. A first SOC 2 typically costs **$10k–$80k+** plus 1–5 months of preparation and a 3–12-month Type 2 window.
- **A can avoid admin consent entirely** by working from client-authorized exports and owner self-registration. It still faces authorization and legal limits on probing apps.

### Cited Findings
- **Publisher verification:**
  - Requires a "Partner One ID for a valid Microsoft AI Cloud Partner Program account that has completed the verification process", an app registered with an Entra work account, and a publisher domain that is not `*.onmicrosoft.com`.
  - "Microsoft doesn't charge developers for publisher verification."
  - Since Nov 2020, if risk-based step-up consent is enabled, "users can't consent to most newly registered multitenant apps that *aren't* publisher verified"; a warning appears instead.
  - The page notes that verification doesn't indicate certifications, and points to Microsoft 365 App Certification.
  - No country restrictions are stated.
  - Source: [Microsoft Learn, updated 15 Jun 2026](https://learn.microsoft.com/en-us/entra/identity-platform/publisher-verification-overview).
- **SAM admin rights:** the "SharePoint Advanced Management Administrator" role includes "Viewing metadata (names, paths, URLs) across SharePoint content" and "Removing permissions from content at scale" — [SAM prerequisites](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-prerequisites).
- **GDAP:** partners get "granular and time-bound access"; "Customers must explicitly grant the least-privileged access to their partners" — [Microsoft Learn GDAP, updated 27 May 2026](https://learn.microsoft.com/en-us/partner-center/customers/gdap-introduction).
- **SOC 2 cost:**
  - "A SOC 2 audit fee usually runs between $10,000 and $50,000".
  - Readiness work from about $10,000; all-in first SOC 2 costs "$10,000 to $80,000 or more".
  - Preparation takes 1–5 months; the Type 2 observation window is 3–12 months.
  - Source: [Vanta (vendor)](https://www.vanta.com/collection/soc-2/soc-2-audit-cost).
- **Competitor trust signals:** Cloudiway claims SOC 2 Type II, ISO 27001, "No data stored" and read-only delegated permissions — [Cloudiway](https://cloudiway.com/products/ai-readiness-assessment). Lovable holds SOC 2 Type II, ISO 27001:2022 and AIUC-1 — [Lovable enterprise docs](https://docs.lovable.dev/introduction/lovable-for-enterprise).

### Inferences
- **For B**, an unknown solo vendor asking an MSP to consent a multi-tenant app with read access to every client's SharePoint competes against a free, self-hosted, open-source tool (CIPP) that MSPs run in their own environment. That is a near-insurmountable trust gap without SOC 2, references and a US entity. Whether a US entity is needed is my inference, not sourced.
- **For A**, an inside-out approach needs no Graph consent: the MSP uploads CSV exports it already has, employees self-register apps, and checks run only on apps the client authorizes. This sidesteps the B-style barrier. It still requires:
  - written client authorization before any active testing;
  - care with platform terms of service;
  - care with laws on unauthorized access.

  The legal points are inferences; no legal source was consulted.

### Gaps
- No source on how MSPs vet small tool vendors (e.g., required SOC 2 or insurance). No source on platform terms of service for third-party security testing of hosted apps. No legal source on US computer-misuse exposure for passive checks.

---

## C3. Consolidated disconfirming evidence (attempts to disprove each candidate)

### Takeaway
**B is disproved on its core premises:**
- Multi-tenant MSP tools exist (including a free one).
- The "owner attestation" gap is native in SAM.
- The work is monetized as services.
- The trust bar is high.

**A survives disproof only in a narrowed form:** cross-platform inventory and handover of *published* apps, discovered inside-out. Platforms, MSP tools and enterprise vendors are absorbing the adjacent pieces, and willingness to pay is unproven.

### Cited Findings
- **B, Microsoft bundling:** SAM with attestation and access reviews is included with Copilot for business tenants — [Microsoft Learn](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license).
- **B, competitors:** CIPP ([newreleases.io](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0)), Orchestry ([pricing](https://www.orchestry.com/pricing)), Cloudiway ([MSP program](https://cloudiway.com/ai-readiness-msp-program/)), Inforcer ([Inforcer](https://www.inforcer.com/insights/microsoft-365-copilot-business-copilot-for-the-smb)), AvePoint ([AvePoint](https://avepoint.com/solutions/scale-msp-growth)), CoreView ([CoreView](https://www.coreview.com/msp)).
- **B, services not tools:** Fusion Computing delivers with SAM and Purview only, "None named" for third-party tools — [Fusion](https://fusioncomputing.ca/microsoft-365-copilot-oversharing-canadian-smb/).
- **B, low urgency signal:** SMB Copilot use is mostly pilots ([Computerworld](https://www.computerworld.com/article/4093224/)). Zero HN stories match "copilot oversharing sharepoint" ([HN Algolia](https://hn.algolia.com/api/v1/search?query=copilot%20oversharing%20sharepoint&tags=story)).
- **A, platform absorption:** Lovable Security Center, publishing controls and Workspace Insights ([docs](https://docs.lovable.dev/introduction/lovable-for-enterprise)); Replit governance tools ([Replit](https://replit.com/blog/new-enterprise-governance-tools)); Vercel protection on all plans ([Vercel](https://vercel.com/docs/deployment-protection)).
- **A, MSP-tool absorption of usage discovery:** CIPP Shadow AI report ([newreleases.io](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0)); Augmentt "AI & SaaS discovery" ([Augmentt](https://www.augmentt.com/)).
- **A, enterprise competitor naming the exact problem:** RedAccess "Shadow Builders Security — Govern Vibe-Coded Apps" ([Red Access](https://www.redaccess.io/)).
- **A, weak willingness to pay:** $856 MRR builder scanner ([TrustMRR](https://trustmrr.com/startup/vibe-app-scanner)); low HN engagement ([HN Algolia](https://hn.algolia.com/api/v1/search?query=vibe%20coded%20apps%20exposed&tags=story)).
- **A, feasibility:** platform suffixes on the PSL ([PSL](https://publicsuffix.org/list/public_suffix_list.dat)); Cert Spotter refuses enumeration ([Cert Spotter API](https://api.certspotter.com/v1/issuances?domain=lovable.app)).

### Inferences
- The strongest argument *against* A is that "vibe-app governance" could become a line item inside existing MSP security stacks (CIPP, Augmentt, SaaS-security tools) once those tools add platform-specific checks. The window may be 12–24 months, which is speculative.
- The strongest argument *for* A is structural. Apps built outside a paying workspace are invisible to platform consoles, and no platform will build a cross-competitor inventory.

### Gaps
- No direct buyer evidence (interviews, forums) for either candidate.

---

## C4. Twenty specific first-customer targets (by type or verifiable public information)

### Takeaway
The same MSP channel serves both candidates. Below are 10 named firms or consultants publicly selling Copilot or AI readiness (prime B targets, and plausible A design partners because they already sell "AI governance" to SMBs), plus 10 verified communities for reaching MSPs at scale. Named firms are **leads, not validated prospects**.

### Cited Findings
**Named MSPs and consultants publicly selling Copilot/AI readiness**
1. **KW Corporation:** published "Copilot permissions debt" (3 Oct 2026) promoting its managed-IT practice — [KW Corp](https://kw-corp.com/2026/10/03/copilot-permissions-debt/).
2. **Strategic Micro Systems** (Parsippany, NJ; serves NJ/NY/CT; "AI-first managed IT") — [StMicro](https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/).
3. **Aldridge** (managed IT outsourcing and co-managed IT; offers a Copilot AI Readiness Self-Assessment) — [Aldridge](https://aldridge.com/microsoft-lowers-copilot-pricing-for-small-and-midsize-businesses/).
4. **Creative Data Concepts** (Copilot readiness $6,500–$10,500) — [Creative Data](https://creativedata.net/services/copilot-readiness).
5. **Inventive HQ** (managed Copilot readiness using AvePoint) — [Inventive HQ](https://inventivehq.com/services/microsoft-365-migration/copilot-readiness) (search summary).
6. **Fusion Computing** (Toronto; 10–150-employee clients; 40–60-hour oversharing projects) — [Fusion](https://fusioncomputing.ca/microsoft-365-copilot-oversharing-canadian-smb/) (Canadian, not US).
7. **Justin McKelvey** (AI readiness for MSP-style clients, $2,500 flat) — [blog](https://justinmckelvey.com/blog/ai-for-msps).
8. **Invero** (Microsoft Marketplace two-week Copilot readiness and oversharing assessment) — [Marketplace](https://marketplace.microsoft.com/nb-no/product/invero.copilot_readiness?country=CA) (search summary).
9. **EPC Group** (publishes SharePoint oversharing remediation guides; enterprise-leaning) — [EPC Group](https://www.epcgroup.net/blog/microsoft-copilot-oversharing-audit-enterprise-guide-2026) (search summary).
10. **CIAOPS / Robert Crane** (sells MSP AI playbooks; Australia; an MSP influencer channel rather than a buyer) — [CIAOPS blog](https://blog.ciaops.com/2026/06/26/before-you-buy-the-copilot-licence-do-this-first/); [Gumroad](https://directorcia.gumroad.com/l/mspaipb) (search summary).

**Communities and peer groups (verified to exist)**

11. **IT Nation Evolve (ConnectWise) peer groups.** Evolve 1 is for small MSPs aiming past $1M revenue (monthly virtual); Evolve 2 is for owners and executives (quarterly in person) — [ConnectWise blog](https://connectwise.com/blog/it-nation/msp-peer-group) (search summary); [IT Nation Evolve](https://itnation.connectwise.com/evolve).
12. **MSPGeek:** open technical community with a Discord — [SuperOps roundup, updated 7 Jul 2026](https://superops.com/blog/top-msp-communities-and-peer-groups).
13. **GTIA ISAO** (comptiaisao.org now redirects to GTIA cybersecurity programs; access included for "MSPs, cloud services providers, MSSPs") — [comptiaisao.org → GTIA](http://gtia.org/membership/cybersecurity-programs). The CompTIA community was reportedly renamed GTIA — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
14. **Pax8** (Academy plus Marketplace; sells the SMB Copilot bundles) — [Pax8](https://www.pax8.com/blog/?p=5825); [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
15. **CIPP user base** ("9000+ active MSPs" claimed; already has Shadow AI and Copilot reports, so it is both a channel and a competitor) — [CyberDrain](https://cyberdrain.com/products/cipp/).
16. **ASCII Group** — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
17. **MSP Alliance** (governance, risk and compliance focus) — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
18. **TechTribe** — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
19. **Taylor Business Group** (peer groups) — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).
20. **MSP-Ignite** (small peer groups) — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups).

Additional channels: r/msp and the SuperOps Community — [SuperOps](https://superops.com/blog/top-msp-communities-and-peer-groups) (r/msp not accessed in this research).

### Inferences
- **For A specifically**, the best first targets by *type* are:
  - MSPs serving regulated SMB verticals that RedAccess's exposures touched: healthcare and long-term care, financial services, logistics ([THN](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html); prior notes).
  - Firms 1–4 and 7 above, which already sell "AI readiness" and could bolt a "vibe-app census" onto it.
- **The HTG Peer Groups name** is commonly said to have been folded into IT Nation Evolve after a ConnectWise acquisition. **I did not verify this.**
- Mid-market IT leader communities (e.g., SIM, CIO forums) were not verified and are excluded.

### Gaps
- US headquarters not confirmed for Aldridge, Creative Data Concepts or Inventive HQ. No contact-level validation was done. Membership counts and costs for peer groups were not published in the sources.

---

## C5. Narrowest MVP (2–8 weeks, solo non-engineer with AI coding tools) and a 14-day experiment with kill criteria

### Takeaway
- **A:** build a *concierge-first* "Vibe-App Census & Handover Pack" sold through MSPs. It is inside-out (CSV uploads plus owner self-registration), checks only authorized apps, and produces a white-label PDF. No Graph consent and no outside-in crawling.
- **B (if tested at all):** a consent-free "SAM evidence pack" that turns exported SAM and CIPP reports into client-ready, multi-tenant before/after PDFs. Its kill criteria are likely to trigger, given B3.

### Cited Findings
- Usable building blocks and constraints:
  - Open-source RLS tester ([supashield](https://github.com/Rodrigotari1/supashield)) and key-leak scanner ([KeyLeak Detector](https://github.com/Amal-David/keyleak-detector)).
  - Platform suffixes on the PSL ([PSL](https://publicsuffix.org/list/public_suffix_list.dat)).
  - SAM reports export to CSV, and site attestation produces a downloadable CSV report ([Microsoft Learn](https://learn.microsoft.com/en-us/sharepoint/request-site-attestations)).
  - CSA recommends lightweight app registration and a three-tier review (prior notes: [CSA, 2 Jun 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/)).
  - Lovable's pre-publish scan already covers RLS, auth gaps and exposed data **for apps inside Lovable**, so the MVP should *invoke* those native scans rather than duplicate them ([Lovable](https://lovable.dev/blog/how-lovable-protects-your-apps-automatically)).

### Inferences

**A: MVP (weeks 1–6)**
1. **Discovery inputs, no app consent:**
   - The MSP uploads exports it already has: the Entra or Google Workspace sign-in or OAuth app list, plus optional mail-gateway logs.
   - A script flags vibe-platform domains: lovable.dev/.app, replit.com/.app, base44.com/.app, bolt.new/.host, v0.app/vercel.app, netlify.app, supabase.co.
   - Limitation: email-plus-password signups are invisible in identity logs.
2. **"App passport" form**, sent by the MSP to the client's staff, records:
   - app URL, platform, account type (personal or company);
   - data used, users, owner, backup owner;
   - whether customer or patient data is involved.
3. **Authorized checks only, on apps the client confirms it owns:**
   - Is the app reachable without login?
   - Is it Google-indexed? (manual `site:` query)
   - Are keys exposed in the JavaScript bundle?
   - Does an RLS test pass (via the open-source CLIs)?
   - Run the platform's native scan where the app sits in a company workspace.
4. **Output:** a white-label PDF with:
   - the inventory;
   - a CSA-style three-tier risk rating;
   - copy-paste "fix prompts" for the builder;
   - a handover checklist: move to the company workspace, export to the company GitHub, rotate secrets, name a backup owner, set a sunset date.
5. **Build:** Next.js or Supabase with Claude, or Airtable/Tally plus a PDF template for a concierge version. Price *hypotheses* to test (not evidence): $500–$1,500 per client census (MSP marks up), or $49–$99/client/month for a quarterly re-census.

**A: 14-day experiment**
- Days 1–2:
  - Landing page.
  - A redacted sample report, built from a deliberately misconfigured demo app the founder makes on Lovable or Base44.
  - A list of 80 US MSPs (communities 11–20, firms 1–7, MSPs with healthcare or finance clients) and 20 mid-market IT managers.
- Days 3–10:
  - 100 personalized messages plus posts in MSPGeek and r/msp.
  - Offer: a free census for one client in exchange for a 30-minute debrief. **The paid price is stated up front.**
- Days 11–14: deliver the censuses and ask for a paid second client.
- **Success:**
  - ≥10 conversations.
  - ≥3 MSPs run a census on a real client.
  - ≥2 censuses surface at least one previously unknown published app holding business or customer data.
  - ≥2 written commitments to pay ≥$500 per census or ≥$50/client/month.
- **Kill if any of these happen:**
  1. <5 conversations from 100 contacts.
  2. ≥3 completed censuses find **zero** vibe-platform usage among SMB clients (the problem is not present in this segment).
  3. Zero payment commitments: interest only at $0.
  4. ≥50% of MSPs say CIPP, Augmentt, Nudge or platform Enterprise tiers already cover it.
  5. Any client or adviser deems the authorization model legally unacceptable.

**B: MVP, only if the founder insists**
- An upload-only tool. The MSP exports SAM data-access-governance and attestation CSVs, or CIPP sharing reports, per tenant.
- It generates a normalized multi-tenant view, plain-English risk summaries, owner email drafts and a QBR-ready before/after PDF.
- No Graph app, no consent.

**B: 14-day experiment**
- 15 calls with MSPs selling Copilot readiness (firms 1–9).
- **Kill if:**
  - <3 say CIPP, Orchestry, Cloudiway and SAM leave a gap they would pay to close; or
  - nobody commits ≥$50/tenant/month; or
  - most of their SMB clients have <5 Copilot seats.

### Gaps
- Not verified:
  - whether Entra or Google sign-in exports reliably show vibe-platform logins (depends on SSO use);
  - the legal and terms-of-service position for authorized external checks;
  - actual MSP price points.

  All of these must be tested in the experiment.

---

## C6. Verdicts

### Takeaway
- **(A) Vibe-coded app discovery, inventory, scanning and handover for SMBs via MSPs: ADVANCE WITH CONDITIONS (confidence: low–medium).** It is advanced only in the narrowed form: a cross-platform, inside-out census plus handover, concierge-first, sold through MSPs. Generic scanning and in-platform governance are already absorbed.
- **(B) Multi-tenant Copilot oversharing cleanup and attestation for MSPs: REJECT.** Its defining premises (no multi-tenant MSP product; owner attestation as the unmet gap) are contradicted by observed products and Microsoft documentation.

### Cited Findings
**Reasons for A (advance with conditions)**
- **Harm is documented and recurring:**
  - 18,697 records in one Lovable app ([The Register](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/)).
  - A private-app auth bypass on Base44 ([Wiz](https://www.wiz.io/blog/critical-vulnerability-base44)).
  - More than 2,000 corporate apps with sensitive data ([THN](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html)).
- **Supply is exploding:** Lovable at $600M annualized revenue and 1M projects a week ([TechCrunch](https://techcrunch.com/tag/lovable/)).
- **Platform governance stops at the paying workspace and is Enterprise-gated:** Lovable publishing controls and audit logs are Enterprise-only ([Lovable plans](https://docs.lovable.dev/introduction/subscription-plans)); Base44 and Bolt SSO are Enterprise-only ([Base44](https://base44.com/pricing); [Bolt](https://bolt.new/pricing)).
- **Conditions come from the disconfirming evidence:**
  - Usage discovery is being absorbed by MSP tools ([CIPP](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0); [Augmentt](https://www.augmentt.com/)).
  - RedAccess targets the same problem for enterprises ([Red Access](https://www.redaccess.io/)).
  - Builder-side willingness to pay is tiny ([TrustMRR](https://trustmrr.com/startup/vibe-app-scanner)).
  - Outside-in enumeration is impeded ([PSL](https://publicsuffix.org/list/public_suffix_list.dat); [Cert Spotter](https://api.certspotter.com/v1/issuances?domain=lovable.app)).

**Reasons for B (reject)**
- **Microsoft ships the remedy free with the license**, including owner attestation, delegated access reviews and enforcement ([SAM features](https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license); [site attestations](https://learn.microsoft.com/en-us/sharepoint/request-site-attestations)).
- **Multi-tenant MSP products exist at every price point:**
  - free and open-source CIPP with a Copilot readiness report and link invalidation ([newreleases.io](https://newreleases.io/project/github/KelvinTegelaar/CIPP/release/v10.6.0));
  - Orchestry Starter at $2,499/tenant/year ([Orchestry](https://www.orchestry.com/pricing));
  - white-label Cloudiway with SOC 2/ISO ([Cloudiway](https://cloudiway.com/products/ai-readiness-assessment));
  - Inforcer, AvePoint and CoreView ([Inforcer](https://www.inforcer.com/insights/microsoft-365-copilot-business-copilot-for-the-smb); [AvePoint](https://avepoint.com/solutions/scale-msp-growth); [CoreView](https://www.coreview.com/msp)).
- **MSPs monetize the work as services using native tools:** 40–60 hours, no third-party tools ([Fusion](https://fusioncomputing.ca/microsoft-365-copilot-oversharing-canadian-smb/)); $6.5k–$10.5k projects ([Creative Data](https://creativedata.net/services/copilot-readiness)).
- **The trust bar for tenant-wide SharePoint access is high**, and competitors carry SOC 2 and ISO 27001. A first SOC 2 costs $10k–$80k+ ([Vanta](https://www.vanta.com/collection/soc-2/soc-2-audit-cost); [publisher verification](https://learn.microsoft.com/en-us/entra/identity-platform/publisher-verification-overview)).

### Inferences
- **A, conditions to stay on the shortlist** (all must hold after the 14-day test):
  1. Discovery is inside-out and authorized: no crawling of third-party-hosted apps.
  2. MSPs commit to pay: ≥2 written commitments at ≥$500/census or ≥$50/client/month.
  3. Censuses actually find unknown, data-bearing apps in SMB clients.
  4. The founder positions the product as an *inventory and handover* product that calls platform-native scans, not as a scanner competing with Lovable, Wiz or Aikido.

  If condition 3 fails, the problem is an enterprise problem (RedAccess's market), not an SMB one, and A should be dropped.
- **B's salvageable sliver** is labor, not software: white-label, India-based remediation delivery for US MSPs at a lower cost than the 40–60 in-house hours. That is a services business with a different risk profile, and it would need its own validation. It should not be counted as this candidate advancing.
- **Founder fit:**
  - A's concierge MVP is buildable with AI coding tools and spreadsheets.
  - B would require secure multi-tenant Graph engineering plus SOC 2 before any MSP would consent. That is a poor fit for a solo, non-engineer, India-based founder with limited capital.

### Gaps
- Both verdicts rest on desk research. **No buyer interviews were conducted, and Reddit and MSP forums were not read.**
- The A verdict is particularly sensitive to condition 3 (prevalence in SMBs), for which no data exists.
