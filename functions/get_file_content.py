import os
from config import CHAR_LIMIT

def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)

    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(path)

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(path, 'r') as file:
        file_content = file.read(CHAR_LIMIT)