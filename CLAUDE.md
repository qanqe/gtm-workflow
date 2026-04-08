# GTM Outbound Workflow

## Project Overview

This project automates outbound sales outreach by ingesting a CSV of leads, scoring each lead against ICP (Ideal Customer Profile) criteria, and producing a prioritized outreach sequence with personalized first lines.

## Workflow

1. **Input**: CSV file of leads (e.g., name, title, company, industry, company size, LinkedIn URL, etc.)
2. **ICP Scoring**: Each lead is evaluated against configurable ICP criteria and assigned a score
3. **Prioritization**: Leads are ranked by score to focus outreach on the best-fit prospects
4. **Personalization**: A personalized first line is generated for each lead based on their profile
5. **Output**: Prioritized outreach sequence ready for use in email or LinkedIn campaigns

## Key Concepts

- **ICP Criteria**: Configurable rules that define the ideal customer (e.g., industry, company size, job title, tech stack)
- **Lead Score**: A numeric score assigned to each lead based on how well they match the ICP
- **First Line**: A short, personalized opening sentence tailored to each lead to improve reply rates
- **Outreach Sequence**: The ordered list of leads with their scores, tiers, and personalized first lines

## File Structure

```
gtm-workflow/
├── CLAUDE.md           # This file
├── leads.csv           # Input: raw lead list
├── icp_config.json     # ICP scoring rules and weights
├── score_leads.py      # Scores leads against ICP criteria
├── generate_lines.py   # Generates personalized first lines
├── workflow.py         # Orchestrates the full pipeline
└── output/
    └── outreach.csv    # Output: prioritized leads with first lines
```

## Usage

```bash
python workflow.py --input leads.csv --config icp_config.json --output output/outreach.csv
```

## Output Format

The output CSV includes:
- All original lead fields
- `icp_score` — numeric score (0–100)
- `icp_tier` — A / B / C bucket based on score
- `first_line` — personalized opening line for outreach
- `outreach_rank` — final prioritized rank
