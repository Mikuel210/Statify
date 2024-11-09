from os import path, unlink, makedirs
import compiler
import context_utilities
from constants import *
from utilities import *

# region Context

context = {}


def get_context_value(key: str):
    return context_utilities.get_context_value(context, key)


def get_context_value_safe(key: str):
    return context_utilities.get_context_value_safe(context, key)


def set_context_value(key: str, value) -> None:
    context_utilities.set_context_value(context, key, value)


# endregion


# region API

def write(input: object) -> None:
    with open(get_context_value(OUTPUT_PATH_KEY), 'a', encoding=ENCODING) as file:
        file.write(str(input))


def compile(new_context: dict, log: bool = True) -> None:
    global context
    previous_context = context.copy()
    context = new_context

    output_path = get_context_value(OUTPUT_PATH_KEY)
    makedirs(path.dirname(output_path), exist_ok=True)

    compiler.main(context, log)

    context = previous_context


def render_partial(new_context: dict) -> None:
    output_path = path.join(TEMP_DIRECTORY, get_temporary_name() + ".html")
    new_context[OUTPUT_PATH_KEY] = output_path

    compile(new_context, False)

    with open(output_path, 'r', encoding=ENCODING) as file:
        write(file.read())

    unlink(new_context[OUTPUT_PATH_KEY])

# endregion
