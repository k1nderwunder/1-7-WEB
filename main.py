from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator
from models import UserCreate

app = FastAPI()

users_storage = []

@app.post("/create_user")
async def create_user(user: UserCreate):
    users_storage.append(user.dict())
    return user

@app.get("/users")
async def get_all_users():
    return users_storage