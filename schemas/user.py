from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from schemas.genre import Genre
from schemas.review import Review
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
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    salt: str = Field(...)
    genres: List[Genre] = Field(...)
    reviews: List[Review] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Rocky",
                "email": "rockyrocky@example.com",
                "password": "examplepassword",
                "salt": "",
                "genres": [
                    {"id": "12345",
                     "name": "Terror"},
                    {"id": "54321",
                     "name": "Comedy"}
                ],
                "reviews": [
                    {"id": "12345",
                     "movie_title": "Saw",
                     "comment": "Godlike movie!",
                     "score": "9.0"
                     }
                ]
            }
        }
