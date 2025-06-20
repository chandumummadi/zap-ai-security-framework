import argparse
import subprocess
import os

def run_zap_scan(mode: str, target: str):
    if mode not in ["baseline", "full"]:
        raise ValueError("Mode must be 'baseline' or 'full'")

    script = "zap-baseline.py" if mode == "baseline" else "zap-full-scan.py"

    report_json = "report.json"
    report_html = "report.html"

    cmd = [
        "docker", "run",
        "-v", f"{os.getcwd()}:/zap/wrk/:rw",
        "-t", "zaproxy/zap-stable",
        script,
        "-t", target,
        "-J", report_json,
        "-r", report_html
    ]

    print(f"Running ZAP scan in {mode} mode against: {target}")
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["baseline", "full"], default="baseline")
    parser.add_argument("--target", required=True, help="Target URL to scan")
    args = parser.parse_args()

    run_zap_scan(mode=args.mode, target=args.target)

# Dummy
