# implement protocol to LLM that contains the following functions:
# - initialization function that takes in a connection string and initializes the LLM connection
# - connect function that connects to the LLM
# - disconnecte function that disconnets form the LLM
# - run query function that takes in a query and returns the results

from typing import Protocol
import openai


class LLMProtocol(Protocol):
    def run_query(self, query: str):
        """Run a query on the LLM and return the results"""

    def connect():
        """Connect to the LLM"""

    def disconnect():
        """Disconnect from the LLM"""

class ChatGPT(LLMProtocol):
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def connect(self):
        # no need to connect to ChatGPT, just initializing the API key is sufficient
        pass

    def disconnect(self):
        # no need to disconnect from ChatGPT, just releasing the API key is sufficient
        openai.api_key = None

    def run_query(self, query: str):
        # using OpenAI's GPT-3 to generate a response to the query
        response = openai.Completion.create(engine="davinci", prompt=query, max_tokens=100)
        return response.choices[0].text.strip()