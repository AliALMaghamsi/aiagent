import os 
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_wrk_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory,file_path))
    
    if not abs_path.startswith(abs_wrk_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'


    
    try:
        new_args = ["python3",file_path] + args
        completed_process = subprocess.run(timeout=30, capture_output=True, cwd=abs_wrk_dir, args= new_args , text=True)
        
        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced"
        
        output = []

        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}\n")
        
        return "\n".join(output) if output else "no output produced."

    except Exception as e:
        return f"Error: executing python file: {e}"
        
