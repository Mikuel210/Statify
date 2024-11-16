import ast
import re

def extract_function_summaries(filename, contents):
    tree = ast.parse(contents, filename=filename)

    function_details = []
    param_pattern = re.compile(r":param (\w+): (.+)")
    return_pattern = re.compile(r":return: (.+)")

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            docstring = ast.get_docstring(node)

            if docstring:
                # Extract function summary (first line of the docstring)
                summary = docstring.splitlines()[0]

                # Initialize parameter and return details
                parameters = []
                return_summary = None

                # Go through each line in the docstring to find :param and :return
                for line in docstring.splitlines():
                    param_match = param_pattern.match(line)
                    return_match = return_pattern.match(line)

                    if param_match:
                        param_name = param_match.group(1)
                        param_description = param_match.group(2)
                        parameters.append({"name": param_name, "description": param_description})

                    if return_match:
                        return_summary = return_match.group(1)

                # Add to function details list
                function_details.append({
                    "name": function_name,
                    "summary": summary,
                    "parameters": parameters,
                    "returns": return_summary
                })
            else:
                # Handle case where no docstring is provided
                function_details.append({
                    "name": function_name,
                    "summary": "No summary provided.",
                    "parameters": [],
                    "returns": None
                })

    return function_details