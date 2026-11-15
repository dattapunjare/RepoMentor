
from architecture_analyzer import analyze_python_file

sample_code = """
import requests

class APIClient:
    def get_data(self):
        return requests.get("https://example.com")

def calculate_total():
    return 100
"""

result = analyze_python_file(sample_code)

print("Architecture Analysis Result:")
print(result)
