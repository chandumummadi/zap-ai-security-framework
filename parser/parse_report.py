import json
from pathlib import Path

def parse_zap_report(file_path):
    with open(file_path, "r") as f:
        report = json.load(f)

    alerts = report.get("site", [])[0].get("alerts", [])
    parsed_results = []

    for alert in alerts:
        parsed_results.append({
            "name": alert.get("alert"),
            "risk": alert.get("riskdesc"),
            "url": alert.get("instances", [{}])[0].get("uri"),
            "param": alert.get("instances", [{}])[0].get("param"),
            "description": alert.get("desc"),
            "solution": alert.get("solution"),
            "cwe": alert.get("cweid"),
            "reference": alert.get("reference"),
        })

    return parsed_results

if __name__ == "__main__":
    input_file = Path("report.json")  # or Path("reports/report.json")
    output_file = Path("reports/parsed_report.json")

    results = parse_zap_report(input_file)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Parsed {len(results)} findings into {output_file}")
