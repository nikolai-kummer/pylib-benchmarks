"""
Class that provides helper functions for the LLM. it contains the following functions:
- initialization function that takes in a connection string and initializes the LLM connection
- connect function that connects to the LLM
- disconnecte function that disconnets form the LLM
- run query function that takes in a query and returns the results
"""

# import pyodbc

class LLMHelper(object):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None

    def connect(self):
        # self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def run_query(self, query):
        """
        Function that runs a query and returns the results.
        :param param1: The first parameter.
        :param param2: The second parameter.
        :return: The return value of the function.
        """
        # self.cursor.execute(query)
        return "sample_query outpu"
