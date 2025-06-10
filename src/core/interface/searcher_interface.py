from abc import ABC, abstractmethod
from typing import List, Optional

from src.models.search_models import SearchResult


class SearchInterface(ABC):
    @abstractmethod
    def search_custom_sites(
        query: str, sites: Optional[List[str]] = None
    ) -> SearchResult:
        """
        Searches for the given query across a list of custom sites.
        Args:
            query (str): The search query string.
            sites (Optional[List[str]], optional): A list of site URLs or identifiers to restrict the search to.
                If None, searches all available custom sites.
        Returns:
            SearchResult: An object containing the search results.
        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """

        raise NotImplementedError

    @abstractmethod
    def search_custom_domains(
        query: str, domains: Optional[List[str]] = None
    ) -> SearchResult:
        """
        Searches for the given query within a specified custom domain.
        Args:
            query (str): The search query string.
            domain (Optional[List[str]], optional): The custom domain to restrict the search to. Defaults to None.
        Returns:
            SearchResult: The result of the search operation.
        Raises:
            NotImplementedError: If the method is not implemented.
        """

        raise NotImplementedError
