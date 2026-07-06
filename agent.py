import os
import requests
from dotenv import load_dotenv

load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")


def make_outbound_call(phone_number, customer_name=""):
    url = "https://api.vapi.ai/call"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "assistantId": VAPI_ASSISTANT_ID,
        "customer": {
            "number": phone_number,
            "name": customer_name
        },
        "phoneNumberId": os.getenv("VAPI_PHONE_NUMBER_ID")
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_call_logs():
    url = "https://api.vapi.ai/call"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def get_call_details(call_id):
    url = f"https://api.vapi.ai/call/{call_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()