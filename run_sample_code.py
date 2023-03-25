from src.common.llm_helper import LLMHelper
from src.common.parse_lib_docs import ParseLibDocs
from src.common.extract_runable_code import ExtractRunableCode

# initialize modules
llm_helper = LLMHelper('connection_string')
lib_parser = ParseLibDocs('numpy', 'https://numpy.org/doc/stable/reference')

# parse the lib docs and get a list of functions in the library
function_list = lib_parser.parse()

    
code_extractor = ExtractRunableCode(function_list[0], 'numpy', llm_helper)
query = code_extractor.extract_code()
query