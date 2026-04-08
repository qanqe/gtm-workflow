import csv
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "leads", "leads.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "output", "scored_leads.csv")

SENIOR_TITLES = {"cro", "ceo", "cto", "coo", "cmo", "chief", "founder", "co-founder", "svp", "evp"}
VP_TITLES = {"vp", "vice president"}
DIRECTOR_TITLES = {"director", "head of"}
MANAGER_TITLES = {"manager", "lead"}

TOP_INDUSTRIES = {"proptech", "b2b saas", "saas"}

def score_title(title: str) -> int:
    t = title.lower()
    if any(k in t for k in SENIOR_TITLES):
        return 4
    if any(k in t for k in VP_TITLES):
        return 3
    if any(k in t for k in DIRECTOR_TITLES):
        return 2
    if any(k in t for k in MANAGER_TITLES):
        return 1
    return 0

def score_industry(industry: str) -> int:
    i = industry.lower().strip()
    if i in TOP_INDUSTRIES:
        return 3
    return 0

def score_company_size(size: str) -> int:
    size = size.strip()
    bands = {
        "11-50": 2,
        "51-200": 3,
        "201-500": 3,
        "501-1000": 2,
        "1-10": 1,
        "1001-5000": 1,
        "5001+": 0,
    }
    return bands.get(size, 0)

def compute_icp_score(row: dict) -> int:
    raw = score_title(row["title"]) + score_industry(row["industry"]) + score_company_size(row["company_size"])
    # raw max = 4 + 3 + 3 = 10
    return min(raw, 10)

def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        fieldnames = reader.fieldnames + ["icp_score"]

    for row in rows:
        row["icp_score"] = compute_icp_score(row)

    rows.sort(key=lambda r: r["icp_score"], reverse=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Scored {len(rows)} leads -> {OUTPUT_FILE}")
    for row in rows:
        print(f"  {row['icp_score']:>2}/10  {row['first_name']} {row['last_name']} | {row['title']} @ {row['company']}")

if __name__ == "__main__":
    main()
