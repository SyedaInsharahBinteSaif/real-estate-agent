from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import make_outbound_call, get_call_logs
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Real Estate Calling Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Real Estate Agent API is running"}


@app.post("/call")
def initiate_call(data: dict):
    phone = data.get("phone_number")
    name = data.get("customer_name", "")
    
    if not phone:
        return {"error": "Phone number required"}
    
    result = make_outbound_call(phone, name)
    return result


@app.get("/logs")
def call_logs():
    logs = get_call_logs()
    return logs


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Webhook received:", data)
    return {"status": "ok"}