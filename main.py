import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)
    verbose = 0

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    if sys.argv[-1] == "--verbose":
        user_prompt = " ".join(sys.argv[1:-1])
        verbose = 1
    else:
        user_prompt = " ".join(sys.argv[1:])

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file

        ]
    )

    model = "gemini-2.0-flash-001"
    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],            
            system_instruction=system_prompt)
        )
    
    function_call_part = response.function_calls

    if function_call_part:
        for call in function_call_part:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(response.text)

        
    # if verbose == 1:
    #     print(f"User prompt: {user_prompt}")
    #     print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    #     print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
