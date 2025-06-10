from typing import List, Optional
from googlesearch import search

from src.core.interface.searcher_interface import SearchInterface
from src.models.search_models import SearchItemResult, SearchResult


class GoogleSearch(SearchInterface):
    def __init__(self):
        pass

    def search_custom_sites(
        self, query: str, sites: Optional[list] = None
    ) -> SearchResult:
        """
        Performs a Google search restricted to a dynamic list of specific sites.

        Args:
            query (str): The user's search query (e.g., "generative AI").
            sites (list): A list of websites to search within (e.g., ['wired.com', 'theverge.com']).

        Returns:
            SearchResult: The search results from the API, or None if an error occurs.
        """
        try:
            # 1. Construct the dynamic query string
            # Joins the sites with " OR " and formats them with the "site:" operator
            site_restriction = (
                " OR ".join([f"site:{site}" for site in sites]) if sites else ""
            )
            full_query = f"{query} {site_restriction}"

            # 2. Execute the search
            result = search(full_query, num_results=5, advanced=True)

            # 3. Check for returned result
            items = [
                SearchItemResult(
                    url=item.url, title=item.title, description=item.description
                )
                for item in result
            ]

            urls = [item.url for item in items if item.url]
            if not urls:
                return SearchResult(items=[])

            return SearchResult(items=items)

        except Exception as e:
            raise Exception(f"An error occurred while searching in Google: {str(e)}")

    def search_custom_domains(
        self, query: str, domains: Optional[List[str]] = None
    ) -> SearchResult:
        """
        Performs a Google search restricted to a custom domain.

        Args:
            query (str): The user's search query (e.g., "generative AI").
            domain (List[str]): A List od domains of websites to search within (e.g., '.edu').

        Returns:
            SearchResult: The search results from the API, or None if an error occurs.
        """
        try:
            # 1. Construct the dynamic query string
            domain_restriction = (
                " OR ".join([f"site: {domain}" for domain in domains])
                if domains
                else ""
            )
            full_query = f"{query} {domain_restriction}"

            # 2. Execute the search
            result = search(full_query, num_results=3, advanced=True)

            # 3. Check for returned result
            items = [
                SearchItemResult(
                    url=item.url, title=item.title, description=item.description
                )
                for item in result
            ]

            urls = [item.url for item in items if item.url]
            if not urls:
                SearchResult(items=[])

            return SearchResult(items=items)

        except Exception as e:
            raise Exception(f"An error occurred while searching in Google: {str(e)}")
