from abc import ABC, abstractmethod

from src.models.scrape_models import ScrapeQuery, ScrapeResult


class ScraperInterface(ABC):
    @abstractmethod
    def get_url_content(url_parameters: ScrapeQuery) -> ScrapeResult:
        """
        Fetches the content of the specified URL and returns the result as a ScrapeResult object.
        Args:
            url_parameters (ScrapeQuery): The URL parameters to fetch content from.
        Returns:
            ScrapeResult: An object containing the scraped content and related metadata.
        Raises:
            NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError
