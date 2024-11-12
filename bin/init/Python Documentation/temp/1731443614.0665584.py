
import sys
sys.path.append(r"C:\Users\loran\OneDrive\Escritorio\Escritorio\Python\Statify")

import statify

import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), ".."))

from pathlib import Path
from config import get_config
"""
code = Path(get_config("code_directory"))

for file in code.iterdir():
    if not file.is_file():
        continue

    if not file.suffix == ".py":
        continue

    statify.compile({
        "input_path": "templates/script.html",
        "output_path": f"public/{file.stem}.html"
    })
"""


statify.compile({
    "input_path": "templates/application.html",
    "output_path": "temp/hi.html"
})