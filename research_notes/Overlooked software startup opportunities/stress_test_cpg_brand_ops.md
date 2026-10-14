# Stress test: (A) retailer/distributor deduction recovery and (B) multi-state packaging EPR reporting for emerging US CPG brands (as of 14 Oct 2026)

**Method note (read first).** This note builds on `physical_economy_ops.md` (Opportunity B for deductions, Opportunity D for EPR) and `regulatory_structural_shifts.md` (Opportunity 4 for EPR). It does not repeat their findings: the Flxpoint 1–5% deduction figure, Zenpack's state table, the Baker Donelson litigation summary, and Lorax EPI as an enterprise, demo-only vendor. It covers only the gaps.

- **Budget used:** all 25 WebSearch calls plus about 30 direct fetches.
- **Pages I could not open:**
  - Jenner & Block and Steptoe alerts (HTTP 403).
  - Capterra review pages (HTTP 403).
  - SupplyPike pricing (HTTP 504, twice).
  - cresicor.com (the domain does not resolve).
  - The L.E.K. PDF and the Oregon producer list PDF could not be read through the fetch tool, so I extracted their text locally with pdftotext.
- **Lower-confidence items:** findings marked "(search summary)" come from a search-result summary, not a page I opened.
- **Vendor figures:** many deduction statistics are vendor marketing and are labelled as such.
- **Labels:** **[F]** = observed fact with a source; **[I]** = my interpretation. All arithmetic in Inferences is mine, built on stated assumptions. None of it is a sourced market size.

## Q1. (A) How large is the deduction problem for emerging brands? (share of revenue, invalid rates, dispute windows, portals)

### Takeaway
The pain is real and documented. Founders, a 2024 class action against UNFI, trade press and accountants all describe deductions as a material, recurring margin leak that small brands struggle to contest. Hard numbers come almost entirely from vendors, though. "Share of revenue lost" claims range from 2–3% to 5–7%, and up to 15% when trade spend is included. Invalid-deduction rates are cited at 10–20%, or 40–60% if "disputable or preventable" is counted too. Dispute windows are short (about 45–90 days at retailers) or easy to miss, and every channel has its own portal (Retail Link/APDP, Partners Online, K-Solve in KeHE CONNECT, UNFI's emailed-spreadsheet process).

### Cited Findings
**Share of revenue lost (mostly vendor or interested-party claims)**
- **[F]** SPS Commerce says "brands lose 5–7% of annual revenue to deductions, chargebacks, and compliance fines." Its estimator says "deduction fees typically range from 1%–5%." Vendor claim, undated product page, accessed 14 Oct 2026 — [SPS Revenue Recovery](https://www.spscommerce.com/products/revenue-recovery/1p/)
- **[F]** Endless Commerce, a vendor (undated, ©2026), cites no sources. It says:
  - Brands selling into retail lose 2–5% of gross revenue to deductions.
  - "40–60% of deductions are invalid, disputable, or preventable."
  - A $15M wholesale brand typically sees $375K–$750K in annual deductions.
  - Structured management recovers $0.60–$0.80 per invalid dollar.
  - Validity by category: trade/promo 70–80% valid; compliance/logistics 50–60%; shortage/damage 30–40%; pricing 20–30%.

  — [Endless Commerce, deduction management playbook](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
- **[F]** Glimpse, in a vendor press release dated 29 Oct 2025: "Most brands lose 2–3% of topline revenue to invalid deductions." Unsourced — [BevNET PR](https://bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands)
- **[F]** Talk Business & Politics (Kim Souza, 4 Jan 2026) quotes Woodridge Group CEO Jon Allen:
  - Deductions and chargebacks "could erode profits by up to 15% of gross sales."
  - "10–20% of deductions are invalid, but untouchable" because teams are overloaded.
  - About 20% may be preventable.

  The same article quotes Smackin' co-CEO Brian Waddick: slotting, promo, free fills, freight and deductions "hit all at once" and nearly bankrupted the company after its first retail deal — [Talk Business & Politics](https://talkbusiness.net/2026/01/the-supply-side-retailer-chargebacks-could-hurt-margins-for-vendors/)

**Founder and community evidence**
- **[F]** Founder anecdote (Foodbevy "Startup To Scale" ep. 98, 13 Mar 2023):
  - The host's brand invoiced KeHE about $32,000 and was paid about $21,000 after deductions and fees, in 2018–2019.
  - It took about 8 months to spot the problem.
  - The guest was Promomash's founder, so this is an interested party. He said trade spend runs about 15–30% of sales and that invalid deductions "most often come in as non-compliance."
  - He cited a gelato brand ($15–18M revenue) that recovered $320K in deductions and $296K in shortages over six months.

  — [Foodbevy podcast](https://podcast.foodbevy.com/1832151/12408975)
- **[F]** UNFI class action, filed 3 Nov 2024 in Bristol County Superior Court, RI, by NYSM Organics LLC. **These are allegations only, and no ruling was found:**
  - It alleges "opaque and constant deductions."
  - It says contesting deductions is "so difficult and time-consuming that it is cost prohibitive for all but the very largest suppliers."
  - It says suppliers that challenge deductions risk a "non-preferred vendors" list.

  UNFI said it was reviewing the complaint — [Grocery Dive, 6 Nov 2024](https://www.grocerydive.com/news/unfi-class-action-lawsuit-payment-discounts-grocery-natural-foods/732132/)
- **[F]** Accountant advice to CPG startups (Claire Pelton of Accountfully, via the SKU accelerator, published 29 Jan 2024, updated 2 Aug 2024):
  - Distributors set their own deadlines, and a late dispute "is immediately denied even if the deduction was invalid."
  - Bills of lading are "the most important document."

  — [SKU](https://sku.is/deduction-management-for-cpg-startups-the-five-keys-to-success/)

**Distributor economics (context, not deductions per se)**
- **[F]** Eightx, a fractional-CFO firm (Matt Putra, 7 Jun 2026):
  - UNFI/KeHE effective margin is 20–28%, plus a 7–12% freight/distribution allowance.
  - Event MCBs average 8–15% of sales; MCB admin fees add 1–3% of net sales.
  - Shrink is 1–3%.
  - Distributor, broker and trade costs "commonly absorb 40–50% of bill-through revenue before COGS."
  - MCBs are often billed 60–90 days after a promotion.

  — [Eightx](https://eightx.co/blog/cpg-broker-distributor-fees)
- **[F]** KeHE charges a 1.5% ongoing allowance for KeHE Connect data syncing. A distributor may add an 18% admin fee on free-placement expense. Post-audit claims can arrive 1–3 years after shipment (Vividly blog, 27 Jun 2023) — [Vividly](https://www.govividly.com/blog/lesser-known-deductions-emerging-cpg-brands)

**Dispute windows and portals (secondary sources; they conflict)**
- **[F]** Retail windows per Endless Commerce, described as "approximate": Walmart 90 days (via APDP), Target 60 days (Partners Online), Costco 60, Kroger 45, Whole Foods 45, Amazon Vendor Central 30 — [Endless Commerce](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
- **[F]** Endless Commerce's "industry data" (unsourced) on dispute win rate by days to dispute: 0–7 days 75–80%; 15–30 days 50–60%; 61–90 days 15–20%; 90+ days under 5% — [Endless Commerce](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
- **[F]** KeHE, per Endless Commerce (undated, ©2026; "confirm against current supplier documentation"):
  - Unloading Discrepancy Reports (UDRs) need a response in about 48 hours, with a signed BOL and packing slip, and "the count at the DC is authoritative."
  - The dispute window is about 180 days, via K-Solve in KeHE CONNECT. Quick search covers only the last 90 days.
  - Fill-rate fines run about 3% of shorted value below 98%.
  - First-year suppliers with about $500K or less in volume can opt into a flat 2% admin allowance.

  — [Endless Commerce, KeHE/UNFI codes and clocks](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/)
- **[F]** UNFI, per Endless Commerce:
  - Codes: 01 shortages ("most often reported as invalid"); 02 pricing; 05 unsaleables; 10–12 advertising/MCB/off-invoice; 30+ compliance/logistics.
  - The dispute window is "reportedly 30 to 60 days," and adjustments older than 12 months are denied.

  **This conflicts with** Confido's UNFI guide, which says suppliers have 12 months to dispute; disputes go by emailed spreadsheet with brand, check number and deduction invoice number in the subject line, and a tracking number arrives within 2 business days (search summary) — [Endless Commerce](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/); [Confido UNFI dispute guide](https://confidotech.com/blogs/unfi-dispute-guide)
- **[F]** Walmart OTIF: Logistics Management reports targets cut to 90% on-time and 95% in-full "as of Feb. 1," with no year given. Fines are 3% of the value of late or missing items, measured monthly (search summary; no 2026 change found) — [Logistics Management](https://www.logisticsmgmt.com/article/walmart_reduces_carrier_requirements_for_otif_shipments)

### Inferences
- **[I]** The pain is not in doubt. What is in doubt is whether it is overlooked (see Q2). Every number on "share lost" or "invalid rate" comes from a party selling a solution, or from a lawsuit's allegations. A realistic planning range for non-trade deductions at a natural-channel brand is 2–5% of gross, with perhaps 10–40% of them invalid. Treat that as a hypothesis to test with real remittance files.
- **[I]** The work is driven by deadlines. Win rates reportedly collapse after about 30 days, KeHE UDRs need a 48-hour reply, and UNFI's window is disputed (30–60 days or 12 months). That favours a near-real-time monitoring service over a quarterly cleanup.
- **[I]** Shortage (UNFI code 01, KeHE UDR) and compliance fines are the most contestable categories. Promotional/MCB deductions are mostly valid, so the money is in reconciling them to plan rather than disputing them.

### Gaps
- No independent (non-vendor) study of invalid-deduction rates for brands with $2–100M revenue. No aggregate write-off data for small brands.
- I did not obtain official dispute windows from UNFI, KeHE, Walmart (APDP), Target, Costco or Kroger, and supplier agreements are not public. The UNFI window conflict is unresolved.
- No access to Reddit or private Slack threads (Startup CPG, CPG Insiders), so there are no direct founder quotes beyond Foodbevy and Talk Business.
- No evidence of a 2026 Walmart or Target retailer policy change, positive or negative.

## Q2. (A) Competitors: what they do, segment, pricing model, funding, complaints, and the segment they ignore

### Takeaway
Deduction recovery for emerging and mid-size CPG brands is not overlooked. Since April 2025 it has drawn some of the most concentrated venture funding in CPG back-office software: Glimpse ($52M total, a16z), Confido ($77M total, Insight Partners, Series B on 24 Sep 2026) and SPS Commerce (about $420M+ for SupplyPike and Carbon6). Older specialists already cover UNFI/KeHE explicitly: Promomash (500 brands) and Vividly (150+ brands). Contingency pricing exists (RevRecoup), and "risk-free trials" or 12-month look-back audits are standard, so outcome-based pricing does not differentiate. The only segment with weak evidence of coverage is brands below roughly $5M with low deduction volume, where the economics per client are thin.

### Cited Findings
| Competitor | What it does / segment | Pricing model (public?) | Funding / scale | Source |
|---|---|---|---|---|
| **Glimpse** | AI agents pull deductions from portals, validate them, dispute invalid ones and sync to the ERP. Integrations: Walmart, UNFI, KeHE, Sam's Club, Amazon, Walgreens, Kroger ("20+ retailers"). Logos: Lemon Perfect, IQBar, Bero, Presence, Suave, Chapstick; case study Miss Jones Baking. Its guarantee requires ≥$100M retail revenue across Walmart/KeHE/UNFI and ≥$1M in shortage deductions. 45-day onboarding. | Not public; ROI "calculator" and risk-free trial | $35M Series A led by a16z (announced 5 Apr 2026; other sources say 25 Mar or 3 Apr); $52M total; 200+ brands; claims 91% dispute win rate and 14x YoY growth (vendor) | [Pulse 2, 5 Apr 2026](https://pulse2.com/glimpse-35-million-raised-for-ai-platform-powering-cpg-and-retail-operations); [Glimpse site](https://www.tryglimpse.com/); earlier $10M round Apr 2025 (search summary) — [Food Industry Executive](https://foodindustryexecutive.com/2025/04/glimpse-secures-10m-to-automate-deduction-management-for-cpg-brands/) |
| **Glimpse × PRESENCE (PLTFRM)** | Distribution partnership: Glimpse sold into PRESENCE's natural/organic brand partners, with a 12-month look-back audit | Not disclosed; "risk-free trial" | Glimpse then claimed 140+ brands across UNFI, KeHE, Target, Walmart, CVS, Amazon | [BevNET PR, 29 Oct 2025](https://bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands) |
| **Confido** | CPG "AI operating system": trade promotion, deductions (auto-code, flag, auto-dispute, submit claims), forecasting, accrual management. Customers include Daisy, Dude Wipes, Kettle & Fire, MUSH, Unilever. Plans to expand into food service. | Annual plans priced by annual retail revenue and integration scope; a "Starter Plan" for CPG startups; no public prices | $55M Series B led by Insight Partners (24 Sep 2026); $77M total; 250+ brands; claims >$1B in deductions processed (search summary) | [Pulse 2, 24 Sep 2026](https://pulse2.com/confido-raises-55-million-series-b-led-by-insight-partners-to-develop-ai-based-software-for-cpg-companies/); [Confido pricing](https://www.confidotech.com/pricing); [NOSH PR, 11 Aug 2025](https://www.nosh.com/pr/2025/08/11/confido-raises-20m-to-modernize-financial-operations-for-cpg-brands) |
| **SPS Commerce – Revenue Recovery** (formerly SupplyPike, plus Carbon6's ChargeGuard and Seller Investigators) | Identify, validate, dispute and prevent deductions across Walmart, Amazon, Kroger, Target, CVS, Walgreens, Lowe's, Home Depot, Kohl's, **UNFI, KeHE**. Offered as full service or platform. SPS is also the EDI provider many emerging brands already use. | "Flexible pricing options"; no public rates | SPS acquired SupplyPike (Aug 2024; about $124.8M cash plus $87.2M stock per SEC filing) and Carbon6 (announced Jan 2025; about $210–212.5M); claims $2B+ recovered (search summary for deal terms) | [SPS page](https://www.spscommerce.com/products/revenue-recovery/1p/); [SPS FY2025 annual report](https://www.sec.gov/Archives/edgar/data/1092699/000109269926000031/a2025_annualreportxfilin.htm); [Digital Commerce 360, 7 Jan 2025](https://www.digitalcommerce360.com/2025/01/07/sps-commerce-carbon6-acquisition/amp/) |
| **Promomash** | Trade promotion plus deduction service: automated capture, AI coding, validation, dispute/recovery, human review. Targets brands "stretched for resources" without an in-house deductions team. Recoveries cited: $1.8M dairy, $1.1M snack, $180K Safe Catch over 3 months. | Priced by monthly deduction-invoice volume; one flat monthly fee; **one-year commitment**; onboarding fee may apply; onboarding takes "a minimum of two to four months"; no prices shown | 500 brands; $600M in deductions processed; since 2015; no funding claims | [Promomash pricing](https://www.promomash.com/pricing) |
| **Vividly** (Capterra lists it under the Cresicor name; cresicor.com no longer resolves) | Trade promotion plus deduction management, auto-disputes, cash application. Typical customer has 500–100K deductions per year. | Not public | 150+ brands; 4.9/5 on G2/Capterra (vendor-displayed) | [Vividly pricing page](https://govividly.com/pricing); Capterra/Cresicor listing (search summary) |
| **iNymbus** | RPA bots dispute claims in retailer portals: Walmart, Amazon, CVS, Target, Walgreens, Home Depot, Costco; 50+ retailers. Also freight claims. Serves larger shippers and distributors (e.g., D&H). | No pricing page; one case study cites "$0.40 to $0.70 per claim" per month | 100+ companies; funding not stated | [iNymbus](https://www.inymbus.com/) |
| **HighRadius** | Enterprise deduction management (AI/RPA), for "Large Enterprises" and "Mid-Sized Organizations." Customers: McCormick (164K deductions/yr), Ferrero, Danone, Dr Pepper. | No public pricing | Enterprise | [HighRadius](https://www.highradius.com/product/deduction-management-software/) |
| **RevRecoup** | White-label recovery of retailer deductions and aged invoices; works Retail Link, Vendor Central and Partners Online | **Pure contingency**, rate quoted per portfolio; "No setup fee, no monthly minimum" | Not stated | [RevRecoup](https://revrecoup.com/go/manufacturing/) |
| Endless Commerce | Prevention-led: native EDI with pre-ship validation (claims a "90% drop" in EDI chargebacks) plus deduction playbooks | Not reviewed | — | [Endless Commerce](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/) |

- **[F]** Typical contingency for recovery firms is "25–35% of recovered dollars," per one vendor guide (unsourced) — [Endless Commerce](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
- **[F]** Customer complaints (thin; search summary because Capterra returned 403):
  - Promomash reviewers mention it is "a bit expensive for a small brand."
  - One Promomash reviewer said a distributor data feed broke because the distributor started charging for dashboard access.
  - Promomash features were called occasionally unclear or glitchy.
  - One reviewer said Vividly's deduction tool "relied heavily on spreadsheets in the background."
  - G2 shows Promomash at 4.7 (57 reviews) and Vividly at 4.8 (40 reviews).

  — [G2 compare](https://g2.com/compare/promomash-inc-promomash-vs-vividly); [Capterra Promomash](https://www.capterra.com/p/210477/Promomash/reviews/) (403 on fetch)
- **[F]** Channel partners are being claimed by funded players. Glimpse partnered with PRESENCE/PLTFRM (Oct 2025). The CPG accounting firm Accountfully "is now BELAY," and BELAY lists Foodbevy and Startup CPG as partners — [BELAY/Accountfully](https://resources.belaysolutions.com/accountfully)
- **[F]** The earlier note's RetailPath (claims 40% recovery) and Doss remain unverified there. The user-named Cascadia, Supplier Pulse, Reconcilie and BlueTape were not checked within budget.

### Inferences
- **[I]** The "ignored segment" thesis from the prior note ("enterprise tools target large CPG; emerging brands have nothing") is **disconfirmed for $5–100M brands**. Glimpse's logos (Lemon Perfect, IQBar, Bero, Miss Jones) and Confido's (MUSH, Daisy, Dude Wipes, Kettle & Fire) are emerging or mid-size brands. Confido sells a Starter Plan, Promomash targets brands without a deductions team, and SPS has an installed EDI base among exactly these brands.
- **[I]** What does look under-served:
  - Brands below about $5M, or with few deductions per year. Promomash's one-year commitment, onboarding fee and 2–4 month onboarding, and Glimpse's guarantee floor (≥$100M), suggest they are not built for these brands.
  - Possibly specific channels: Costco appears on iNymbus but not on SPS's or Glimpse's named lists; regional distributors, DSD and foodservice also look thin, though Confido says it is expanding into food service.

  Neither gap is proven. Both could be uneconomic rather than ignored (see Q5).
- **[I]** Contingency pricing is not a moat. RevRecoup already sells pure contingency with no minimum, and Glimpse offers risk-free trials and 12-month look-backs.
- **[I]** Retailer portal access (Retail Link/APDP, Partners Online, KeHE CONNECT, UNFI supplier portal) and evidence capture from 3PLs are where funded players invest engineering. A solo non-engineer would compete on service labour, not product.

### Gaps
- No public price for any of Glimpse, Confido, Vividly, SPS Revenue Recovery, iNymbus or HighRadius.
- Could not verify SupplyPike's current standalone pricing (fetch timed out twice).
- No independent customer-complaint corpus. G2 and Capterra pages were blocked or thin.
- Did not verify Cascadia, Supplier Pulse, Reconcilie, BlueTape, Doss or RetailPath funding and pricing, or which CPG-specialist accounting firms offer deduction recovery as a paid service.

## Q3. (B) Status of state packaging EPR programs (Oct 2026): CAA reporting cycles, small-producer thresholds, lawsuits, enforcement

### Takeaway
Packaging EPR is live, enforced and survived its first merits test:
- On 27 Aug 2026 a federal judge upheld Oregon's law in full, and NAW has appealed to the Ninth Circuit.
- Oregon DEQ's first quarterly "Producer Status List" (as of 9 Apr 2026) names 304 non-compliant producers by my count, including several emerging food and personal-care brands and KeHE itself.
- California's final CAA program plan went to CalRecycle on 13 Oct 2026, ahead of a 1 Jan 2027 start.
- Seven states have laws, and no eighth state had enacted one as of Aug 2026.

The big disconfirmer for small brands is that thresholds and flat fees remove or simplify much of the work. Brands under $1–5M revenue are exempt in most states, and Oregon and Colorado let low-volume producers pay a flat fee ($800–$5,800) instead of calculating by material category.

### Cited Findings
**Enforcement in Oregon**
- **[F]** Oregon DEQ released its first Recycling Modernization Act Producer Status List on 9 Apr 2026. The process ran: CAA flagged producers under ORS 459A.869(10)(a) with 90 days' notice → DEQ warning letters on 5 Mar 2026 with 30 days to correct → listed if still not corrected. Penalties run up to $25,000/day, and Oregon DOJ may seek a sales prohibition. Named examples include Yamaha Motor, Mercedes-Benz NA, Papa John's, Hobby Lobby and Jack in the Box — [Resource Recycling, 21 Apr 2026](https://resource-recycling.com/policy-now/2026/04/21/oregon-deq-flags-250-producers-for-rma-noncompliance/)
- **[F]** Count conflict:
  - Resource Recycling says 250; Venable says about 300 (search summary); rePurpose says "300+."
  - My count of the list PDF ("RMA Quarterly Producer Status List as of 4-9-2026") is **304 entries**. The PDF carries DEQ's non-discrimination statement but is hosted on a third-party Squarespace URL linked by rePurpose, so its provenance should be checked against DEQ's site.
  - The list includes **KeHE Distributors, LLC**, C&S Wholesale Grocers and Performance Food Group, plus consumer brands such as Good Culture, Peanut Butter & Co, Humble Bee Honey, Tribe 9 Foods, Aramara Beauty (Glow Recipe), Hood River Juice, Horseshoe Beverage, Caruso's Coffee, Honeysticks, Seattle Gourmet Foods, Virtue Labs, Organic India USA, Macaron Queen, Galleon Chocolate, The Philosopher's Stoneground, Three Limes, Facile Skincare and Newman's Own.

  — [List PDF via rePurpose, 6 May 2026](https://static1.squarespace.com/static/64260ed078c36925b1cf3385/t/69d903d0c3c096784a3aeb66/1775829968918/RMA+Quarterly+Producer+Status+List_as+of+4-9-2026.pdf); [rePurpose blog](https://repurpose.global/blog/oregon-just-named-300-brands-out-of-epr-compliance-heres-what-that-means-for-your-company)

**Litigation**
- **[F]** On 27 Aug 2026 Judge Michael H. Simon (D. Or.) upheld Oregon's law after a five-day bench trial, in a 71-page ruling in *NAW v. Feldon*, No. 3:25-cv-01334-SI:
  - It rejected the dormant Commerce Clause and Due Process claims, and the claim that CAA fees are "clearly excessive" (citing CAA's growing reserves).
  - The February 2026 preliminary injunction for NAW members is superseded.
  - DEQ: "The law remains in effect."

  — [Packaging Dive, 28 Aug 2026](https://www.packagingdive.com/news/oregon-epr-law-naw-constitution-judge-ruling/829036/)
- **[F]** NAW filed a notice of appeal to the Ninth Circuit (reported 25 Sep 2026). In *Lollicup USA v. Feldon*, a putative class action for non-NAW producers filed in July 2026, the parties were waiting on the appeal, with a joint status report due 16 Oct 2026. NAW is also litigating in California and Colorado — [Packaging Dive, 25 Sep 2026](https://www.packagingdive.com/news/wholesalers-appeal-oregon-epr-decision-ninth-circuit/831347/); [Foley, 6 Jul 2026](https://www.foley.com/insights/publications/2026/07/oregon-epr-producers-may-have-an-off-ramp-from-paying-caa-at-least-temporarily/). One source estimates the appeal may not be resolved until late 2027 (search summary).
- **[F]** California SB 54 faces two suits:
  - Oceana, NRDC and Californians Against Waste sued in San Francisco Superior Court (2 Jun 2026), arguing the regulations are too weak.
  - 17 states led by Nebraska, plus NAW, sued in E.D. Cal. (*Nebraska v. Heller*, 22 Jun 2026).

  No ruling was found as of Oct 2026 (search summary) — [Greenberg Glusker](https://www.greenbergglusker.com/publications/sb-54-under-fire-states-and-industry-challenge-californias-packaging-epr-law); [Resource Recycling, 5 Jun 2026](https://resource-recycling.com/policy-now/2026/06/05/oceana-nrdc-caw-sue-calrecycle-over-sb-54-regs/). Faegre Drinker (2 Jul 2026) says there is no injunctive relief and the regulations remain in effect. It also lists an ILMA suit in Colorado state court (12 Mar 2026) — [Faegre Drinker](https://www.faegredrinker.com/en/insights/publications/2026/7/packaging-sustainability-and-compliance-including-extended-producer-responsibility)

**California timeline**
- **[F]** CalRecycle: permanent regulations were effective 1 May 2026, CAA submitted its plan to the Advisory Board on 15 Jun 2026, and the Advisory Board meets on 16 Oct 2026 — [CalRecycle SB 54 page](https://calrecycle.ca.gov/packaging/packaging-epr/). CAA says the comment period ran 15 Jun–14 Aug 2026 with more than 2,400 comments, and it **submitted the final California plan to CalRecycle on 13 Oct 2026** — [CAA California program plan](https://circularactionalliance.org/ca/program-plan-public-comment)
- **[F]** From 1 Jan 2027, producers may not sell in California unless they participate in an approved PRO. The PRO's $500M Plastic Pollution Mitigation Fund remittance is due 1 Mar 2027. CalRecycle administrative fees run from 1 Jul 2027 — [Brightest, updated 10 Sep 2026 (verified 10 Aug 2026)](https://www.brightest.io/packaging-epr-laws-by-state)

**The 2026 consolidated reporting cycle (CAA)**
- **[F]** The 2026 cycle was the first consolidated round, due 1 Jun 2026 (31 May fell on a Sunday). A producer could owe up to **eight reports**:
  - Simplified supply reports for Minnesota, Maryland and Washington.
  - Annual supply reports for Oregon, Colorado and California.
  - A California baseline report and a California Individual Source Reduction Plan.
  - Voluntary eco-modulation reports for Colorado and Oregon.

  Colorado and Oregon fee schedules were expected by Oct 2026, with Jan 2027 invoices based on 2025 supply data. Both offered 50% installment billing in 2026 — [Holland & Knight, 7 Jul 2026](https://www.hklaw.com/en/insights/publications/2026/07/2026-epr-reporting-lessons-learned-initial-consolidated-reporting)
- **[F]** CAA's Oregon page: the 2026 report (2025 data) was due 31 May 2026, with payment in January 2027. Producers report sales and packaging weights of covered materials, brands, and affiliated producers through the Producer Portal — [CAA producer reporting](https://circularactionalliance.org/producer-reporting). CAA is running a "Understanding Producer Fee-Setting" webinar on 21 Oct 2026 — [CAA home](https://circularactionalliance.org/)

**State-by-state status and small-producer exemptions** (all from [Brightest, verified 10 Aug 2026](https://www.brightest.io/packaging-epr-laws-by-state) unless noted)

| State | Status / next dates | Small-producer exemption |
|---|---|---|
| Oregon | Active since 2025; annual report 31 May; CAA approved 21 Feb 2025 | Seven routes under ORS 459A.863(32), including gross revenue under $5M, under 1 metric ton into Oregon, and beverage makers under 5 metric tons |
| Colorado | Active; producers cannot sell without participating (since Jul 2025); dues due by 1 Jan; first admin dues remitted 30 Jun 2026 | Revenue threshold set by rule and adjusted annually (figure not given). The earlier note cited under $5M or under 1 tonne ([Zenpack](https://www.zenpack.us/blog/us-packaging-epr-compliance-guide/)) |
| California | Regulations effective 1 May 2026; registration closed 1 Jun 2026; program and sales restriction from 1 Jan 2027 | "Gross annual sales under $1 million," but the producer must still register with CalRecycle to claim it. **Sources differ** on whether this means California sales or total sales (Zenpack says California revenue) |
| Maine | No PRO yet; registration and invoicing expected to start end of 2026 | Under $2M revenue for the first 3 years, then under $5M; under 1 ton; first 15 tons of perishable food packaging exempt |
| Minnesota | Simplified report 31 May 2026; producers fund 50% of costs from 1 Feb 2029 | Under 1 ton, or global gross revenue under $2M |
| Maryland | Registration closed 1 Jul 2026; cost reimbursement from 1 Jul 2028 | Being set by rulemaking |
| Washington | Registration closed 1 Jul 2026; annual producer fees from 1 May 2027; programs Jan 2030 | Being set by rulemaking |

- **[F]** No eighth state had enacted packaging EPR as of 10 Aug 2026 (Brightest). Bills were reintroduced in New Hampshire, Wisconsin and New Jersey (search summary) — [Brightest](https://www.brightest.io/packaging-epr-laws-by-state); [Compliance & Risks](https://www.complianceandrisks.com/blog/packaging-epr-expansion-new-developments-across-the-u-s/)

**Fees and penalties**
- **[F]** Flat fees for low-volume producers (EcoEnclose, a packaging supplier, page dated 12–13 Oct 2026):
  - **Colorado**, if Colorado-allocated weight is ≤10 short tons: $800 (1–2.5 t), $1,600 (2.5–5 t), $2,600 (5–7.5 t), $3,600 (7.5–10 t).
  - **Oregon**, if Oregon-allocated weight is ≤10 metric tons **and revenue is under $10M**: $1,200 / $2,500 / $4,100 / $5,800 for the same bands.

  — [EcoEnclose](https://www.ecoenclose.com/blog/epr-fees-by-state)
- **[F]** Per-pound rates, per EcoEnclose:
  - Colorado 2026 final dues: corrugate $0.08/lb; PE film $0.48; PP film $0.64; plastic laminates $0.74.
  - Oregon 2026: PE film $0.43; PP film and laminates $1.02.
  - California 2027 is illustrative only, PE film $0.29–0.76, plus a Plastic Pollution Mitigation Fund fee of $0.17–0.25/lb of plastic and a per-component fee.

  EcoEnclose calls EPR a "rounding error" for most brands today and "a real line item for plastic-heavy ones." On its population shares, today's invoicing states (CO, OR) are about 3% of the US population, about 15% once California is added (Jan 2027), and about 21% with all seven states (around 2029) — [EcoEnclose](https://www.ecoenclose.com/blog/epr-fees-by-state)
- **[F]** L.E.K. Consulting (Executive Insights, July 2026, per the file path):
  - Oregon fee rates cover 60 materials, from $0.01/lb to $2.73/lb.
  - Oregon's fee-assessable supply is estimated at 400K–450K tons, with estimated 2026 EPR fees of $200M–$300M.
  - Penalties as of Nov 2025: OR up to $25K/day; CA up to $50K/day; CO $5K–$20K (first day), then per-day; MN $25K–$100K/day; MD $5K–$20K/day; WA $1K–$10K/day; ME up to $100 per package.
  - Flat or fixed fees for small producers exist in OR, ME and CO.

  — [L.E.K. PDF](https://www.lek.com/sites/default/files/2026-07/the-erp-inflection-point-understanding-the-impact-of-erp-regulations-ei_0.pdf)

### Inferences
- **[I]** Regulatory durability improved materially in Aug–Oct 2026: Oregon was upheld on the merits, California's plan was submitted, and Washington's fees are dated. Litigation is now a tail risk on a 12–24 month horizon (Ninth Circuit, *Nebraska v. Heller*), not a near-term blocker.
- **[I]** The Oregon list is mostly non-consumer companies (industrial, auto, apparel, Chinese e-commerce sellers). It does include about 20 identifiable food, beverage and personal-care brands, which is direct evidence that some emerging CPG brands are failing the process. Some of them may be exempt or may have fixed their status since April.
- **[I]** The pain step-change is **January–May 2027**. CO/OR invoices on 2025 data, the California start and sales restriction, Washington fees (May 2027) and the next 31 May 2027 report all land then. Q4 2026 is the right time to test demand.

### Gaps
- The exact California small-producer definition (California sales vs. total gross sales) is not confirmed from the regulation text.
- Colorado's current inflation-adjusted dollar threshold is not given. Maryland and Washington thresholds are still in rulemaking.
- Final 2027 CO/OR fee schedules (expected Oct 2026) were not found. California fees are illustrative only.
- Whether flat-fee producers must still file full material-level supply reports, or only tonnage bands, is unconfirmed. This matters a lot for the small-brand pain thesis.
- DEQ's own copy of the list, and any later quarterly list (e.g., July 2026), were not checked.

## Q4. (B) How many producers are obligated, who competes (with pricing), and what is the actual hard step?

### Takeaway
California alone estimates more than 5,700 obligated producers across all sectors, and CAA is paid by "thousands" of producers. No counts by revenue tier exist. The competitive field is barbell-shaped:
- **Low end:** cheap Shopify apps ($48/year for a US CAA export, launched June 2026).
- **Top end:** enterprise or demo-only platforms (Lorax EPI, Assent, Ecoveritas, rePurpose, RLG) with no public pricing.

The hard step, confirmed by the 2026 cycle, is building defensible data and methodology. Producers lacked data in the required format and missing PCR data, wrote one-line or copied methodologies that CAA rejects, missed eco-modulation bonuses, and over-reported, which inflates fees.

### Cited Findings
**Obligated population**
- **[F]** CalRecycle estimates "more than 5,700 producers" in scope across all sectors, its largest EPR program by number of regulated entities. Brightest, updated 10 May 2026, also cites up to $50,000/day per violation — [Brightest SB 54](https://www.brightest.io/california-sb-54-packaging-epr); also [JD Supra summary](https://www.jdsupra.com/legalnews/california-epr-update-sb-54-regulations-2634738/) (search summary). Producer fees are expected to total about $5B over 10 years (search summary, same sources).
- **[F]** Foley (6 Jul 2026) says "thousands of producers" currently pay CAA — [Foley](https://www.foley.com/insights/publications/2026/07/oregon-epr-producers-may-have-an-off-ramp-from-paying-caa-at-least-temporarily/)

**The hard step (what went wrong in 2026)**
- **[F]** Holland & Knight's 2026 lessons learned:
  - Data "often did not exist in the required format."
  - Producers were unaware of state differences; Colorado required PCR data some had not tracked.
  - Weak methodology sections (single-line or copy-pasted) were flagged or rejected, requiring full resubmission.
  - Some reports were auto-rejected at validation, and submitted reports cannot be edited.
  - Eco-modulation bonuses were missed because they had to be filed through "Help & Support."
  - Over-reporting inflates fees, and CAA guidance arrived late.
  - Inaccurate reporting can cost "up to $5,000 or the associated Producer Fees, whichever is greater," plus compounded interest on late payments. Self-identified errors fixed within 60 days carry no penalty.
  - Recommended: per-SKU applicability analysis and collecting data from business partners.
  - Expected for 2027: "stricter scrutiny."

  — [Holland & Knight, 7 Jul 2026](https://www.hklaw.com/en/insights/publications/2026/07/2026-epr-reporting-lessons-learned-initial-consolidated-reporting)
- **[F]** Eco-modulation upside (Holland & Knight):
  - Colorado: four bonuses of 5% each, capped at $50,000 per producer.
  - Oregon: LCA disclosure bonus capped at $20,000 per report; design improvements up to 30% of base fees (max $50,000); reuse up to $1.5M over three years.
  - Claiming all CO and OR bonuses can take up to seven separate forms.

  — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/07/2026-epr-reporting-lessons-learned-initial-consolidated-reporting)
- **[F]** State sales allocation: when retail point-of-sale data by state is unavailable, CAA's guidance ("Preparing to report your supply data") gives a national-apportionment formula. Producers still have to substantiate it, and Oregon rules require a written methodology for calculating covered weight (search summary; the CAA guidance itself was not retrieved) — [CAA webinar 303, 4 Feb 2025](https://circularactionalliance.org/producer-webinars/303-feb-4); [Holland & Knight, 10 Apr 2026](https://www.hklaw.com/en/insights/publications/2026/04/are-you-ready-to-report-your-packaging-data-next-month)

**Competitors and pricing**
- **[F]** **PacForm – US EPR & CAA Reports** (Shopify app by Merchard):
  - Launched 5 Jun 2026; data setup is free and "Premium Export" costs $48/year.
  - Assigns default packaging weights to orders and exports CSVs.
  - 0 reviews.
  - The listing describes CAA as the "Clean Air Act," a quality red flag.

  — [PickYourApp listing](https://pickyourapp.com/collections/store-management-security/products/u-s-epr-caa-reports)
- **[F]** **EPR Insights** (Shopify; Denmark) covers EU EPR only, not US states. Plans run $15–$59/month, it launched 26 Aug 2025, and it has 3 reviews — [Shopify App Store](https://apps.shopify.com/epr-insights). **MokshEPR** lists pay-as-you-go pricing for US state EPR (search summary) — [Net Zero Compare](https://netzerocompare.com/software/mokshepr)
- **[F]** **Lorax EPI** offers EPR reporting, obligation assessment, fee modelling and a regulatory subscription. It claims "Over 200 Schemes," has no public pricing ("Request a demo"), and its logo files suggest Colgate and Newell. It does not mention US state packaging EPR — [Lorax EPI](https://www.lorax-epi.com/)
- **[F]** **Assent** offers "EPR Packaging": data collection, fee estimates and reports, aimed at manufacturers in medical devices, electronics, industrial, auto and aerospace. No US states are named and no prices are shown — [Assent](https://www.assent.com/solutions/extended-producer-responsibility/)
- **[F]** **Ecoveritas** offers managed services plus software ("my.ecoveritas"), with UK-centric client logos (Harrods, Waitrose, John Lewis) and coverage "from the US to Canada." No US state detail and no pricing — [Ecoveritas](https://www.ecoveritas.com/)
- **[F]** **rePurpose Global** offers packaging compliance (EPR reporting, centralized supply data) and a "Packaging Simulator" for California source-reduction plans. No pricing; a free assessment is offered — [rePurpose](https://repurpose.global/blog/oregon-just-named-300-brands-out-of-epr-compliance-heres-what-that-means-for-your-company). Earlier notes list Certivo, Reverse Logistics Group, Asuene, Zenpack and Brightest.
- **[F]** Packaging suppliers publish free state fee breakdowns and guidance (EcoEnclose, Oct 2026; Zenpack, Jul 2026) — [EcoEnclose](https://www.ecoenclose.com/blog/epr-fees-by-state)

### Inferences
- **[I]** The work in the hard step:
  1. A SKU → component → material-category → unit-weight bill of materials. Oregon alone has 60 fee categories.
  2. Units by state, which is hard for brands selling through UNFI/KeHE and retailers without state point-of-sale data, hence CAA's apportionment fallback.
  3. A defensible written methodology.
  4. State-specific extras: Colorado PCR %, California baseline and source-reduction plan, eco-mod forms.
  5. Exemption and flat-fee eligibility checks per state and per affiliated entity.

  Steps 1 and 3 are where 2026 filers failed. That is AI-friendly document work: spec-sheet and invoice extraction plus narrative drafting.
- **[I]** The market is a barbell. DTC microbrands get $48/year apps; enterprises get Lorax, Assent or Sphera. The middle, $10–150M omnichannel food, beverage and personal-care brands, shows no public-priced, US-state-specialist, done-for-you offer in what I could verify. That is an absence of evidence, not proof of a gap.
- **[I]** Sphera, 3E, SmartWaste and "Ecopreneur" were not verified. I would not assume they are absent from the mid-market.

### Gaps
- No producer counts for Oregon, Colorado, Minnesota, Maryland or Washington, and none by revenue tier.
- No consultant or law-firm fee benchmarks for EPR filing work.
- No published pricing for rePurpose, RLG, Certivo, Ecoveritas, Lorax, Assent, Sphera or 3E. CAA's own guidance documents and portal templates were not retrieved.

## Q5. For both: buyer population, per-brand economics, willingness to pay, why incumbents skip small brands, and software vs service vs outcome pricing

### Takeaway
- **(A)** The pain per brand scales with retail volume. At $2–5M revenue, plausible contingency revenue per client is low hundreds to low thousands of dollars a year. At $20–100M it is meaningful, but funded competitors already sell there.
- **(B)** EPR fees for a $10M brand are low thousands per year today and likely five figures once California starts. Willingness to pay therefore rests on compliance risk and time saved, not fee savings, except for larger plastic-heavy brands where eco-modulation and over-reporting corrections matter.
- No direct willingness-to-pay evidence was found for either: no published prices, no surveys.

### Cited Findings
- **[F]** Buyer-population proxies:
  - Expo West 2026 drew about 3,000–3,200 exhibiting brands and companies (search summary; Abasto says 3,200+, NBC LA "more than 3,000") — [Abasto](https://abasto.com/en/news/expo-west-turns-45-66000-leaders-unite-in-anaheim/); [NBC Los Angeles](https://nbclosangeles.com/news/local/see-the-exhibitors-at-natural-products-expo-west-2026-in-anaheim/3856941)
  - Startup CPG says "nearly 40K founders, service providers, and industry partners," and its Slack is free — [Startup CPG](https://www.startupcpg.com/)
  - California: 5,700+ EPR producers across sectors — [Brightest](https://www.brightest.io/california-sb-54-packaging-epr)
- **[F]** Existing deduction-tool penetration: Glimpse 200+ brands, Confido 250+, Promomash 500, Vividly 150+ (each vendor's own claim, with overlap possible) — sources in Q2.
- **[F]** Fractional CFO pricing benchmark: Eightx serves $5–150M brands and quotes $5,000–$12,000/month for a CPG fractional CFO (search summary) — [Eightx](https://eightx.co/fractional-cfo-for-food-beverage-brands)
- **[F]** Recovery yield and fee benchmarks (vendor): $0.60–$0.80 recovered per invalid dollar; contingency 25–35% — [Endless Commerce](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
- **[F]** EPR fee benchmarks: flat fees CO $800–$3,600 and OR $1,200–$5,800 (OR flat fee only if revenue is under $10M); per-pound rates as in Q3 — [EcoEnclose](https://www.ecoenclose.com/blog/epr-fees-by-state)

### Inferences
**(A) Illustrative economics.** My arithmetic, not sourced market data. Assumptions: non-trade deductions are 2–5% of retail-channel gross; 10–20% of them are invalid (low case) up to 40% (high case); recovery is $0.60–0.80 per invalid dollar; contingency is 25–35%.

| Brand revenue (retail channel) | Non-trade deductions/yr | Recoverable/yr | Contingency revenue per client/yr |
|---|---|---|---|
| $3M | $60K–$150K | ~$4K–$48K | ~$1K–$17K (low case nearer $1–3K) |
| $10M | $200K–$500K | ~$12K–$160K | ~$3K–$56K (low case nearer $3–10K) |
| $50M | $1M–$2.5M | ~$60K–$800K | ~$15K–$280K |

- **[I]** A solo operator would need roughly 50–100 clients in the $3–10M band to reach about $250K/year of fees under the low case. Each client brings portal credential set-up and 3PL evidence chasing. The $50M+ band is attractive but contested by Glimpse, Confido, SPS and Promomash.
- **[I]** Why incumbents skip sub-$5M brands, inferred from their terms: a one-year commitment and 2–4 month onboarding (Promomash), and guarantee floors (Glimpse ≥$100M). Fixed onboarding cost per retailer integration and low deduction counts make these brands unprofitable for SaaS. That is a rational skip, not an oversight.

**(B) Illustrative economics.** My arithmetic. Assumptions: a $10M food brand ships about 100 metric tons of packaging nationally (mostly flexible film plus corrugate); population shares from EcoEnclose.
- Oregon allocation ~1.3 t; Colorado ~1.7 t (~1.9 short tons). The Colorado flat fee is ~$800. Oregon's flat fee is unavailable at ≥$10M revenue, so per-pound: about 2,900 lb × $0.08–$1.02 ≈ $0.2K–$3K. Total for OR + CO today is roughly **$1K–$4K/year**.
- California adds about 11–12% of US supply (~12 t ≈ 26,000 lb). Using illustrative CA rates plus the Plastic Pollution Mitigation Fund surcharge on the plastic share, that could be roughly **$3K–$25K/year from 2027**, depending on plastic share.
- A $100M brand would be roughly ten times that.
- **[I]** Willingness to pay is therefore probably **$1–5K/year for a $10–30M brand** (done-for-you filing plus risk removal) and **$10–30K/year for a $100M+ brand**, where eco-mod bonuses (up to $50K in Colorado) and correcting over-reporting can pay for the service. **This is a hypothesis to test, not evidence.**
- **[I]** Delivery model:
  - (A) suits a **contingency service** (outcome pricing), but that is already offered by RevRecoup and others.
  - (B) suits a **fixed annual done-for-you service** with a software back-end. Outcome pricing only makes sense as a share of eco-mod bonuses or verified fee reductions for larger brands. Pure self-serve software is commoditized at the low end ($48/year) and distrusted at the high end, where producers fear rejection.

### Gaps
- No survey or price point showing what $2–100M brands pay, or would pay, for deduction recovery or EPR filing.
- No count of US CPG brands by revenue tier selling through UNFI, KeHE or big-box retail.
- No data on how many CAA filers used consultants versus filing in-house.

## Q6. Disconfirming evidence (both candidates)

### Takeaway
- **(A)** fails the "overlooked" test. The segment is crowded with recently and heavily funded AI-native entrants plus SPS, the incumbent EDI channel, and outcome-based pricing is already standard.
- **(B)** survives, with real caveats: small-brand exemptions and flat fees, "rounding-error" fee levels for fibre-heavy brands, an active Ninth Circuit appeal and California litigation, and a commoditized low end.

### Cited Findings
**(A) Deductions**
- **[F]** Crowding:
  - Glimpse raised $35M from a16z (Apr 2026), Confido $55M from Insight (24 Sep 2026), and SPS bought SupplyPike and Carbon6 (2024–25) — sources in Q2.
  - Glimpse claims 14x and Confido 5x year-over-year growth (vendor claims).
  - Glimpse is distributed through PRESENCE (Oct 2025). BELAY/Accountfully partners with Startup CPG and Foodbevy.
- **[F]** Outcome pricing is already offered: RevRecoup is pure contingency with no minimum, Glimpse offers a "risk-free trial" and 12-month look-back, and SPS offers a full-service option — [RevRecoup](https://revrecoup.com/go/manufacturing/); [BevNET PR](https://bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands); [SPS](https://www.spscommerce.com/products/revenue-recovery/1p/)
- **[F]** Prevention is eroding the problem upstream: Endless Commerce claims a "90% drop in retailer EDI chargebacks" with pre-ship validation (vendor) — [Endless Commerce](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/). Flxpoint's prevention tool appears in the earlier note.
- **[F]** Retailer policy: Walmart reportedly loosened OTIF targets to 90% on-time and 95% in-full, year unstated (search summary) — [Logistics Management](https://www.logisticsmgmt.com/article/walmart_reduces_carrier_requirements_for_otif_shipments). No 2026 tightening was found.

**(B) EPR**
- **[F]** Exemptions: OR under $5M; MN under $2M; ME under $2M, then $5M; CA under $1M; CO set by rule — [Brightest](https://www.brightest.io/packaging-epr-laws-by-state)
- **[F]** Flat fees for low-volume producers in CO and OR. EPR is a "rounding error" for most brands, and fibre-based brands stay under 2% of packaging cost — [EcoEnclose, Oct 2026](https://www.ecoenclose.com/blog/epr-fees-by-state)
- **[F]** Legal: NAW's Ninth Circuit appeal (Sep 2026); the Lollicup class action; *Nebraska v. Heller* (17 states plus NAW); the NGO suit asking for stronger California rules; ILMA in Colorado — sources in Q3. NAW calls the options for distributors "three terrible options," including to "stop selling into EPR states" — [Packaging Dive, 25 Sep 2026](https://www.packagingdive.com/news/wholesalers-appeal-oregon-epr-decision-ninth-circuit/831347/)
- **[F]** Commoditization at the low end: PacForm at $48/year (Jun 2026) — [PickYourApp](https://pickyourapp.com/collections/store-management-security/products/u-s-epr-caa-reports)
- **[F]** Fee relief possible: the Oregon ruling notes CAA reserves could reduce producer fees "this year and next" — [Packaging Dive, 28 Aug 2026](https://www.packagingdive.com/news/oregon-epr-law-naw-constitution-judge-ruling/829036/)

### Inferences
- **[I]** For (A), the strongest disconfirmer is capital concentration, not low pain. A solo, non-engineer, capital-light founder would be selling labour against AI-native products with retailer integrations, venture subsidy and channel partnerships.
- **[I]** For (B), the strongest disconfirmer is low pain at the small end: exemptions plus flat fees plus small fee amounts. The opportunity only holds for brands above the flat-fee tier, or with California exposure from 2027. That narrows the market to perhaps the low thousands of US brands (unquantified).
- **[I]** For (B), if the Ninth Circuit reversed on Due Process (delegation to CAA), programs would likely be restructured rather than repealed. Reporting demand would likely persist in some form. This is speculative.

### Gaps
- No evidence on churn or failure rates among the funded deduction startups.
- No data on how many brands sit just above versus below the EPR thresholds.

## Q7. Twenty specific first-customer targets (by type or verifiable public information)

### Takeaway
For (B), the strongest verifiable list is the consumer brands on Oregon DEQ's April 2026 Producer Status List. For (A), the most practical routes are fractional-CFO and CPG-accounting firms, free founder communities, and brands newly announced into big-box or natural distribution. Some of these channels are already partnered with funded competitors.

### Cited Findings
**(B) EPR targets: brands named on Oregon's Producer Status List as of 9 Apr 2026** ([list PDF](https://static1.squarespace.com/static/64260ed078c36925b1cf3385/t/69d903d0c3c096784a3aeb66/1775829968918/RMA+Quarterly+Producer+Status+List_as+of+4-9-2026.pdf)). Revenue and current status are not verified; some may be exempt or may since have complied.
1. Good Culture (cottage cheese)
2. Peanut Butter & Co, Inc.
3. Humble Bee Honey Inc.
4. Tribe 9 Foods
5. Hood River Juice Company
6. Horseshoe Beverage Company LLC
7. Caruso's Coffee, LLC
8. Honeysticks Creative LLC
9. Seattle Gourmet Foods, LLC
10. Aramara Beauty LLC dba Glow Recipe
11. Virtue Labs LLC
12. Organic India USA LLC

Further consumer names on the same list: Macaron Queen, Galleon Chocolate Trade Company, The Philosopher's Stoneground, Three Limes, Facile Skincare, Ferndale Farmstead, Icelandic Plus, Savory Creations International.

**(A) Deduction targets and channels**
13. **Eightx** (fractional CFO for $5–150M ecommerce/CPG brands; trade spend and deductions are a core engagement area) as a white-label or referral partner — [Eightx](https://eightx.co/fractional-cfo-for-food-beverage-brands)
14. **BELAY (formerly Accountfully)** (CPG and F&B accounting; partners Foodbevy and Startup CPG; Accountfully authored deduction guidance for SKU) — [BELAY/Accountfully](https://resources.belaysolutions.com/accountfully); [SKU article](https://sku.is/deduction-management-for-cpg-startups-the-five-keys-to-success/)
15. **Startup CPG Slack** (~40K members, free) for founder interviews and offers — [Startup CPG](https://www.startupcpg.com/)
16. **SKU accelerator cohorts and alumni** (Austin; publishes deduction content) — [SKU](https://sku.is/deduction-management-for-cpg-startups-the-five-keys-to-success/)
17. **Foodbevy community and "Startup To Scale" audience** (has run deduction episodes) — [Foodbevy podcast](https://podcast.foodbevy.com/1832151/12408975)
18. **Brands in BevNET's 2026 "Distribution" column** newly entering Target or Sprouts. Headlines seen in search results (content not retrieved): "The Zero Proof hits Target," "The Cycle goes nationwide with Sprouts," "Zero Co starts shipping" — [BevNET](https://www.bevnet.com/news/2026/distribution-the-zero-proof-hits-target); [BevNET](https://www.bevnet.com/news/2026/distribution-the-cycle-goes-nationwide-with-sprouts)
19. **Expo West 2026 exhibitors** (3,000–3,200 brands), filtered to those carried by UNFI or KeHE — [Abasto](https://abasto.com/en/news/expo-west-turns-45-66000-leaders-unite-in-anaheim/)
20. **Natural-channel brands that sell through UNFI to Whole Foods** (the supplier type described in *NYSM Organics v. UNFI*), reached via founder communities for problem interviews — [Grocery Dive](https://www.grocerydive.com/news/unfi-class-action-lawsuit-payment-discounts-grocery-natural-foods/732132/)

### Inferences
- **[I]** For (B), outreach to Oregon-list brands should be framed as a factual "public list" exposure check, not a fear pitch. Some were likely flagged for registration lapses that a single CAA portal session fixes, which would signal low willingness to pay.
- **[I]** For (A), Glimpse already owns PRESENCE/PLTFRM brands and BELAY partners with the main communities. A newcomer would likely need to target fractional CFOs that are not yet partnered.
- **[I]** KeHE itself appears on the Oregon list. That is a curiosity, not a target.

### Gaps
- Revenue, current compliance status and contact owners for the named Oregon-list brands were not verified.
- CPG Insiders' community size was not checked. Accelerator cohort lists (e.g., Target Takeoff, Whole Foods LEAP, KeHE Elevate) were not fetched within budget.

## Q8. Narrowest MVP (2–8 weeks, solo non-engineer with AI coding tools) and a 14-day experiment with kill criteria

### Takeaway
Both MVPs are "files in → evidence or report packet out" tools run as a service, not self-serve SaaS. For (A): a UNFI/KeHE deduction triage and dispute-packet generator. For (B): a packaging bill-of-materials builder plus a CAA-ready file and methodology generator, with exemption and flat-fee screening. Each has a 14-day test with hard numeric kill thresholds.

### Cited Findings
- **[F]** Anchors for (A):
  - UNFI dispute submission is an emailed spreadsheet with brand, check number and deduction invoice number in the subject line (search summary) — [Confido UNFI guide](https://confidotech.com/blogs/unfi-dispute-guide)
  - UNFI deduction codes (01 shortage, 02 pricing, 05 unsaleables, 10–12 promo/MCB, 30+ compliance); KeHE UDR 48-hour clock; K-Solve ~180-day window — [Endless Commerce](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/)
  - The BOL is "the most important document" — [SKU](https://sku.is/deduction-management-for-cpg-startups-the-five-keys-to-success/)
- **[F]** Anchors for (B):
  - CAA Producer Portal reporting of sales and weights by covered material — [CAA](https://circularactionalliance.org/producer-reporting)
  - Weak methodologies get rejected; per-SKU applicability analysis is recommended; CO/OR fee schedules due by Oct 2026 for Jan 2027 invoices — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/07/2026-epr-reporting-lessons-learned-initial-consolidated-reporting)
  - Flat-fee bands — [EcoEnclose](https://www.ecoenclose.com/blog/epr-fees-by-state)

### Inferences
**(A) MVP: "UNFI/KeHE Deduction Desk"** (3–4 weeks)
- **Inputs:**
  - UNFI and KeHE remittance and deduction exports (CSV/PDF) that the brand downloads.
  - PO, invoice and BOL/POD PDFs from the 3PL.
  - A promo calendar (MCB commitments).
- **Processing:**
  - An LLM extracts and normalizes lines, maps them to UNFI/KeHE codes, and sorts them into four groups: likely valid promo/MCB (reconcile only), disputable shortage, compliance, or pricing.
  - It attaches matching BOL/POD evidence and computes a deadline clock for each line.
  - It outputs the UNFI dispute spreadsheet and a KeHE K-Solve evidence packet.
- **Build stack:** Python/Streamlit or Retool plus the Claude API, Google Drive intake, and an Airtable tracker.
- **Pricing to test:** a free 12-month look-back audit, then 25–30% contingency on recovered dollars, or a flat $300–$750/month for brands under $5M.

**(A) 14-day experiment**
- **Days 1–3:** post an offer in Startup CPG and Foodbevy, and email 15 fractional-CFO or bookkeeping firms not partnered with Glimpse or Confido.
- **Days 4–10:** run manual audits, with AI assist, on any data received.
- **Days 11–14:** ask for a signed contingency agreement.
- **Kill if any of these hold:**
  1. Fewer than 15 qualified conversations (brands of $2–30M with UNFI/KeHE or big-box exposure).
  2. Fewer than 5 brands share deduction data.
  3. Fewer than 2 signed contingency or paid agreements.
  4. Recoverable dollars identified across all audits under $25K.
  5. More than half of qualified brands already use Glimpse, Confido, Vividly, Promomash or SPS Revenue Recovery.

**(B) MVP: "EPR Pack File"** (4–6 weeks)
- **Inputs:**
  - The SKU list with annual units.
  - Packaging spec sheets, supplier invoices or co-packer specs (PDFs), and photo-plus-scale weights where specs are missing.
  - Sales by channel, and by state where available.
- **Processing:**
  - An LLM extracts components and maps each to CAA material categories (Oregon's 60, plus each state's list).
  - It computes national tonnage and allocates it by state, using actual state sales or the CAA apportionment fallback.
  - It runs an exemption and flat-fee screen per state (revenue and tonnage bands) and estimates fees for CO, OR and illustrative CA rates.
  - It drafts the written methodology narrative.
  - It produces a CAA-portal-ready workbook plus a checklist of eco-mod bonus forms (CO 5% bonuses; OR LCA bonus).
- **Build stack:** spreadsheet templates, the Claude API for extraction and methodology, and a lightweight web form.
- **Pricing to test:** a free "EPR exposure check," then a $1,500–$5,000/year done-for-you filing for the 2027 cycle (31 May 2027 reports plus CA readiness), with a deposit taken now.

**(B) 14-day experiment** (run in Oct–Nov 2026 while CO/OR fee schedules and the CA plan are in the news)
- Contact 60 brands: the 20 consumer brands on the Oregon list plus 40 mid-size food, beverage and personal-care brands with California retail distribution (Expo West exhibitor list, Startup CPG).
- Offer the free exposure check, delivered within 48 hours.
- **Kill if any of these hold:**
  1. Fewer than 10 discovery calls.
  2. More than 60% of respondents are exempt, on flat fees, or report that filing took under one day in-house.
  3. Fewer than 3 brands agree to pay a deposit of at least $500 toward a 2027 filing at a price of at least $1,500/year.
  4. Fewer than 2 brands can supply packaging spec data within the 14 days (if data is unobtainable, the service cannot be delivered).
- **Advance signal:** at least 3 deposits plus at least 1 brand above $30M asking for eco-mod or over-reporting review.

### Gaps
- The CAA portal's upload template format was not retrieved, so the MVP's export spec needs confirming from a registered producer's account or CAA guidance.
- The legal or contractual risk of an India-based operator handling retailer portal credentials (A) or filing on a producer's behalf (B) was not researched.

## Q9. Verdicts

### Takeaway
- **(A) Deduction recovery for $2M–$100M CPG brands: REJECT for the top-five shortlist.** The pain is real, but this is not an overlooked market. At most it is a fallback services business.
- **(B) Multi-state packaging EPR data compilation and reporting for small and mid-size brands: ADVANCE WITH CONDITIONS.** It is lower-confidence than the earlier notes implied, because small brands are largely exempt or on flat fees. The viable target is brands of roughly $10M–$150M with California and multi-state exposure, served as a done-for-you service. Willingness to pay must be proven in the 14-day test before building.

### Cited Findings
- **[F]** Reasons to reject (A):
  - Glimpse: $52M raised, a16z-led, Apr 2026, 200+ brands, integrations for UNFI, KeHE and Walmart.
  - Confido: $77M raised, Insight-led, 24 Sep 2026, 250+ brands, a startup plan.
  - SPS Revenue Recovery covers UNFI and KeHE, includes full service, and is backed by about $420M+ of acquisitions.
  - Promomash (500 brands) and Vividly (150+) already serve emerging brands.
  - Contingency, no-minimum offers already exist (RevRecoup), as do risk-free trials and look-backs (Glimpse).
  - Channel partnerships are taken (Glimpse–PRESENCE; BELAY with Startup CPG and Foodbevy).

  Sources: Q2 table and Q6.
- **[F]** Reasons to advance (B):
  - Oregon was upheld on 27 Aug 2026.
  - The California plan was submitted on 13 Oct 2026, with the sales restriction from 1 Jan 2027.
  - Up to eight CAA reports per year; weak methodologies are rejected; inaccuracy charges run up to $5,000 or the fee amount.
  - 304 non-compliant producers are publicly listed, including emerging food brands.
  - California has 5,700+ producers.
  - Incumbents are either enterprise and demo-only (Lorax, Assent, Ecoveritas) or ultra-cheap and low-quality (PacForm at $48/year).

  Sources: Q3 and Q4.
- **[F]** Conditions and risks for (B): exemptions under $1–5M; flat fees of $800–$5,800 in CO and OR; EPR a "rounding error" for most brands today; the NAW Ninth Circuit appeal and California suits — sources in Q3 and Q6.

### Inferences
- **[I]** Why (A) is rejected despite real pain:
  - A solo, India-based non-engineer would compete on labour against venture-subsidized AI products with portal integrations and channel partners.
  - The segment funded players ignore (under $5M) yields only about $1–10K/year per client, by my illustrative arithmetic.
  - Retailer portal credential access is a trust hurdle for an offshore operator.

  Keep it only as a possible cash-flow service, not a top-five startup.
- **[I]** Conditions for advancing (B):
  1. Target $10–150M omnichannel food, beverage and personal-care brands with California retail exposure. Avoid DTC-only microbrands, which are commoditized.
  2. Sell as a fixed-fee, done-for-you annual filing with an AI-assisted back-end. Add an outcome kicker (a share of eco-mod bonuses or verified over-reporting corrections) only for brands above $50M.
  3. Pass the Q8 kill criteria by late Nov 2026, so the service is ready for Jan 2027 invoices and the 31 May 2027 reports.
  4. Re-check the Ninth Circuit and *Nebraska v. Heller* each quarter, and confirm the flat-fee producers' reporting burden.

  If more than 60% of contacted brands turn out to be exempt or on flat fees with trivial filing, downgrade (B) to reject.

### Gaps
- Neither verdict rests on direct willingness-to-pay evidence; none was found publicly for either candidate.
- The (B) verdict depends on the unconfirmed share of brands above the flat-fee and exemption thresholds, and on whether flat-fee producers still face full material-level reporting.
