from google.genai import types
from functions.function_declration import schema_get_files_info,schema_get_file_content,shcema_write_file_content,schema_run_python_file



available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            shcema_write_file_content,
            schema_run_python_file,
            
        ]
    )