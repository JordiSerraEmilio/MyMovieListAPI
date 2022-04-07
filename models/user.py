from pydantic import BaseModel
from typing import Optional, List
from schemas.genre import Genre
from schemas.review import Review


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
    password: str
    salt: str
    genres: List[Genre]
    reviews: List[Review]
