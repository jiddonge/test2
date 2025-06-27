from fastapi import FastAPI
from pydantic import BaseModel
import csv
import os

app = FastAPI()
CSV_FILE = "chat_log.csv"

class ChatLog(BaseModel):
    session_id: str
    사용자유형: str
    선택항목: str
    추천정책: str
    추천날짜: str
    정책최종수정일: str

@app.post("/log")
async def log_data(log: ChatLog):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=log.dict().keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(log.dict())
    return {"message": "Log saved"}
