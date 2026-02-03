from openai import AzureOpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# -------------------------------------------------
# NOTE:
# The menu and conversation loop are included only
# to demonstrate reusable prompt templates and
# parameterized prompt usage.
# Assignment focus remains on prompt engineering.
# -------------------------------------------------

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

if not AZURE_OPENAI_API_KEY:
    raise ValueError("AZURE_OPENAI_API_KEY not loaded")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# Load prompt from file
def load_prompt(prompt_filename):
    prompt_path = Path(__file__).resolve().parents[1] / "prompts" / prompt_filename
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()

# Conversation handler
def start_conversation(prompt_file, base_variables):
    system_prompt = load_prompt(prompt_file).format(**base_variables)

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    print("\nType 'exit' to end the conversation.\n")

    while True:
        user_input = input("Customer: ").strip()

        if user_input.lower() == "exit":
            print("\nConversation ended.\n")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            temperature=0.4
        )

        assistant_reply = response.choices[0].message.content.strip()

        print("\nSupport:", assistant_reply, "\n")

        messages.append({"role": "assistant", "content": assistant_reply})

# Menu
def main_menu():
    print("\nCustomer Support Response Generator")
    print("1. General Support")
    print("2. Technical Support")
    print("3. Billing Support")

    choice = input("\nSelect an option (1/2/3): ").strip()

    if choice == "1":
        start_conversation(
            "general_support.txt",
            {"product_name": "Smart Fitness Watch"}
        )
    elif choice == "2":
        start_conversation(
            "technical_support.txt",
            {"product_name": "Smart Fitness Watch"}
        )
    elif choice == "3":
        start_conversation(
            "billing_support.txt",
            {"product_name": "Smart Fitness Watch"}
        )
    else:
        print("\nInvalid option. Please restart and select 1, 2, or 3.\n")

# Entry point
if __name__ == "__main__":
    main_menu()


