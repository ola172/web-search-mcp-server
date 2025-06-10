from src.core.types import SearcherType
from src.searcher.open_google_search import GoogleSearch


class SearcherFactory:
    @staticmethod
    def initialize_searcher(searcher_type: str):
        if searcher_type == SearcherType.OPEN_GOOGLE_SEARCH:
            return GoogleSearch()
        else:
            raise Exception(
                f"Unsupported searcher type please choose from {[searcher_type for searcher_type in SearcherType.__annotations__]}"
            )
