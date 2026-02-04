# 🧾 Customer Feedback Triage System

A Python-based text-to-decision system that automatically classifies and prioritizes customer feedback using Azure OpenAI, and compares the results with a simple rule-based baseline to evaluate decision quality and consistency.

---

## 🎯 Objective

The goal of this project is to build a triage system that can:

- Classify customer feedback into predefined categories
- Assign an urgency level
- Recommend the next action
- Provide reasoning for every decision
- Compare AI-based decisions with a deterministic rule-based system

This project demonstrates how large language models can be used as intelligent decision systems and how their outputs can be evaluated against traditional rule-based logic.

---

## 🚀 Features

### 📌 Feedback classification
- Complaint
- Feature Request
- Praise
- Question

### ⏱️ Urgency levels
- Low
- Medium
- High

### 🧭 Suggested actions
- Respond
- Escalate
- Forward
- Ignore

### 🧠 Reasoning provided for every decision

### ⚖️ Side-by-side comparison
- Azure OpenAI decision
- Rule-based decision

### 📊 Evaluation metrics
- Category match
- Urgency match

---

## 🛠️ Tech Stack

- Python 3.10+
- Azure OpenAI
- OpenAI Python SDK
- pandas
- python-dotenv

---

## 🧩 Project Structure

```
customer-feedback-triage-system/
│
├── src/
│   ├── ai_triage.py
│   ├── rule_triage.py
│   ├── evaluator.py
│   └── main.py
│
├── sample_feedback.csv
├── requirements.txt
├── .env
└── .gitignore
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>
```

Note:  
AZURE_OPENAI_DEPLOYMENT must be the deployment name, not the base model name.

---

## ▶️ How to Run

### 1️⃣ Create and activate a virtual environment

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

---

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

From the project root:
```
python src/main.py
```

---

## 📄 Sample Input (sample_feedback.csv)

```
feedback
The app crashes every time I open settings.
Please add dark mode support.
I really love your service.
How can I change my email address?
```

---

## 📊 Example Output (Simplified)

```
Feedback: The app crashes every time I open settings.

AI Decision:
{
  "category": "Complaint",
  "urgency": "High",
  "action": "Escalate",
  "reasoning": "The issue affects core functionality and requires immediate attention."
}

Rule Decision:
{
  "category": "Complaint",
  "urgency": "High",
  "action": "Escalate",
  "reasoning": "Rule-based keyword matching."
}

Comparison:
{
  "category_match": true,
  "urgency_match": true
}
```

---

## 🧠 How It Works

1. Customer feedback is loaded from a CSV file.
2. Each feedback message is sent to Azure OpenAI, which returns:
   category, urgency, action and reasoning.
3. The same feedback is processed using a simple rule-based logic.
4. Both results are compared.
5. Match metrics highlight the differences in decision quality.

---

## 👤 Author

Isha Shetty  
GitHub: https://github.com/Ishashetty07
