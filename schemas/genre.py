from pydantic import BaseModel
from typing import Optional


class Genre(BaseModel):
    id: Optional[str]
    name: str

