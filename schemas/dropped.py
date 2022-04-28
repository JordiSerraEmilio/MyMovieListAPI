from pydantic import BaseModel
from typing import Optional


class Dropped(BaseModel):
    id: Optional[str]
    movie_id: str
