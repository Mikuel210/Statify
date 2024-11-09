from json import load
from constants import ENCODING

COMPILE_FILE_KEY = "compile_file"
TEMP_DIRECTORY_KEY = "temp_directory"
PUBLIC_DIRECTORY_KEY = "public_directory"
DEBUG_KEY = "debug"

default_configuration = {
    COMPILE_FILE_KEY: "./compile_file.py",
    TEMP_DIRECTORY_KEY: "./temp/",
    PUBLIC_DIRECTORY_KEY: "./public/",
    DEBUG_KEY: False
}


def get_configuration(key: str):
    """
    Gets a configuration value by key.

    :param key: The key to get the value for.
    :return: The value.
    """

    json = {}

    configuration_locations = [".statifyconfig", "config/.statifyconfig"]

    for location in configuration_locations:
        try:
            with open(location, 'r', encoding=ENCODING) as file:
                json = load(file)
                break
        except FileNotFoundError:
            pass

    if key in json:
        return json[key]
    elif key in default_configuration:
        return default_configuration[key]
    else:
        raise ValueError("Key wasn't found in the configuration dictionary.")
