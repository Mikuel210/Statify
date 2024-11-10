from os import path, listdir

init = path.abspath(path.join(path.dirname(__file__), f"./init/"))

print("Available templates: \n - ", end="")

templates = [name for name in listdir(init) if name != "__default__"]
print(*templates, sep="\n - ")
