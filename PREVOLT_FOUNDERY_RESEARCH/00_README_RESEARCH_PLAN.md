# PREVOLT — Research Plan, Source-Quality Criteria and Evidence Labels

Prepared: 1 October 2026. Purpose: commercial diligence for a possible relaunch of PREVOLT. This is research, not a pitch deck.

## Starting position (input audit)
- No project files, decks, photographs, quotations or survey records were available to this research. The repository was empty when work began.
- Everything about PREVOLT's history comes from the founder's written brief (1 Oct 2026) and is labelled **FOUNDER-REPORTED**.
- `thefoundery.in` is blocked by this environment's network proxy, so Foundery programme details are taken only from the founder's brief and secondary coverage, and are labelled as such.

## Evidence labels used in every file
| Label | Meaning |
|---|---|
| **VERIFIED** | Read at the cited primary or authoritative URL during this research (Oct 2026). |
| **VERIFIED-SECONDARY** | Read at a cited secondary source (news or trade article) and not traced to a primary document. |
| **FOUNDER-REPORTED** | Stated by Saket Gairola. No supporting document has been seen. |
| **ESTIMATE** | A third-party estimate, such as a market-research forecast, whose methodology is not fully disclosed. |
| **ASSUMED** | An assumption made by this analysis for modelling. It must be replaced by a quotation or a test. |
| **UNKNOWN** | No reliable evidence. States what evidence would resolve it. |

## Source-quality hierarchy (highest first)
1. Indian statute or regulator text (FSSAI regulations, gazette notifications, CBIC/GST notifications).
2. Audited company filings (annual reports, investor presentations, stock-exchange disclosures).
3. Peer-reviewed research (with its date stated; older papers are used only for stable scientific principles).
4. Dated retailer listings that I observed directly (price and date recorded).
5. Market-research firms with a disclosed scope (these are **ESTIMATES**; their definitions are compared, not averaged).
6. Reputable business press (context only; never the sole basis for a major number unless marked VERIFIED-SECONDARY).

Excluded: search-engine snippets, AI summaries, uncited blogs and press-release mills, used as evidence.

## Research order (highest-impact uncertainties first)
1. Market demand and definition: energy drinks only, separated from adjacent categories.
2. Competitive pricing at SKU level (price per 100 ml).
3. Regulatory gate: FSSAI caffeinated-beverage standard, permitted ingredients, sweeteners, labelling, GST.
4. Feasibility of the natural-fruit formulations (blueberry, lemon, coconut water).
5. Manufacturing economics at 2k/5k/10k units.
6. Distribution, consumer validation, ReSeal, first 30 days, and the Foundery synthesis.

## File index
See `EXECUTIVE_FINDINGS.md` for the synthesis, and `SOURCE_REGISTER.csv` for every sourced number.

## Status log
- 2026-10-01 (a): Input audit: no files were provided. Page fetches were initially blocked by the environment's network policy, and research paused.
- 2026-10-01 (b): After network access was widened, primary sources were downloaded directly (curl / headless Chromium / NCBI and Europe PMC APIs) and read in full or in relevant part. All deliverables were produced.

## Quality control (1 Oct 2026)

### Access and evidence limits
- **Read directly:** FSSAI regulatory compendia (Ch. 2.10, Ch. 2.3, Appendix A, Advertising & Claims, Nutraceuticals 2021), FSSAI steviol advisory (2023), GST Notification 01/2026 (third-party-hosted copy), Varun Beverages Annual Report CY2025, Q3 CY2025 presentation and Q4 CY2024 call transcript (BSE), Euromonitor free articles, market-research landing pages, retailer listings (1mg, Hyperpure, Flipkart, Amazon), Foundery FAQ, PubMed abstracts, and two full papers (Europe PMC).
- **Blocked or inaccessible:** BigBasket, JioMart, Blinkit, Zepto and Swiggy Instamart (bot protection); redbull.com and monsterenergy pages (403); Reuters (blocked to the search tool); Packaging Digest (bot challenge); CBIC's own server (connection reset; a hosted copy of the notification was used).
- **Paywalled, not purchased:** Euromonitor data tables, The Ken, all market-research reports (only landing-page figures used).
- **Not located:** the FSSAI orders of 30 Jun / 1 Jul / 3 Jul / 17 Jul 2026 on the "energy drink" descriptor (known only through press coverage); the outcome of the 29 Sept 2026 Delhi High Court hearing.
- **No primary research was conducted:** no interviews, tastings or manufacturer contacts. All such items are plans.

### Link audit
All 61 unique URLs in `SOURCE_REGISTER.csv` were re-requested on 1 Oct 2026. 59 returned HTTP 200/203 (PubMed links were spot-checked after replacing DOI links). Amazon search (S35) and Google Patents (S63) rate-limit automated checks (503); both were read in a rendered browser session the same day. Peer-reviewed items link to PubMed because publisher DOI pages return 403 to automated clients; DOIs are recorded in the methodology column.

### Definitions and dates checked
- Market figures are energy-drink-only. Sports drinks, electrolyte powders and soft drinks were excluded, including Amazon search noise.
- Retail-value estimates (including GST and trade margins) are kept separate from company revenue (Red Bull India, net of GST).
- Price observations are dated 1 Oct 2026. Older prices (Charged at ₹20, Euromonitor 2023) are labelled with their year.
- USD and INR figures are not converted (no sourced exchange rate is used).

### Contradictions found (and how they are handled)
| # | Contradiction | Handling |
|---|---|---|
| 1 | Market-size estimates range from USD 0.75 bn to USD 4.93 bn (2025) | Shown side by side; outlier excluded; planning range USD 0.75–1.5 bn |
| 2 | Euromonitor-via-Storyboard18 says 33.5 million litres (2022), but VBL disclosures imply far more | Storyboard18 figure excluded as unreliable |
| 3 | Euromonitor 0.4 L per capita (2023, off-trade) vs Monster's "5 servings per capita" (2026) | Both shown; different years, channels and units |
| 4 | Mordor CAGR 2.25% vs 6–13% elsewhere and recent double-digit volume growth | Mordor CAGR treated as an outlier |
| 5 | DH Brands website says "No MOQ policy" vs founder-reported 2,000-unit MOQ (2025) | Flagged; ask in writing |
| 6 | Acesulfame-K 300 ppm (carbonated-water standard) vs 600 mg/kg (Appendix A, category 14.1.4); aspartame 700 vs 600 | Flagged for the regulatory consultant |
| 7 | Original "performance energy drink" positioning vs FSSAI's 2026 order | Positioning changed to "caffeinated beverage, taste-led" |
| 8 | Historical ₹22 cost and ₹70 price vs the model: ₹70 MRP nets ≈ ₹36.8 at base margins | Historical sheet isolated; ₹70 shown to be very unlikely to work |
| 9 | Original functional ingredients vs FSSAI's permitted list and the efficacy literature | Removed from the launch formula |
| 10 | "Blueberry as a differentiator" vs Sting Gold Blue Berry at ₹20 | Reframed as a hypothesis |

### Mandatory statements
- **The historical Dark Horse Brands quote (MOQ ~2,000; ~₹22/unit at ~10,000 units) was for an ARTIFICIAL-POWDER formulation in 2025. It is NOT applicable to any natural-fruit (blueberry, lemon or coconut) formulation, none of which has been quoted.**
- **No conceptual can image, AI artwork or ReSeal animation is evidence of a manufactured product.** None was available to this research.
- **The original consumer-insight slide was not available and has not been reconstructed.**

### Workbook verification
LibreOffice could not open files in this container, so `UNIT_ECONOMICS.xlsx` was evaluated with the Python `formulas` engine (Excel-compatible). All formula cells evaluated without errors, and the workbook is set to recalculate fully when opened. Key base outputs:
- MRP ₹99 → net realisation ₹52.04 per can at base margins
- Contribution per can sold, 5k batch: powder −₹7.7, lemon −₹11.6, blueberry −₹29.2, coconut −₹33.8
- First-batch cash need: ₹3.2–9.9 lakh per flavour
- Three flavours × 2k: ≈ ₹13.6 lakh
