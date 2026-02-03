import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def generate_support_response(issue):
    prompt = f"""
    You are a professional customer support agent.
    Write a polite and helpful response for the following issue:

    Issue: {issue}
    """

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    issue = input("Enter customer issue: ")
    reply = generate_support_response(issue)
    print("\nSupport Response:")
    print(reply)
