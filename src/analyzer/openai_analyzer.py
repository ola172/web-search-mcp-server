
from typing import List
from openai import OpenAI

from src.core.types import DEFAULT_OPENAI_ANALYZER, DEFAULT_SYSTEM_PROMPT, DEFAULT_USER_PROMPT

from src.models.analyzer_models import AnalyzerResult
from src.models.scrape_models import ScrapeResult

from src.core.interface.analyzer_interface import AnalyzerInterface


class OpenaiAnalyzer(AnalyzerInterface):
    def __init__(self, api_key, model_name = DEFAULT_OPENAI_ANALYZER):
       self.client = OpenAI(api_key=api_key)
       self.model_name = model_name

    def analyze_search_result(self, query: str, search_results: List[ScrapeResult]) -> AnalyzerResult:
        """
        Analyzes the provided search results based on the given query.
        Args:
            query (str): The search query string.
            search_results (List[ScrapeResult]): A list of search results to be analyzed.
        Returns:
            AnalyzerResult: The result of the analysis.
        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        try:
            user_prompt = DEFAULT_USER_PROMPT.replace("query", query).replace("scrape_results", f"{search_results}")
            completion = self.client.beta.chat.completions.parse(model=self.model_name,
                                                                 messages=[
                                                                     {
                                                                         "role": "system",
                                                                         "content": DEFAULT_SYSTEM_PROMPT
                                                                     },
                                                                     {
                                                                         "role": "user",
                                                                         "content": user_prompt
                                                                     }
                                                                 ],
                                                                 response_format=AnalyzerResult)
            response = completion.choices[0].message.parsed
            return response
        except Exception as e:
            raise Exception(f"Error while analyzing search result: {str(e)}")