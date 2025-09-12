import os
from functions.config import MAX_CHARS


def get_file_content(working_directory, file_path):
        abs_wrk_dir = os.path.abspath(working_directory)
        abs_path = os.path.abspath(os.path.join(working_directory,file_path))
        
        
        
        if not abs_path.startswith(abs_wrk_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        try:
             
            with open(abs_path,"r") as f:
                
                file_content = f.read()
                
                
                if len(file_content) > MAX_CHARS:
                    content_tranc = file_content[:MAX_CHARS]
                    
                    content_tranc += f'[...File "{file_path}" truncated at 10000 characters]'
                    return content_tranc
                
                return file_content

        except Exception as e:
            return f"Error: {e}"