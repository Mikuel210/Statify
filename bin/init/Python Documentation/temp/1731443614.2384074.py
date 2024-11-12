
import sys
sys.path.append(r"C:\Users\loran\OneDrive\Escritorio\Escritorio\Python\Statify")

import statify


import statify
statify.context = {'input_path': 'templates/application.html', 'output_path': 'temp/hi.html'}

open(statify.get_context_value("output_path"), 'w').close()


statify.write("<!DOCTYPE html>")
statify.write("<html lang=\"en\">")
statify.write("<head>")
statify.write("<meta charset=\"UTF-8\">")
statify.write("<title>Title</title>")
statify.write("</head>")
statify.write("<body>")
statify.write("")
statify.write("")


print("hi")


statify.write("")
statify.write("")
statify.write("</body>")
statify.write("</html>")

