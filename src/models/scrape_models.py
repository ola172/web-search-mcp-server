from typing import Optional
from pydantic import BaseModel, Field

from src.models.search_models import SearchItemResult


class ScrapeQuery(SearchItemResult):
    pass


class ScrapeResult(BaseModel):
    url: str = Field(description="URL.")
    content: Optional[str] = Field("", description="URL content.")
    title: str = Field(description="Title of result item.")
    description: str = Field(description="Description of result item.")
