import csv
import os
import runpy
import sys

ROOT = os.path.dirname(__file__)
AGENTS = os.path.join(ROOT, "agents")
FINAL_OUTPUT = os.path.join(ROOT, "output", "final_leads.csv")


def run_agent(name: str):
    path = os.path.join(AGENTS, name)
    print(f"\n{'='*50}")
    print(f"  Running {name}")
    print(f"{'='*50}")
    runpy.run_path(path, run_name="__main__")


def print_summary():
    with open(FINAL_OUTPUT, newline="", encoding="utf-8") as f:
        leads = list(csv.DictReader(f))

    total = len(leads)
    top5 = sorted(leads, key=lambda r: int(r["icp_score"]), reverse=True)[:5]

    print(f"\n{'='*50}")
    print(f"  PIPELINE COMPLETE")
    print(f"{'='*50}")
    print(f"  Leads processed : {total}")
    print(f"  Output file     : {FINAL_OUTPUT}")
    print(f"\n  Top 5 Leads:")
    print(f"  {'-'*44}")
    for i, lead in enumerate(top5, 1):
        name = f"{lead['first_name']} {lead['last_name']}"
        print(f"  {i}. [{lead['icp_score']}/10] {name:<22} {lead['title']} @ {lead['company']}")
        print(f"      {lead['first_line']}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    run_agent("icp_scorer.py")
    run_agent("first_line_generator.py")
    print_summary()
