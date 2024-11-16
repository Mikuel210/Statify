# Allow to import local modules
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from constants import ENCODING
from pathlib import Path
from config import get_config

# Get application view and controler
APPLICATION_VIEW_PATH = "views/__application__.html"
APPLICATION_CONTROLLER_PATH = "controllers/__application__.py"

application_controller_template = ""

try:
    with open(APPLICATION_CONTROLLER_PATH, 'r', encoding=ENCODING) as file:
        application_controller_template = file.read()
except:
    pass

# Get paths
controllers_path = get_config("controllers_path")
views_path = get_config("views_path")
public_path = get_config("public_path")
partials_path = get_config("partials_path")

controllers = Path(controllers_path)
views = Path(views_path)

# Compile views
for controller in views.iterdir():
    if not controller.is_dir():
        continue

    controller_template = ""

    try:
        with open(f"{controllers_path}/{controller.name}.py", 'r', encoding=ENCODING) as file:
            controller_template = file.read()
    except:
        pass

    for view in controller.iterdir():
        if not view.is_file():
            continue

        venv_template = f"{application_controller_template}\n{controller_template}"

        statify.compile({
            "input_path": APPLICATION_VIEW_PATH,
            "output_path": f"{public_path}/{controller.name}/{view.name}",
            "venv_template": application_controller_template,
            "controller_input_path": f"{views_path}/{controller.name}.html",
            "target_input_path": str(view),
            "target_venv_template": venv_template
        })

# Add entry point
entry_point = get_config("entry_point")

statify.compile({
    "input_path": f"{partials_path}/redirect.html",
    "output_path": f"{public_path}/index.html",
    "url": entry_point
})