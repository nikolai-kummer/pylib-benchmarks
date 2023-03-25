import json
import numpy as np

# Get a list of all NumPy function names
np_functions = [func for func in dir(np) if callable(getattr(np, func)) and not func.startswith("__")]

# Write the list of NumPy function names to a JSON file
with open('numpy_functions.json', 'w') as outfile:
    json.dump(np_functions, outfile)
