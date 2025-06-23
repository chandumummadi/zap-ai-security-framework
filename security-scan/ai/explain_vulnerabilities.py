# from openai import OpenAI

import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm
from openai import OpenAI
from openai._exceptions import RateLimitError, OpenAIError  # ✅ Correct for v1.88.0




load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File paths
INPUT_FILE = Path("output/parsed_report.json")
OUTPUT_FILE = Path("output/enriched_report.json")


# Optional: test mode to avoid using full quota
TEST_MODE = False  # Set to True to test on 2 items only
def build_prompt(alert):
    return f"""
You are a security expert. Given this vulnerability, explain:
1. What it means
2. Why it matters
3. How a developer can fix it (with a code/config example if possible)


Vulnerability:
- Name: {alert['name']}
- Risk: {alert['risk']}
- URL: {alert['url']}
- Description: {alert['description']}
- Suggested Solution: {alert['solution']}
- CWE ID: {alert['cwe']}
"""



def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content
    except RateLimitError as e:
        return f"Rate limit error: {str(e)}"
    except OpenAIError as e:
        return f"OpenAI API error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def run_ai_enrichment():
    with open(INPUT_FILE, "r") as f:
        alerts = json.load(f)

    enriched = []
    for alert in tqdm(alerts, desc="Explaining alerts"):
        prompt = build_prompt(alert)
        explanation = get_ai_response(prompt)
        enriched.append({
            **alert,
            "ai_explanation": explanation
        })

    with open(OUTPUT_FILE, "w") as f:
        json.dump(enriched, f, indent=2)

    print(f"✅ Saved enriched report to: {OUTPUT_FILE}")

if __name__ == "__main__":
    run_ai_enrichment()
