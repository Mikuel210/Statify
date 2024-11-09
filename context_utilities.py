from constants import *

default_context = {}


def get_context_value(context: dict, key: str):
    if key in context:
        return context[key]
    elif key in default_context:
        return default_context[key]
    else:
        raise ValueError("Key wasn't found in the context dictionary.")


def get_context_value_safe(context: dict, key: str):
    try:
        return get_context_value(context, key)
    except ValueError:
        return None


def set_context_value(context: dict, key: str, value) -> None:
    context[key] = value
