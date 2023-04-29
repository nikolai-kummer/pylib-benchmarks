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
    def __init__(self, api_key: str, model: str="gpt-3.5-turbo", temperature: float=0.0):
        openai.api_key = api_key
        self.model = model
        self.temperature = temperature

    def get_prompt_completion(self, prompt: str):
        message = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = message,
            temperature=self.temperature)
        return response.choices[0].message["content"]
        

    def connect(self):
        # no need to connect to ChatGPT, just initializing the API key is sufficient
        pass

    def disconnect(self):
        # no need to disconnect from ChatGPT, just releasing the API key is sufficient
        openai.api_key = None

    def run_query(self, query: str):
        # using OpenAI's GPT-3 to generate a response to the query
        return self.get_prompt_completion(query)
