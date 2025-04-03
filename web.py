from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}