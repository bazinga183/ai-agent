import os
from google.genai import types

def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)

    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(path)

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target):
        try:
            os.makedirs(os.path.dirname(abs_target), exist_ok=True)
        except Exception as e:
            return f'Error: creating directory {e}'

    if os.path.exists(abs_target) and os.path.isdir(abs_target):
        return f'Errir: "{file_path}" is a directory, not a file'
    
    try:
        with open(abs_target, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: writing to file: {e}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to write files from, relative to the working directory. If not listed, make the directory and write the file.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is being written into the file."
            )
        },
    ),
)