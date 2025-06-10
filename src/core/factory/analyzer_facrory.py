import os
from dotenv import load_dotenv

from src.core.types import AnalyzerType
from src.analyzer.openai_analyzer import OpenaiAnalyzer

load_dotenv()  # Loads from .env file


class AnalyzerFactory:
    @staticmethod
    def initialize_analyzer(analyzer_type: str):
        if analyzer_type == AnalyzerType.OPENAI_ANALYZER:
            return OpenaiAnalyzer(api_key=os.getenv("OPENAI_API_KEY"))
        else:
            raise Exception(
                f"Unsupported analyzer type please choose from {[analyzer_type for analyzer_type in AnalyzerType.__annotations__]}"
            )
