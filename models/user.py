from pydantic import BaseModel
from typing import Optional, List
from schemas.genre import Genre
from schemas.review import Review
from schemas.seen import Seen
from schemas.toWatch import ToWatch
from schemas.dropped import Dropped


class User(BaseModel):
    id: Optional[str]
    image: str
    username: str
    email: str
    password: str
    salt: str
    isLogged: int
    genres: List[Genre]
    reviews: List[Review]
    seen: List[Seen]
    toWatch: List[ToWatch]
    dropped: List[Dropped]
