# Product Feasibility: Blueberry Blast, Lemon Zest, Coconut

Prepared 1 Oct 2026. This is desk research only. **No laboratory work has been done on any natural-fruit formulation.** Nothing here is a recipe, and nothing establishes that any of the three products can be made shelf-stable at an acceptable cost. Source IDs refer to `SOURCE_REGISTER.csv`.

## 1. Starting point (FOUNDER-REPORTED, unverified)
- In 2025 the founder developed physical prototypes with Dark Horse Brands (Mahaveer Group, Bengaluru), using **artificial flavour powders**.
- About 250 students tasted the prototypes. Flavour feedback was "generally encouraging", with blueberry favoured. The founder was not satisfied with the overall formulation, and development stopped when the budget ran out.
- Separately, the founder experimented with (a) a real-blueberry drink with pulp, which the founder found particularly appealing when carbonated, and (b) carbonated coconut water.
- **No records, recipes, test data or photographs survive.** No natural-fruit formulation has been made in the manufacturer's laboratory.

## 2. Design constraints that apply to all three flavours
| Constraint | Source | Effect on design |
|---|---|---|
| Caffeine of 36–75 mg per 250 ml if sold as a caffeinated beverage | S01 | Defines the "functional" ceiling |
| Only taurine, glucuronolactone, inositol, pantothenic acid and B-vitamins may be added without approval | S01 | L-theanine, beta-alanine and citrulline are effectively out for launch (see `REGULATORY_REVIEW.md`) |
| Sweeteners: sucralose, acesulfame-K, aspartame, neotame, saccharin; stevia up to 200 mg/kg steviol equivalents; **no monk fruit extract** | S02, S66, S67 | Sugar reduction must rely on these |
| "Natural" or "real" claims are heavily restricted | S08 | Fruit content must be described factually |
| 40% GST on caffeinated or carbonated drinks | S13 | Every rupee of extra ingredient cost needs about ₹1.9 of extra MRP to protect the brand's net margin at base trade margins |
| Canned format: aluminium blocks light, which helps light-sensitive stevia and anthocyanins (S49). Liner compatibility with acidic fruit must be pack-tested. | S49 | A can is a better choice than clear PET |

## 3. Real fruit vs concentrate vs extract vs natural flavour vs artificial powder

| Option | What it is | Taste impact | Stability risks | Cost (India) | Claim you can make |
|---|---|---|---|---|---|
| Whole fruit / puree / pulp | Fruit solids in suspension | Most "authentic"; texture and colour | Sedimentation; needs stabilisers (gellan gum is permitted at GMP in carbonated water, S02); pulp can raise foaming during carbonated filling (process risk, **verify with co-packer**); microbial load requires heat treatment; colour loss | **UNKNOWN.** Highest. Blueberries are largely imported. | Ingredient list and % declaration (QUID). "Natural" claim **not** allowed (S08). |
| NFC juice or juice concentrate | Clarified or cloudy juice, reconstituted | Fruity, adds sugar | Anthocyanin and vitamin C loss with heat and storage (S54–S56); browning | UNKNOWN; lower than puree | "Contains X% blueberry juice". At ≥10% the product may fall under the fruit-beverage standard (S04). |
| Fruit extract / essence | Concentrated aroma or colour fractions | Aroma without much sugar | Volatile loss; oxidation | Low–medium | "Flavoured", per label rules |
| Natural flavouring substances | Flavour preparations from natural sources | Controllable, consistent | Generally designed for shelf life | Low | "Contains added flavour (natural flavouring substances)", which is **not** a claim that the product is natural |
| Nature-identical or artificial flavour (the historical powder route) | Synthetic or nature-identical aroma | Consistent, cheapest | Most stable | Lowest. The historical ₹22/can at ~10k units included this (founder-reported). | "Contains added flavour (nature-identical/artificial)" |

**Bottom line:** to Indian consumers and regulators, a "real-fruit" story is mostly a label-percentage story. Whether a few percent of juice changes taste and purchase intent enough to pay for itself is **unknown** and must be blind-tested (see `CONSUMER_RESEARCH.md`).

## 4. Flavour-by-flavour assessment

### 4.1 Blueberry Blast
**Technical risks (evidence-based):**
- **Colour and pigment instability.** Blueberry anthocyanins degrade during storage. One blueberry juice blend lost **62% of anthocyanins in 20 days even at 4 °C** without added antioxidant (S55). Conventional HTST pasteurisation (95 °C, 15 s) led to continuing degradation and destroyed ascorbic acid (S54). A shelf-stable product stored warm in Indian retail will lose more. Anthocyanin degradation follows first-order kinetics (S56), so loss is continuous rather than a one-off.
- **Mitigations to test:** copigmentation, antioxidants such as gallic acid (shown in juice studies, S55), oxygen control at filling, the can's light barrier, and permitted anthocyanin colour (INS 163(i) at GMP in category 14.1.4, S68). Added colour must be declared, which weakens the "real fruit" story.
- **Pulp in a carbonated can:** sedimentation and appearance; stabiliser system (e.g. gellan gum); possible foaming and fill-level variation on a semi-automatic line. **Co-packer must trial this.**
- **Sugar:** juice adds natural sugar. Cutting sugar while keeping a fruit-forward taste means relying on high-intensity sweeteners, which brings their aftertaste (see §5).
- **Sourcing:** blueberries are not a mainstream Indian crop. Price, origin and continuity of supply are **UNKNOWN** and need quotes.
- **Regulatory:** combining ≥10% juice with caffeine has an unresolved classification (REGULATORY_REVIEW §2).
- **Competitive reality:** **Sting Gold already sells a blueberry-flavoured caffeinated drink at ₹20 for 250 ml** (S33). Campa sells "Berry Kick" (S36). A blueberry flavour by itself is therefore not a gap. Only a demonstrably better taste, or a credible juice-content difference, could be.

**Feasibility verdict:** *technically possible in principle*, as many fruit sodas exist, but **unproven**. It carries the highest cost and stability risk of the three, and it needs a 3–6-month shelf-life study before any commercial run.

### 4.2 Lemon Zest
- **Options:** NFC lemon juice (≥5% juice = carbonated fruit beverage; 2.5–5% = "with fruit juice", S04), lemon juice concentrate, or natural lemon flavour or peel-oil emulsion (estergum up to 100 ppm is permitted for clouding in carbonated water, S02).
- **Technical risks:** citrus flavour volatiles oxidise and change in acidic beverages over storage. This is a well-known industry risk; **no study was retrieved here**, and an accelerated shelf-life test is needed. Lemon is acidic, which supports microbial stability at low pH.
- **Cost:** likely the cheapest natural option (hypothetical ₹1–5/can adder in the model; **no quote**).
- **Competitive reality:** citrus is crowded. Campa has "Lemon Kick" and a zero-sugar "Citrus Kick" (S16, S36), Sprite and Nimbooz occupy lemon sodas, and Sting's range includes multiple flavours.
- **Feasibility verdict:** **the most feasible and the cheapest**, but also **the least differentiated**. It is a sensible first SKU *only if* blind tests show a clear taste preference over Campa Citrus Kick and Sting.

### 4.3 Coconut (carbonated coconut water)
- **Perishability:** coconut water is highly susceptible to microbial and enzymatic deterioration once exposed (S57). Commercial producers use thermal processing. Non-thermal methods (high-pressure processing at 500 MPa, high-pressure CO₂ plus ultrasound) achieved **only ~25 days to 4 weeks under refrigeration** in published studies (S57). These are not shelf-stable at ambient temperature.
- **Low-acid risk:** coconut water is a relatively low-acid fruit liquid (**measure the pH of the actual supply**). If the finished product's pH is above about 4.6 in a hermetically sealed can, it falls into the low-acid canned-food risk class (*Clostridium botulinum*). That requires either acidification or validated retort sterilisation. This is a **food-safety design decision for a process authority or food technologist, not desk research.**
- **Flavour:** heat treatment changes delicate coconut aroma (S57 notes processing trade-offs). Carbonation and coconut water together is unusual and untested commercially in India as far as this research found.
- **Sugar:** mature coconut water has 1.8–4.4 g sugar/100 ml (S57), lower than many sodas. That is a genuine plus for a "less sugar" story.
- **Positioning conflict:** coconut water signals hydration and naturalness, while caffeine signals stimulation. Adding caffeine makes it a 40%-GST caffeinated beverage. A still, non-caffeinated coconut drink *may* fall into the 5% GST bracket (S13, **CA to confirm**).
- **Feasibility verdict:** **do not launch as an energy (caffeinated) SKU.** Treat it as a separate future "sparkling or still coconut hydration" line, pending (a) process-safety validation, (b) GST classification and (c) consumer interest. It is the costliest and riskiest option in the model.

### 4.4 Can all three share one formulation, process and cost?
**No.** They differ in acidity (lemon low pH, coconut potentially low-acid), heat sensitivity (blueberry and coconut), particulates (blueberry pulp), sugar contribution and likely processing route (simple cold-fill plus pasteurisation, versus hot-fill or tunnel pasteurisation, versus retort or acidification). Each needs its own development, shelf-life study, quote and possibly its own line. MOQs and changeovers are usually per flavour (S42). See `UNIT_ECONOMICS.xlsx`, sheet *Three_Flavour_vs_Staged*.

## 5. Sweetener science: the stevia question

**Founder recollection (unverified):** a competition judge connected with supplying a large coffee chain described stevia problems in long storage and in hot applications. This is **a recollection, not evidence**. The judge is not named, and no claim is made about any coffee chain.

**What published research says:**
| Finding | Source | Relevance |
|---|---|---|
| Steviol glycosides degraded **by up to 70%** in soft drinks stored at 80 °C for 24–72 h; stevioside less stable than Reb A | S50 (2010) | Supports the *direction* of the heat concern. 80 °C is an accelerated condition, not normal storage. |
| Reb A degrades in aged acidic beverages through acid-catalysed pathways; other ingredients (e.g. caramel colour) change degradation by 80–90% | S51 (2022) | Stability is **formulation-specific**. It must be tested in the actual recipe. |
| UV light accelerates Reb A degradation, and citrate buffer increased light sensitivity about 10× vs phosphate | S49 (2017) | Cans (opaque) help; citric acid is the usual acidulant. |
| Reb A activates bitter-taste receptor (TAS2R4) signalling | S53 (2023) | Mechanistic support for the familiar bitter or licorice aftertaste |
| Reb M has a cleaner sweet taste but still a "slight bitter or licorice aftertaste"; similar degradation pathways at pH 2–8 | S52 (2014, industry-authored) | Newer glycosides reduce but do not remove aftertaste |

**Implications:**
1. Stevia is permitted (S66) and can work in cold-filled, canned, acidic drinks, but **stability and taste must be validated in the exact formula** with accelerated (e.g. 35–40 °C) and real-time storage.
2. Hot applications (the judge's point) are irrelevant to a cold canned drink, **except** if PREVOLT uses hot-fill or pasteurisation steps, which apply heat briefly.
3. Blending (e.g. sucralose + acesulfame-K, or stevia + sucralose, or partial sugar) is the industry norm for masking aftertaste. Sting and Charged use sucralose with sugar (S30).
4. **Monk fruit** is not a legal sweetener option in India based on the documents reviewed (S67, S64).

## 6. Questions that cannot be answered without a food technologist and laboratory trials
1. Minimum fruit inclusion that consumers can detect in a blind test, for each flavour.
2. Anthocyanin, colour and flavour retention of Blueberry Blast over 6–12 months at ambient Indian temperatures.
3. Pulp suspension and filling behaviour (foam, fill height, seam integrity) on the co-packer's line.
4. Required thermal process (pasteurisation units) and microbial stability for each SKU; pH and process authority review for coconut.
5. Sweetener blend that meets sensory targets and stays stable.
6. Can liner compatibility and corrosion risk with fruit acids, pulp and chloride (coconut).
7. Carbonation level retention over shelf life.
8. Real cost per can of each formulation at 2k/5k/10k units.

## 7. Recommendation for R&D sequencing
1. **One caffeinated SKU first:** Lemon *or* Blueberry, whichever wins a blind test against Sting and Campa equivalents, built as a natural-flavour plus modest-juice formula rather than heavy pulp.
2. **Run a pulp variant as a lab experiment only** until a shelf-life study shows it survives 6+ months.
3. **Park Coconut** as a separate non-caffeinated hydration concept and revisit after the first SKU's pilot.
4. **No ReSeal in launch costs** (see `RESEAL_STRAP.md`).
