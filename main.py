from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

feedback_storage: List[Feedback] = []

@app.post("/feedback")
async def post_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    response_message = f"Feedback received. Thank you, {feedback.name}!"
    
    return {"message": response_message}

@app.get("/all-feedback")
async def get_all_feedback():
    return feedback_storage