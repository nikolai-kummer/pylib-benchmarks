# Function that takes in a query and an llm_helper object
# The function has a query variable called ALTERTNATE_RUNABLE_CODE_QUERY
# The function assigns the input query into the query variable called runable_code_query

ALTERTNATE_RUNABLE_CODE_QUERY = """
Act as a python developer. Be concise and provide only code and no explanation. 
Write code that performs the exact same action but with a different python libary for the following code:
{runable_code_query}
Add comments above the code labelling the library: example: numpy.fft.fft -> numpy
Add comments above labelling the path to function: example: numpy.fft.fft -> fft.fft
The function must only be called once. 
If an array is needed for the function, label it as array1. 
If more than one array is needed then increment the count. 
If a constant is needed, then label it constant 1. 
If more than one constant is needed, increment the count.
"""


class AlternateRunableCode(object):
    def __init__(self,llm_helper):
        self.llm_helper = llm_helper

    def get_alternate_runable_code(self, query:str) -> str:
        """
        Function that extracts the runable code from the function and returns it as a string
        :param param1: The first parameter.
        :param param2: The second parameter.
        :return: The return value of the function.
        """
        try:
            run_query = ALTERTNATE_RUNABLE_CODE_QUERY.format(runable_code_query=query)
            result = self.llm_helper.run_query(run_query)
        except:
            Exception("Error running query")
            return ""

        return result