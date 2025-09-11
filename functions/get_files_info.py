import os


def get_files_info(working_directory, directory = "."):
   
        abs_wrk_dir = os.path.abspath(working_directory)
        abs_path = os.path.abspath(os.path.join(working_directory,directory))
        
        
        if not abs_path.startswith(abs_wrk_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory'
        
        try:

            dir_info = []
            
            for file in os.listdir(abs_path):
                
                path = os.path.abspath(os.path.join(abs_path,file))
                info = f"-{file}: {os.path.getsize(path)} bytes, is_dir={os.path.isdir(path)}"
                dir_info.append(info)
            
            return "\n".join(dir_info)
        
        except Exception as e:
            return f"Error : {e}"
        
    
   


