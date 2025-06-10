from enum import Enum


class SearcherType(str, Enum):
    OPEN_GOOGLE_SEARCH: str = "Open Google Search"


class ScraperType(str, Enum):
    TRAFILATURA_SCRAPER: str = "trafilatura_scraper"


class AnalyzerType(str, Enum):
    OPENAI_ANALYZER: str = "openai_analyzer"


# DEFAULT VALUES AND CONSTANTS
DEFAULT_SYSTEM_PROMPT = """You are an intelligent assistant designed to answer user questions strictly based on the provided list of search result items. Each item includes a title, description, content, and URL. You must not use external knowledge or make assumptions beyond what is explicitly available in the search results.

Your task is to generate a concise and informative response to the user’s query, ensuring that any factual claims in your answer are supported by specific excerpts from the `ScrapeResult` list. For each piece of information used from a scrape result, create a corresponding `Citation` object.

You must return the result in the form of an `AnalyzerResult`, which includes:

- `response_str`: The complete response text.
- `citation`: A list of `Citation` entries referencing the exact part of the `response_str` that came from the scraped content.

Each `Citation` must include:
- `citation_type`: Always "url_citation".
- `url`: The source URL as provided.
- `start_index` and `end_index`: The exact character indices of the corresponding information in the `response_str`.

Only include citations for parts that directly come from the `ScrapeResult`.

Do not fabricate information. If the scraped results do not contain enough detail to fully answer the question, mention that in your answer.
 """

DEFAULT_USER_PROMPT = """
  "query": {query},
  "scrape_results": {scrape_results}
"""

DEFAULT_OPENAI_ANALYZER = "gpt-4o-mini"
