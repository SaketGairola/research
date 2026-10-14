# Stress test: (A) Section 232 supplier-declaration hub and (B) long-tail IEEPA refund / protest-deadline tracker (as of 14 Oct 2026)

Scope note: this file covers only the gaps left by `physical_economy_ops.md` (section 2 and Opportunities A and C) and `regulatory_structural_shifts.md` (IEEPA/CAPE entries and Opportunity 1). Those files already cover the Feb 20, 2026 *Learning Resources* ruling, CAPE Phases 1–3, the ~$166B / ~53M-entry / ~330k-importer pool, the Sidley secondary-market data, the April/June 2026 232 overhaul as summarized by law firms, Gaia Dynamics, Zollback, TariffsTool and Flexport drawback pricing. They are not repeated here except where new primary evidence changes them.

Method and limits: 25 WebSearch calls were used (2 returned errors because of blocked Indian news domains). Wherever possible I read primary documents directly instead: Federal Register PDFs from govinfo.gov, the White House 232 annex PDF, the CIT slip opinion, CBP pages and a CBP CSMS bulletin, and supplier and broker PDFs. federalregister.gov full-text and ecfr.gov blocked this IP, so the govinfo PDFs and Cornell LII stood in for them. These could not be read: CRS IN12519 (403), EEPC India site (JavaScript-only), ICPA answer database (members only), Hobby Lobby's 232 vendor sheet (403), Altana product pages (JavaScript-only) and the Barnes Richardson article (empty render). Labels: **[F]** = observed fact with source; **[I]** = my interpretation.

## 1. What is the current (Oct 2026) status of Section 232 steel/aluminum/copper/derivative tariffs and their reporting requirements, and how many HTS lines and importers are affected?

### Takeaway
Section 232 metals duties are fully in force and still expanding. The Supreme Court IEEPA ruling did not touch them. CBP is now **hard-rejecting** entry summaries that lack copper smelt/cast data for four HTS lines (from Sep 14, 2026). The supplier data an importer needs per part is now metal **weight** (for the 15% threshold and the 85%-US-metal test), **country of melt/pour or smelt/cast**, and for USMCA goods the **value of US-made parts**. Metal *value* is no longer needed for most goods. My count of the April 2026 annexes is about 246 + 339 + 42 dutiable HTS references (mixed 4- to 10-digit), but I found **no count of affected importers**.

### Cited Findings
**Legal instruments (primary)**
- **[F] Proclamation 11021** (Apr 2, 2026; 91 FR 18201, published Apr 9, 2026) applies to goods entered on or after 12:01 a.m. EDT Apr 6, 2026. Its main provisions:
  - Duty applies to full value. Annex I-A is 50% and Annex I-B is 25%. Annex III lists temporary reduced-rate derivatives, and Annex II removes products from scope.
  - A **10% rate** applies to derivatives whose aluminum was "smelted and cast in the United States," or steel "melted and poured in the United States," or copper "smelted and cast in the United States."
  - The 200% rate on Russian-smelted or Russian-cast aluminum continues.
  - Clause 11 **terminates the old 232 inclusion processes** and lets Commerce and USTR add derivatives directly.
  - Clause 20 says: "Importers shall provide to CBP the information necessary to identify the countries where the copper used in the manufacture of copper article imports … are smelted and … cast. CBP shall implement the smelt and cast information requirements as soon as practicable."
  - Source: [Federal Register 2026-06960](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states) ([govinfo PDF](https://www.govinfo.gov/content/pkg/FR-2026-04-09/pdf/2026-06960.pdf))
- **[F] Annex IV** (US note 16(c)) says the 232 headings "apply to the full customs value." For articles **not in HTS chapters 72, 73, 74 or 76**, they "only apply where the weight of the applicable metal is at least 15 percent of the weight of the imported article". "If an article is classified in a provision that is present on multiple lists, use the aggregate weight of the listed metals." — [White House annexes PDF, Apr 2026](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf)
  - This settles a conflict. One vendor says the 15% test is "by value" — [FreightFigures](https://www.freightfigures.com/articles/section-232-15-percent-de-minimis-metal-content-test-2026) (search summary). The primary annex text says weight.
- **[F] Proclamation 11032** (Jun 1, 2026; 91 FR 34085, published Jun 4; effective Jun 8, 2026):
  - Adds "aluminum lithographic plates and steel racks" as derivatives.
  - Lowers the "entirely" American-metal threshold "from 95 percent … to 85 percent". Metal is deemed entirely US "if such aluminum, steel, and copper account for at least 85 percent of weight."
  - Sets a **25%** rate for Annex I-C articles from Jun 8, 2026 to Dec 31, 2027. Products of Argentina, Ecuador, El Salvador, Guatemala, Japan, Korea, Liechtenstein, Switzerland, Taiwan, the UK and the EU are capped at a **15% all-in** rate.
  - USMCA goods pay 25% "only to the non-U.S. content," where non-US content is "the total value of the product minus the value attributable to parts produced in the United States". The total is floored at 15%, and "If CBP determines that an importer has engaged in fraud or has deliberately misled … regarding the United States content … CBP shall impose penalties."
  - Annex I-C rates revert to the Proclamation 11021 rates on **Jan 1, 2028**.
  - Source: [Federal Register 2026-11314](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states) ([govinfo PDF](https://www.govinfo.gov/content/pkg/FR-2026-06-04/pdf/2026-11314.pdf))
- **[F] Proclamation 11045** (Jul 20, 2026; 91 FR 46635, Jul 23, 2026) creates an aluminum "onshoring" program. Companies with approved plans to build primary-aluminum capacity (construction start by Jan 20, 2029) may import a matching quantity of primary aluminum "at half the section 232 rate." — [Federal Register 2026-14990](https://www.federalregister.gov/documents/2026/07/23/2026-14990/further-strengthening-actions-taken-to-adjust-imports-of-aluminum-into-the-united-states)
- **[F] Proposed expansion:** BIS requested comments (91 FR 50756, Aug 6, 2026; comments due Aug 27, 2026) on adding 14 derivative categories. They are aluminum powder, brass-wind instruments, welding-machine parts, floor safes, certain conductor cables, fire extinguishers, heat-exchange-unit parts, hydraulic engine/motor parts, certain cranes, mobile lifting frames and straddle carriers, three types of trailers and semi-trailers, and filled steel containers. Most would be at 25%, and agricultural trailers at 15%. — [Federal Register 2026-15961](https://www.federalregister.gov/documents/2026/08/06/2026-15961/request-for-public-comments-on-the-proposed-implementation-of-duties-on-additional-aluminum-steel); [SteelOrbis, Aug 11, 2026](https://www.steelorbis.com/steel-news/latest-news/us-proposes-expanding-section-232-tariffs-to-14-additional-derivative-product-categories-1470151.htm). **No final inclusion decision was found.**

**CBP reporting mechanics**
- **[F]** CBP's 232 FAQ (last modified Sep 21, 2026) says "ACE will still require the steel melt and pour or aluminum smelt and cast country to be reported." The page does not address the 15% or 85% thresholds. — [CBP 232 FAQs](https://www.cbp.gov/trade/programs-administration/entry-summary/232-tariffs-aluminum-and-steel-faqs)
- **[F] CSMS #69711865** (Aug 31, 2026) says that effective **Sep 14, 2026**, ACE "will reject entry summaries" for HTS 8544.42.10, 8544.42.20, 8544.42.90 and 8544.49.10 where the copper primary country of smelt and country of cast are not reported. The fatal error is F794 "ADDTNL DEC TYPE RQRD FOR ARTICLE". "OTH" is allowed when a country is unknown. — [CBP CSMS via GovDelivery](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/427b7f9)
- **[F]** The underlying copper requirement is **CSMS #69252300** (Jul 15, 2026), effective Jul 30, 2026, with Additional Declaration Type 12 and CATAIR v109. This comes from broker and law-firm summaries, not the CSMS itself. — [Mohawk Global](https://mohawkglobal.com/trade-translation/cbp-issues-guidance-on-section-232-copper-smelt-and-cast-reporting-requirements/); [Willson Intl](https://www.willsonintl.com/news/guidance-on-section-232-copper-smelt-and-cast-reporting-requirements/) (search summaries)
- **[F]** June 2026 implementation guidance came in **CSMS #68855869** (posted Jun 8, 2026) with a supplemental HTS mapping document. — [Willson Intl, Jun 8, 2026](https://www.willsonintl.com/news/guidance-issued-on-updated-section-232-duties/). April guidance was CSMS #68253075 (Apr 3, 2026). — [SEKO 232 timeline PDF, Apr 27, 2026](https://www.sekologistics.com/media/gldhncwq/section232_2026timeline.pdf)
- **[F]** A Jun 13, 2025 CBP notice (CSMS #65340246) introduced reporting rules for aluminum with unknown smelt or cast countries. — [SEKO timeline](https://www.sekologistics.com/media/gldhncwq/section232_2026timeline.pdf). A UPS broker form says products "of unknown country of cast or smelt … have a duty rate 200%, applied to the full value." — [UPS Section 232 form (hosted copy)](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf); also [Z2Data, mod. Jul 16, 2026](https://www.z2data.com/insights/why-you-need-supply-chain-visibility-for-section-232/)

**Scale**
- **[F] My count** of unique HTS references in the April 2026 White House annex PDF, which mixes 4-, 6-, 8- and 10-digit references:
  - Annex I-A (50%): 246, chapters 72/73/74/76.
  - Annex I-B (25%): 339, chapters 73/76/82/83/84/85/86/87/94.
  - Annex III (temporary list): 42, chapters 82/84/85/90.
  - Annex II (removed): 166.
  - Source: [White House annexes PDF](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf)
  - A third-party site gives different post-June counts: I-A 279, I-B 313, II 175 and IV 882. — [ustariffrates.com](https://ustariffrates.com/section-232-tariffs) (search summary). The difference likely reflects the June 8 changes and counting method. Neither is a count of 10-digit statistical lines.
- **[F]** Section 232 added "over 400 new HTSUS subheadings" of derivatives on Aug 18, 2025. — [SEKO timeline](https://www.sekologistics.com/media/gldhncwq/section232_2026timeline.pdf)
- **[F]** The 232 metals regime dates back to Proclamations 9704/9705 of March 8, 2018, as recited in Proclamation 11045. — [FR 2026-14990](https://www.federalregister.gov/documents/2026/07/23/2026-14990/further-strengthening-actions-taken-to-adjust-imports-of-aluminum-into-the-united-states)

### Inferences
- **[I]** The April 2026 full-value switch removed the *value* half of the old data problem but left the *weight and origin* half. A product outside chapters 72–76 now flips between 0% and 25–50% of its entire value at the 15%-by-weight line. That makes weight data more consequential per part than before, even though there are fewer fields.
- **[I]** The copper hard-reject is the clearest evidence of an "entry cannot be filed without supplier data" moment. It covers only four 8544 lines today. Clause 20 of 11021 implies copper reporting could broaden.
- **[I]** Section 232 is being actively built on: an inclusion proposal in August, an aluminum incentive in July and new derivatives in June. It is now the administration's main metals tool. Policy churn per HTS line is ongoing, which favours a "re-check my catalogue each time the list changes" feature.

### Gaps
- **Number of US importers paying 232 duties and the dollar value of 232 collections in 2026:** not found. CRS IN12519 returned 403, and I found no CBP collections table.
- Whether the 14 proposed derivative categories were finalized after Aug 27, 2026: not found.
- Annex IV's HTSUS note says it is effective "April 7, 2026," while the proclamation says April 6. This is a minor discrepancy I did not resolve; FR 2026-08297 (Apr 29, 2026) published "technical corrections."
- Whether CBP has issued 15%-weight or 85%-US-content substantiation guidance, such as required documents: not found on the CBP FAQ page.

## 2. What happened to the Section 122 surcharge after July 2026, and to IEEPA refunds and appeals after the Oct 8, 2026 class certification? How much refund money remains unclaimed, and by whom?

### Takeaway
The 10% Section 122 surcharge **expired on Jul 24, 2026** and was effectively replaced the same day by Section 301 "forced-labor" tariffs of 10% or 12.5% on 60 economies, India among them at 10%. These **exempt goods subject to Section 232**. Section 122 refunds exist only for three plaintiffs. The Federal Circuit has said the government is "likely to prevail."

For IEEPA, about **$126B of roughly $166B has already been refunded** (as of Oct 2, 2026). The CIT says about **$30B** would stay in the Treasury without further action, held mostly by **"tens of thousands" of "overwhelmingly small importers"** and non-plaintiffs with finally liquidated entries. The Oct 8 class certification is designed to get that money back through a *single automated mass-reliquidation order*, not through individual claims.

### Cited Findings
**Section 122**
- **[F]** The surcharge "expired on its own on July 24, 2026" under the 150-day cap, and "Congress did not act to extend it." — [Strix, last reviewed Aug 31, 2026](https://www.strixsmart.com/section-122-surcharge); [Strix, Sep 8, 2026](https://strixsmart.com/resources/blog/section-122-refund-status) (vendor sources)
- **[F]** The CIT held the surcharge invalid on May 7, 2026. On Jun 11, 2026 the Federal Circuit stayed that judgment pending appeal and found the government likely to prevail ("may be incorrect" of the CIT's reading). The injunction covers only three plaintiffs: the State of Washington and two importers. — [Steptoe via Mondaq, Jul 1, 2026](https://www.mondaq.com/unitedstates/international-trade-investment/1810106/appellate-court-raises-more-uncertainty-in-section-122-tariff-litigation)
- **[F]** As of Sep 8, 2026 there was no merits opinion in Fed. Cir. Nos. 2026-1804/-1805 and **no CBP refund process for Section 122** ("As of September 8, 2026, there isn't one"). Protests must be filed within 180 days *after*, not before, liquidation. — [Strix, Sep 8, 2026](https://strixsmart.com/resources/blog/section-122-refund-status)
- **[F] Replacement tariffs:** USTR imposed Section 301 tariffs in 60 investigations. The rate is 10% for economies with a forced-labor import ban or an Agreement on Reciprocal Trade commitment (including **India**, Canada, Mexico and the UK) and 12.5% for others (including China). They apply to goods entered on or after 12:01 a.m. Jul 24, 2026. Exemptions include "all articles and parts of articles subject to tariffs under Section 232." USTR notes "auto parts already subject to Section 232 tariffs, are exempt." — [Federal Register 2026-15181, Jul 28, 2026](https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies)

**IEEPA after Oct 8, 2026 (primary: CIT Slip Op. 26-123)**
- **[F]** *Freestyle World, Inc. v. CBP*, Court No. 26-01088, decided Oct 8, 2026 (Judge Eaton). Class certified under **USCIT Rule 23(b)(2)**, which works "without requiring notice or opt-out rights." The class covers IORs that paid IEEPA duties from Feb 1, 2025 to Feb 19, 2026 and have not filed a separate suit. Class counsel are Barnes Richardson & Colburn and Lieff Cabraser. — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf); [Thompson Hine, Oct 9, 2026](https://www.thompsonhinesmartrade.com/2026/10/cit-certifies-a-tariff-refund-class/)
- **[F]** As of Oct 2, 2026, "approximately $136.6 billion in potential and certified refunds has been accepted for processing in CAPE, and … approximately $126 billion in duties plus interest has been refunded." CAPE has processed 27.4M entries and liquidated or reliquidated 21.19M. — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)
  - This updates the earlier ~$122B "certified" figure (Sep 11) in `physical_economy_ops.md`.
- **[F]** "were CAPE to cease to function today approximately $30 billion in unlawfully collected duties would remain on deposit in the Treasury." Many IORs "have not taken advantage of CAPE. It is believed that these are overwhelmingly small importers who, because of the cost or effort involved in filing a CAPE declaration, or because they are unaware of the program, will never take advantage of CAPE." The class "includes some tens of thousands of importers." — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)
- **[F]** As of Oct 7, 2026, "more than 4,000 nearly identical cases have been filed involving around 7,000 plaintiffs." CAPE Phase 3 (Oct 6, 2026) lets those plaintiffs file for finally liquidated entries. — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)
- **[F]** The court reasons that relief "would not be labor-intensive, individualized, or manual." "The mechanical, formulaic task of calculating refunds has already been performed by Customs millions of times." — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)
- **[F]** On Jun 3, 2026 the government appealed the CIT order requiring liquidation or reliquidation of all affected entries (*V.O.S. Selections*, appeal docketed No. 26-1895, Fed. Cir.). Briefs have been filed, and "the CAFC's decision will be rendered in due course." — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf). No argument date was found — [Foley, Jun 2026](https://www.foley.com/insights/publications/2026/06/what-every-multinational-should-know-about-the-governments-ieepa-federal-circuit-appeal/) (search summary).
- **[F]** Next steps were a closed conference on Oct 13 and proposed scheduling due Oct 22, 2026. A practitioner said the class "doesn't immediately expand refund eligibility or direct payment." — [Supply Chain Dive, Oct 9, 2026](https://www.supplychaindive.com/news/federal-court-clears-way-for-class-action-suit-against-ieepa-tariffs/832600/)
- **[F]** CBP rules (last modified Sep 30, 2026):
  - "Only the IOR or the licensed customs broker who filed the entries can file a CAPE Declaration." Attorneys cannot file.
  - "All refunds are required to be paid electronically via Automated Clearing House (ACH)."
  - "To get a refund, bank account information must be provided using an ACE Portal account."
  - Finally liquidated entries of non-litigants have no CBP path yet; CBP is "evaluating" them.
  - Source: [CBP IEEPA Duty Refunds](https://www.cbp.gov/trade/programs-administration/trade-remedies/ieepa-duty-refunds)

### Inferences
- **[I]** The unclaimed IEEPA pool (~$30B) is real, but the CIT is explicitly trying to return it **without any action by small importers** beyond having an ACE portal account and ACH banking on file. If the class injunction issues and survives appeal, a "help me claim" product loses most of its job. If the government wins the appeal, non-plaintiffs with finally liquidated entries may have no remedy at all. In both cases a tracker has little to track.
- **[I]** The remaining work for a small importer is mostly one-time administration: create an ACE portal account, enroll for ACH refunds, and possibly file CAPE for still-eligible entries through its broker. This is cheap and quick, CBP gives it free guidance, and it does not recur.
- **[I]** The Section 301 replacement tariffs exempt 232 goods. For goods outside chapters 72–76, the 15%-by-weight determination now also decides **whether a 10–12.5% Section 301 duty applies instead of a 25–50% Section 232 duty**. That strengthens the case for A, not B.
- **[I]** Section 122 refunds are a speculative second wave. Entries from Feb 24 to Jul 24, 2026 will liquidate in 2027 (the typical ~314-day liquidation cycle is my general knowledge, not verified this session), so protest deadlines fall in 2027. But the Federal Circuit's stay finding makes refunds for non-plaintiffs uncertain.

### Gaps
- Total Section 122 duties collected: not found. Strix says only "roughly five months of duties."
- How many class members lack an ACE portal account or ACH enrollment, which is the real residual friction: not found.
- Federal Circuit argument dates for No. 26-1895 and Nos. 2026-1804/-1805: not found.
- Whether the government will appeal the class certification: Thompson Hine says this is "possible," and no notice of appeal was found.

## 3. How do importers collect supplier metal-content and origin data today, and what evidence exists of errors, penalties, CBP requests for information, or rejected entries?

### Takeaway
Collection today is **free paper forms and invoice annotations**. Large buyers push the obligation and the financial liability onto overseas suppliers through purchase-order terms. Brokers use PDF intake forms that can be kept on file for a year as "blanket" declarations. There is solid evidence of enforcement in general: ACE hard rejects, CF-29 notices of action, and False Claims Act settlements including Section 232. There is **no public evidence of complaint volume** specifically about supplier non-response.

### Cited Findings
- **[F] GE Vernova supplier memo (Jul 22, 2026, to "GE Vernova Global Suppliers")**, publicly posted:
  - Required on commercial invoices: country of melt & pour and steel content by weight; for aluminum and copper, country of smelt, second smelt and cast, plus content by weight.
  - In-scope parts with no steel, aluminum or copper "must report zero (0) SAC weight."
  - For multi-sourced metal, suppliers may use "FIFO" and "must maintain documentation … available for audit."
  - "shipments … lacking this information will not be allowed entry into the U.S. and will be returned to sender."
  - Suppliers "shall reimburse GE Vernova for any duties, penalties, fines, storage fees, redelivery costs."
  - Data "may be reported on the invoice in any format."
  - Source: [GE Vernova, Section 232 supplier requirements](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)
- **[F] UPS broker intake form.** The "Section 232 Copper, Steel, & Aluminum Form" asks per part number for country of melt & pour, the aluminum cast, largest-smelt and second-largest-smelt countries, and content value and weight in kg.
  - It has a "blanket document for multiple entries" option: "The information provided will be kept on file for a period of one year."
  - Guidance on the form: "Best place to find melt/pour countries: steel mill test certificate"; "value/weight: costed bill of material"; signer certifies "reasonable care."
  - The form predates the April 2026 full-value change. — [UPS form (hosted copy, file dated 10/14/25)](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf)
- **[F] Intel** publishes a "Customs Affidavit – Section 232 Aluminum & Steel": an "Affidavit of weight, value, and country of smelt/melt or cast/pour." It is dated 2025-06-02 and sits in the "Intel Supplier Documents" collection. — [Intel](https://www.intel.com/content/www/us/en/content-details/850985/customs-affidavit-section-232-aluminum-steel.html)
- **[F]** An ICPA (trade-compliance association) members' forum thread is titled "Template for Requesting Mill Certifications from Suppliers" for 232 smelt/cast. Content is members-only. — [ICPA answer database](https://www.icpainc.org/category/answer-database/sec-232/) (search snippet)
- **[F]** CBP or its 232 guidance customarily points to mill test certificates for melt/pour, and the mill certificate is filed via the Document Image System. — [CSMS #62582900 (GovDelivery)](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3baf074) (search summary; an older bulletin)
- **[F]** Vendor guidance tells importers to "Get the smelt-and-cast countries from the manufacturer before quoting." It says "CBP Notice of Action" applies for missing melt-and-pour data and that there is False Claims Act exposure for unsupported US-content claims. — [Tandom, updated May 5, 2026](https://tandom.ai/resources/section-232-steel-aluminum-copper-duties-2026) (vendor)
- **[F] CF-29s.** One trade-law firm received "six CF-29s across four clients in one recent week" on 232 derivative valuation. Only one of six extension requests was granted. CBP's Base Metals Center was rejecting exclusion of fabrication and labor from metal content. — [OFW Law, Dec 15, 2025](https://ofwlaw.com/cf-28-29-enforcement-what-importers-are-seeing-now-on-ieepa-and-steel-aluminum-tariffs/). This was under the *old* content-value regime.
- **[F] FCA enforcement:** On May 20, 2026, Farjess Inc., Royal Canadian Steel and their owner paid **$19M** over misrepresenting the origin of flat-rolled steel to evade AD/CVD **and Section 232** duties. The whistleblower was the company's own customs broker. — [JD Supra](https://www.jdsupra.com/legalnews/canadian-steel-companies-and-owner-to-9283735/) (search summary)
- **[F]** Perfectus Aluminum paid $549.5M (May 1, 2026), but that case concerned AD/CVD, not 232. — [Crowell](https://www.crowell.com/en/insights/client-alerts/not-alls-weld-that-ends-weld-duty-evasion-scheme-ends-in-historic-dollar5495m-fca-settlement)
- **[F] Litigation:** A fastener importer (Express Fasteners) reportedly sued CBP after CBP rejected its metal-content method and applied 50% to the full value of screws and fasteners. — [Barnes Richardson](https://www.barnesrichardson.com/importer-challenges-legality-of-section-232-steelaluminum-valuation-guidance) (search summary; page did not render; date and outcome unverified)
- **[F] Recordkeeping:** Millproof says the "recordkeeping obligation under 19 CFR 163 sits with you as importer of record" and "Records stay demandable for five years." — [Millproof](https://www.millproof.com/) (vendor)

### Inferences
- **[I]** The dominant workflow is a **buyer-imposed supplier obligation**: put the data on the invoice in any format and keep proof. That makes the **overseas supplier the party with the most direct pain and liability**, through chargeback clauses. The US importer and broker are secondary.
- **[I]** Brokers and buyers solve "collection" with free forms. What they do not solve is maintaining that data **per part, per supplier and over time**: mill switches, FIFO across multiple sources, the 85%-US-metal test, and five-year substantiation. That residual is the only defensible product surface, and it is narrower than in the original sketch.
- **[I]** Enforcement evidence is about valuation and origin fraud, not about failing to collect supplier data. It shows stakes but does not prove routine pain.

### Gaps
- No quantified data on CF-28 or CF-29 volume for 232 after April 2026, rejected-entry counts, or supplier non-response rates.
- No practitioner complaints (forums, Reddit, LinkedIn) were collected. Search budget was spent on primary documents.
- Hobby Lobby's "Section 232 Detail Sheet – August 2025" for vendors appeared in search but returned 403. It is unverified evidence that a retailer pushes the requirement to vendors.

## 4. Competitors for (A): who already offers Section 232 supplier-declaration collection, for which segment, and at what price?

### Takeaway
The candidate is **no longer "overlooked"**. **Millproof** sells almost exactly the MVP sketched in `physical_economy_ops.md`: per-part supplier links, mill-certificate extraction, a per-SKU ledger with the 15% calculation, a broker data pack and an audit binder, at **$299/month** with self-serve pricing. Enterprise players (Sourcemap, Assent, Z2Data, Altana) have 232 supplier-data offerings. GTM and ABI software (Thomson Reuters ONESOURCE) already carries the filing fields. Free broker forms cover the low end.

### Cited Findings
| Vendor | What it does for 232 (as stated) | Segment | Public pricing | Source |
|---|---|---|---|---|
| **Millproof** | "Each supplier gets one link and a short form per part number: metal weight, metal value, country of melt and pour or smelt and cast. Reminders, escalation"; mill certificate and invoice extraction "with the source document attached to every value"; "per-SKU ledger with version history, staleness flags, the 15% threshold calculation"; "entry-line data pack for your broker, and an audit binder when CBP asks under 19 CFR 163"; re-runs catalogue against new lists; free "content-gap check" | US importers of record | **$299/month, 3 months prepaid ($897); first 250 part numbers; "Six slots"; full refund if "no usable ledger 30 days in"** | [millproof.com, accessed Oct 14, 2026](https://www.millproof.com/) |
| **MyCustomsInfo (CustomsPlus Ltd)** | Independent 232 compliance *audit* reconciling ACE entries with melt-and-pour or smelt-and-cast certificates, supplier composition certificates and BOMs (sub-15% test); "never" files with CBP | CFOs, customs managers; "Every US importer with metal in the supply chain" | **$8,000–$50,000 per audit cycle** | [mycustomsinfo.com, last reviewed Oct 12, 2026](https://mycustomsinfo.com/section-232-compliance) |
| **Sourcemap** | "Section 232, Tariff Management and Customs Compliance — Map steel, aluminum, copper and critical minerals to the exact processing sta[ge]"; "Assemble complete, audit-ready documentation for Section 232 tariffs and US Customs inquiries"; "Gather tariff data … directly from suppliers across all tiers" | "250+ major brands"; semiconductor, solar, "largest infrastructure suppliers" | None public | [sourcemap.com](https://sourcemap.com/); [tariff solution page (metadata Oct 9, 2026)](https://sourcemap.com/solutions/tariff-solution) |
| **Assent** | Recommends collecting smelt/melt data; "Our trade compliance solution enables multi-level country of origin collection"; "Metal Sourcing" solution: "Verify the origin of your metals" | Manufacturers (enterprise network) | None public | [Assent blog, Sep 3, 2025](https://www.assent.com/blog/prepare-for-section-232-tariffs/) |
| **Z2Data** | "Z2 Sub-Tier Intelligence" helps "identify and document the countries of origin, smelt, cast, and pour"; Z2 teams "reach out to suppliers" for composition, melt/pour, mill certs | Importers with tier-3/4 metal suppliers; electronics | None; free trial or demo | [Z2Data, mod. Jul 16, 2026](https://www.z2data.com/insights/why-you-need-supply-chain-visibility-for-section-232/) |
| **Thomson Reuters ONESOURCE Global Trade** | Import Management "Copper Smelt and Cast" action (primary smelt mandatory, secondary optional, most-recent cast mandatory); data "fed on to our USABI self-filing solution … or … to a broker"; no supplier-solicitation feature mentioned | Enterprise self-filers | None public | [TR help page (undated)](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/import-management/copper-smelt-and-cast) |
| **GingerControl** | "Compliance Radar" maps new notices to your HTS codes; Parts Library models 232 duty; explicitly does **not** collect supplier data or file melt/pour | Importers, exporters, brokers | None public | [GingerControl, Jul 1 / upd. Oct 11, 2026](https://gingercontrol.com/blog/section-232-derivative-inclusion-list-exposure-monitoring) |
| **Altana** | Product pages titled "For Suppliers," "For Customs Brokerage: Automate the Full Workflow," "Tariffs & Trade Compliance"; works with US customs "since 2023" (press quote on homepage). Pages rendered only titles, so 232 features are unverified | Enterprise, government, brokers | None found | [altana.ai](https://altana.ai/); [for customs brokerage](https://altana.ai/solutions/for-customs-brokerage) |
| **Descartes** | Customs compliance suite (ABI filing, HTS classification, duty and tariff data); Datamyne blog covered the April 232 change (Jul 9, 2026). **No 232 supplier-declaration module found** | Brokers, forwarders, importers | None public | [Descartes customs page](https://www.descartes.com/solutions/customs-and-regulatory-compliance); [Datamyne blog](https://www.datamyne.com/knowledge-center/imports/recast-section-232-tariffs-apply-rates-to-full-value-of-products-with-metal-content/) (search summary) |
| **Gaia Dynamics** | Tariff discovery, classification, alerts, tariff audits, API; **no 232 or supplier module mentioned** | Brokers and importers | None; free trial | [gaiadynamics.ai](https://www.gaiadynamics.ai/) |
| **Brokers' own forms** (UPS; C.H. Robinson advises "Reach out to your customs broker") | Free PDF intake forms, blanket for one year | Broker clients | Free (bundled) | [UPS form](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf); [C.H. Robinson, Apr 16, 2026](https://www.chrobinson.com/en-GB/resources/blog/section-232-changes-for-aluminum-copper-steel/) |
| **Large buyers' own requirements** | GE Vernova invoice-data mandate; Intel affidavit | Their suppliers | Free (imposed) | [GE Vernova](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf); [Intel](https://www.intel.com/content/www/us/en/content-details/850985/customs-affidavit-section-232-aluminum-steel.html) |

- **[F]** Prewave and Source Intelligence homepages showed no 232 mention in a text scan on Oct 14, 2026. That is a homepage-only check, not proof that no product exists. — [Prewave](https://www.prewave.com/); [Source Intelligence](https://www.sourceintelligence.com/)
- **[F]** Flexport: I found no 232 supplier-data product. A search returned nothing Flexport-specific. Avalara was not re-checked for 232; prior notes found classification and rates only.
- **[F]** Millproof's page says lists change "at each BIS inclusion window (January, May, September)." Proclamation 11021 *terminated* those inclusion processes. — [Millproof](https://www.millproof.com/) vs [FR 2026-06960](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states)

### Inferences
- **[I]** Millproof is evidence that a solo-scale team can build this product and price it self-serve. It is also evidence that the importer-side niche is being contested **right now**. I found no evidence of Millproof's traction, and "six slots" suggests it is very early. Matching Millproof on features is not a moat.
- **[I]** The space that looks least crowded is the **supplier (exporter) side**: a tool that helps an overseas manufacturer keep one per-part SAC record and output it in each US buyer's required format (GE Vernova invoice lines, UPS form, Intel affidavit). No vendor reviewed positions itself there. Enterprise tools target the buyer. This is a hypothesis.
- **[I]** Enterprise tools (Sourcemap, Assent, Z2Data) mean large importers are served. The segment left is small and mid importers, small brokers and small suppliers, where free forms compete.

### Gaps
- No pricing for Assent, Sourcemap, Z2Data, Altana, Descartes or ONESOURCE.
- No traction, customer or founding data for Millproof.
- I could not confirm whether Flexport, Avalara, Descartes CustomsInfo or CargoWise have *launched* a supplier-facing 232 declaration feature since July 2026.

## 5. Competitors for (B): who offers IEEPA refund recovery and at what fees, how much refund money remains unclaimed, and does preparing filings for others require a licensed customs broker?

### Takeaway
The long tail already has many contingency-fee vendors, with advertised fees **as low as 1.5%**, plus brokers, law firms and claim buyers. Under 19 CFR 111.1, preparing documents "intended to be filed with CBP" for a refund on someone else's behalf is **"customs business,"** which needs a broker license, "whether or not signed or filed by the preparer." CBP limits CAPE filing to the IOR or its filing broker, and excludes attorneys. A non-licensed, India-based founder cannot legally run B as a done-for-you service. The money pool is shrinking toward an automated class remedy.

### Cited Findings
- **[F] 19 CFR 111.1:** "Customs business" includes activities involving "the refund, rebate, or drawback of those duties." It also includes "the preparation, and activities relating to the preparation, of documents in any format and the electronic transmission of documents and parts of documents intended to be filed with CBP in furtherance of any other customs business activity, whether or not signed or filed by the preparer." It "does not include the mere electronic transmission of data received for transmission to CBP" or "corporate compliance activity" for a *related* entity. — [19 CFR 111.1 (Cornell LII)](https://www.law.cornell.edu/cfr/text/19/111.1)
- **[F] 19 CFR 111.2(a):** a license is required "to transact customs business as a broker." The exception is "An importer or exporter transacting customs business solely on his own account and in no sense on behalf of another." — [19 CFR 111.2 (Cornell LII)](https://www.law.cornell.edu/cfr/text/19/111.2)
- **[F]** "Only the IOR or the licensed customs broker who filed the entries can file a CAPE Declaration." — [CBP IEEPA Duty Refunds, Sep 30, 2026](https://www.cbp.gov/trade/programs-administration/trade-remedies/ieepa-duty-refunds)
- **[F] Refund vendors and fees:**
  - **Tariff Recovery Group:** "Fees as low as 1.5%," "$0" upfront, "Built for Small Business Importers." States it is "not a law firm or customs broker" yet "prepares CAPE filings." No date shown. — [tariffrecoverygroup.com](https://tariffrecoverygroup.com/)
  - **The Tariff Bureau:**
    - Contingency ("no recovery, no charge") plus flat-fee assessment and valuation tiers; amounts are "set forth in a written Engagement Letter."
    - Targets importers "typically with $500K or more in tariff exposure."
    - "CAPE claims are submitted by the importer of record or their licensed customs broker." (dateModified Oct 12, 2026) — [tariffbureau.com/services](https://tariffbureau.com/services)
    - Conflict: a search snippet attributed "$4,000 base + 12–15% contingency" and "$8,000–$18,000 flat fee" to this vendor (search summary). The page I fetched showed no amounts.
  - **GingerControl:** litigation firms "sometimes propose contingency fees of 15 to 25 percent," against hourly rates of $500–$1,500. It says small importers with unliquidated or recent entries need only their broker plus CAPE. — [GingerControl IEEPA guide](https://gingercontrol.com/blog/ieepa-tariff-refund-guide) (search summary)
  - **Freight Right:** files "for a small one-time fee," amount not stated. — [Freight Right](https://www.freightright.com/solution/ieepa-tariff-refund) (search summary)
  - **Flexport:** names IEEPA claims as one of "four separate programs" but publishes no IEEPA fee. Drawback is priced as a percentage of recovery. It has "returned more than $1B in refunds and tariff savings … over the last five years." — [Flexport](https://www.flexport.com/solutions/claim-tariff-refunds/)
  - Others in search results, not opened: [One Eagle Advisory](https://www.oneeagleadvisory.com/service/tariff-refund-recovery), [Capital Gurus IEEPA Recovery](https://ieepa.capitalgurus.com/), [TariffApprove](https://www.tariffapprove.com/). Prior notes add Zollback, TariffsTool, law firms and claim purchasers.
- **[F] Unclaimed money:** about $30B would remain if CAPE stopped (CIT, Oct 8, 2026). It is held by "tens of thousands" of mostly small importers and non-plaintiffs with finally liquidated entries. — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)

### Inferences
- **[I]** Software sold to the IOR, which then files "solely on his own account," appears to be the only clean model for a non-licensed founder. Done-for-you preparation for third parties looks like customs business. Several vendors appear to prepare CAPE filings without being brokers, which may be legal exposure for them and a warning for this founder. **Counsel review is needed. This is not legal advice.**
- **[I]** With fees advertised at 1.5% and a remedy designed to need no claimant action, the margin left for a new tracker is thin and short-lived.

### Gaps
- Actual realized fee levels and win rates for long-tail refund vendors: not found.
- Whether CBP has enforced 19 USC 1641 against unlicensed refund preparers in 2026: not found.
- Penalty amounts for unlicensed customs business were not verified. The 111.2 page cites none.

## 6. Indian angle: are Indian exporters (engineering goods, steel/aluminum derivatives, auto components) being asked by US buyers for melt-and-pour or metal-content data?

### Takeaway
I found **no Indian trade-press or EEPC/FIEO coverage** of US buyers demanding melt-and-pour or metal-content declarations from Indian exporters. Indirect evidence does exist. US buyers' requirements are addressed to "global suppliers" (GE Vernova). Steel, aluminium and derivatives were about a quarter of India's engineering exports to the US (2025). India gets no favourable 232 rate in the June 2026 proclamation. EEPC's chairman says uniform 232 duties are not hurting Indian exporters.

### Cited Findings
- **[F]** EEPC (June 2025): steel, aluminium and derivatives "account for nearly a quarter" of India's engineering goods shipments to the US, about **USD 5 billion** a year. — [The Tribune/ANI, Jun 2, 2025](https://www.tribuneindia.com/news/business/trumps-50-tariff-on-steel-aluminium-could-hurt-indias-engineering-goods-exports-eepc-india/amp)
- **[F]** EEPC Chairman Pankaj Chadha (Sep 2, 2026): "As long as my duty is the same as other nations, I see no reason why my business should go down." He cited "the 50 per cent Section 232 duty that applies uniformly." Engineering exports are "set to cross USD 23 billion this financial year." The reporter wrote that iron and steel products grew "102 per cent." — [ANI via webindia123, Sep 2, 2026](https://news.webindia123.com/news/Articles/Business/20260902/4493853.html)
- **[F]** India is **not** among the jurisdictions given the 15% all-in cap for Annex I-C articles (EU, Japan, Korea, UK, Switzerland, Taiwan and others). Indian Annex I-C goods pay 25% through Dec 31, 2027. — [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states)
- **[F]** Indian goods face the 10% Section 301 forced-labor tariff from Jul 24, 2026, but goods subject to 232 are exempt. — [FR 2026-15181](https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies)
- **[F]** GE Vernova's 232 memo is addressed to "GE Vernova Global Suppliers." It covers wind components such as "hubs, blades, pitch bearings, main shafts, generators" and makes suppliers reimburse costs. — [GE Vernova, Jul 22, 2026](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf). I did **not** verify that GE Vernova has Indian suppliers covered by this memo.
- **[F]** An older ET story (2023) quoted India's steel secretary favouring "melt and pour" as an FTA rule of origin. That is unrelated to US buyers. — (search summary of Economic Times, 2023; URL not accessible to the crawler)

### Inferences
- **[I]** The mechanism that would create Indian demand already exists: buyer purchase-order clauses that make the supplier liable. That makes an exporter-side "232 data pack" plausible. But I have **zero direct evidence** that Indian exporters are struggling with it. The founder's first experiment must collect that evidence through calls, not desk research.
- **[I]** EEPC's public stance is "uniform duty, no disadvantage," so the industry body is unlikely to push this as a pain point. Outreach would need to go to individual exporters and clusters (fasteners, castings, forgings, wire and cable).

### Gaps
- EEPC India circulars, FIEO advisories, ACMA (auto components) and IIF (foundries) guidance: not accessed (JavaScript sites or blocked domains).
- The Economic Times, Financial Express, Mint, Hindu BusinessLine and Indian Express were blocked for the search tool.
- No count of Indian exporters shipping 232-covered HTS lines to the US.

## 7. Disconfirming evidence: is this a temporary spike likely to reverse, do brokers or ERPs absorb it for free, and is the buyer too small or too concentrated?

### Takeaway
**(A)** is not a spike in the IEEPA sense. Section 232 rests on separate authority, dates back to 2018 and is being expanded. Its weakness is that (i) free broker forms and buyer-imposed invoice fields absorb basic collection, (ii) GTM and ABI software already carries the filing fields, and (iii) a near-identical low-priced product already exists. **(B)** is a spike that is ending. Most money is already refunded, the remaining pool is targeted by an automated class remedy, the work is legally restricted, and fees are compressed.

### Cited Findings
- **[F] Durability of 232:** the regime was established by Proclamations 9704/9705 (Mar 8, 2018) and modified again on Apr 2, Jun 1 and Jul 20, 2026. — [FR 2026-14990](https://www.federalregister.gov/documents/2026/07/23/2026-14990/further-strengthening-actions-taken-to-adjust-imports-of-aluminum-into-the-united-states). New derivatives were proposed on Aug 6, 2026. — [FR 2026-15961](https://www.federalregister.gov/documents/2026/08/06/2026-15961/request-for-public-comments-on-the-proposed-implementation-of-duties-on-additional-aluminum-steel). The IEEPA and 122 rulings "do not alter Section 232" (Miller Nash, Jul 8, 2026, cited in `physical_economy_ops.md`).
- **[F] Built-in sunset points:** the temporary Annex I-C rates end Dec 31, 2027, reverting to higher rates on Jan 1, 2028. — [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states). Country deals lower rates for some partners, but they still turn on where the metal was melted or smelted ("Trade Agreement Partner" clause in [Proclamation 11021](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states)).
- **[F] Free absorption:**
  - UPS blanket form kept for a year — [UPS form](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf)
  - GE Vernova's "any format" invoice data — [GE Vernova](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)
  - ONESOURCE copper fields feeding ABI — [TR](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/import-management/copper-smelt-and-cast)
  - C.H. Robinson: "Reach out to your customs broker" — [C.H. Robinson](https://www.chrobinson.com/en-GB/resources/blog/section-232-changes-for-aluminum-copper-steel/)
- **[F] Buyer concentration:**
  - NCBFAA "represents more than 1500 member companies" (elsewhere on the page "more than 1,400"). — [NCBFAA](https://www.ncbfaa.org/)
  - About 13,000 individually licensed brokers (CBP Dec 2024, per `physical_economy_ops.md`).
  - Large importers buy enterprise tools: Sourcemap cites "250+ major brands." — [Sourcemap](https://sourcemap.com/solutions/tariff-solution)
- **[F] B is ending:** $126B of ~$166B refunded; the class remedy is designed to be automated; CAPE filing is restricted to the IOR or broker; fees "as low as 1.5%" (all cited above). For Section 122, the Federal Circuit found the government likely to prevail. — [Steptoe/Mondaq, Jul 1, 2026](https://www.mondaq.com/unitedstates/international-trade-investment/1810106/appellate-court-raises-more-uncertainty-in-section-122-tariff-litigation)

### Inferences
- **[I]** For A, the realistic buyer is a **mid-size importer with hundreds to thousands of part numbers across many overseas suppliers**, or a **supplier serving several US OEMs**. The single-supplier, few-SKU long tail is served well enough by free forms. The reachable segment is real but smaller than "every importer with metal."
- **[I]** A political reversal (for example, a new administration in 2029) is the main long-run risk for A. The 2018 to 2026 history suggests 232 metals tariffs have outlasted administrations. That is background knowledge, not verified this session.
- **[I]** Even if tariffs fell, the five-year records obligation (19 USC 1508, per Millproof) would keep a smaller substantiation need alive for entries already made.

### Gaps
- No survey data on what share of importers or brokers already use a structured tool versus forms.
- No evidence on willingness to pay among small brokers or Indian exporters.

## 8. Who are 20 specific first-customer targets, by type or by verifiable public information?

### Takeaway
The verifiable targets fall into four groups: (1) importers of HTS lines with **hard-reject or newly proposed** 232 requirements, (2) suppliers of **named US buyers that publish 232 supplier mandates**, (3) **NCBFAA and regional broker associations** with public directories and events, and (4) Indian exporter networks (unverified demand). For B, the only identifiable pool is class members, who cannot be listed publicly.

### Cited Findings
Targets for A:
1. **Importers of insulated copper wire and cable (HTS 8544.42.10/.20/.90, 8544.49.10).** ACE has rejected summaries without copper smelt/cast data since Sep 14, 2026. — [CSMS #69711865](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/427b7f9)
2. **Importers of the 14 proposed derivative categories** (trailers, fire extinguishers, cranes, welding-machine parts, heat-exchanger parts, aluminum powder and others) and the companies that commented on the docket by Aug 27, 2026. Comments are public on regulations.gov; the docket was not opened. — [FR 2026-15961](https://www.federalregister.gov/documents/2026/08/06/2026-15961/request-for-public-comments-on-the-proposed-implementation-of-duties-on-additional-aluminum-steel)
3. **Importers of Annex III and Annex I-C machinery** (chapters 82/84/85/90). Temporary rates end Dec 31, 2027. — [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states); [annex PDF](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf)
4. **Importers of newly added steel racks and aluminum lithographic plates** (from Jun 8, 2026). — [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states)
5. **GE Vernova's global wind-component suppliers** (hubs, blades, pitch bearings, main shafts, generators). They are liable for 232 data failures under the Jul 22, 2026 memo. — [GE Vernova](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)
6. **Intel suppliers** asked to complete the public 232 aluminum and steel affidavit. — [Intel](https://www.intel.com/content/www/us/en/content-details/850985/customs-affidavit-section-232-aluminum-steel.html)
7. **Fastener importers (HTS 7318)**, given the Express Fasteners dispute over 232 metal content. — [Barnes Richardson](https://www.barnesrichardson.com/importer-challenges-legality-of-section-232-steelaluminum-valuation-guidance) (search summary)
8. **Companies in FTZ production notices** in the Federal Register that list Section 232 components (the Aug 6, 2026 issue includes FTZ Board notices, e.g., B-98-2026, FTZ 45). — [FR Aug 6, 2026 issue (govinfo PDF)](https://www.govinfo.gov/content/pkg/FR-2026-08-06/pdf/2026-15961.pdf)
9. **NCBFAA member brokerages** (1,400–1,500 firms) through the public "Find a Broker" directory. — [NCBFAA directory](https://www.ncbfaa.org/search-our-membership/find-a-broker-search)
10. **Los Angeles Customs Brokers & Freight Forwarders Association** (NCBFAA Area 9). — [NCBFAA Affiliate Presidents Network](https://www.ncbfaa.org/about-ncbfaa/affiliate-presidents-network) (search summary)
11. **Laredo, Brownsville, Mid Valley, Nogales, San Diego and West Texas/New Mexico broker associations** (Area 8, southern border). These are relevant to USMCA non-US-content splits. — [NCBFAA affiliate network](https://www.ncbfaa.org/about-ncbfaa/affiliate-presidents-network) (search summary)
12. **Northern Border Customs Brokers Association** (Area 1, Canada and USMCA). — same source.
13. **New Jersey Foreign Freight Forwarders & Brokers Association / NY-NJ FFF&BA** (annual dinner Jan 28, 2027). — [NCBFAA event listing](https://www.ncbfaa.org/event-details/2027/01/28/industry-events/new-york-new-jersey-foreign-freight-forwarders---brokers-association-annual-dinner)
14. **JFK Airport Customs Brokers & Forwarders Association and Baltimore Customs Brokers & Forwarders Association** (Areas 2–3). — [NCBFAA affiliate network](https://www.ncbfaa.org/about-ncbfaa/affiliate-presidents-network) (search summary)
15. **Houston, North Texas and Mid-South broker associations** (listed; area numbers unconfirmed). — same source.
16. **AAEI Fall 2026 Virtual Conference attendees** (Oct 22, 2026; importer trade-compliance managers). — [NCBFAA calendar listing](https://www.ncbfaa.org/event-details/2026/10/22/industry-events/aaei-fall-2026-virtual-conference--the-new-trade-frontier--technology--governance--and-global-risk)
17. **NCBFAA 2027 Annual Conference** (Apr 11–14, 2027) exhibitors and attendees. — [NCBFAA](https://www.ncbfaa.org/event-details/2027/04/11/ncbfaa-conferences/2027-ncbfaa-annual-conference)
18. **ACI's 2nd Annual Forum on International Trade Investigations, Enforcement & Litigation** (Feb 2–3, 2027). Trade lawyers there are a referral channel. — [NCBFAA calendar listing](https://www.ncbfaa.org/event-details/2027/02/02/industry-events/aci's-2nd-annual-forum-on-international-trade-investigations--enforcement---litigation)
19. **EEPC India member exporters of iron and steel products and derivatives** (about $5B a year of US-bound steel, aluminium and derivatives). — [Tribune/ANI, Jun 2, 2025](https://www.tribuneindia.com/news/business/trumps-50-tariff-on-steel-aluminium-could-hurt-indias-engineering-goods-exports-eepc-india/amp). The membership directory was not accessed.
20. **Audit and advisory partners that need supplier data but do not collect it**: MyCustomsInfo/CustomsPlus (audits, "never" files) and GingerControl (explicitly no supplier data). — [MyCustomsInfo](https://mycustomsinfo.com/section-232-compliance); [GingerControl](https://gingercontrol.com/blog/section-232-derivative-inclusion-list-exposure-monitoring)

Targets for B (weak):
- Class members ("tens of thousands," mostly small IORs). No public list exists. Class counsel (Barnes Richardson & Colburn; Lieff Cabraser) asked for "mechanisms for small importers … to seek refunds." — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)

### Inferences
- **[I]** The Indian-cluster targets (Ludhiana fasteners; Pune, Chennai and Rajkot castings and forgings) come from prior notes and founder context, not verified evidence. Treat them as hypotheses to test, not as validated leads.
- **[I]** Targets 1, 2, 5 and 8 are the highest-signal because each has a dated, documented trigger (a hard reject, a proposed inclusion, a supplier liability clause, or an FTZ filing naming 232 parts).

### Gaps
- I did not open the regulations.gov docket, NCBFAA member listings, EEPC member lists or trade-show exhibitor lists, so **no individual company names** are verified beyond GE Vernova and Intel as buyers that impose requirements.

## 9. What is the narrowest MVP a solo non-engineer could build in 2–8 weeks with AI coding tools, and what is a 14-day experiment with concrete kill criteria?

### Takeaway
For A, the narrowest credible MVP is **concierge first, then tooling**: an exporter-side or importer-side "232 SAC ledger" built on forms, a sheet and LLM extraction of mill certificates. It outputs (a) the buyer's required invoice lines and forms and (b) an audit binder. To avoid the Part 111 question, it should not prepare entry data for third parties. For B, no MVP is recommended. If it is tested at all, it should be a 7-day landing-page test framed as education plus self-filing.

### Cited Findings
- **[F]** The data elements to capture are those in GE Vernova's mandate: steel melt & pour and steel weight; aluminum and copper smelt, second smelt, cast and weight; zero-SAC declarations; FIFO documentation for multi-source metal. — [GE Vernova](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf). Also UPS form fields (part number, melt & pour, cast and smelt countries, weight). — [UPS form](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf)
- **[F]** The thresholds to compute are the 15% aggregate-weight test (non-chapter 72–76 goods) and the 85%-by-weight US-metal test. — [Annex IV](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf); [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states)
- **[F]** The price benchmarks are Millproof at $299/month (250 parts) and audits at $8K–$50K per cycle. — [Millproof](https://www.millproof.com/); [MyCustomsInfo](https://mycustomsinfo.com/section-232-compliance)
- **[F]** The legal boundary: preparing "documents … intended to be filed with CBP … whether or not signed or filed by the preparer" counts as customs business. — [19 CFR 111.1](https://www.law.cornell.edu/cfr/text/19/111.1)

### Inferences
**MVP for A (all [I]; 2–8 weeks, under $100/month in tools)**
- **Weeks 0–2 (concierge, no code):**
  - A Google Sheet "SAC ledger" with one row per part, holding HTS, metal weights, origin countries, source document link, valid-until date and buyer format.
  - A Tally or Google Form per supplier.
  - Mill certificate and BOM extraction run by hand through Claude: heat number, mill, melt country, chemistry, weights.
  - A generated PDF "232 declaration pack" per buyer format: GE Vernova invoice lines, UPS form, Intel-style affidavit.
- **Weeks 3–8 (light tooling built with Claude Code):**
  - Next.js + Supabase, or Airtable + Softr.
  - Magic-link supplier upload, LLM extraction with source-document pinning, staleness alerts when a supplier changes mills, and multi-buyer output templates.
  - A catalogue re-check against Annex lists, and an audit binder export.
- **Positioning to avoid head-on with Millproof:** sell to **exporters or suppliers** ("answer every US buyer's 232 request from one record"), or to **small brokers as a white-label intake portal**. Do *not* generate ACE entry-line data for third parties unless a licensed broker is in the loop and US customs counsel has confirmed the model.

**14-day experiment for A**
- **Days 1–2:**
  - Publish a one-page site and a free "232 data-gap check" spreadsheet.
  - Build a list of 60 contacts: 20 US importers or compliance managers in targets 1–4 and 7; 20 small brokers from NCBFAA and regional association directories; 20 Indian exporters in fasteners, castings, forgings and wire/cable.
- **Days 3–10:**
  - Send 60 personalized messages (LinkedIn and email).
  - Aim for 10 discovery calls. On each call ask for the most recent 232 data request they sent or received, the part count, hours per month, any held, rejected or CF-28/29 entry, who bears the cost (for example a chargeback clause), and what tool they use now.
- **Days 11–14:** offer a paid concierge pilot. Price it at $300–$500 for the first 100 parts for US importers or brokers, or about ₹25,000 for an exporter. Deliver one buyer-format pack within 72 hours.
- **Kill criteria. Stop if any of these hold:**
  - Fewer than 5 calls from 60 contacts.
  - Fewer than 3 of 10 calls describe a *current, unresolved* supplier-data problem costing at least 5 hours a week or at least one held or rejected entry or CF-28/29 in the last 90 days.
  - Zero paid pilots or signed commitments at $300 or more.
  - At least half say the broker form or invoice annotation "handles it."
  - Every interested prospect already uses Millproof, Sourcemap, Assent or Z2Data.
- **Advance signal:** at least 2 paid pilots, plus at least 1 broker or exporter willing to introduce 3 or more peers.

**B (only if the founder insists; 7 days)**
- Build a landing page titled "Small importer? Check if your IEEPA refund is stuck." Offer a free checklist for ACE portal setup, ACH refund enrollment and a broker CAPE request.
- **Kill if:** fewer than 10 sign-ups from 300 targeted visitors; fewer than 3 with at least $25K stuck; or any prospect needs third-party preparation (licensing problem); or class or appeal developments make reliquidation automatic.

### Gaps
- I could not verify whether supplier-side SaaS for 232 has any paying users anywhere. No vendor targets this side publicly.
- Exact ACE export formats such as ES-003 were not checked this session.

## 10. Verdict: should each candidate advance to the top-five shortlist?

### Takeaway
- **(A) Section 232 supplier-declaration hub: ADVANCE WITH CONDITIONS, Medium-Low confidence.** The obligation is real, dated, enforced and expanding. It has primary-source evidence: hard rejects from Sep 14, 2026; supplier-liability clauses; FCA cases. But the "overlooked" premise is false at the importer end, where Millproof, Sourcemap, Assent, Z2Data and free broker forms already compete. It advances only if repositioned to the **supplier/exporter side or small-broker white-label** and it passes the 14-day kill test.
- **(B) Long-tail IEEPA refund and protest tracker: REJECT.** About 76% of the ~$166B is already refunded. The ~$30B residual is the target of a court remedy designed to be automatic. CAPE filing is limited to the IOR or broker, and third-party preparation looks like licensed customs business. Fees are advertised at 1.5%. The Section 122 follow-on depends on an appeal the government is favoured to win.

### Cited Findings
- **A, for:**
  - Copper hard reject from Sep 14, 2026 — [CSMS #69711865](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/427b7f9)
  - 15%-weight and 85%-US-metal tests — [Annex IV](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf); [Proclamation 11032](https://www.federalregister.gov/documents/2026/06/04/2026-11314/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states)
  - Supplier liability — [GE Vernova, Jul 22, 2026](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)
  - Expansion — [FR 2026-15961](https://www.federalregister.gov/documents/2026/08/06/2026-15961/request-for-public-comments-on-the-proposed-implementation-of-duties-on-additional-aluminum-steel)
  - 232 exempts goods from the new 301 tariff — [FR 2026-15181](https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies)
  - Price points exist — [Millproof](https://www.millproof.com/); [MyCustomsInfo](https://mycustomsinfo.com/section-232-compliance)
- **A, against:**
  - Near-identical competitor — [Millproof](https://www.millproof.com/)
  - Enterprise coverage — [Sourcemap](https://sourcemap.com/solutions/tariff-solution); [Z2Data](https://www.z2data.com/insights/why-you-need-supply-chain-visibility-for-section-232/); [Assent](https://www.assent.com/blog/prepare-for-section-232-tariffs/)
  - Free forms — [UPS](https://blog.navlungo.com/wp-content/uploads/2026/04/13-Section-232-Copper-Steel-and-Aluminum-Form-updated-10-14-25.pdf)
  - "Any format" invoice data — [GE Vernova](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)
  - No Indian-demand evidence — [EEPC chair, Sep 2, 2026](https://news.webindia123.com/news/Articles/Business/20260902/4493853.html)
- **B, against:**
  - $126B refunded; ~$30B residual; class remedy automated; "overwhelmingly small importers" — [CIT Slip Op. 26-123](https://www.cit.uscourts.gov/sites/cit/files/26-123.pdf)
  - IOR or broker-only filing — [CBP](https://www.cbp.gov/trade/programs-administration/trade-remedies/ieepa-duty-refunds)
  - Customs-business definition — [19 CFR 111.1](https://www.law.cornell.edu/cfr/text/19/111.1)
  - 1.5% fees — [TRG](https://tariffrecoverygroup.com/)
  - Section 122 stay — [Steptoe/Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1810106/appellate-court-raises-more-uncertainty-in-section-122-tariff-litigation)

### Inferences
- **[I] Conditions for A to stay on the shortlist:**
  1. Pass the 14-day kill criteria (at least 2 paid pilots).
  2. Lead with the supplier/exporter or broker-white-label wedge, not importer-side SaaS.
  3. Get a short written opinion from US customs counsel on the Part 111 boundary before outputting anything resembling entry data.
  4. Re-check by Q1 2027 whether Millproof, Altana, Descartes or Flexport have launched a supplier-side 232 feature.
- **[I]** B's only residual value is as **content-led lead generation** for A, since the importers and brokers are the same people. It should not be a company.

### Gaps
- No direct customer-interview evidence for either candidate. Demand intensity and willingness to pay are unverified beyond competitor price points.
- No count of US importers affected by 232, and no figure for 232 duty collections.
- Indian trade press and association sources could not be accessed.
