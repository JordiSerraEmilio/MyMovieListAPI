from pydantic import BaseModel
from typing import Optional


class Review(BaseModel):
    id: Optional[str]
    movie_id: str
    backdrop_path: str
    movie_title: str
    comment: str
    score: float
