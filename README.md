# GTM Outbound Workflow

An automated outbound sales pipeline that scores leads against ICP criteria and generates personalized first lines — ready to drop into any email or LinkedIn sequence.

---

## The Problem

Sales teams waste hours manually triaging lead lists — eyeballing titles, guessing company fit, and writing openers from scratch. The result is generic outreach sent to the wrong people in the wrong order.

This workflow fixes that. Drop in a CSV, run one command, get a prioritized list with personalized first lines for every lead.

---

## How It Works

**Step 1 — Score**
Each lead is evaluated across three ICP dimensions: title seniority, industry fit, and company size. Scores are calculated on a 0–10 scale and leads are ranked accordingly.

**Step 2 — Prioritize**
The scored list is sorted highest to lowest, surfacing the best-fit prospects at the top so reps know exactly where to start.

**Step 3 — Personalize**
A signal-aware first line is generated for each lead based on their recent activity — funding rounds, new hires, market expansions, job postings, and more.

---

## How to Run

**1. Add your leads**

Place a CSV file in the `/leads` folder with these columns:

```
first_name, last_name, email, title, company, industry, company_size, city, country, signal
```

**2. Run the pipeline**

```bash
py run_pipeline.py
```

That's it. Both agents run in sequence and results are written to `/output`.

**3. Review output**

| File | Description |
|---|---|
| `output/scored_leads.csv` | All leads with ICP scores, sorted by rank |
| `output/final_leads.csv` | Final output with personalized first lines |

---

## Example Output

```
==================================================
  PIPELINE COMPLETE
==================================================
  Leads processed : 15
  Output file     : output/final_leads.csv

  Top 5 Leads:
  --------------------------------------------
  1. [10/10] Sofia Andersson        Director of Partnerships @ DwellIQ
      Saw DwellIQ is pushing into a new market — that kind of expansion
      usually brings a fresh set of GTM challenges.

  2. [10/10] Ryan Okafor            CRO @ RenterBase
      Saw RenterBase is actively hiring on the sales side — clearly in
      growth mode.

  3. [10/10] Tom Whitfield          CRO @ ClarityHQ
      Congrats on ClarityHQ's recent raise — impressive momentum for the team.
==================================================
```

---

## Project Structure

```
gtm-workflow/
├── leads/                    # Drop input CSV files here
├── output/                   # Scored and prioritized results
│   ├── scored_leads.csv
│   └── final_leads.csv
├── agents/
│   ├── icp_scorer.py         # Scores leads against ICP criteria
│   └── first_line_generator.py  # Generates personalized first lines
├── run_pipeline.py           # Single command to run the full workflow
└── README.md
```

