import os

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)

    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(path)

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    files_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        files_list.append(f"{file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")

    return f'Results for "{directory if directory != "." else "current"}" directory:\n'+'\n'.join(files_list)
