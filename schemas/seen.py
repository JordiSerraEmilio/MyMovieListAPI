from pydantic import BaseModel
from typing import Optional


class Seen(BaseModel):
    id: Optional[str]
    movie_id: str
    backdrop_path: str
    movie_title: str
