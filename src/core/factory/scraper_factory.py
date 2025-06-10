from src.core.types import ScraperType
from src.scraper.trafilatura_scraper import TrafilaturaScraper


class ScraperFactory:
    @staticmethod
    def initialize_scraper(scraper_type: str):
        if scraper_type == ScraperType.TRAFILATURA_SCRAPER:
            return TrafilaturaScraper()
        else:
            raise Exception(
                f"Unsupported scraper type please choose from {[scraper_type for scraper_type in ScraperType.__annotations__]}"
            )
