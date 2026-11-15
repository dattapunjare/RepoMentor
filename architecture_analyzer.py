
import ast


def analyze_python_file(code):
    """
    Analyze Python source code and extract
    imports, functions and classes.
    """

    try:
        tree = ast.parse(code)

        analysis = {
            "imports": [],
            "functions": [],
            "classes": []
        }

        for node in ast.walk(tree):

            # Detect imports
            if isinstance(node, ast.Import):
                for name in node.names:
                    analysis["imports"].append(name.name)

            elif isinstance(node, ast.ImportFrom):
                analysis["imports"].append(
                    node.module or "unknown"
                )

            # Detect functions
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                analysis["functions"].append(node.name)

            # Detect classes
            elif isinstance(node, ast.ClassDef):
                analysis["classes"].append(node.name)

        return analysis

    except SyntaxError as error:
        return {
            "error": f"Could not parse Python code: {error}"
        }
