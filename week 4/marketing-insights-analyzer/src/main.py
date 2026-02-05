import os
import json
import time
import pandas as pd
from dotenv import load_dotenv
from openai import AzureOpenAI


# -----------------------------
# Load environment
# -----------------------------
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")


# -----------------------------
# Load feedback
# -----------------------------
def load_feedback(path):
    df = pd.read_csv(path)
    return df["feedback"].dropna().tolist()


# -----------------------------
# Azure OpenAI insight extractor
# -----------------------------
def extract_with_llm(feedback_list):

    prompt = f"""
You are a marketing analyst.

From the following customer feedback, extract:

1. key_themes (list)
2. sentiment_summary (one of: Positive, Negative, Mixed)
3. common_complaints (list of short phrases)
4. improvement_suggestions (list of short phrases)

Return ONLY valid JSON in this format:

{{
  "key_themes": [],
  "sentiment_summary": "",
  "common_complaints": [],
  "improvement_suggestions": []
}}

Feedback:
{json.dumps(feedback_list, indent=2)}
"""

    start = time.time()

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a helpful marketing analytics assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    duration = time.time() - start

    content = response.choices[0].message.content

    tokens = response.usage.total_tokens

    return content, duration, tokens


# -----------------------------
# Rule-based baseline
# -----------------------------
def baseline_insights(feedback_list):

    themes = set()
    complaints = []
    improvements = []

    negative_words = ["slow", "confusing", "hard", "high", "bad", "poor", "delay"]
    positive_words = ["love", "good", "great", "helpful", "excellent"]

    pos_count = 0
    neg_count = 0

    for f in feedback_list:
        text = f.lower()

        if "price" in text:
            themes.add("Pricing")

        if "checkout" in text or "navigate" in text or "website" in text:
            themes.add("Website usability")

        if "shipping" in text or "delivery" in text:
            themes.add("Shipping")

        if "customer service" in text or "support" in text:
            themes.add("Customer service")

        for w in negative_words:
            if w in text:
                neg_count += 1
                complaints.append(f)
                break

        for w in positive_words:
            if w in text:
                pos_count += 1
                break

        if "wish" in text or "should" in text or "need" in text:
            improvements.append(f)

    if pos_count > 0 and neg_count > 0:
        sentiment = "Mixed"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Positive"

    return {
        "key_themes": list(themes),
        "sentiment_summary": sentiment,
        "common_complaints": complaints,
        "improvement_suggestions": improvements
    }


# -----------------------------
# Consistency score
# -----------------------------
def theme_overlap(llm_themes, base_themes):

    s1 = set([t.lower() for t in llm_themes])
    s2 = set([t.lower() for t in base_themes])

    if not s1 and not s2:
        return 1.0

    return len(s1 & s2) / max(len(s1), len(s2))


# -----------------------------
# Main
# -----------------------------
def main():

    feedback = load_feedback("sample_feedback.csv")

    print("\n--- Running Azure OpenAI ---")

    llm_raw, llm_time, tokens = extract_with_llm(feedback)

    try:
        llm_result = json.loads(llm_raw)
    except Exception:
        print("Model did not return valid JSON:")
        print(llm_raw)
        return

    print("\n--- Running baseline ---")

    start = time.time()
    baseline_result = baseline_insights(feedback)
    base_time = time.time() - start

    overlap = theme_overlap(
        llm_result["key_themes"],
        baseline_result["key_themes"]
    )

    print("\n================ AI RESULT ================\n")
    print(json.dumps(llm_result, indent=2))

    print("\n================ BASELINE RESULT ================\n")
    print(json.dumps(baseline_result, indent=2))

    print("\n================ COMPARISON ================\n")

    comparison = {
        "llm_time_seconds": round(llm_time, 3),
        "baseline_time_seconds": round(base_time, 5),
        "token_usage_cost_proxy": tokens,
        "llm_theme_count": len(llm_result["key_themes"]),
        "baseline_theme_count": len(baseline_result["key_themes"]),
        "theme_consistency_score": round(overlap, 2)
    }

    print(json.dumps(comparison, indent=2))


if __name__ == "__main__":
    main()
