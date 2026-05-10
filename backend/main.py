import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    message: str
    chat_history: list = []

@app.get("/")
def root():
    return {"message": "Urban Feast API is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = run_agent(request.message, request.chat_history)
    return {"response": response}