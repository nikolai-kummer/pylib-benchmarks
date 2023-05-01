import matplotlib.pyplot as plt
import os

from dotenv import load_dotenv

from common.alternate_runable_code import AlternateRunableCode
from common.extract_runable_code import ExtractRunableCode
from common.llm_protocol import ChatGPT
from common.parse_lib_docs import ParseLibDocs
from common.query_timer import QueryTimer

load_dotenv()

# initialize modules
llm_helper = ChatGPT(os.getenv("OPENAI_API_KEY"))
lib_parser = ParseLibDocs('numpy', 'https://numpy.org/doc/stable/reference')

# parse the lib docs and get a list of functions in the library
function_list = lib_parser.parse()

# Get the sample query
code_extractor = ExtractRunableCode(function_list[1], 'numpy', llm_helper)
query = code_extractor.extract_code()

alternate_query_extractor = AlternateRunableCode(llm_helper)
alternate_query = alternate_query_extractor.get_alternate_runable_code(query)

# Get the query timer object
query_timer = QueryTimer()
original_time = query_timer.time_function(query)
alterante_time = query_timer.time_function(alternate_query)



fig = plt.figure(figsize=(10, 10))
# plot the keys and values on a log scale for original and alternate values
plt.plot(original_time.keys(), original_time.values(), 'r-', label=query)
plt.plot(alterante_time.keys(), alterante_time.values(), 'b-', label=alternate_query)

plt.xscale('log')
plt.yscale('log')
plt.legend()

print("here")