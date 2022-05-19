from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from schemas.genre import Genre
from schemas.review import Review
from schemas.seen import Seen
from schemas.toWatch import ToWatch
from schemas.dropped import Dropped
from typing import List


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    image: str = Field(...)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    salt: str = Field(...)
    isLogged: int = Field(...)
    genres: List[Genre] = Field(...)
    reviews: List[Review] = Field(...)
    seen: List[Seen] = Field(...)
    toWatch: List[ToWatch] = Field(...)
    dropped: List[Dropped] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "image": "https://abogadolaboralistaenmadrid.es/wp-content/uploads/2020/08/user-pic.jpg",
                "name": "Rocky",
                "email": "rockyrocky@example.com",
                "password": "examplepassword",
                "salt": "",
                "isLogged": "0",
                "genres": [
                    {"id": "12345",
                     "name": "Terror"},
                    {"id": "54321",
                     "name": "Comedy"}
                ],
                "reviews": [
                    {"id": "12345",
                     "movie_id": "1",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw",
                     "comment": "Godlike movie!",
                     "score": "9.0"
                     }
                ],
                "seen": [
                    {"id": "12345",
                     "movie_id": "11",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw"
                     }
                ],
                "toWatch": [
                    {"id": "12345",
                     "movie_id": "2",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw",
                     }
                ],
                "dropped": [
                    {"id": "12345",
                     "movie_id": "23",
                     }
                ]
            }
        }


class UpdateUserModel(BaseModel):
    image: str
    name: str
    email: EmailStr
    password: str
    salt: str
    isLogged: int
    genres: List[Genre]
    reviews: List[Review]
    seen: List[Seen]
    toWatch: List[ToWatch]
    dropped: List[Dropped]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1200px-User_icon_2.svg.png",
                "name": "RockyUPDATED",
                "email": "rockyrockyUPDATED@example.com",
                "password": "examplepasswordUPDATED",
                "salt": "",
                "isLogged": "0",
                "genres": [
                    {"id": "12345",
                     "name": "Terror"},
                    {"id": "54321",
                     "name": "Comedy"}
                ],
                "reviews": [
                    {"id": "12345",
                     "movie_id": "1",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw",
                     "comment": "Godlike movie!",
                     "score": "9.0"
                     }
                ],
                "seen": [
                    {"id": "12345",
                     "movie_id": "11",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw"
                     }
                ],
                "toWatch": [
                    {"id": "12345",
                     "movie_id": "2",
                     "backdrop_path": "ni idea",
                     "movie_title": "Saw"
                     }
                ],
                "dropped": [
                    {"id": "12345",
                     "movie_id": "23",
                     }
                ]
            }
        }
