import asyncio
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body
from pydantic import EmailStr
from starlette import status
from starlette.responses import JSONResponse
from utils import encrypt_things
from schemas.user import UserModel
from config.db import db

user = APIRouter()

db = db


# region GET REQUESTS


# 1 USER
@user.get("/users/{email}", response_model=UserModel)
async def find_user(email: EmailStr):
    _user = await db["users"].find_one({"email": email})
    return _user


# FILTER BY NAME
@user.get("/usersnames/{searchName}", response_model=List[UserModel])
async def find_usernames_like_search(search_name: str):
    # _users es una lista con dicionarios de todos los usuarios
    _users = await db["users"].find().to_list(10)
    # _filtered_users es el dicionario de los usuarios filtrados
    _filtered_users = [d for d in _users if search_name in d['name']]
    return _filtered_users


# ALL USER
@user.get("/users", response_model=List[UserModel])
async def find_all_users():
    _users = await db["users"].find().to_list(1000)
    return _users


# endregion

# region POST REQUESTS


@user.post("/users", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):

    # Crear la salt per l'usuari
    user.salt = encrypt_things.generate_salt()
    print(user.salt)

    # Contrasenya + SALT
    concat_password = user.password.encode() + user.salt
    print(concat_password)

    # Hash del concat_password
    user.password = encrypt_things.convert_to_sha256(concat_password)
    print(user.password)

    _user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(_user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


# endregion
