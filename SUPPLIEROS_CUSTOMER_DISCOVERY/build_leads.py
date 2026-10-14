"""Builds leads_master.csv and leads_master.xlsx from the verified lead records below.

Scoring rubric (max points): pain 25, trade 20, access 15, pay 15, freq 10, contact 10, mvp 5.
Priority: P1 >= 67, P2 50-66, P3 < 50, unless `prio_override` is set (reason given in `score_note`).
"NV" = Not verified. No LinkedIn URL was verified in this session (LinkedIn is not readable
from the research environment), so every LinkedIn field says so instead of guessing a URL.
"""
import csv
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

NV = "Not verified"
LI = "Not verified - search LinkedIn manually for name + company"

FIELDS = [
    "lead_id", "company", "country_city", "segment", "website", "products",
    "us_exposure_evidence", "us_exposure_confidence", "contact_name", "title",
    "linkedin", "email_or_official_channel", "phone_published", "evidence_why_relevant",
    "source_links", "pain_classification",
    "s_pain25", "s_trade20", "s_access15", "s_pay15", "s_freq10", "s_contact10", "s_mvp5",
    "lead_score", "priority", "score_note", "outreach_angle",
]

L = []


def add(**k):
    k.setdefault("linkedin", LI)
    k.setdefault("prio_override", None)
    L.append(k)


# ---------------- Segment A: Indian exporters ----------------
add(lead_id="A01", company="Corona Steel Industry Pvt Ltd", country_city="India, Kolkata (West Bengal)", segment="A",
    website="NV (IndiaMART storefront: https://m.indiamart.com/coronasteelindustry)",
    products="Fasteners, pole-line hardware, scaffolding accessories, garage shelving (100+ steel products)",
    us_exposure_evidence="Fastener World (Aug 2025): US long a major market, 100+ steel products incl. fasteners; ~30% of orders cancelled after tariff hike. Panjiva: ~881 US shipments since 2007, top HS ch.72/73.",
    us_exposure_confidence="High",
    contact_name="Aditya Garodia", title="Director (Fastener World) / Managing Director (Down To Earth)",
    email_or_official_channel="No public email found; IndiaMART enquiry form", phone_published="+91 80460 48321 (IndiaMART listing number; confirm)",
    evidence_why_relevant="VERIFIED PAIN (adjacent regime): Garodia told Down To Earth the firm is struggling to obtain the data/certifications to establish product emissions for EU CBAM, especially for inputs from secondary mills; spent months with consultants; est. Rs 5-10M compliance cost. Same input-traceability problem as US melt-and-pour.",
    source_links="https://www.downtoearth.org.in/economy/eus-carbon-rules-enter-implementation-phase-putting-indian-msmes-under-pressure ; https://fastener-world.com/en/article/9224.html ; https://panjiva.com/Corona-Steel-Industries-Pvt-Ltd/1243436",
    pain_classification="Verified (CBAM input data); Strong inference (S232 melt-and-pour)",
    s=(18, 17, 12, 9, 8, 5, 5),
    score_note="Only lead where the owner publicly described an input-traceability documentation problem AND has heavy US steel-derivative exposure.",
    outreach_angle="You told Down To Earth that collecting certifications for inputs from secondary mills is the hardest part of CBAM. US buyers now ask for the same upstream fact (country of melt and pour) per part.")
add(lead_id="A02", company="Binayak Hi-Tech Engineering Ltd", country_city="India, Howrah (West Bengal)", segment="A",
    website=NV, products="Iron/steel articles (HS 73), machinery parts (HS 84), castings",
    us_exposure_evidence="Panjiva: ~1,390 US shipments since 2007; 2025 consignees include General Foundries Inc (NJ) and Eric'sons Dura Trench.",
    us_exposure_confidence="High",
    contact_name="Atul Jhunjhunwala", title="Managing Director (per Down To Earth)",
    email_or_official_channel="NV - no official site found; use Panjiva-listed address (117 Mirpara Road, Liluah, Howrah 711203)", phone_published=NV,
    evidence_why_relevant="VERIFIED PAIN (adjacent): MD said product-level emissions are hard because data depends on suppliers; asked its electricity supplier for data for 8-9 months without success; flagged confidentiality concerns in sharing supplier/production details with buyers. That confidentiality point is the case for supplier-held records.",
    source_links="https://www.downtoearth.org.in/economy/eus-carbon-rules-enter-implementation-phase-putting-indian-msmes-under-pressure ; https://panjiva.com/Binayak-Hi-Tech-Engineering-Ltd/2167928",
    pain_classification="Verified (CBAM supplier data + confidentiality); Strong inference (S232)",
    s=(18, 17, 12, 9, 8, 4, 5),
    score_note="Direct quote on supplier-dependent data plus confidentiality concern; recurring US castings shipments.",
    outreach_angle="You mentioned not wanting to share supplier and cost details just to answer a buyer's data request. I'm testing a model where the exporter keeps the records and shares only the declaration.")
add(lead_id="A03", company="Chandan Steel Ltd", country_city="India, Gujarat", segment="A", website=NV,
    products="Stainless steel products incl. flanges",
    us_exposure_evidence="Named respondent in US antidumping order on stainless steel flanges from India (A-533-877); India->US SS flange trade ~$60M (2023). Current US volume NV.",
    us_exposure_confidence="Medium",
    contact_name="Chaitanya Chandan", title="Director (per Down To Earth)", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="VERIFIED PAIN (adjacent): cites additional CBAM paperwork; smaller EU buyers stopped ordering. US side carries AD-review documentation history (Commerce applied adverse facts available in a 2021 preliminary review).",
    source_links="https://www.downtoearth.org.in/economy/eus-carbon-rules-enter-implementation-phase-putting-indian-msmes-under-pressure ; https://www.customsmobile.com/adcvd/8291305",
    pain_classification="Verified (CBAM paperwork); Industry fit (S232)",
    s=(14, 12, 12, 10, 7, 4, 3),
    score_note="Pain verified but on EU side; AD-order complexity is outside MVP scope.",
    outreach_angle="Your comment on CBAM's extra paperwork. Do US flange buyers now ask you for melt-and-pour per heat as well, and is that kept in the same place?")
add(lead_id="A04", company="Uniparts India Ltd", country_city="India, Noida / Ludhiana", segment="A", website=NV,
    products="3-point linkage, precision machined parts, hydraulic cylinder components for ag & construction OEMs",
    us_exposure_evidence="ICRA rating rationale: ~50% of consolidated revenue from US; most US-bound products fall under Section 232; renegotiated pricing and shifted some output to its US plant.",
    us_exposure_confidence="High",
    contact_name=NV, title="Target: Head of Exports / Trade Compliance (name NV)", email_or_official_channel="Company investor-relations / contact page (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: rating agency confirms most US products are in S232 scope; ag-equipment parts may qualify for the June 2026 15% tier, which makes per-part metal-weight records directly valuable.",
    source_links="https://www.icra.in/Rating/GetRationalReportFilePdf?id=137686",
    pain_classification="Strong inference",
    s=(12, 19, 5, 13, 9, 5, 3),
    score_note="Very high exposure but no named contact and likely ERP-centric; good later-stage account.",
    outreach_angle="ICRA notes most of your US-bound products are now under Section 232. How is per-part metal weight and melt-and-pour supplied to each OEM today?")
add(lead_id="A05", company="Dynamic Cables Ltd", country_city="India, Jaipur (Rajasthan)", segment="A", website=NV,
    products="Power & control cables, conductors (copper/aluminium); UL 854 service-entrance cable",
    us_exposure_evidence="UL 854 certification for US market (Dec 2025); dedicated US team; DDP pricing model for US/Australia; exports ~10% of revenue.",
    us_exposure_confidence="Medium-High",
    contact_name="Ashish Mangal", title="Managing Director (quoted in FY26 results commentary)", email_or_official_channel="Company investor-relations channel (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE + TIMING: CBP made copper primary-smelt and cast country mandatory for HTS 8544.42/8544.49.10 (insulated copper cable), ACE fatal-rejecting entries from 14 Sep 2026. Under DDP the exporter bears the clearance consequences.",
    source_links="https://www.businesstoday.in/amp/markets/stocks/story/dynamic-cables-shares-rise-today-two-factors-behind-the-rally-504430-2025-12-01 ; https://valueeducator.substack.com/p/connecting-india-one-line-at-a-time ; https://www.valexander.com/?p=3878 ; https://strixsmart.com/resources/blog/ace-copper-smelt-cast-fatal-error-september-2026",
    pain_classification="Strong inference",
    s=(13, 13, 12, 12, 8, 5, 5),
    score_note="Fresh, hard regulatory trigger (copper smelt/cast) and DDP model, but US share still small.",
    outreach_angle="Since 14 Sep, CBP rejects 8544 cable entries without copper smelt and cast country. With your DDP model for the US, I'd like to learn how you source that per shipment.")
add(lead_id="A06", company="Pradeep Metals Ltd", country_city="India, Navi Mumbai (Maharashtra)", segment="A", website=NV,
    products="Closed-die steel forgings & machined components (valves, oil & gas, petrochem)",
    us_exposure_evidence="ImportGenius: ~1,500 US shipments since 2006, mostly to valve makers; US subsidiary set up FY14 (CRISIL).",
    us_exposure_confidence="High",
    contact_name="Pradeep Goyal", title="Chairman & Managing Director (per CRISIL 2020 - re-verify)", email_or_official_channel="Company contact page (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: closed-die steel forgings sit in the 50% full-value annex where melt-and-pour reporting is mandatory; many SKUs across many valve OEMs means repeated per-buyer requests.",
    source_links="https://crisil.com/mnt/winshare/Ratings/RatingList/RatingDocs/Pradeep_Metals_Limited_April_09_2020_RR.html ; https://www.importgenius.com/suppliers/pradeep-metals-ltd ; https://www.cornellforge.com/section-232-tariffs-domestic-steel-forging/",
    pain_classification="Strong inference",
    s=(10, 18, 9, 11, 8, 6, 5),
    score_note="Ideal SME profile (many SKUs, many US valve buyers); contact info dated.",
    outreach_angle="With ~1,500 US shipments mostly to valve makers, do each OEM's Section 232 data requests differ? How do you answer them per forging today?")
add(lead_id="A07", company="Nelcast Ltd", country_city="India, Nellore/Chennai", segment="A", website=NV,
    products="Ductile & grey iron castings (CV, tractor, off-highway)",
    us_exposure_evidence="Q1 FY26 call: 80% of export revenue from US; FY26 exports picked up led by US.",
    us_exposure_confidence="High",
    contact_name="Deepak Reddy Ponnavolu", title="Managing Director & CEO", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT, APPLICABILITY TO CHECK: iron (not steel) castings may be outside steel S232 data (GE Vernova's supplier memo exempts iron content), but castings sold as auto/ag parts can fall under other S232 lists. Needs HTS-level check before pitching.",
    source_links="https://www.gurufocus.com/stock/BOM:532864/transcripts/3028971 ; https://nsearchives.nseindia.com/corporate/NELCAST_18052026191054_PressReleaseQ418052026Upload.pdf",
    pain_classification="Industry fit only",
    s=(8, 18, 12, 12, 8, 5, 3),
    score_note="Large US share but S232 applicability uncertain for iron castings.",
    outreach_angle="Do your US customers ask for any metal-content or origin declaration on iron castings, or has that stayed with steel parts?")
add(lead_id="A08", company="Steelcast Ltd", country_city="India, Bhavnagar (Gujarat)", segment="A", website=NV,
    products="Steel castings for mining, earthmoving, rail, engineering OEMs",
    us_exposure_evidence="MNCL: US ~30% of sales; FY26 guidance cut citing US tariffs; exports to US, Germany, Mexico, Brazil etc.",
    us_exposure_confidence="High",
    contact_name="Chetan Tamboli", title="Chairman, Managing Director & CEO", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: steel castings are a 50% full-value category requiring melt-and-pour; also exports to EU (melt-and-pour declaration from 1 Oct 2026) - one record, two regimes.",
    source_links="https://www.mnclgroup.com/steelcast-ltd-tariff-risk-weighs-on-near-term-growth-long-term-outlook-stable ; https://scanx.trade/stock-market-news/earnings/steelcast-limited-reports-42-revenue-growth-in-q2fy26-revises-fy26-guidance-amid-us-tariff-challenges/24000547 ; https://info.expeditors.com/newsflash/eu-introduces-melt-and-pour-traceability-requirement-for-steel-imports",
    pain_classification="Strong inference",
    s=(11, 17, 12, 12, 8, 5, 4),
    score_note="US + EU melt-and-pour overlap; mid-size, can pay.",
    outreach_angle="You sell steel castings to both US and EU buyers; both now require melt-and-pour per heat. Is that one record internally, or rebuilt per buyer?")
add(lead_id="A09", company="Sundram Fasteners Ltd", country_city="India, Chennai", segment="A", website="https://www.sundram.com",
    products="High-tensile fasteners, powder metal parts, auto components",
    us_exposure_evidence="Q3 FY26 analyst meet (29 Jan 2026): products hit at 25% or 50% 'depending on the iron and steel content'; export revenue -15% YoY.",
    us_exposure_confidence="High",
    contact_name=NV, title="Target: export compliance / customs documentation lead", email_or_official_channel="Company contact via sundram.com", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: management explicitly ties duty rate to per-product steel content, so content records are already a tracked variable.",
    source_links="https://www.sundram.com/pdf/SFLTranscriptAnalystmeet29012026.pdf ; https://www.mnclgroup.com/sundram-fasteners-ltd-q3fy26-company-update",
    pain_classification="Strong inference",
    s=(14, 18, 5, 14, 9, 4, 1),
    score_note="Large enterprise with ERP; poor 10-day MVP fit; good learning interview.",
    outreach_angle="Your Jan 2026 analyst call said rates vary by iron and steel content per product. Who maintains that per-part data for US customers?")
add(lead_id="A10", company="Happy Forgings Ltd", country_city="India, Ludhiana (Punjab)", segment="A", website=NV,
    products="Crankshafts, heavy forgings & machined parts (CV, farm, off-highway)",
    us_exposure_evidence="Q2 FY26 call summary: 35-40% decline in US business; Q1 called direct US exposure 'limited' (sources conflict).",
    us_exposure_confidence="Medium",
    contact_name="Ashish Garg", title="Managing Director", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: steel forgings for farm/off-highway (possible 15% tier) - documentation determines rate tier.",
    source_links="https://themachinemaker.com/news/happy-forgings-reports-stable-q1-fy26-results-with-growth-across-key-metrics/ ; https://www.gurufocus.com/stock/BOM:544057/transcripts/3200028",
    pain_classification="Industry fit only",
    s=(8, 14, 12, 13, 7, 4, 2),
    score_note="Ludhiana anchor account; listed, likely ERP-heavy.",
    outreach_angle="Farm/off-highway parts got a separate 15% tier in June. Did that change what your US customers ask you to document per part?")
add(lead_id="A11", company="Tirupati Forge Ltd", country_city="India, Rajkot (Gujarat)", segment="A", website=NV,
    products="Forged flanges (MS/CS/SS), closed-die auto parts, bearings, gears",
    us_exposure_evidence="Company profile: set up mainly to serve US customers; US reliance and US flange investigation flagged as risks.",
    us_exposure_confidence="Medium-High",
    contact_name="Hitesh Thummar", title="Chairman & Managing Director (undated listing - re-verify)", email_or_official_channel="NSE SME investor contact (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: flanges = steel articles at 50%; melt-and-pour per heat and mill certs per lot to multiple US distributors.",
    source_links="https://www.indiainfoline.com/company/tirupati-forge-ltd/summary ; https://enrichmoney.in/orca/stock-analysis/tirupati-forge-company-details",
    pain_classification="Strong inference",
    s=(9, 15, 11, 9, 8, 5, 5),
    score_note="Classic Rajkot SME exporter; good MVP fit.",
    outreach_angle="Tirupati was built around US flange buyers. How many different melt-and-pour/mill-cert formats do your US distributors ask for?")
add(lead_id="A12", company="Aeroflex Industries Ltd", country_city="India, Navi Mumbai (Taloja)", segment="A", website=NV,
    products="Stainless steel corrugated flexible hoses & assemblies",
    us_exposure_evidence="ICICI Securities (Oct 2025): ~73% revenue from exports; orders deferred, not cancelled, under 50% US tariff.",
    us_exposure_confidence="Medium (US share NV)",
    contact_name="Asad Daud", title="Managing Director (Reuters; Crunchbase lists Yusuf Kagzi as founder-MD - conflict)", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: SS hose assemblies are multi-material (steel braid + fittings), so % metal by weight matters for tiering.",
    source_links="https://www.icicidirect.com/mailcontent/idirect_aeroflex_q2fy26.pdf ; https://sharpely.in/stocks/stock-detail/Aeroflex-Industries-Ltd./AEROFLEX",
    pain_classification="Industry fit only",
    s=(8, 12, 12, 12, 8, 5, 4),
    score_note="Export-heavy, multi-material assemblies; confirm US share.",
    outreach_angle="Hose assemblies mix braid, fittings and non-metal parts. Do US buyers ask you for steel weight as a share of each assembly?")
add(lead_id="A13", company="Patton International Ltd", country_city="India, Kolkata; US affiliate Patton International Inc, Germantown TN", segment="A", website=NV,
    products="Industrial fasteners, builders' hardware, electrical stampings, pressed steel tanks",
    us_exposure_evidence="Panjiva: Patton International Inc (Germantown, TN) is US consignee of Kolkata shipments; govt-recognised export house.",
    us_exposure_confidence="High",
    contact_name="S. Budhia (CEO per IndiaMART); Sanjay Budhia (MD per 2018 profile)", title="CEO / MD - re-verify", email_or_official_channel="IndiaMART enquiry (m.indiamart.com/patton-int)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: exporter that also controls the US importing entity - holds both sides of the declaration problem.",
    source_links="https://m.indiamart.com/patton-int/aboutus.html ; https://panjiva.com/Patton-International-Ltd/1214149 ; https://marwar.com/archive/?p=3598",
    pain_classification="Strong inference",
    s=(8, 15, 8, 10, 8, 4, 5),
    score_note="Owns US affiliate - rare two-sided view; leadership data dated.",
    outreach_angle="Because Patton ships to its own Tennessee entity, you see Section 232 from both the exporter and importer side. Where does that data break down?")
add(lead_id="A14", company="VINIR Engineering Pvt Ltd", country_city="India, Bengaluru / Hosur", segment="A", website="https://vinirforge.org",
    products="Forge-to-finish critical forgings (oil & gas, defence, aerospace, nuclear)",
    us_exposure_evidence="Publishes buyer guide 'Importing forgings from India to USA' with documentation list; offers HTS pre-classification.",
    us_exposure_confidence="Medium",
    contact_name=NV, title="Target: export/quality head", email_or_official_channel="connect@vinirforge.org (public company email)", phone_published="+91 80 27832313",
    evidence_why_relevant="STRONG INFERENCE: already assembles MTRs, heat-treat, PMI, CoC and CoO packs for US buyers, which is exactly the supporting-documentation package SupplierOS generates.",
    source_links="https://vinirforge.org/blog/importing-forgings-india-usa-lead-times-documentation/",
    pain_classification="Strong inference",
    s=(9, 10, 4, 9, 7, 8, 5),
    score_note="Reachable by email; documentation-heavy workflow already exists.",
    outreach_angle="Your US import guide lists a full documentation pack per forging. How long does it take to assemble one, and is any of it reused between buyers?")
add(lead_id="A15", company="Siddharth Group (Siddharth Foundry Pvt Ltd)", country_city="India, Kolhapur (MIDC Shiroli)", segment="A", website="https://www.siddharthfoundry.com",
    products="Grey & SG iron castings and sub-assemblies for pumps and motors",
    us_exposure_evidence="Self-reported exports to USA, Mexico, Germany, Italy, etc.", us_exposure_confidence="Low-Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact form", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: pump castings and sub-assemblies; iron castings applicability must be checked.",
    source_links="https://www.siddharthfoundry.com/",
    pain_classification="Industry fit only", s=(5, 9, 3, 8, 6, 6, 4), score_note="Cluster representative only.",
    outreach_angle="For pump sub-assemblies shipped to the US, do buyers ask for steel/aluminium/copper weight per assembly?")
add(lead_id="A16", company="Bharti Enterprise (Bharti Brass)", country_city="India, Jamnagar (Gujarat)", segment="A", website="https://www.bhartibrass.com",
    products="CNC turned brass parts, precision brass components (since 1979)",
    us_exposure_evidence="Self-reported exports to UK, USA, Europe; directory notes long-term US buyer relationships.", us_exposure_confidence="Medium",
    contact_name="Nitesh Gori", title="Sales Head (per company website)", email_or_official_channel="Website contact (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: brass = copper alloy; copper-derivative S232 lines; Jamnagar cluster reports US copper-content duties made pricing unpredictable.",
    source_links="https://bhartibrass.com/?p=7993 ; https://www.brassroute.com/blog/jamnagar-brass-industry-potential-and-hurdles",
    pain_classification="Strong inference", s=(7, 9, 9, 7, 7, 6, 5), score_note="Small, reachable, copper angle.",
    outreach_angle="US buyers of brass parts now face copper-specific duty rules. Have any asked you for copper weight or smelt/cast origin per part number?")
add(lead_id="A17", company="Ashish Brass Components Pvt Ltd", country_city="India, Jamnagar (Gujarat)", segment="A", website=NV,
    products="Precision turned & machined brass/copper-alloy components",
    us_exposure_evidence="IndiaMART profile lists exports to USA, EU, Middle East, Oceania.", us_exposure_confidence="Low-Medium",
    contact_name="Vishal Sharma", title="Director (IndiaMART profile)", email_or_official_channel="IndiaMART enquiry (m.indiamart.com/ashish-brass-components)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: same copper-derivative logic as A16.",
    source_links="https://m.indiamart.com/ashish-brass-components/profile.html",
    pain_classification="Strong inference", s=(7, 9, 10, 7, 7, 5, 5), score_note="Named director; verify US share.",
    outreach_angle="Do US customers send you their own copper-content declaration forms, and how many different ones do you fill in?")
add(lead_id="A18", company="Suraj Brass Industries", country_city="India, Jamnagar (Gujarat)", segment="A", website=NV,
    products="Brass components", us_exposure_evidence="Issuu profile: serves USA, UK, Europe, Australia, Brazil.", us_exposure_confidence="Low",
    contact_name="Sujit Bhanderi / Amit Bhanderi", title="Leaders (formal titles NV)", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: copper-alloy exporter.", source_links="https://issuu.com/surajbrassindustries",
    pain_classification="Industry fit only", s=(5, 8, 7, 6, 6, 4, 5), score_note="Thin evidence.",
    outreach_angle="Short question on how US buyers' copper-content requests reach you.")
add(lead_id="A19", company="Harsha Engineers International Ltd", country_city="India, Ahmedabad (Changodar)", segment="A", website=NV,
    products="Bearing cages, precision stampings", us_exposure_evidence="ImportGenius: US shipments of taper roller bearing cages; PL Capital: US exports improved Q4 FY26.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: steel/brass cages to global bearing OEMs (each with own supplier declaration process).",
    source_links="https://www.plindia.com/pl-research/harsha-engineers-international-harsha-in-q4fy26-result-update-healthy-q4-romania-revival-remains-watchful-hold/ ; https://static.importgenius.com/suppliers/harsha-engineers-ltd-changodar",
    pain_classification="Industry fit only", s=(6, 12, 4, 13, 7, 4, 2), score_note="Large-OEM supplier; ERP likely.",
    outreach_angle="Bearing OEMs each run their own supplier compliance portals. How many metal-origin requests per year?")
add(lead_id="A20", company="Synergy Green Industries Ltd", country_city="India, Kolhapur (Maharashtra)", segment="A", website=NV,
    products="Large SG iron castings for wind turbines (hubs, frames)",
    us_exposure_evidence="Supplies major global wind OEMs (Vestas >1/3 of order book); US shipments NV.", us_exposure_confidence="Low-Medium",
    contact_name="Sachin R. Shirgaokar", title="Chairman & Managing Director", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE (buyer-side signal): GE Vernova's 22 Jul 2026 supplier memo makes wind suppliers state steel/Al/Cu weight + melt/smelt country on every invoice and bear all costs of missing data. Note: memo exempts iron content, so applicability depends on the part.",
    source_links="https://www.energetica-india.net/news/synergy-green-bags-orders-worth-inr-16374-cr-from-vestas-wind-systems ; https://www.gevernova.com/content/dam/wind-power/documents/suppliers/us-section-232-supplier-requirements.pdf",
    pain_classification="Strong inference", s=(8, 6, 12, 12, 7, 5, 3), score_note="Wind OEM supplier memos are a real trigger; US flow NV.",
    outreach_angle="Wind OEMs such as GE Vernova now require metal weight and melt/smelt origin on every invoice. Has any wind customer sent you a similar notice?")
add(lead_id="A21", company="Fortran Steel Pvt Ltd", country_city="India, Mumbai / Taloja", segment="A", website="https://www.fortran.in",
    products="Stainless & mild steel bars, pipes, wires, flanges, fittings, fasteners",
    us_exposure_evidence="Publishes a 2026 Section 232 guide aimed at US steel buyers.", us_exposure_confidence="Low-Medium",
    contact_name=NV, title=NV, email_or_official_channel="sales@fortran.in (public sales email)", phone_published="+91 91676 22536",
    evidence_why_relevant="STRONG INFERENCE: wrote a US-buyer S232 guide, which suggests it fields these questions from buyers.",
    source_links="https://www.fortran.in/post/us-india-steel-tariffs-2026-section-232-indian-steel-exporters-us-buyers",
    pain_classification="Strong inference", s=(9, 9, 3, 7, 7, 9, 5), score_note="Reachable; trader/stockist mix may mean no mill data ownership.",
    outreach_angle="Your Section 232 guide for US buyers. What do US buyers actually ask you for after reading it?")
add(lead_id="A22", company="Vision Alloys", country_city="India, Mumbai", segment="A", website="https://www.stainlesssteelfasteners.net",
    products="Stainless steel fasteners", us_exposure_evidence="Website lists USA among export markets.", us_exposure_confidence="Low",
    contact_name=NV, title=NV, email_or_official_channel="sales@stainlesssteelfasteners.net (public)", phone_published="+91 22 6659 5948",
    evidence_why_relevant="INDUSTRY FIT: SS fastener exporter.", source_links="https://www.stainlesssteelfasteners.net/",
    pain_classification="Industry fit only", s=(4, 7, 2, 6, 6, 8, 5), score_note="Reachable but thin evidence.",
    outreach_angle="Quick question on mill-cert and melt-and-pour requests from US fastener buyers.")
add(lead_id="A23", company="Crescent Foundry Co Pvt Ltd", country_city="India, Howrah/Kolkata; Baroda", segment="A", website="https://crescentfoundry.in (per directory; confirm)",
    products="Ductile & cast iron manhole covers, gratings, municipal castings",
    us_exposure_evidence="Directory: presence in 50+ countries incl. USA, Columbus OH contact listed; BSI listing omits US (conflict).", us_exposure_confidence="Low-Medium",
    contact_name=NV, title=NV, email_or_official_channel="cf@crescentfoundry.in (per search result; confirm on site)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: cast iron manhole covers (HTS 7325.10) appear on the April 2026 25% full-value annex; origin marking rules apply.",
    source_links="https://www.enggpro.com/company/crescent-foundry ; https://www.whitehouse.gov/wp-content/uploads/2026/04/Metals-ANNEXES-I-A-I-B-II-III-IV.pdf",
    pain_classification="Industry fit only", s=(6, 10, 3, 10, 7, 7, 4), score_note="Municipal castings niche.",
    outreach_angle="Manhole covers moved onto the 25% Section 232 annex in April. Did US distributors change what they ask you to certify?")
add(lead_id="A24", company="PTC Industries Ltd", country_city="India, Lucknow", segment="A", website="https://www.ptcil.com",
    products="Precision castings, aerospace/defence titanium & superalloy parts",
    us_exposure_evidence="Exports to US/UK/EU; Blue Origin order, Honeywell agreement.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Investor relations via ptcil.com", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: aerospace documentation already heavy; S232 applicability per product unclear.",
    source_links="https://nsearchives.nseindia.com/corporate/PTCINDUSTRIES_18022026181707_20260218_Press_release_Q3FY26_Earning_Exchange.pdf",
    pain_classification="Industry fit only", s=(5, 14, 4, 13, 6, 4, 1), score_note="Enterprise/aero QMS; poor MVP fit.",
    outreach_angle="Not recommended for first wave.")
add(lead_id="A25", company="Ramkrishna Forgings Ltd", country_city="India, Kolkata/Jamshedpur", segment="A", website=NV,
    products="Forgings for North American Class 8 trucks", us_exposure_evidence="Reported recovery tied to NA Class 8 truck orders (secondary source).", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: MHDV parts carry separate S232 (25%) regime from Nov 2025.",
    source_links="https://univest.in/blogs/forgings-exporter-stock-rises-25-percent-in-1-year ; https://www.thompsonhinesmartrade.com/2026/02/president-trump-lowers-ieepa-based-tariffs-on-india-and-announces-framework-for-bilateral-interim-trade-agreement/",
    pain_classification="Industry fit only", s=(6, 15, 4, 14, 7, 3, 1), score_note="Large; ERP; learning interview only.",
    outreach_angle="Not recommended for first wave.")
add(lead_id="A26", company="RR Kabel Ltd", country_city="India, Mumbai / Silvassa / Waghodia", segment="A", website=NV,
    products="Wires & cables (copper), UL-listed SKUs", us_exposure_evidence="Industry sources: adding UL-listed SKUs for North America; large exporter.", us_exposure_confidence="Medium",
    contact_name=NV, title="Target: export compliance / logistics head", email_or_official_channel="Investor relations (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: copper smelt/cast mandatory for 8544.42/49 since 30 Jul (fatal 14 Sep 2026).",
    source_links="https://www.federalsynergies.com/post/india-s-cable-industry-expanding-global-horizons-through-strategic-export-opportunities ; https://strixsmart.com/resources/blog/ace-copper-smelt-cast-fatal-error-september-2026",
    pain_classification="Strong inference", s=(11, 12, 4, 14, 8, 4, 2), score_note="Large; strong trigger; enterprise sale.",
    outreach_angle="How did your US importers handle copper smelt/cast after the 14 Sep ACE rejections began?")
add(lead_id="A27", company="SIP Industries Pvt Ltd", country_city="India (location NV)", segment="A", website=NV,
    products="Cast iron manhole covers / municipal castings", us_exposure_evidence="Approved supplier to City of Fort Worth since 2001 (Dallas Express).", us_exposure_confidence="Medium (dated)",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: municipal castings now on S232 annex.", source_links="https://dallasexpress.com/state/why-some-texas-manhole-covers-say-made-in-india/",
    pain_classification="Industry fit only", s=(6, 10, 2, 8, 7, 3, 4), score_note="Need to locate company.",
    outreach_angle="Research first.")
add(lead_id="A28", company="Bhalla Fasteners (Bhalla Auto Manufacturing Co.)", country_city="India, Ludhiana", segment="A", website=NV,
    products="High-tensile fasteners, sprinkler nuts, carriage bolts", us_exposure_evidence="Third-party profile: serves customers in India and USA (self-reported).", us_exposure_confidence="Low",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: Ludhiana fastener SME.",
    source_links="https://bitrated.com/Bhallafasteners", pain_classification="Industry fit only", s=(4, 6, 2, 5, 6, 4, 5), score_note="Thin.", outreach_angle="Research first.")
add(lead_id="A29", company="Vidya Fasteners", country_city="India, Mumbai (Masjid Bunder)", segment="A", website="https://vidyafasteners.com",
    products="Stainless steel fasteners", us_exposure_evidence="Website lists United States among export countries.", us_exposure_confidence="Low",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://vidyafasteners.com/stainless-steel-fasteners-manufacturer-india/", pain_classification="Industry fit only", s=(4, 6, 2, 5, 6, 5, 5),
    score_note="Thin.", outreach_angle="Research first.")
add(lead_id="A30", company="Investment & Precision Castings Ltd", country_city="India, Bhavnagar", segment="A", website=NV,
    products="Investment castings", us_exposure_evidence="Listed castings company; US share NV.", us_exposure_confidence="Low",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://anandrathi.com/stocks/sectors/castings-forgings-and-fastners-stocks", pain_classification="Industry fit only", s=(4, 7, 3, 10, 6, 4, 4),
    score_note="Thin.", outreach_angle="Research first.")
add(lead_id="A31", company="Hex Forge Inc", country_city="India, Mumbai (Rajkot page)", segment="A", website="https://www.hexforgeinc.com",
    products="SS fasteners", us_exposure_evidence="Exporter claim; US NV.", us_exposure_confidence="Low",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published="+91 96194 44982",
    evidence_why_relevant="INDUSTRY FIT.", source_links="https://www.hexforgeinc.com/stainless-steel-fasteners-manufacturer-suppliers-rajkot/",
    pain_classification="Industry fit only", s=(3, 5, 2, 5, 6, 6, 5), score_note="Thin; possibly trader.", outreach_angle="Research first.")

# ---------------- Segment B: US importers / distributors ----------------
add(lead_id="B01", company="Express Fasteners, Ltd.", country_city="USA, Illinois", segment="B", website=NV,
    products="Imported steel fasteners", us_exposure_evidence="Filed suit at US Court of International Trade vs CBP (reported 3 Mar 2026) over 50% duty applied to full value instead of steel content.", us_exposure_confidence="High",
    contact_name=NV, title="Target: owner / import operations", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="VERIFIED PAIN: litigating how steel content is valued. Any refund/reliquidation depends on per-part steel content records from suppliers.",
    source_links="https://fastener-world.com/en/article/9410.html",
    pain_classification="Verified (S232 valuation dispute)", s=(20, 18, 4, 10, 9, 5, 4),
    score_note="Rare verified-pain importer; must find the person via CIT docket counsel.",
    outreach_angle="Your CIT case argues duty should follow steel content. How do you document steel content per part from overseas suppliers today?")
add(lead_id="B02", company="General Foundries Inc", country_city="USA, North Brunswick NJ (1 Progress Rd)", segment="B", website=NV,
    products="Construction/municipal castings, steel fabricated products; US + overseas manufacture",
    us_exposure_evidence="Began as importer of foundry products (1983), historic India foundry; 2025 consignee of Binayak Hi-Tech (Panjiva).", us_exposure_confidence="High",
    contact_name=NV, title="Target: owner / purchasing", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: imports Indian castings into categories on the S232 annex; would request declarations from Indian foundries (could introduce SupplierOS to them).",
    source_links="https://manhole.co.il/manufDetails.asp?m=88 ; https://panjiva.com/Binayak-Hi-Tech-Engineering-Ltd/2167928 ; https://www.cisleads.com/company/details/12738",
    pain_classification="Strong inference", s=(9, 15, 3, 10, 8, 5, 4), score_note="Importer-introduces-supplier channel test.",
    outreach_angle="You import castings from Indian foundries such as Binayak. Which supplier documents are hardest to get complete before entry?")
add(lead_id="B03", company="Eric'sons Dura Trench", country_city="USA (location NV)", segment="B", website=NV,
    products="Trench drain/grating systems", us_exposure_evidence="2025 consignee of Binayak Hi-Tech shipments (Panjiva).", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="STRONG INFERENCE: imports Indian cast/steel grating components.",
    source_links="https://panjiva.com/Binayak-Hi-Tech-Engineering-Ltd/2167928", pain_classification="Strong inference", s=(7, 14, 2, 8, 7, 3, 4),
    score_note="Need company details.", outreach_angle="Research first.")
add(lead_id="B04", company="Star Pipe Products", country_city="USA, Houston TX", segment="B", website="https://www.starpipeproducts.com",
    products="Ductile iron fittings, flanges, restraints for water/wastewater", us_exposure_evidence="Publishes separate 'Import Flange' vs 'Domestic Flange' submittals (Jan 2026); AD scope litigation history.", us_exposure_confidence="High",
    contact_name=NV, title="Target: trade compliance / import ops", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: maintains import vs domestic product documentation lines for municipal submittals; origin-sensitive buyers.",
    source_links="https://www.starpipeproducts.com/wp-content/uploads/Import_Flange_submittal_2601.pdf ; https://access.trade.gov/resources/remands/20-114.pdf",
    pain_classification="Strong inference", s=(9, 13, 3, 12, 8, 5, 3), score_note="Mid-size; documentation-heavy.",
    outreach_angle="You keep separate import and domestic flange submittals. How do you collect melt-and-pour evidence from overseas foundries per lot?")
add(lead_id="B05", company="Matco-Norca", country_city="USA, Brewster NY", segment="B", website="https://www.matco-norca.com",
    products="Valves, PVF, plumbing products (imported)", us_exposure_evidence="2025 tariff price letters; moved 1,600 products to other countries of origin since 2018.", us_exposure_confidence="High",
    contact_name=NV, title="Target: VP sourcing / compliance", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: multi-country re-sourcing (incl. away from China) means new suppliers to onboard with metal-origin data.",
    source_links="https://www.inddist.com/supply-chain/news/22933648/plumbing-and-pvf-supplier-increasing-prices-after-latest-tariff-announcement ; https://www.cooneybrothers.com/userfiles/files/tariffs/matco-norca-price-decrease-letter-05-2025.pdf",
    pain_classification="Strong inference", s=(8, 14, 3, 12, 8, 5, 3), score_note="Importer side; may push suppliers to a tool.",
    outreach_angle="After moving 1,600 SKUs to new origins, how do you onboard new suppliers' metal and origin data?")
add(lead_id="B06", company="Texas Flange", country_city="USA, Texas", segment="B", website="https://texasflange.com",
    products="Pipe flanges (domestic & imported)", us_exposure_evidence="Blog posts on S232 flange pricing and 2026 market update.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="INDUSTRY FIT: flange distributor communicating tariff changes to buyers.",
    source_links="https://texasflange.com/blog/flange-market-regulations-update/", pain_classification="Industry fit only", s=(8, 11, 2, 9, 7, 5, 4),
    score_note="Small distributor.", outreach_angle="Your 2026 flange market update. Which supplier documents do your customers now ask you to pass through?")
add(lead_id="B07", company="Chapman Smith Corporation", country_city="USA, Warsaw IN (1668 E. Kosciusko Dr.)", segment="B", website="https://www.chapmansmith.com",
    products="Sourced steel coil, stainless, aluminum extrusions, castings, molded parts for OEMs (since 1997)",
    us_exposure_evidence="Blog 'Section 232 Tariffs for OEM Parts in 2026'; advises auditing 85% US-melt via mill certs.", us_exposure_confidence="Medium-High",
    contact_name=NV, title="Target: owner / sourcing lead", email_or_official_channel="Website contact", phone_published="(574) 372-3117",
    evidence_why_relevant="STRONG INFERENCE: sourcing intermediary that must collect mill certs and HTS/annex data from overseas suppliers for OEM customers.",
    source_links="https://www.chapmansmith.com/blog/section-232-tariffs-oem-parts-2026", pain_classification="Strong inference", s=(11, 10, 4, 9, 8, 8, 5),
    score_note="Small, reachable sourcing firm; good pilot candidate.",
    outreach_angle="Your blog tells OEMs to audit US-melt claims through mill certs. Who on your team does that audit, and how long does it take per part?")
add(lead_id="B08", company="Redstone Manufacturing", country_city="USA (factories in India, China, Taiwan, Vietnam, Mexico)", segment="B", website="https://redstonemanufacturing.com",
    products="Contract-manufactured metal parts (stamping, tube bending, machining, laser-cut)",
    us_exposure_evidence="Acts as importer of record on modified DDP; applies metal-origin rule per part; publishes 2026 S232 guides.", us_exposure_confidence="High",
    contact_name="'mihir' (article author; full name/role NV)", title=NV, email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE (near-verified): says it manages mill-cert, metal-content BOM and supplier certification documentation as IOR across India/Asia factories, which is exactly the SupplierOS workflow.",
    source_links="https://redstonemanufacturing.com/resources/articles/section-232-tariffs-steel-aluminum/ ; https://redstonemanufacturing.com/resources/articles/section-232-tariffs-still-effective/",
    pain_classification="Strong inference", s=(15, 17, 6, 11, 9, 5, 5), score_note="Holds the per-part workflow across Indian factories; ideal design partner.",
    outreach_angle="You manage S232 documentation as importer of record across India, China and Vietnam factories. How do you keep per-part metal records current when a factory changes mills?")
add(lead_id="B09", company="IC&T Manufacturing (IN Consulting & Trade)", country_city="USA / India (Pune sourcing office)", segment="B", website="https://inconsultingandtrade.com",
    products="Castings, forgings, machined metals sourced from India for US OEMs", us_exposure_evidence="Site: India is primary sourcing hub; Pune office.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact (site returned 503 during research)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: India-to-US sourcing intermediary handling supplier documentation.",
    source_links="https://inconsultingandtrade.com/", pain_classification="Strong inference", s=(9, 12, 3, 9, 8, 4, 5), score_note="Channel to many Indian suppliers.",
    outreach_angle="As a Pune-based sourcing team, how many Indian suppliers do you chase for melt-and-pour data each month?")
add(lead_id="B10", company="Brighton-Best International", country_city="USA (national fastener master distributor)", segment="B", website=NV,
    products="Imported fasteners", us_exposure_evidence="Feb 2025 customer notice: substantially all imported fasteners pulled under S232.", us_exposure_confidence="High",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: high-volume importer; would require supplier data from Asian/Indian mills.",
    source_links="https://www.abcsupplyinteriors.com/wp-content/uploads/2025/03/announcement_brighton-best_02-19-2025.pdf", pain_classification="Strong inference",
    s=(10, 18, 3, 14, 9, 4, 1), score_note="Enterprise; learning interview or later.", outreach_angle="Not first wave.")
add(lead_id="B11", company="Hillman Group", country_city="USA (Canada entity is Chin Well consignee)", segment="B", website=NV,
    products="Fasteners & hardware (imported)", us_exposure_evidence="Hillman Group Canada is a consignee of Chin Well Fasteners (Vietnam).", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: large importer requesting supplier declarations.",
    source_links="https://panjiva.com/Chin-Well-Fasteners-Vn-Co-Ltd/1049191", pain_classification="Industry fit only", s=(8, 15, 2, 15, 9, 3, 0),
    score_note="Enterprise; not MVP fit.", outreach_angle="Not first wave.")
add(lead_id="B12", company="Topy Precision Mfg Inc", country_city="USA (location NV)", segment="B", website=NV,
    products="Fasteners (from Topy Fasteners Vietnam)", us_exposure_evidence="Panjiva consignee of Topy Fasteners Vietnam.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: intra-group importer.",
    source_links="https://panjiva.com/Topy-Fasteners-Vietnam-Co-Ltd/21996591", pain_classification="Industry fit only", s=(5, 11, 2, 10, 7, 3, 2),
    score_note="Japanese group; slow sale.", outreach_angle="Not first wave.")
add(lead_id="B13", company="Tata International Metals Americas", country_city="USA", segment="B", website=NV,
    products="Fastener distribution partnership with Cetin Civata (Turkey)", us_exposure_evidence="2021 partnership to expand Cetin Civata's US fastener business.", us_exposure_confidence="Medium (dated)",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: importer of Turkish fasteners.",
    source_links="https://tatainternational.com/?p=10706", pain_classification="Industry fit only", s=(7, 12, 3, 13, 8, 4, 2), score_note="Dated.", outreach_angle="Not first wave.")

# ---------------- Segment C: brokers & trade compliance ----------------
add(lead_id="C01", company="Vigilant Global Trade Services", country_city="USA (phones 216 Ohio / 208 Idaho)", segment="C", website="https://vigilantgts.com",
    products="Classification, compliance help desk; Section 232 mill-certificate collection, validation & exception management",
    us_exposure_evidence="Sells structured database linking products, metal content, origin and supporting docs.", us_exposure_confidence="High",
    contact_name=NV, title="Target: founder / compliance lead", email_or_official_channel="Website contact page", phone_published="(216) 245-8117 ; (208) 975-9481",
    evidence_why_relevant="VERIFIED PAIN (as described by service provider): 'Many suppliers are reluctant to share upstream details'; contracts often don't require mill certs; missing docs can trigger 200% aluminium rate. Also a COMPETITOR/PARTNER.",
    source_links="https://vigilantgts.com/prove-origin-prevent-costly-tariffs-hb/", pain_classification="Verified (market-level, from provider)", s=(18, 14, 3, 10, 9, 8, 5),
    score_note="Best partner/white-label test; also competitive intel.", outreach_angle="Your page says suppliers are reluctant to share upstream mill details. I'm testing whether suppliers share more readily if they keep and control the record. Would you compare notes?")
add(lead_id="C02", company="Strix (Strix LLC / TBI Brokers Inc)", country_city="USA, Bozeman MT", segment="C", website="https://strixsmart.com",
    products="Licensed customs brokerage, self-filing software ($30/entry), consulting, PSC filing",
    us_exposure_evidence="Detailed blog on copper smelt/cast ACE fatal error (14 Sep 2026); advises building supplier-data process so 'OTH' is temporary.", us_exposure_confidence="High",
    contact_name=NV, title="Target: head of consulting", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="VERIFIED (market-level): documents importers lacking supplier smelt data and the need for a supplier-data process; sells software already, so a natural integration/white-label partner.",
    source_links="https://strixsmart.com/resources/blog/ace-copper-smelt-cast-fatal-error-september-2026 ; https://strixsmart.com/company/about", pain_classification="Verified (market-level)",
    s=(16, 15, 4, 10, 9, 6, 5), score_note="Software-minded broker; white-label test.",
    outreach_angle="Your copper smelt/cast post recommends a supplier-data process so OTH is temporary. What does that process look like for your clients today?")
add(lead_id="C03", company="V. Alexander & Co., Inc.", country_city="USA (multi-location broker/forwarder)", segment="C", website="https://www.valexander.com",
    products="Customs brokerage, forwarding, trade compliance (TradeInsights)", us_exposure_evidence="Published copper smelt & cast advisory (Sep 2026).", us_exposure_confidence="High",
    contact_name="Brian Walczyk", title="Compliance Manager, TradeInsights (LCB, CCS) - article byline", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: licensed broker who writes the client advisories, so likely sees incomplete supplier declarations firsthand.",
    source_links="https://www.valexander.com/?p=3878", pain_classification="Strong inference", s=(12, 14, 13, 10, 9, 5, 5),
    score_note="Named, credentialed, hands-on person.", outreach_angle="Your copper smelt-and-cast advisory. After 14 Sep, what share of client entries arrive without usable smelt/cast data from the supplier?")
add(lead_id="C04", company="Braumiller Consulting Group, LLC", country_city="USA (Texas-based; national)", segment="C", website=NV,
    products="Trade compliance consulting", us_exposure_evidence="Presented LACBFFA webinar 'Mastering Section 232: recent changes and practical solutions for brokers' (30 Jul 2026).", us_exposure_confidence="High",
    contact_name="Robert Stein", title="Vice President (36+ yrs brokerage/forwarding/consulting)", email_or_official_channel="Via firm website (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: taught brokers 'common filing challenges, documentation best practices' for S232.",
    source_links="https://www.lacbffa.org/events/mastering-section-232-recent-changes-and-practical-solutions-for-brokers", pain_classification="Strong inference",
    s=(13, 13, 13, 11, 8, 5, 5), score_note="Named expert; channel to brokers.", outreach_angle="Your July LACBFFA session on Section 232 filing challenges. Which documentation failures came up most from brokers?")
add(lead_id="C05", company="Braumiller Law Group, PLLC", country_city="USA (Texas)", segment="C", website=NV,
    products="International trade & customs law", us_exposure_evidence="Same LACBFFA S232 webinar.", us_exposure_confidence="High",
    contact_name="Kerry Wang", title="Attorney, international trade & customs", email_or_official_channel="Via firm website (NV)", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: advises importers on S232 substantiation.", source_links="https://www.lacbffa.org/events/mastering-section-232-recent-changes-and-practical-solutions-for-brokers",
    pain_classification="Strong inference", s=(11, 12, 12, 11, 7, 5, 3), score_note="Advisor/referrer, not buyer.", outreach_angle="What evidence package do you tell clients to hold for a 15%-threshold or US-melt claim?")
add(lead_id="C06", company="Diaz Trade Law", country_city="USA, Miami FL", segment="C", website="https://diaztradelaw.com",
    products="Customs & international trade law", us_exposure_evidence="Publishes S232 updates (June 2026 proclamation).", us_exposure_confidence="High",
    contact_name="Jennifer Diaz", title="Founder (per FreightWaves)", email_or_official_channel="Via firm website", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: advises importers; potential referral partner.", source_links="https://diaztradelaw.com/new-section-232-action-what-the-june-2026-aluminum-steel-copper-proclamation-means-for-your-imports/ ; https://www.freightwaves.com/news/executive-moves-ups-and-diaz-trade-law",
    pain_classification="Strong inference", s=(10, 12, 11, 11, 7, 6, 3), score_note="Referrer.", outreach_angle="Which supplier-side records do your importer clients struggle to obtain for melt-and-pour or the 85% US-content tier?")
add(lead_id="C07", company="Green Worldwide Shipping", country_city="USA, Atlanta GA (national offices)", segment="C", website="https://www.greenworldwide.com",
    products="3PL with in-house licensed customs brokers in every office", us_exposure_evidence="Published Section 232 steel & aluminium fact sheet (Jun 2025).", us_exposure_confidence="High",
    contact_name="Thomas Jorgensen", title="President & CEO", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: mid-size broker network handling S232 entries.", source_links="https://www.greenworldwide.com/wp-content/uploads/2025/06/Section-232-Steel-and-Aluminum-Fact-Sheet-2025-Updated-6.19.25.pdf ; https://www.greenworldwide.com/san-francisco-freight-forwarder-ted-l-rausch-co-joins-green-worldwide-shipping/",
    pain_classification="Strong inference", s=(10, 14, 10, 12, 8, 5, 4), score_note="Ask for intro to compliance lead rather than CEO pitch.",
    outreach_angle="Ask for 15 min with whoever runs Section 232 entries: how often do supplier declarations arrive incomplete?")
add(lead_id="C08", company="Mallory Alexander International Logistics", country_city="USA, Concordville PA / Memphis TN", segment="C", website="https://www.mallorygroup.com",
    products="Licensed customs brokerage, trade compliance, freight", us_exposure_evidence="Blog on 15% de minimis: checklist (BOM, total weight, metal kg, supplier attestations); flags 'inconsistent supplier data'.", us_exposure_confidence="High",
    contact_name=NV, title="Target: trade compliance manager", email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: publicly names inconsistent supplier data as a compliance risk.", source_links="https://www.mallorygroup.com/blog-posts/section-232-tariff-update-new-15-de-minimis-threshold-details-for-u-s-importers",
    pain_classification="Strong inference", s=(12, 14, 3, 12, 8, 5, 4), score_note="Checklist matches our data model.", outreach_angle="Your 15% checklist (BOM, metal kg, supplier attestation). How often do client files arrive missing one of these?")
add(lead_id="C09", company="Willson International", country_city="USA/Canada (Buffalo NY / Ontario)", segment="C", website="https://www.willsonintl.com",
    products="Customs brokerage, trade compliance", us_exposure_evidence="Requires 'Steel and Aluminum Declaration'; copper smelt/cast guidance (Jul 2026).", us_exposure_confidence="High",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="STRONG INFERENCE: broker issues own declaration form, adding to buyer-specific format sprawl.",
    source_links="https://www.willsonintl.com/news/guidance-on-section-232-copper-smelt-and-cast-reporting-requirements/", pain_classification="Strong inference", s=(10, 13, 3, 11, 8, 6, 4),
    score_note="", outreach_angle="Would a supplier-maintained record that pre-fills your Steel and Aluminum Declaration reduce back-and-forth?")
add(lead_id="C10", company="Mohawk Global Logistics", country_city="USA, NY (national)", segment="C", website="https://mohawkglobal.com",
    products="Customs brokerage & trade advisory", us_exposure_evidence="Invoice & duty FAQs for S232 derivatives; copper smelt/cast guidance.", us_exposure_confidence="High",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="STRONG INFERENCE.",
    source_links="https://mohawkglobal.com/word-from-the-white-house/steel-aluminum-derivatives-key-invoice-duty-guidelines/", pain_classification="Strong inference", s=(10, 14, 3, 12, 8, 5, 4),
    score_note="", outreach_angle="Your invoice FAQ for derivatives. What do supplier invoices most often get wrong?")
add(lead_id="C11", company="A.N. Deringer", country_city="USA, Vermont (national)", segment="C", website="https://www.anderinger.com",
    products="Customs brokerage, forwarding, compliance", us_exposure_evidence="Published S232 modification guidance.", us_exposure_confidence="High",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://www.anderinger.com/modification-section-232-tariffs/", pain_classification="Industry fit only", s=(8, 14, 2, 13, 8, 4, 2), score_note="Larger broker.", outreach_angle="Learning interview.")
add(lead_id="C12", company="Shapiro", country_city="USA, Baltimore MD", segment="C", website="https://www.shapiro.com",
    products="Customs brokerage & forwarding", us_exposure_evidence="Section 232 tariff resource page incl. country-specific rates.", us_exposure_confidence="High",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://www.shapiro.com/?p=199639", pain_classification="Industry fit only", s=(8, 13, 2, 12, 8, 4, 3), score_note="", outreach_angle="Learning interview.")
add(lead_id="C13", company="MyCustomsInfo", country_city="USA", segment="C", website="https://mycustomsinfo.com",
    products="Customs audits reconciling entries vs supporting docs ($8k-$50k per cycle)", us_exposure_evidence="Section 232 compliance service page.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="STRONG INFERENCE: audit service sees documentation gaps; partner and price anchor.",
    source_links="https://mycustomsinfo.com/section-232-compliance", pain_classification="Strong inference", s=(11, 10, 2, 10, 7, 5, 4), score_note="Partner/price anchor.",
    outreach_angle="In your Section 232 audits, which supporting document is most often missing or unreconcilable?")
add(lead_id="C14", company="Allied Customs House Brokers", country_city="USA (NV)", segment="C", website="https://alliedchb.com",
    products="Customs brokerage", us_exposure_evidence="Posts CBP CSMS S232 guidance.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT: small broker.",
    source_links="https://alliedchb.com/news/csms-68253075-section-232-duties-on-imports-of-aluminum-steel-and-copper", pain_classification="Industry fit only", s=(7, 12, 2, 8, 7, 4, 4),
    score_note="", outreach_angle="Learning interview.")
add(lead_id="C15", company="J.S. Connor", country_city="USA", segment="C", website="https://jsconnor.com",
    products="Customs brokerage", us_exposure_evidence="Post on implementing new S232 duties.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://jsconnor.com/tariffs/implementation-of-new-section-232-duties-on-aluminum-steel-copper-imports/", pain_classification="Industry fit only", s=(8, 12, 2, 10, 8, 4, 4),
    score_note="", outreach_angle="Learning interview.")
add(lead_id="C16", company="Stile International", country_city="USA", segment="C", website="https://stileintl.com",
    products="Customs brokerage / trade compliance", us_exposure_evidence="Post: what importers must review before filing S232 entries.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://stileintl.com/new-section-232-tariffs-on-steel-aluminum-and-copper/", pain_classification="Industry fit only", s=(8, 12, 2, 10, 8, 4, 4),
    score_note="", outreach_angle="Learning interview.")
add(lead_id="C17", company="ExFreight", country_city="USA", segment="C", website="https://www.exfreight.com",
    products="Digital freight forwarding & customs", us_exposure_evidence="S232 importer guides.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://www.exfreight.com/section-232-tariffs-steel-aluminum-imports-guide/", pain_classification="Industry fit only", s=(7, 11, 2, 10, 7, 4, 4),
    score_note="", outreach_angle="Learning interview.")
add(lead_id="C18", company="SEKO Logistics", country_city="USA (global)", segment="C", website="https://www.sekologistics.com",
    products="Forwarding & customs", us_exposure_evidence="Published Section 232 2026 timeline.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://www.sekologistics.com/media/gldhncwq/section232_2026timeline.pdf", pain_classification="Industry fit only", s=(7, 12, 2, 13, 8, 3, 2),
    score_note="Large.", outreach_angle="Learning interview.")

# ---------------- Segment D: overseas beyond India ----------------
add(lead_id="D01", company="Chin Well Fasteners (Vietnam) Co Ltd / Chin Well Holdings", country_city="Vietnam, Dong Nai (Nhon Trach 3 IZ); parent Penang, Malaysia", segment="D", website=NV,
    products="Steel fasteners (guard rails, transmission towers, furniture)", us_exposure_evidence="Directory: ~30% exports to USA; Panjiva ~1,091 US shipments.", us_exposure_confidence="Medium-High",
    contact_name=NV, title=NV, email_or_official_channel="Listed company IR (Bursa) - NV", phone_published=NV, evidence_why_relevant="INDUSTRY FIT: high-volume fastener exporter to US and EU (EU melt-and-pour also applies).",
    source_links="https://www.fasten.it/en/Company/Details/18573 ; https://panjiva.com/Chin-Well-Fasteners-Vn-Co-Ltd/1049191", pain_classification="Industry fit only",
    s=(7, 15, 3, 13, 8, 4, 3), score_note="US + EU double exposure.", outreach_angle="You ship fasteners to both the US and EU; both now want melt-and-pour per lot. Is that one record or two processes?")
add(lead_id="D02", company="Co Win Fasteners Industries Vietnam", country_city="Vietnam", segment="D", website=NV,
    products="Fasteners", us_exposure_evidence="Panjiva: ~835 US shipments; buyers incl. Hold Tite, Viscan, Sil Fasteners.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://es.panjiva.com/Co-Win-Fasteners-Industries-Vietnam/87798756", pain_classification="Industry fit only", s=(5, 13, 2, 9, 8, 3, 4), score_note="", outreach_angle="Research first.")
add(lead_id="D03", company="Topy Fasteners Vietnam Co Ltd", country_city="Vietnam", segment="D", website=NV,
    products="Fasteners", us_exposure_evidence="Panjiva: ~362 US shipments to Topy Precision Mfg Inc.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT.",
    source_links="https://panjiva.com/Topy-Fasteners-Vietnam-Co-Ltd/21996591", pain_classification="Industry fit only", s=(5, 12, 2, 11, 7, 3, 2), score_note="Intra-group.", outreach_angle="Not first wave.")
add(lead_id="D04", company="Cetin Civata", country_city="Turkey", segment="D", website=NV,
    products="Fasteners", us_exposure_evidence="2021 partnership with Tata International Metals Americas to grow US business; 45% exported mainly to W. Europe.", us_exposure_confidence="Low-Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: Turkish fasteners to US ~$48M (2024); EU-centric.",
    source_links="https://tatainternational.com/?p=10706 ; https://www.fastener-world.com/data/pdf_download/FW_217_E_202.pdf", pain_classification="Industry fit only", s=(6, 10, 3, 11, 7, 4, 3),
    score_note="EU melt-and-pour more relevant than US.", outreach_angle="Research first.")
add(lead_id="D05", company="New Age Aluminium Industries Sdn Bhd", country_city="Malaysia", segment="D", website=NV,
    products="Aluminium extrusions", us_exposure_evidence="Named producer/exporter in USITC aluminum extrusions AD/CVD investigation.", us_exposure_confidence="Medium",
    contact_name=NV, title=NV, email_or_official_channel=NV, phone_published=NV, evidence_why_relevant="INDUSTRY FIT: aluminium smelt-and-cast reporting; AD/CVD complexity.",
    source_links="https://www.usitc.gov/publications/701_731/pub5560.pdf", pain_classification="Industry fit only", s=(5, 8, 2, 9, 7, 3, 3), score_note="AD/CVD out of MVP scope.", outreach_angle="Not first wave.")

# ---------------- Segment E: adjacent compliance ----------------
add(lead_id="E01", company="Mondelez International", country_city="USA, Chicago", segment="E", website="https://www.mondelezinternational.com",
    products="CPG (packaging EPR producer)", us_exposure_evidence="EPR producer in CA/OR/CO etc.; CAA reporting deadline 31 May 2026.", us_exposure_confidence="High (EPR, not S232)",
    contact_name="Brie Seferian", title="Senior Manager, EPR North America (per Packaging World, SPC Impact 2026)", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="VERIFIED PAIN (adjacent): said many companies are still assembling packaging information from disconnected systems.",
    source_links="https://www.packworld.com/sustainable-packaging/recycling/article/22966054/spc-impact-2026-epr-moves-from-theory-to-operational-reality", pain_classification="Verified (EPR data)",
    s=(20, 18, 8, 15, 8, 3, 1), prio_override="P2", score_note="Learning interview about the brand-side EPR workflow, not a near-term buyer; not an MVP fit.",
    outreach_angle="Your SPC Impact remark about assembling packaging data from disconnected systems. I'm studying the supplier side of that request. 15 minutes?")
add(lead_id="E02", company="Sonoco Products", country_city="USA, Hartsville SC", segment="E", website="https://www.sonoco.com",
    products="Packaging converter", us_exposure_evidence="Converter supplying EPR data to brand owners.", us_exposure_confidence="High (EPR)",
    contact_name="Scott Byrne", title="Sonoco representative quoted at Recycling Today conference (exact title NV)", email_or_official_channel=NV, phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: says converters provide 'the foundational data' brand owners need for EPR, so converters face many brand-specific requests (the supplier-held analog to SupplierOS).",
    source_links="https://www.oemmagazine.org/home/article/22952828/brands-and-converters-align-on-epr-data-demands", pain_classification="Strong inference",
    s=(15, 17, 8, 15, 8, 3, 2), prio_override="P2", score_note="Strongest adjacent analog of supplier-held reusable records; enterprise.",
    outreach_angle="You described converters as the source of foundational EPR data. How many brand-specific formats does Sonoco answer per packaging spec?")
add(lead_id="E03", company="Pakka Ltd", country_city="India, Ayodhya / Bengaluru", segment="E", website="https://pakka.com",
    products="Compostable paper packaging; converter guide on EPR", us_exposure_evidence="Indian EPR (paper packaging) + exports; publishes 2026 converter EPR guide.", us_exposure_confidence="Medium (EPR)",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="STRONG INFERENCE: own guide says every brand owner a converter supplies asks for EPR-aligned data from April (claims 30-60% more documentation work - unsourced).",
    source_links="https://pakka.com/blog/epr-paper-packaging-india-converters-2026/", pain_classification="Strong inference", s=(10, 12, 3, 10, 8, 5, 3),
    score_note="Indian supplier-side EPR analog.", outreach_angle="Your converter EPR guide estimates 30-60% more documentation work. Where did that number come from?")
add(lead_id="E04", company="ESGen Ltd", country_city="UK", segment="E", website="https://esgen.co.uk",
    products="ESG/CBAM reporting software + services", us_exposure_evidence="Guide on what EU buyers ask Indian steel/aluminium exporters for under CBAM.", us_exposure_confidence="N/A",
    contact_name=NV, title=NV, email_or_official_channel="Website contact", phone_published=NV,
    evidence_why_relevant="PARTNER/COMPETITOR: works Indian exporter CBAM data flows; possible referral for exporters who need both CBAM and S232 records.",
    source_links="https://esgen.co.uk/resources/blog/eu-cbam-indian-steel-aluminium-exporters/", pain_classification="Industry fit only", s=(8, 6, 3, 8, 6, 5, 2),
    score_note="Partner, not buyer.", outreach_angle="Partner conversation only.")


def build():
    rows = []
    for k in L:
        s = k.pop("s")
        total = sum(s)
        prio = k.pop("prio_override") or ("P1" if total >= 67 else "P2" if total >= 50 else "P3")
        k.update(dict(zip(["s_pain25", "s_trade20", "s_access15", "s_pay15", "s_freq10", "s_contact10", "s_mvp5"], s)))
        k["lead_score"] = total
        k["priority"] = prio
        rows.append(k)
    rows.sort(key=lambda r: (r["segment"], r["lead_id"]))
    return rows


def main():
    out = os.path.dirname(os.path.abspath(__file__))
    rows = build()
    with open(os.path.join(out, "leads_master.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    wb = Workbook()
    ws = wb.active
    ws.title = "Leads"
    ws.append(FIELDS)
    for r in rows:
        ws.append([r[c] for c in FIELDS])
    hdr = PatternFill("solid", fgColor="1F3A5F")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = hdr
        c.alignment = Alignment(wrap_text=True, vertical="top")
    fills = {"P1": "D9EAD3", "P2": "FFF2CC", "P3": "F4F4F4"}
    pcol = FIELDS.index("priority") + 1
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        row[pcol - 1].fill = PatternFill("solid", fgColor=fills[row[pcol - 1].value])
    widths = {"evidence_why_relevant": 70, "us_exposure_evidence": 50, "source_links": 60, "outreach_angle": 60, "products": 35, "company": 30}
    for i, name in enumerate(FIELDS, 1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = widths.get(name, 16)
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(os.path.join(out, "leads_master.xlsx"))

    from collections import Counter
    print(len(rows), Counter(r["segment"] for r in rows), Counter(r["priority"] for r in rows))
    for r in sorted(rows, key=lambda r: -r["lead_score"])[:32]:
        print(r["lead_id"], r["lead_score"], r["priority"], r["company"])


if __name__ == "__main__":
    main()
