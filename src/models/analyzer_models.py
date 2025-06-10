from typing import List, Optional
from pydantic import BaseModel, Field


class Citation(BaseModel):
    citation_type: str = Field(description="Citation type.")
    url: str = Field(description="Citation URL.")
    start_index: int = Field(description="Citation start index in response.")
    end_index: int = Field(description="Citation end index in response.")


class AnalyzerResult(BaseModel):
    response_str: str = Field(description="Final response string.")
    citation: Optional[List[Citation]] = Field(
        default=[], description="Final response string."
    )
