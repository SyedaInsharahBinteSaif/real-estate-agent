# Real Estate AI Calling Agent

An AI-powered calling agent built for real estate businesses. It handles inbound calls, answers property inquiries, captures leads, and manages inappropriate questions automatically.

## What it does

When a customer calls, the agent:
- Greets them and asks how it can help
- Answers questions about properties, pricing, and viewings
- Captures their name, email, budget, and requirements
- Handles off-topic or inappropriate questions politely
- Never shares any internal system information

## Tech stack

- Python
- FastAPI
- Vapi.ai (voice calling infrastructure)
- Gemini 3.5 Flash (AI model)
- Streamlit (dashboard UI)
- Railway (deployment)

## Project structure
real-estate-agent/
├── agent.py        # Vapi API calls and call management
├── main.py         # FastAPI backend
├── app.py          # Streamlit dashboard
├── requirements.txt
└── .env            # API keys (not included)
## How to run locally

1. Clone the repo
2. Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create a `.env` file with your keys
4. Create a `.env` file with your keys
VAPI_API_KEY=your_key
GEMINI_API_KEY=your_key
VAPI_ASSISTANT_ID=your_assistant_id
VAPI_PHONE_NUMBER_ID=your_phone_number_id
5. Run the backend
uvicorn main:app --reload
6. Run the dashboard
streamlit run app.py
## Live API
https://real-estate-agent-production-0dcb.up.railway.app
## Notes

The Vapi assistant is configured with Gemini 3.5 Flash and handles real inbound calls. The agent is designed specifically for real estate use cases but the architecture can be adapted for any industry.