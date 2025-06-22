# Two types of Modules :
# - Built-in modules
# - External modules
# List of built-in modules: https://docs.python.org/3/py-modindex.html

import math #Built-in module
import CustomORMymodule
import os #External modul
import requests #External module

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200 (if the request was successful)

# print(CustomORMymodule.hello())  # Output: Hello from mymodule!
CustomORMymodule.hello()  # Call the function from the custom module



print(math.sqrt(16))  # Output: 4.0