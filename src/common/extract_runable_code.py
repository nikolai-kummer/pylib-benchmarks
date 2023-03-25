# Class that accepts a function and library name and returns python code as a string
# It calls the llm_helper.py to get the function code

from .llm_helper import LLMHelper

RUNABLE_CODE_QUERY = """
Act as a python developer. Be concise and provide only code and no explanation. 
Write a sample code for the {function_name} function from the {library_name} python library. 
The function must only be called once. 
If an array is needed for the function, label it as array1. 
If more than one array is needed then increment the count. 
If a constant is needed, then label it constant 1. 
If more than one constant is needed, increment the count.
"""


class ExtractRunableCode(object):
    def __init__(self, function, lib_name, llm_helper: LLMHelper):
        self.function = function
        self.lib_name = lib_name
        self.llm_helper = llm_helper
        self.code = None

    def extract_code(self) -> str:
        """
        Function that extracts the runable code from the function and returns it as a string
        :param param1: The first parameter.
        :param param2: The second parameter.
        :return: The return value of the function.
        """
        try:
            result = self.llm_helper.run_query(RUNABLE_CODE_QUERY.format(function_name=self.function, 
                                                                         library_name=self.lib_name))
        except:
            Exception("Error running query")
            return ""
        
        self.code = result
        return self.code
        
        