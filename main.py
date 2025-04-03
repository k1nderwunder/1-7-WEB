from fastapi import FastAPI
from pydantic import BaseModel
from models import User

app = FastAPI()

@app.post("/user")
def check_user_age(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}