from typing import Optional

from src.core.factory.analyzer_facrory import AnalyzerFactory
from src.core.factory.scraper_factory import ScraperFactory
from src.core.factory.searcher_factory import SearcherFactory
from src.core.types import AnalyzerType, ScraperType, SearcherType
from src.models.analyzer_models import AnalyzerResult
from src.utils.url_validator import validate_urls

searcher = SearcherFactory.initialize_searcher(
    searcher_type=SearcherType.OPEN_GOOGLE_SEARCH
)
scraper = ScraperFactory.initialize_scraper(ScraperType.TRAFILATURA_SCRAPER)
analyzer = AnalyzerFactory.initialize_analyzer(AnalyzerType.OPENAI_ANALYZER)


def search_custom_sites(query: str, sites: Optional[list] = None) -> AnalyzerResult:
    """
    Performs a custom site search, scrapes the resulting URLs, and analyzes the content.
    Args:
        query (str): The search query string. Must not be empty.
        sites (Optional[list], optional): A list of site URLs to restrict the search to. Defaults to None.
    Returns:
        AnalyzerResult: The analyzed result of the scraped search results.
    Raises:
        ValueError: If the query is empty.
        Exception: Propagates any exception raised during validation, searching, scraping, or analysis.
    """

    try:
        # 1. Validate search parameters
        if not query or query.strip() == "":
            raise ValueError("Query can't be empty.")

        validate_urls(urls=sites)

        # 2. Run initial search
        searcher_result = searcher.search_custom_sites(query=query, sites=sites)

        # 3. Scrape search result
        scrape_result = []
        for item in searcher_result.items:
            url_scrape_result = scraper.get_url_content(url_parameters=item)
            scrape_result.append(url_scrape_result)

        # 4. Analyze search result
        final_result = analyzer.analyze_search_result(
            query=query, search_results=scrape_result
        )

        return final_result
    except Exception as e:
        raise e
