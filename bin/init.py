import os.path
import shutil
from os import path, listdir
from sys import argv


def copy_contents(source, destination):
    for item in listdir(source):
        src_path = path.join(source, item)
        dest_path = path.join(destination, item)

        if path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dest_path)


def get_correct_folder_name(parent_dir, target_folder_name):
    target_folder_name = target_folder_name.lower()

    for entry in listdir(parent_dir):
        if path.isdir(os.path.join(parent_dir, entry)) and entry.lower() == target_folder_name:
            return entry

    return None


def main():
    init = path.abspath(path.join(path.dirname(__file__), f"./init/"))

    if len(argv) < 2:
        folder_name = "__default__"
    else:
        folder_name = argv[1]
        folder_name = get_correct_folder_name(init, folder_name)
        
    folder = path.join(init, f"{folder_name}")

    if not path.exists(folder):
        print("Template wasn't found. Available templates: ", end="")

        templates = [name for name in listdir(init) if name != "__default__"]
        print(*templates, sep=", ")

        return

    copy_contents(folder, "./")

    if folder_name == "__default__":
        print("Initialized new Statify project.")
    else:
        print(f"Initialized new Statify project with template: {folder_name}")


if __name__ == "__main__":
    main()
