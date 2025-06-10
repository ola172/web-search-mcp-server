from typing import Optional
from mcp.server.fastmcp import FastMCP

from models.analyzer_models import AnalyzerResult
from src.tools import (
    custom_sites_search_tool,
    custom_domains_search_tool,
    search_on_web_tool,
)

mcp = FastMCP("Custom-Search")


@mcp.tool()
def search_custom_sites(query: str, sites: Optional[list] = None) -> AnalyzerResult:
    """
    Performs a custom sites search, scrapes the resulting URLs, and analyzes the content.
    Args:
        query (str): The search query string. Must not be empty.
        sites (Optional[list], optional): A list of site URLs to restrict the search to. Defaults to None.
    Returns:
        AnalyzerResult: The analyzed result of the scraped search results (Object of `AnalyzerResult`).
    Raises:
        ValueError: If the query is empty.
        Exception: Propagates any exception raised during validation, searching, scraping, or analysis.
    """
    try:
        return custom_sites_search_tool.search_custom_sites(query=query, sites=sites)
    except Exception as e:
        raise e


@mcp.tool()
def search_custom_domains(query: str, domains: Optional[list] = None) -> AnalyzerResult:
    """
    Performs a custom site search, scrapes the resulting URLs, and analyzes the content.
    Args:
        query (str): The search query string. Must not be empty.
        domain (Optional[list], optional): A list of domain strings to restrict the search (e.g., ['edu', 'gov']). Must not be empty.
    Returns:
        AnalyzerResult: The analyzed result of the scraped search results (Object of `AnalyzerResult`).
    Raises:
        ValueError: If the query is empty.
        Exception: Propagates any exception raised during validation, searching, scraping, or analysis.
    """
    try:
        return custom_domains_search_tool.search_custom_domain(
            query=query, domains=domains
        )
    except Exception as e:
        raise e


@mcp.tool()
def search_on_web(query: str) -> AnalyzerResult:
    """
    Performs a general search on web, scrapes the resulting URLs, and analyzes the content.
    Args:
        query (str): The search query string. Must not be empty.
    Returns:
        AnalyzerResult: The analyzed result of the scraped search results (Object of `AnalyzerResult`).
    Raises:
        ValueError: If the query is empty.
        Exception: Propagates any exception raised during validation, searching, scraping, or analysis.
    """
    try:
        return search_on_web_tool.search_on_web(query=query)
    except Exception as e:
        raise e
