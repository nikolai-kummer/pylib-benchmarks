# Module that parses the lib docs and generates a list of functions and returns them
# contains an init class that takes in a string name, and a url

PARSED_LIBS = {'numpy': ['fft.fft', 'random.choice']}

class ParseLibDocs(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.functions = []

    def parse(self):
        """
        Function that parses the lib docs and returns a list of functions
        :param param1: The first parameter.
        :param param2: The second parameter.
        :return: The return value of the function.
        """
        if not self.name in PARSED_LIBS:
            raise NotImplementedError("Library not implemented")
        else:
            self.functions = PARSED_LIBS[self.name]
        return self.functions
