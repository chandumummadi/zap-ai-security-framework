import argparse
from pathlib import Path
from scanner.zap_scan import run_zap_scan
from parser.parse_report import parse_zap_report
from ai.explain_vulnerabilities import run_ai_enrichment
from ai.generate_html_report import generate_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["baseline", "full"], default="baseline")
    parser.add_argument("--target", required=True, help="Target URL to scan")
    args = parser.parse_args()

    print(f"🚀 Starting ZAP AI security scan in {args.mode} mode on {args.target}")

    # Step 1: Run ZAP
    print("🔍 Step 1: Running ZAP scan...")
    run_zap_scan(mode=args.mode, target=args.target)
    zap_report = Path("output/report.json")
    if not zap_report.exists():
        print("❌ Step 1 Failed: ZAP report not found. Exiting.")
        return
    print("✅ Step 1 Complete: ZAP scan finished")

    # Step 2: Parse report
    print("📄 Step 2: Parsing ZAP JSON report...")
    parsed = parse_zap_report(file_path=zap_report)
    if not parsed:
        print("⚠️ Step 2 Warning: No alerts found in report.")
    print(f"✅ Step 2 Complete: Parsed {len(parsed)} alerts")

    # Step 3: AI explanations
    print("🧠 Step 3: Generating AI explanations...")
    run_ai_enrichment()
    enriched_report = Path("output/enriched_report.json")
    if not enriched_report.exists():
        print("❌ Step 3 Failed: Enriched report not found. Exiting.")
        return
    print("✅ Step 3 Complete: AI explanations added")

    # Step 4: Generate HTML
    print("🖼️ Step 4: Generating HTML report...")
    generate_report()
    final_report = Path("output/final_report.html")
    if not final_report.exists():
        print("❌ Step 4 Failed: HTML report not generated. Exiting.")
        return
    print(f"✅ Step 4 Complete: Report saved to {final_report}")

    print(f"🎉 DONE: Final report available at {final_report}")

if __name__ == "__main__":
    main()
