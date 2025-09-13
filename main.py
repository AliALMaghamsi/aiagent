import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.available_functions import available_functions
from ai_prompt import system_prompt

def ai_agent(user_prompt , verbose):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = messages,
        config= types.GenerateContentConfig(tools=[available_functions],system_instruction = system_prompt),
    )

    if verbose:

        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
       for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
      
    else:
        print(f"Response: {response.text}")

    
    


def main():
    
    
    user_prompt = []

    verbose = "--verbose" in sys.argv
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            continue
        user_prompt.append(arg)

    if not user_prompt:
        print("No prompt parsed ")
        print("\nUsage: python main.py 'prompt here' [--verbose]")
        print("\nExample: python main.py 'why we still here ?' ")
        sys.exit(1)
    user_text = " ".join(user_prompt)
    
    
    ai_agent(user_text,verbose)

    
    

if __name__ == "__main__":
    main()

