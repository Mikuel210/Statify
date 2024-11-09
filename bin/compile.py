import os, sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import compiler
from configuration import *
from pathlib import Path
from shutil import rmtree


def main():
    # Get the content of the compile file
    try:
        with open(get_configuration(COMPILE_FILE_KEY), 'r', encoding=ENCODING) as file:
            content = file.read()
    except FileNotFoundError:
        print("The compile file wasn't found. Check your Statify configuration file.")
        return
    except Exception as e:
        print(f"Couldn't open the compile file: \n{e}")
        return

    # Delete contents of temp and public folders
    temp = Path(get_configuration(TEMP_DIRECTORY_KEY))
    public = Path(get_configuration(PUBLIC_DIRECTORY_KEY))

    for file in temp.iterdir():
        # Safety check
        if file.suffix == ".py" or file.suffix == ".html":
            file.unlink()

    for file in public.iterdir():
        try:
            if file.is_file() or file.is_symlink():
                os.unlink(file)
            elif file.is_dir():
                rmtree(file)
        except PermissionError:
            pass

    # Execute the compile file
    compiler.execute_venv(content)


if __name__ == "__main__":
    main()
