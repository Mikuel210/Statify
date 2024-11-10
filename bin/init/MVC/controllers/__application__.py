# Allow to import local modules
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import get_config

partials_path = get_config("partials_path")


def application_render_page() -> None:
    context = statify.context.copy()
    context["input_path"] = context["controller_input_path"]
    context["venv_template"] = context["target_venv_template"]

    statify.render_partial(context)

def controller_render_page() -> None:
    context = statify.context.copy()
    context["input_path"] = context["target_input_path"]

    statify.render_partial(context)


def render_partial(name: str, context: dict = {}) -> None:
    context["input_path"] = f"{partials_path}/{name}.html"
    statify.render_partial(context)