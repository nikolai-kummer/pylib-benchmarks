RUNABLE_CODE_QUERY = """
Act as python developer and be concise and format answer as code only.
Write a minimum working code for the function enclosed triple backticks from the library enclosed in tripple dashes.
You will be penalized for any variable that is defined but not used.

Function Name: ```{function_name}```
Library Name: ---{library_name}---

Follow the following rules:
1. Add all required imports
2. Define the input array as numpy array1 = [1,2,3,4,5] 
3. If the function requires any constants, then define them as constant1 = 1, constant2 = 2
4. Run the function and store results in a variable named result

Examples:

Function Name: ```all```
Library Name: ---numpy---
Code:
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
result = np.all(array1)

Function Name: ```sin```
Library Name: ---numpy---
Code:
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
result = np.sin(array1)

Function Name: ```{function_name}```
Library Name: ---{library_name}---
Code:
"""