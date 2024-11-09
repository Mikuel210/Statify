from json import load
from constants import ENCODING

default_configuration = {
    "controllers_path": "controllers",
    "views_path": "views",
    "public_path": "public"
}


def get_config(key: str):
    json = {}

    with open("config.json", 'r', encoding=ENCODING) as file:
        json = load(file)

    if key in json:
        return json[key]
    elif key in default_configuration:
        return default_configuration[key]
    else:
        raise ValueError("Key wasn't found in the configuration dictionary.")