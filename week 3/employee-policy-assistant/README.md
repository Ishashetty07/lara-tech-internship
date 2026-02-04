# 🏢 Employee Policy Assistant (RAG using Azure AI)

A simple command-line based Retrieval-Augmented Generation (RAG) application that allows employees to ask questions about internal company policy documents and get answers strictly from those documents using Azure AI Search and Azure OpenAI.

This project is created as part of an internship assignment under the Agentic AI Bootcamp.

---

## 🚀 Features

- Ask questions about internal employee policy documents
- Retrieves relevant content from Azure AI Search
- Generates answers using Azure OpenAI
- Answers are grounded only in indexed documents
- If information is not found, the assistant clearly says so

---

## 🛠️ Tech Stack

- Python
- Azure AI Search
- Azure OpenAI
- Azure Blob Storage
- REST API

---

## 📁 Project Structure

```
employee-policy-assistant/
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env   (not committed)
```

---

## 🌐 Azure Services Used

- Azure Blob Storage – stores policy PDF files
- Azure AI Search – indexes and searches document content
- Azure OpenAI – generates final answers

---

## 📄 Prerequisites

- Policy documents must be uploaded to Azure Blob Storage
- Azure AI Search index must be created and indexed
- The search index must contain a field named:

```
content
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
AZURE_SEARCH_ENDPOINT=https://<your-search-service>.search.windows.net
AZURE_SEARCH_API_KEY=<your-search-admin-key>
AZURE_SEARCH_INDEX=docqna-index

AZURE_OPENAI_ENDPOINT=https://<your-openai-resource>.openai.azure.com
AZURE_OPENAI_KEY=<your-azure-openai-key>
AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

⚠️ Do NOT commit the `.env` file to GitHub.

---

## ▶️ How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python main.py
```

---

## 🧪 Example Questions

- What are the working hours?
- What is the leave policy?
- Is remote work allowed?
- What is the attendance policy?

---

## 🧠 How It Works

1. User enters a question.
2. The app queries Azure AI Search.
3. Relevant document text is retrieved from the index.
4. The retrieved content is passed to Azure OpenAI.
5. Azure OpenAI generates an answer only from the provided context.

---

## 🔒 Grounded Answer Rule

If the answer is not present in the documents, the assistant responds with:

```
I could not find this information in the policy documents.
```

---

## 👤 Author

Isha Shetty  
Intern – Agentic AI Bootcamp  
GitHub: https://github.com/Ishashetty07
