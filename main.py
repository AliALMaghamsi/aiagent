import os
import sys
from dotenv import load_dotenv
from google import genai
def ai_agent(content):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = content
    )

    print(f"Response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


def main():
    if len(sys.argv)<2:
        print("no prompt added to parse.")
        sys.exit(1)
    
    content = sys.argv[1]
    ai_agent(content)


if __name__ == "__main__":
    main()