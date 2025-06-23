
# 🔐 ZAP AI Security Framework

## 🚀 Project Overview

**ZAP AI Security Framework** is an automated, developer-friendly security testing toolkit designed to integrate directly into the software development lifecycle (SDLC). Built on top of the OWASP ZAP (Zed Attack Proxy) scanner and enhanced by GPT-powered explanations, this framework enables **continuous security testing**, **plain-English vulnerability reporting**, and **CI/CD integration** — all in a plug-and-play Python project.

It supports both **CLI-based local execution** and **GitHub Actions-based CI pipelines**, making it suitable for security-conscious teams and individual developers alike.

---

## 🎯 Project Goals

- ✅ Automate Dynamic Application Security Testing (DAST) using OWASP ZAP  
- ✅ Explain vulnerabilities in plain English using OpenAI GPT-3.5/4  
- ✅ Generate clean HTML reports that are developer-readable  
- ✅ Integrate seamlessly into CI/CD pipelines  
- ✅ Provide a CLI-driven interface for on-demand scanning  
- ✅ Encourage developers to fix issues early, enforcing secure-by-default workflows  


## 🧱 System Architecture

```
            ┌────────────────────────────┐
            │  User (CLI / GitHub PR)    │
            └────────────┬───────────────┘
                         │
           ┌────────────▼────────────┐
           │  Run ZAP Scan (Docker)  │
           └────────────┬────────────┘
                         │
     ┌──────────────────▼─────────────────────┐
     │     Parse Raw ZAP JSON Vulnerabilities │
     └──────────────────┬─────────────────────┘
                        ▼
     ┌────────────────────────────────────────┐
     │  Use GPT to Explain Each Vulnerability │
     └──────────────────┬─────────────────────┘
                        ▼
      ┌────────────────────────────────────┐
      │   Generate Final HTML AI Report    │
      └────────────────┬───────────────────┘
                       ▼
  📨 Upload to CI Logs / 📄 Save Locally / ❌ Fail PR
```



---

## 🔍 Key Features

### ✅ CLI-Based Scanning

Run this tool manually via:

```bash
python security-scan/main.py --mode baseline --target https://your-app.com
````

* Supports both `baseline` and `full` ZAP scans
* Automatically saves raw, parsed, enriched, and HTML reports under `/output/`

---

### 🤖 AI-Powered Vulnerability Explanation

Each finding from ZAP is:

* Parsed for essential details (name, risk, URL, solution, CWE, etc.)
* Sent to GPT-3.5/4 for a natural language explanation:

  * What does it mean?
  * Why is it risky?
  * How can developers fix it?

---

### 🖼️ HTML Report Generation

* Converts AI-enriched JSON to a polished `final_report.html`
* Great for sharing with teammates, product owners, or for documentation
* *(Coming soon: severity filters, grouping, remediation links)*

---

### 🔁 GitHub Actions Integration

This project includes a **ready-to-use workflow** in `.github/workflows/zap-scan.yml` that:

* Triggers on **every pull request**
* Runs ZAP in Docker
* Parses and explains results using GPT
* Uploads an HTML report as an artifact
* (Optional) Comments on the PR and fails the build if `High` severity risks exist

---

## 📁 Project Folder Structure

```
zap-ai-security-framework/
├── .github/workflows/zap-scan.yml     # GitHub Actions integration
├── output/                            # All report outputs
│   ├── report.json, parsed_report.json, enriched_report.json, final_report.html
├── security-scan/
│   ├── main.py                        # CLI entry point
│   ├── ai/
│   │   ├── explain_vulnerabilities.py
│   │   └── generate_html_report.py
│   ├── parser/
│   │   └── parse_report.py
│   ├── scanner/
│   │   └── zap_scan.py
│   └── templates/
│       └── report_template.html
├── requirements.txt
└── README.md
├── src/                               # target application code in CI/CD
```

---

## 🛠️ Technologies Used

* **Python 3.10**
* **OWASP ZAP (Docker)**
* **OpenAI Python SDK (v1.88)**
* **Jinja2**
* **GitHub Actions**
* **dotenv, tqdm, argparse**

---

## 🧪 How to Use

### 🧷 Prerequisites

* Docker must be installed and running
* Python 3.10+
* OpenAI API Key in `.env` file:

```env
OPENAI_API_KEY=your_key_here
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🚀 Run the Scan Locally

```bash
python security-scan/main.py --mode baseline --target https://example.com
```

Check results in:

* `output/final_report.html`
* `output/enriched_report.json`

---

## 💡 Future Improvements

* [ ] Add login/auth support via ZAP context files
* [ ] Add Slack/email notifications
* [ ] Group findings by severity
* [ ] Auto-open report in browser after scan
* [ ] Export report in PDF

---

## 📬 Feedback & Contributions

Pull requests, issues, and suggestions are welcome! Feel free to fork and improve this framework to suit your team’s needs.

---


