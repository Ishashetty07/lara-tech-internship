# 📊 Marketing Insights Analyzer

A Python-based backend system that converts raw customer feedback into structured marketing insights using Azure OpenAI, and compares the results against a rule-based baseline approach.

This project is built as part of the Weekend Assignment – Option 1 and focuses on backend AI insight extraction and evaluation without any frontend.

## 🎯 Objective

Build a system that:

- Accepts unstructured customer feedback as input  
- Extracts meaningful marketing insights using Azure OpenAI  
- Identifies key themes, sentiment, common complaints, and improvement suggestions  
- Compares AI-generated insights with a deterministic baseline approach  
- Measures speed, cost proxy, and consistency between both approaches  

## 🧠 Use Case Context

Marketing teams receive large volumes of unstructured customer feedback from:

- Reviews  
- Surveys  
- Social media comments  
- Support tickets  

This system converts noisy feedback into clear and actionable insights for downstream analysis and decision-making.

## 🚀 Features

- Accepts raw customer feedback from a CSV file  
- Insight extraction using Azure OpenAI:
  - Key themes
  - Sentiment summary
  - Common complaints
  - Improvement suggestions
- Rule-based baseline using keyword and heuristic logic  
- Side-by-side comparison between AI and baseline:
  - Execution time
  - Token usage (cost proxy)
  - Number of themes identified
  - Theme consistency score
- Structured JSON output  
- Secure configuration using environment variables  
- Python-only backend (no frontend)

## 🛠️ Tech Stack

- Python 3.10+
- Azure OpenAI
- OpenAI Python SDK
- pandas
- python-dotenv

## 🧩 Project Structure

```
marketing-insights-analyzer/
│
├── src/
│   └── main.py
│
├── sample_feedback.csv
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

## 🔐 Environment Variables

Create a .env file in the project root:

```
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

Important:  
AZURE_OPENAI_DEPLOYMENT must be your Azure OpenAI deployment name, not the model name.

## ▶️ Run the Project Locally

### 1. Create and activate virtual environment

Windows

```
python -m venv venv
venv\Scripts\activate
```

macOS / Linux

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

From the project root:

```
python src/main.py
```

## 📄 Sample Input (sample_feedback.csv)

```
feedback
"The checkout process was confusing and slow."
"I love the product quality, but the price feels high."
"Customer service was helpful and resolved my issue quickly."
"The website is hard to navigate on mobile."
"I wish shipping was faster."
```

## 📊 Example Output (Simplified)

```json
{
  "key_themes": ["Website usability", "Pricing", "Shipping"],
  "sentiment_summary": "Mixed",
  "common_complaints": [
    "The checkout process was confusing and slow.",
    "The website is hard to navigate on mobile."
  ],
  "improvement_suggestions": [
    "I wish shipping was faster."
  ]
}
```

## 🧠 How It Works

1. Customer feedback is loaded from a CSV file  
2. Azure OpenAI extracts structured marketing insights using a prompt  
3. A rule-based baseline processes the same feedback  
4. Results from both approaches are compared  
5. Metrics are generated for execution time, token usage, and theme consistency  

## 📌 Assignment Alignment

- Phase 1 – Azure OpenAI insight extraction  
- Phase 2 – Deterministic baseline logic  
- Phase 3 – Comparison of speed, cost proxy, and consistency  

## 👤 Author

Isha Shetty
