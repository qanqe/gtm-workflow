# GTM Outbound Workflow

An automated outbound sales pipeline that ingests a CSV of leads, scores them against ICP criteria, and outputs a prioritized outreach sequence with personalized first lines.

## What It Does

1. Reads a CSV of leads from `/leads`
2. Scores each lead against configurable ICP criteria
3. Ranks leads by fit (A / B / C tiers)
4. Generates a personalized first line for each lead
5. Writes a prioritized outreach CSV to `/output`

## Project Structure

```
gtm-workflow/
├── leads/              # Drop input CSV files here
├── output/             # Scored and prioritized results appear here
├── agents/             # Workflow logic (scoring, personalization, orchestration)
├── CLAUDE.md           # Project context for Claude Code
└── README.md           # This file
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your leads

Place your lead CSV in the `/leads` folder. Expected columns:

| Column        | Description                        |
|---------------|------------------------------------|
| first_name    | Lead's first name                  |
| last_name     | Lead's last name                   |
| title         | Job title                          |
| company       | Company name                       |
| industry      | Industry vertical                  |
| company_size  | Number of employees                |
| linkedin_url  | LinkedIn profile URL               |
| email         | Work email address                 |

### 3. Run the workflow

```bash
python agents/workflow.py --input leads/your_file.csv --output output/outreach.csv
```

### 4. Review results

Open `output/outreach.csv`. Each row includes the original lead data plus:

| Column         | Description                              |
|----------------|------------------------------------------|
| icp_score      | Numeric fit score (0–100)                |
| icp_tier       | A (best fit) / B / C                     |
| first_line     | Personalized opening line for outreach   |
| outreach_rank  | Final send order (1 = highest priority)  |

## Configuration

ICP scoring rules are defined in `agents/icp_config.json`. Edit the criteria and weights to match your target customer profile before running.
