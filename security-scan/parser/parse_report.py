import json
from pathlib import Path

def parse_zap_report(file_path: Path = Path("output/report.json")):
    with open(file_path, "r") as f:
        report = json.load(f)
    # 🔍 DEBUG: Show full structure to inspect what to parse
    print("🔍 Raw ZAP Report JSON Structure:")
    print(json.dumps(report, indent=2))

    # ✅ Defensive parsing in case 'site' or 'alerts' is missing or empty
    sites = report.get("site", [])
    if not sites:
        print("⚠️ No 'site' field found in report.")
        return []

    alerts = sites[0].get("alerts", [])
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

    output_file = Path("output/parsed_report.json")
    with open(output_file, "w") as f:
        json.dump(parsed_results, f, indent=2)

    print(f"✅ Parsed {len(parsed_results)} findings into {output_file}")
    return parsed_results

if __name__ == "__main__":
    parse_zap_report()
