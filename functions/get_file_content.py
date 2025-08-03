import os
from config import CHAR_LIMIT
from google.genai import types

def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)

    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(path)

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, 'r') as file:
            file_content = file.read(CHAR_LIMIT)
            if os.path.getsize(abs_target) > CHAR_LIMIT:
                file_content += (
                    f'...[File "{file_path}" truncated at {CHAR_LIMIT} characters]'
                )
        return file_content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets file content in the specified directory along with if they are at or below the character limit, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, get content in the working directory itself.",
            ),
        },
    ),
)