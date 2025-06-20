import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

INPUT_FILE = Path("reports/enriched_report.json")
TEMPLATE_PATH = Path("templates")
OUTPUT_FILE = Path("reports/final_report.html")

def load_data():
    with open(INPUT_FILE, "r") as f:
        return json.load(f)

def render_html(data):
    env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    template = env.get_template("report_template.html")
    return template.render(vulnerabilities=data)

def save_output(html):
    with open(OUTPUT_FILE, "w") as f:
        f.write(html)
    print(f"✅ Report saved to {OUTPUT_FILE}")

def main():
    data = load_data()
    html = render_html(data)
    save_output(html)

if __name__ == "__main__":
    main()
