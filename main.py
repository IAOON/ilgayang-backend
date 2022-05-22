from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Submitted(BaseModel): #제출한 답안
    id: int
    answer: str

@app.post("/judge")
async def judge(req: Submitted):
    # print(id, answer)
    if (req.id == 1 and req.answer == "test"):
        return {"result": True, "message": "correct"}
    else:
        return {"result": False, "message": "incorrect"}

@app.get("/problems/{number}")
async def show(number: int):
    if number == 20220522:
        return {
            "author":"대탈출(문제적 남자)","title": "이어질 숫자","body": "717-721-473-217-(???)에서 ???에 들어갈 3문자 숫자는??","answer": "428"
        }
    if number == 20220523:
        return {
            "author": "AKA",
            "title": "숫자 변환",
            "body": "OhL = 740일때, EEB의 값은?",
            "answer": "833"
        }
    return HTTPException(status_code=404, detail="Question not found")

@app.get("/")
async def root():
    return {"message": "Heroku test"}
