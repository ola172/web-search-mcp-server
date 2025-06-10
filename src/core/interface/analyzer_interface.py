from abc import ABC, abstractmethod
from typing import List

from src.models.scrape_models import ScrapeResult
from src.models.analyzer_models import AnalyzerResult


class AnalyzerInterface(ABC):
    @abstractmethod
    def analyze_search_result(
        query: str, search_result: List[ScrapeResult]
    ) -> AnalyzerResult:
        """
        Analyzes the provided search results based on the given query.
        Args:
            query (str): The search query string.
            search_result (List[ScrapeResult]): A list of search results to be analyzed.
        Returns:
            AnalyzerResult: The result of the analysis.
        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError
