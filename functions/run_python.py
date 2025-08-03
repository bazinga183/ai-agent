import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(        
            ["python", abs_target] + args,
            timeout=30,
            capture_output=True,
            cwd=working_directory,
            text=True
        )

        if not completed_process.stdout and not completed_process.stderr and completed_process.returncode == 0:
            return 'No output produced'
        
        output = []

        if completed_process.stdout:
            output.append(f'STDOUT: {completed_process.stdout}')
        if completed_process.stderr:
            output.append(f'STDERR: {completed_process.stderr}')
        if completed_process.returncode != 0:
            output.append(f'Process exited with code {completed_process.returncode}')
        
        return '\n'.join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"