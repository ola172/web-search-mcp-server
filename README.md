# Search Tool

## Overview

**Search Tool** is a modular Python framework for performing advanced web searches, scraping content from search results, and analyzing the retrieved information using AI-powered models. The project is designed for extensibility, allowing easy integration of new search engines, scrapers, and analyzers.

## Features

- **Custom Site Search:** Search within a specified list of websites.  
- **Custom Domain Search:** Restrict searches to specific domains (e.g., `.edu`, `.gov`).  
- **General Web Search:** Perform open web searches.  
- **Content Scraping:** Extracts main textual content from URLs using [trafilatura](https://trafilatura.readthedocs.io/).  
- **AI Analysis:** Summarizes and analyzes scraped content using OpenAI models.  
- **Validation:** Ensures URLs are valid before processing.  
- **Extensible Architecture:** Easily add new searchers, scrapers, or analyzers.

## Project Structure

```
search_tool/
├── src/
│   ├── analyzer/         # AI-powered analyzers (e.g., OpenAI)
│   ├── core/
│   │   ├── factory/      # Factories for searcher, scraper,    
│   │   ├── interface/    # Abstract interfaces for extensibility
│   │   └── types.py      # Enums and constants
│   ├── mcp_servers/      # MCP server integration
│   ├── models/           # Pydantic models for data validation
│   ├── scraper/          # Web scrapers (e.g., Trafilatura)
│   ├── searcher/         # Search engine integrations
│   ├── tools/            # User-facing tool functions
│   └── utils/            # Utility functions (e.g., URL validation)
├── test.py               # Example/test script
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata and dependencies
├── .env                  # Environment variables (e.g., API keys)
└── README.md             # Project documentation
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ola172/web-search-mcp-server.git
   cd search_tool
   ```

2. **Set up a virtual environment (recommended):**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` 
   - Add your secrets:

## Usage

### Core Tools

Each tool validates input, performs the search, scrapes the results, and analyzes the content.

- **General Web Search:** `search_on_web`
- **Custom Sites Search:** `search_custom_sites`
- **Custom Domains Search:** `search_custom_domain`

### MCP Server Integration

The project includes an MCP server (`web_search_server.py`) for exposing search tools as mcp tools.

## Extending the Framework

- **Add a new searcher:** Implement the `SearchInterface` and register it in `SearcherFactory`.  
- **Add a new scraper:** Implement the `ScraperInterface` and register it in `ScraperFactory`.  
- **Add a new analyzer:** Implement the `AnalyzerInterface` and register it in `AnalyzerFactory`.

## Configuration

- **API Keys:** Store sensitive keys (e.g., OpenAI) in the `.env` file.  
- **Search Engine IDs:** For Google Custom Search, configure `API_KEY` and `SEARCH_ENGINE_ID` in the relevant modules.

## Dependencies

- `openai`  
- `trafilatura`  
- `pydantic`  
- `googlesearch-python`  
- `python-dotenv`  
- `google-api-python-client`  

See `requirements.txt` for the full list.

## License

This project is for educational and research purposes. Please ensure compliance with the terms of service of any third-party APIs used.

## Acknowledgements

- OpenAI  
- Trafilatura  
- Google Custom Search  

For questions or contributions, please open an issue or pull request.
