import os
from pathlib import Path
from config import get_config
from constants import ENCODING
import json

code = Path(get_config("code_directory"))
local_tree = ""

with open("config.json", 'r') as file:
    public_path: str = json.load(file)["public_directory"]

with open("venv_template.py", 'r') as file:
    venv_template = file.read()

def generate_tree(directory):
    global local_tree
    folder_contains_python = False
    temp_tree = ""

    for file_path in directory.iterdir():
        if not file_path.is_file():
            # Recursively check if the subdirectory contains Python files
            subdirectory_contains_python = generate_tree(file_path)

            # Only add the subdirectory if it contains Python files
            if subdirectory_contains_python:
                # Add the folder with a nested <ul> only if it has Python files
                temp_tree += f"<li><strong>{file_path.name}/</strong><ul>"
                temp_tree += generate_tree(file_path)
                temp_tree += "</ul></li>"
                folder_contains_python = True
            continue

        # Check for Python files
        if file_path.suffix == ".py":
            filename = str(file_path).removeprefix(str(code)).removesuffix(".py") + ".html"
            filename = filename.removeprefix("\\").removeprefix("/")
            root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            public = os.path.join(root, public_path)
            path = os.path.join(public, filename)

            temp_tree += f'<li><a href="{path}">{file_path.name}</a></li>'
            folder_contains_python = True

    # Return the tree for this directory, or empty if no Python files were found
    return temp_tree if folder_contains_python else ""



def compile_directory(directory):
    global local_tree
    local_tree += "<ul>"

    for file_path in directory.iterdir():
        if not file_path.is_file():
            local_tree += f"<li><strong>{file_path.name}/</strong></li>"

            compile_directory(file_path)
            continue

        if not file_path.suffix == ".py":
            continue

        with open(file_path, 'r', encoding=ENCODING) as file:
            script_content = file.read()

        filename = str(file_path).removeprefix(str(code)).removesuffix(".py")

        local_tree += f"<li>{file_path.name}</li>"

        statify.compile({
            "input_path": "templates/application.html",
            "output_path": f"public/{filename}.html",
            "venv_template": venv_template,
            "target_input_path": "templates/script.html",
            "script_content": script_content,
            "script_filename": str(file_path)
        })

    local_tree += "</ul>"

with open("tree.json", 'w') as file:
    dictionary = {
        "tree": generate_tree(code)
    }

    file.write(json.dumps(dictionary))

compile_directory(code)
