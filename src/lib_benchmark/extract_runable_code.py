# Class that accepts a function and library name and returns python code as a string
# It calls the llm_helper.py to get the function code

from common.llm_helper import LLMHelper

class ExtractRunableCode(object):
    def __init__(self, function, lib_name, llm_helper: LLMHelper):
        self.function = function
        self.lib_name = lib_name
        self.code = None

    def extract(self):
        """
        Function that extracts the runable code from the function and returns it as a string
        :param param1: The first parameter.
        :param param2: The second parameter.
        :return: The return value of the function.
        """
        
        
        