from google.genai import types



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read content from the specifed file, constrained to the working directory and if the file path in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to read the content from , relative to the working directory, if not provided or is not in the working directory will give an error",
            ),
        },
        required=["file_path"],
    ),
)


shcema_write_file_content= types.FunctionDeclaration(
    name="write_file_content",
    description="Write content in the specifed file, if the file doesn't exist create it and write content in it , constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to write the content in , relative to the working directory, if not provided or is not in the working directory will create the file and write in it the content",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="the content that will be written in the file_path"
            )
        },
        required=["file_path","content"],
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run the specifed python file, constrained to  working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the python file that will be ran reltive to the working directory if not provided or it wasn't a python file it will give an error.",
            ),
            "args":types.Schema(
                type=types.Type.STRING,
                description="the args that will give to run the python file if not provided the python file will run without them",
            )
        },
        required=["file_path"],
    ),
)
