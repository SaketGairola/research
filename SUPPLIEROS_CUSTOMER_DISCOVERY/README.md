# SupplierOS customer discovery and lead research (Oct 2026)

Research and drafting only. No one was contacted, no accounts were logged into, and no restricted sources were scraped.

## Files

| File | What it is |
|---|---|
| `leads_master.xlsx` / `leads_master.csv` | **Output A:** 71 leads with scores, sources, pain classification and outreach angle. The XLSX is filterable and colour-coded by priority. |
| `01_top30_outreach_targets.md` | **Output B:** top 30 ranked, the 10 people to contact today, and a personalized opening line for each lead. |
| `02_discovery_playbook.md` | **Output C:** email, LinkedIn, follow-up and paid-pilot templates, the 12-question interview script, how to estimate cost, qualification criteria, pricing hypotheses and cadence. |
| `03_market_findings.md` | **Output D:** the best segment, verified pain, who pays, the best first buyer, adjacent use cases, the evidence against the thesis, and open questions. |
| `00_regulatory_baseline.md` | The 2026 S232, copper, EU melt-and-pour and CBAM changes; the GE Vernova supplier memo; the competitor map with Millproof's $299/month anchor. |
| `build_leads.py` | Source of truth for the lead records and scores. Edit it and run `python3 build_leads.py` to regenerate the CSV and XLSX. |
| `research_log.md` | Raw research notes, kept in the order they were made. |

## Scoring

Pain 25 · trade 20 · decision-maker access 15 · ability to pay 15 · frequency 10 · contactability 10 · MVP fit 5. Priority: P1 ≥ 67, P2 50–66, P3 < 50. Two enterprise EPR leads are capped at P2 because they are learning interviews, not MVP buyers. Every score is broken down by criterion in the CSV.

## Verification standard

- **Names** come from cited public sources. Entries marked "re-verify" come from dated sources.
- **LinkedIn:** not verified for any lead, because LinkedIn wasn't readable from this environment. Confirm each one manually before you message.
- **Email:** only addresses the company published. No pattern-guessed emails.
- **Pain:** "Verified" means the company or its people stated the problem publicly. "Strong inference" means public evidence makes the workflow likely. "Industry fit only" means there is no direct evidence.
