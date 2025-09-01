# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Request model
class AnalyzeRequest(BaseModel):
    text: str

# Response model
class AnalyzeResponse(BaseModel):
    summary: str
    category: str

# Helper function to extract JSON safely from LLM output
def extract_json(text: str) -> dict:
    """
    Extract the first JSON object from a string and return it as a dict.
    Raises ValueError if no JSON object is found.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in the model output")
    return json.loads(match.group())

# Endpoint
@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_text(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    prompt = f"""
    You are an AI assistant. Given the following text, provide a concise summary (2-3 sentences)
    and classify it into one of these categories: Business, Technology, Health, Entertainment, Others.

    Text:
    {req.text}

    Respond **ONLY** in JSON format like this:
    {{
        "summary": "...",
        "category": "..."
    }}
    """

    try:
        # Create the model object
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Generate response
        response = model.generate_content(prompt)

        # Safely extract JSON
        result = extract_json(response.text)

        return AnalyzeResponse(summary=result["summary"], category=result["category"])

    except ValueError as ve:
        raise HTTPException(status_code=500, detail=f"Failed to parse model output: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model request failed: {e}")
