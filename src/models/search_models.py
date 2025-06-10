from typing import List, Optional
from pydantic import BaseModel, Field


class SearchItemResult(BaseModel):
    url: str = Field(description="URL of result item.")
    title: str = Field(description="Title of result item.")
    description: str = Field(description="Description of result item.")


class SearchResult(BaseModel):
    items: Optional[List[SearchItemResult]] = Field(
        default=[], description="Search result items."
    )
