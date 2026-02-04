import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")


SYSTEM_PROMPT = """
You are an enterprise customer feedback triage system.

You must classify the feedback using the following fixed schema:

Category: Complaint | Feature Request | Praise | Question
Urgency: Low | Medium | High
SuggestedAction: Respond | Escalate | Forward | Ignore

You must return a JSON object with:
category
urgency
action
reasoning
"""


def triage_with_ai(feedback_text):

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": feedback_text}
        ]
    )

    content = response.choices[0].message.content
    return json.loads(content)
