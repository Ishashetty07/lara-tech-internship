import os
import time
import requests
from openai import AzureOpenAI
import openai
from dotenv import load_dotenv

load_dotenv()

# ---------- Azure AI Search ----------
SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_API_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX")

# ---------- Azure OpenAI ----------
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

client = AzureOpenAI(
    api_key=OPENAI_KEY,
    api_version=API_VERSION,
    azure_endpoint=OPENAI_ENDPOINT
)


def search_documents(query):
    url = f"{SEARCH_ENDPOINT}/indexes/{INDEX_NAME}/docs/search?api-version=2023-11-01"

    headers = {
        "Content-Type": "application/json",
        "api-key": SEARCH_KEY
    }

    body = {
        "search": query,
        "top": 5
    }

    response = requests.post(url, headers=headers, json=body)
    results = response.json()

    docs = results.get("value", [])

    content_list = []
    for d in docs:
        if "content" in d and d["content"]:
            content_list.append(d["content"])

    return "\n".join(content_list)


def ask_openai(context, question):

    prompt = f"""
You are an internal employee policy assistant.

Answer ONLY using the information below.
If the answer is not present, say:
"I could not find this information in the policy documents."

Context:
{context}

Question:
{question}
"""

    # retry logic for Azure 429
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=DEPLOYMENT,
                messages=[
                    {"role": "system", "content": "You answer only from provided documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=300   # very important to reduce quota usage
            )

            return response.choices[0].message.content

        except openai.RateLimitError:
            print("\nAzure OpenAI rate limit reached. Waiting 60 seconds and retrying...\n")
            time.sleep(60)

    return "Azure OpenAI is currently busy. Please try again after some time."


def main():
    print("Employee Policy Assistant")
    print("Type 'exit' to stop\n")

    while True:
        question = input("Ask your question: ")

        if question.lower() == "exit":
            break

        docs = search_documents(question)

        if not docs.strip():
            print("No relevant documents found.")
            continue

        answer = ask_openai(docs, question)
        print("\nAnswer:\n", answer)
        print("-" * 50)


if __name__ == "__main__":
    main()

