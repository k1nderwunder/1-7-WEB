from fastapi import FastAPI
from pydantic import BaseModel
from models import User

app = FastAPI()

# Создаем экземпляр пользователя
user = User(name="John Doe", id=1)

@app.get("/users")
def get_user():
    return user

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}