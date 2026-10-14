# Output D: market findings

## 1. Which segment looks most promising

**For first paying customers: Segment B intermediaries plus Segment A Indian SMEs that ship to both the US and the EU.**

- **Sourcing intermediaries and contract manufacturers acting as importer of record** (Redstone, Chapman Smith, IC&T): they already do the per-part mill-cert and BOM work across many Indian and Asian factories. They feel the cost directly and buy software. They can also bring their factories onto SupplierOS.
- **Indian exporters selling steel to both the US and the EU** (Steelcast, Corona Steel, Chin Well in Vietnam): from 1 Oct 2026 the same melt-and-pour fact is required by the EU (Reg. 2026/1963) and by US entry reporting. "Maintain once, reuse for several buyers and markets" is now a concrete pitch, not just a vision.
- **Copper cable exporters (8544):** the most urgent trigger. Smelt/cast entries have been fatally rejected since 14 Sep 2026. But the qualifying exporters found so far are larger companies (RR Kabel) or have a small US share (Dynamic Cables).

## 2. Which companies show direct evidence of pain

**Verified, from the company's own statements:**

| Company | What was said or done | Regime |
|---|---|---|
| Corona Steel (A01), Aditya Garodia | Struggling to collect certifications for inputs from secondary mills; months with consultants; estimates Rs 5–10M cost. | EU CBAM |
| Binayak Hi-Tech (A02), Atul Jhunjhunwala | Data depends on suppliers; 8–9 months chasing electricity-supplier data; confidentiality concerns. | EU CBAM |
| Chandan Steel (A03), Chaitanya Chandan | CBAM paperwork; smaller EU buyers stopped ordering. | EU CBAM |
| Express Fasteners (B01) | Suing CBP over steel-content valuation. | US S232 |
| Mondelez (E01), Brie Seferian | "Assembling packaging information from disconnected systems." | US EPR |
| Vigilant GTS, Strix, Mallory Alexander (C01/C02/C08) | Market-level descriptions: suppliers reluctant to share upstream data, "inconsistent supplier data," the need for a supplier-data process. | US S232 |

**Verified buyer-side demand:** the GE Vernova supplier memo (22 Jul 2026) requires metal weight and melt/smelt origin per part on every invoice and makes suppliers reimburse every cost of missing data. That is the demand SupplierOS's users would be answering.

**Gap:** I found **no Indian exporter publicly describing Section 232 declaration pain specifically.** The direct pain quotes from Indian MSMEs are about CBAM. The S232 pain is described by importers, brokers and service providers. Your interviews need to confirm or reject this point.

## 3. Which segments are most likely to pay

1. **Importers and sourcing intermediaries (B):** they carry the legal recordkeeping burden and the duty risk, including the 200% aluminium default and the 15% and 85% tiers. There's already a public market price: Millproof charges $299/month for a 3-month pilot covering 250 part numbers, and audits cost $8k–50k.
2. **Mid-size Indian exporters (A, ₹100–1,000 crore revenue):** they can pay modest SaaS fees when a contract (like GE Vernova's) shifts liability to them, or when a major buyer requires it. Small MSMEs are price-sensitive and usually lean on their CHA or a consultant.
3. **Brokers (C):** they are more likely **partners or channels** than buyers. They earn per entry and usually pass document collection back to the importer. White-label only makes sense with brokers who already sell software (Strix).

## 4. Best initial buyer: manufacturer, importer, or broker?

**Recommendation: sell to the importer or sourcing intermediary first, and design the product so the manufacturer owns the record.**

- The importer has the legal obligation and the budget. The manufacturer has the data and the repeated work.
- A supplier-held model wins only if suppliers accept it. Lead A02's confidentiality comment is the strongest argument for it: suppliers don't want to hand over mill, supplier and cost details.
- Practical wedge: an importer or intermediary with 5–20 Indian suppliers pays for the pilot. Each supplier gets a free SupplierOS workspace to maintain its records and share declarations. Then test whether suppliers will pay to reuse those records with *other* buyers. That test is the real proof of the network thesis.

## 5. Are adjacent material-compliance use cases more promising than Section 232?

**Not yet. Use them as reuse arguments, not as a pivot.**

| Workflow | Who holds the data | Recurrence | Why it differs from S232 | Fit with the MVP as built |
|---|---|---|---|---|
| **EU melt-and-pour (from 1 Oct 2026)** | Mill → exporter | Per shipment | Nearly the same data field as US S232; the mill test certificate is mandatory as evidence from Oct 2027 | **High: same record** |
| **EU CBAM** | Exporter's plant energy and precursor data | Quarterly/annual; verifier needed | Emissions calculation, accredited verification, installation boundary. Not a document extraction problem. | Low for the MVP; high pain |
| **Packaging EPR (US states, India)** | Packaging converter → brand | Annual reporting, frequent spec changes | Material composition and weight by packaging component, not metal origin; brands are the "producer" | Medium: same "one record, many brand formats" pattern, different schema |
| **IPC-1752 / REACH / RoHS full material declarations** | Component maker → OEM | Per part, recurring | Substance-level composition; established standards and tools already exist (Assent, Certivo) | Medium–low; crowded |
| **USMCA / certificate of origin** | Producer | Per part, annual blanket certificates | Tariff-shift and regional value rules, not metal melt | Medium |

The best adjacent bet is **EU melt-and-pour**, because it reuses the identical record. CBAM has more verified pain, but it would need a different product: emissions accounting and verification.

## 6. Strongest evidence against the thesis

1. **The full-value switch (6 Apr 2026) removed the "metal content value" calculation** that made per-part declarations complex. For goods in the 50% and Annex I-A tiers (castings, forgings, flanges), the importer now needs mainly the **melt-and-pour country**, which is already on the mill certificate. That's a thin data need.
2. **Iron castings appear to be exempt** in at least one large buyer's guidance (GE Vernova: "Iron content (iron castings, etc.) is exempt"). A big share of Indian foundry exports (Nelcast, Rajkot investment casters, municipal castings) may fall outside S232 data requirements, or carry only partial requirements. Check by HTS code.
3. **"OTH" is an accepted placeholder** for unknown derivative-steel and copper origins, so some importers may just file OTH and accept the outcome rather than pay for traceability.
4. **Buyers accept data in "any format" on the invoice** (GE Vernova). That weakens the "different buyers, different formats" pain for at least some buyers.
5. **No Indian exporter was found publicly describing S232 declaration pain.** The verified Indian pain is about CBAM.
6. **Competition is moving fast on the importer side:** Millproof, SmartCert, Assent, Z2Data, Vigilant. If importers adopt those tools, suppliers just fill in the importers' forms, and a supplier-held layer has to prove it saves the supplier time across several of those portals.
7. **Policy volatility:** six or more rule changes in 2026, and the June tiers expire on 31 Dec 2027. Prospects may wait instead of buying.
8. **Tariff-driven demand loss:** several exporters cut their US exposure (Sundram moved volume away from the US; Happy Forgings' US business fell 35–40%). Fewer US shipments means less recurring workflow.

## 7. What interviews still need to answer

1. Have Indian exporters actually received **per-part metal weight and origin requests** from US buyers since April 2026, or only mill certificates? How many requests per month?
2. Do buyers impose **contractual liability** (like GE Vernova's)? How common is that among mid-size US OEMs?
3. Who does the work today, and how many hours does it take? Is it the export documentation clerk, the QA manager or the CHA?
4. Will exporters **share records from their own workspace**, or do buyers insist on their own portals?
5. Of the importers filing "OTH" today, what share would pay to replace it with real origin data, and what is the duty or penalty exposure that drives that?
6. Does the **EU + US reuse** happen in practice? Are the same people and documents used for both?
7. Which **HTS codes** in each prospect's catalogue are really in scope after the iron exemption and the 15% rule?
8. What price would a supplier pay **without** a buyer mandate, compared with when a buyer requires it?

## Can you land a first paying customer around launch?

**Plausibly yes, if you aim at an intermediary or importer with a pilot, not a pure-play Indian SME.** Within 10 days:
- Run 10–15 interviews from the top-10 list.
- Expect most yeses from brokers and intermediaries, and fewer from Indian MSMEs (slow email response, WhatsApp-first culture; ask for WhatsApp in the follow-up once there's a connection).
- Offer one paid pilot that processes a real document set, priced under the Millproof anchor.
- Treat every confirmed exporter interview as evidence for or against the supplier-held thesis. Don't treat it as a sale.

## Coverage and honesty notes

- **71 leads**, short of the 100–150 target: A 31, B 13, C 18, D 5, E 4. I stopped rather than pad the list with directory listings that showed no US exposure or relevant contact.
- **10 are P1, 34 P2, 27 P3.** 23 have named individuals sourced from press, filings or event pages. **No LinkedIn URL is verified**, because LinkedIn couldn't be read from this environment. **Only public company emails are listed; none were guessed.**
- Segment D (Mexico, Turkey, Thailand) is thin. Public sources rarely name individual exporters with US-specific metal documentation. The fastest way to fill it is to ask importers (Segment B) who their suppliers are.
- Several facts come from secondary sources (Panjiva or ImportGenius shipment counts, analyst notes, directories), and some leadership details are dated (marked "re-verify" in the CSV).
