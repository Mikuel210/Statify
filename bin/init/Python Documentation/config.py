from json import load
from constants import ENCODING


def get_config(key: str):
    with open("config.json", 'r', encoding=ENCODING) as file:
        json = load(file)

    if key in json:
        return json[key]
    else:
        raise ValueError("Key wasn't found in the configuration dictionary.")