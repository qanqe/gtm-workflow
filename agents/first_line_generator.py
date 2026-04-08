import csv
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "output", "scored_leads.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "output", "final_leads.csv")

# Map signals to sentence templates.
# Each template receives: first_name, company, signal (cleaned), title
SIGNAL_TEMPLATES = {
    "raised series":    "Congrats on {company}'s recent raise — impressive momentum for the team.",
    "raised seed":      "Saw {company} just closed a seed round — exciting stage to be building.",
    "hired new vp":     "Noticed {company} just brought on a new VP of Sales — looks like you're scaling the revenue org.",
    "posted":           "Saw {company} is actively hiring on the sales side — clearly in growth mode.",
    "expanded":         "Saw {company} is pushing into a new market — that kind of expansion usually brings a fresh set of GTM challenges.",
    "attended saastr":  "Fellow SaaStr attendee here — always good to connect with folks in the community.",
    "acquired":         "The recent acquisition by {company} caught my eye — big move.",
    "named to":         "Congrats on {company} making the Gartner Magic Quadrant — well deserved recognition.",
    "launched":         "Saw {company} just launched a new product tier — great timing to be expanding the offering.",
}

FALLBACK_TEMPLATE = "Been following {company}'s growth and wanted to reach out directly."

def build_first_line(row: dict) -> str:
    signal = row.get("signal", "").strip()
    company = row.get("company", "").strip()
    first_name = row.get("first_name", "").strip()

    signal_lower = signal.lower()
    template = FALLBACK_TEMPLATE
    for key, tmpl in SIGNAL_TEMPLATES.items():
        if key in signal_lower:
            template = tmpl
            break

    return template.format(
        first_name=first_name,
        company=company,
        signal=signal,
    )

def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        fieldnames = list(reader.fieldnames) + ["first_line"]

    for row in rows:
        row["first_line"] = build_first_line(row)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated first lines for {len(rows)} leads -> {OUTPUT_FILE}")
    for row in rows:
        print(f"\n  [{row['icp_score']}/10] {row['first_name']} {row['last_name']} @ {row['company']}")
        print(f"  {row['first_line']}")

if __name__ == "__main__":
    main()
