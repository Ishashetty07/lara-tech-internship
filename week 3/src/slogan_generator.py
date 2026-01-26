import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Get project root directory (Marketing-Slogan-Generator)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute paths for prompt files
PROMPT_FILES = {
    "professional": os.path.join(BASE_DIR, "prompts", "professional.txt"),
    "friendly": os.path.join(BASE_DIR, "prompts", "friendly.txt"),
    "bold": os.path.join(BASE_DIR, "prompts", "bold.txt"),
}


def load_prompt(tone, product, audience):
    """Load and format prompt template based on tone"""
    with open(PROMPT_FILES[tone], "r", encoding="utf-8") as file:
        prompt = file.read()
    return prompt.format(product=product, audience=audience)


def generate_slogan(prompt):
    """Generate slogan using Azure OpenAI"""
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    return response.choices[0].message.content


def main():
    print("Available tones:", ", ".join(PROMPT_FILES.keys()))
    tone = input("Select tone: ").lower()

    if tone not in PROMPT_FILES:
        print("Invalid tone selected.")
        return

    product_name = "Smart Fitness Watch"
    target_audience = "Young professionals"

    prompt = load_prompt(tone, product_name, target_audience)
    slogan = generate_slogan(prompt)

    print("\nGenerated Slogan:")
    print(slogan)

if __name__ == "__main__":
    main()

