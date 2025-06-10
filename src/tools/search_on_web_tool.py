from src.core.factory.analyzer_facrory import AnalyzerFactory
from src.core.factory.scraper_factory import ScraperFactory
from src.core.factory.searcher_factory import SearcherFactory
from src.core.types import AnalyzerType, ScraperType, SearcherType
from src.models.analyzer_models import AnalyzerResult

searcher = SearcherFactory.initialize_searcher(
    searcher_type=SearcherType.OPEN_GOOGLE_SEARCH
)
scraper = ScraperFactory.initialize_scraper(ScraperType.TRAFILATURA_SCRAPER)
analyzer = AnalyzerFactory.initialize_analyzer(AnalyzerType.OPENAI_ANALYZER)


def search_on_web(query: str) -> AnalyzerResult:
    """
    Performs a general search on web, scrapes the resulting URLs, and analyzes the search results.
    Args:
        query (str): The search query string. Must not be empty.
    Returns:
        AnalyzerResult: The analyzed result of the search, as returned by the analyzer.
    Raises:
        ValueError: If the query or domains are empty.
        Exception: Propagates any exceptions raised during the search, scraping, or analysis process.
    """
    try:
        # 1. Validate search parameters
        if not query or query.strip() == "":
            raise ValueError("Query can't be empty.")

        # 2. Run initial search
        searcher_result = searcher.search_custom_domains(query=query)

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
