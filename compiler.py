import re
from sys import argv
from pathlib import Path
from os import system, remove, makedirs
from utilities import *
from constants import *
from configuration import *
from context_utilities import *


def main(context: dict, log: bool = True) -> None:
    content = template_to_venv_content(context)

    execute_venv(f"""
import statify
statify.context = {str(context)}

open(statify.get_context_value("{OUTPUT_PATH_KEY}"), 'w').close()

{content}
""")

    if log:
        print("Page compiled: " + Path(context["output_path"]).stem)


def template_to_venv_content(context: dict) -> str:
    input_path: str = get_context_value(context, INPUT_PATH_KEY)
    output = get_venv_template(context)

    with open(input_path, 'r', encoding=ENCODING) as file:
        in_python_block = False

        for line in file:
            parts = re.split(r'(<python>|</python>)', line)

            for part in parts:
                stripped_part = part.strip()

                if stripped_part == "<python>":
                    in_python_block = True
                elif stripped_part == "</python>":
                    in_python_block = False
                else:
                    if in_python_block:
                        output += f"\n{part}\n"
                    else:
                        escaped_html = escape_string(stripped_part)
                        output += f'statify.write("{escaped_html}")\n'

    return output


def execute_venv(content: str) -> None:
    content = f"""
import sys
sys.path.append("{INSTALLATION_PATH}")

import statify

{content}"""

    venv_path: str = path.join(TEMP_DIRECTORY, get_temporary_name()) + ".py"

    makedirs(path.dirname(venv_path), exist_ok=True)
    with open(venv_path, 'w', encoding=ENCODING) as venv_file:
        venv_file.write(content)

    system("python " + venv_path)

    if not get_configuration(DEBUG_KEY):
        remove(venv_path)


def get_venv_template(context: dict) -> str:
    template: str = get_context_value_safe(context, VENV_TEMPLATE_KEY)

    if template is None:
        template = ""

    return template + "\n"


def escape_string(string):
    escaped_string = string.replace('"', '\\"')
    escaped_string = escaped_string.replace("\n", "\\n")

    return escaped_string


if __name__ == "__main__":
    main({
        INPUT_PATH_KEY: argv[1],
        OUTPUT_PATH_KEY: argv[2]
    })
