from src.core.interface.scraper_interface import ScraperInterface
from src.models.scrape_models import ScrapeQuery, ScrapeResult

import trafilatura


class TrafilaturaScraper(ScraperInterface):
    def __init__(self):
        pass

    def get_url_content(self, url_parameters: ScrapeQuery) -> ScrapeResult:
        """
        Fetches and extracts the main textual content from the specified URL using trafilatura.
        Args:
            url_parameters (ScrapeQuery): The URL parameters of the web page to scrape.
        Returns:
            ScrapeResult: An object containing the extracted content from the URL.
        Raises:
            Exception: If an error occurs during fetching or extraction, an exception is raised with a descriptive message.
        """
        try:
            downloaded = trafilatura.fetch_url(url_parameters.url)
            result = trafilatura.extract(downloaded)

            return ScrapeResult(
                content=result,
                url=url_parameters.url,
                title=url_parameters.title,
                description=url_parameters.description,
            )

        except Exception as e:
            raise Exception(f"Error occurred while getting url content: {str(e)}")
