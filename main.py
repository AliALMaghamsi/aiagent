import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.available_functions import available_functions
from ai_prompt import system_prompt
from functions.call_function import call_function

def ai_agent(client,messages , verbose):
    
    

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = messages,
        config= types.GenerateContentConfig(tools=[available_functions],system_instruction = system_prompt),
    )

    if response.candidates:
        for cand in response.candidates:
            messages.append(cand.content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("")
        
    

    if not response.function_calls:
       return response.text
    
    function_responses= []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part,verbose)
        if (not function_call_result.parts or not function_call_result.parts[0].function_response):
            raise Exception ("Empty functions call results")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    messages.append(types.Content(role="user",parts=function_responses))
    
        

    
    


def main():
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
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

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_text)])
    ]
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    final_response = ""
    for _ in range(20):
        try:
            final_response=ai_agent(client,messages,verbose)
            if final_response:
                print("Final Response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error: {e}")
    
    if not final_response:
        print("Maximumu itrations reached")
        sys.exit(1)

    
    

if __name__ == "__main__":
    main()