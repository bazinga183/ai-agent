import os

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