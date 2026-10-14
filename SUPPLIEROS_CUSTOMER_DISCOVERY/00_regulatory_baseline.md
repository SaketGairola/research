# Regulatory baseline as of 14 Oct 2026, and what it means for SupplierOS

This is research context, not legal advice. Secondary sources disagree on some rates and dates. Confirm anything you quote to a prospect against the CBP CSMS messages and the Federal Register.

## What changed in 2026

| Date | Change | Why it matters for SupplierOS | Source |
|---|---|---|---|
| 6 Apr 2026 | Proclamation 11021: S232 duty is now charged on the **full customs value**, not the metal-content value. Tiers: 50% for (almost) all-metal articles and Annex I-A goods (castings, forgings), 25% for derivatives substantially of metal. Goods outside ch. 72/73/74/76 are out of scope when the applicable metal is **<15% of weight**. | **Cuts against the thesis:** importers no longer need the *value* of the metal content. **Keeps the need for** metal **weight** per part (the 15% test), melt/smelt origin, and the US-content share. | [CBP CSMS 68253075](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/4117593), [Federal Register 2026-06960](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states), [GHY](https://www.ghy.com/trade-compliance/us-adjusts-section-232-tariffs-on-aluminum-steel-and-copper-full-customs-value-now-applies/) |
| 8 Jun 2026 | Proclamation 11032: the threshold for treating a good as made of US metal drops from 95% to **85%** by weight (10% rate). A 15% temporary tier applies to ag equipment, some HVAC and some industrial equipment through 31 Dec 2027. A USMCA content regime was added. | Each tier depends on documented metal weight and origin per part. | [Plante Moran](https://www.plantemoran.com/explore-our-thinking/insight/2026/06/section-232-update), [Diaz Trade Law](https://diaztradelaw.com/new-section-232-action-what-the-june-2026-aluminum-steel-copper-proclamation-means-for-your-imports/) |
| 30 Jul → 14 Sep 2026 | **Copper:** the primary country of smelt and the country of cast are now required for HTS 8544.42.10/.20/.90 and 8544.49.10 (insulated copper wire and cable). Since 14 Sep, ACE **fatally rejects** entries that lack them. "OTH" is allowed as a placeholder. | A hard, dated trigger. Cable exporters (Segment A) and their importers are the most time-sensitive targets. | [V. Alexander](https://www.valexander.com/?p=3878), [Strix](https://strixsmart.com/resources/blog/ace-copper-smelt-cast-fatal-error-september-2026), [Livingston](https://www.livingstonintl.com/cbp-to-implement-section-232-copper-smelt-and-cast-reporting-requirements-on-july-30-2026/) |
| Ongoing since Nov 2024 | **Steel** melt-and-pour and **aluminium** smelt-and-cast country must be reported on the entry summary. An unknown aluminium origin can trigger the 200% rate. | This is the recurring, per-shipment data need. | [FedEx alert](https://www.fedex.com/content/dam/fedex/us-united-states/services/Section_232_Steel_Melt_Pour_Reporting_Requirements.pdf), [Vigilant GTS](https://vigilantgts.com/prove-origin-prevent-costly-tariffs-hb/) |
| 1 Oct 2026 | **EU** melt-and-pour declaration on steel imports covered by the EU safeguard (Reg. (EU) 2026/1963). The mill test certificate is preferred. From 1 Oct 2027, other documents count only as support for an MTC. | **Supports the thesis:** the same melt-and-pour record can now be reused for EU and US buyers. | [Expeditors](https://info.expeditors.com/newsflash/eu-introduces-melt-and-pour-traceability-requirement-for-steel-imports) |
| 1 Jan 2026 | **EU CBAM** definitive period. EU importers want installation-level embedded-emissions data from Indian steel and aluminium exporters, and default values cost more. | The adjacent regime where Indian MSMEs have **publicly described** data pain (see leads A01–A03). | [Down To Earth](https://www.downtoearth.org.in/economy/eus-carbon-rules-enter-implementation-phase-putting-indian-msmes-under-pressure), [ESGen](https://esgen.co.uk/resources/blog/eu-cbam-indian-steel-aluminium-exporters/) |
| Late Jul 2026 | A USTR Section 301 "forced labor" duty adds about 10% on many Indian goods. **Goods covered by S232 are exempt** from it. | Classifying a good correctly as in or out of S232 now carries a second financial consequence. | [China Daily, 8 Aug 2026](https://www.chinadaily.com.cn/a/202608/08/WS6a766f6da310986e2b469aaf.html) |

## Primary evidence that buyers push this work onto suppliers

**GE Vernova supplier memo, dated 22 Jul 2026** ([PDF](https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf)):
- It requires *every* commercial invoice for in-scope parts to show:
  - **steel:** country of melt and pour, and steel weight;
  - **aluminium:** country of smelt, second smelt and cast, and aluminium weight;
  - **copper:** the same fields, with copper weight.
- These requirements become part of the purchase-order terms. Suppliers **reimburse** "any duties, penalties, fines, storage fees, redelivery costs" caused by missing or inaccurate data.
- Suppliers must keep supporting documentation available for audit. Multi-sourced material has to be resolved to one country, with a FIFO-type method documented.
- Parts in scope with zero steel, aluminium or copper must still report 0.
- **Iron content (iron castings) is exempt.** This matters for Segment A foundries.

This is the clearest public example of the supplier-side burden SupplierOS targets: per part, per invoice, with liability. Wind suppliers (hubs, pitch bearings, main shafts, generators) are named as in scope.

**DHL Express "Section 232 content reporting" form, Jan 2026** ([PDF, reposted by a shipper](https://doorro.com/storage/files/board/notice/2026-01/232_Content_Reporting_January%202026_260126035312.pdf)): shippers must certify, per part, the country of cast/smelt/melt/pour, the metal content value and the weight in kg. It predates the 6 April full-value change, but it shows that carriers and brokers each issue their own forms. That is the "same data, different format" problem.

## Competitors and adjacent vendors (all importer-side unless noted)

| Vendor | What it does | Implication |
|---|---|---|
| [Millproof](https://www.millproof.com/) | Importer-side per-part S232 ledger. Sends suppliers a form, extracts mill certs, runs the 15% calculation, produces a broker data pack and audit binder. **$299/month, 3-month prepaid pilot, first 250 part numbers.** | Closest competitor and a public price anchor. SupplierOS's difference has to be **supplier-held and reusable across buyers**. |
| [SmartCert](https://www.smartcert.tech/the-new-section-232-rules-are-exactly-why-smartcert-exists/) (Aramid Technologies) | Quality-certificate management with extraction and traceability, positioned for S232. | Buyer-side certificate platform. |
| [Vigilant GTS](https://vigilantgts.com/prove-origin-prevent-costly-tariffs-hb/) | A service: mill-cert collection and validation, plus a product↔metal↔origin database. | Possible partner for white-label (lead C01). |
| [Strix](https://strixsmart.com/) | Broker with $30/entry self-filing software. | Possible partner (lead C02). |
| Assent, Z2Data, Sourcemap, GingerControl, Carra Globe, MyCustomsInfo ($8k–50k audits) | Enterprise supply-chain compliance, classification and audit tools. | Validate that importers pay. None found that is supplier-held. |
| Certivo, SafetyChain, ESGen | Material-declaration (IPC-1752), EPR and CBAM data tools. | Adjacent workflows (Segment E). |
