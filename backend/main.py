# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re
from fastapi.middleware.cors import CORSMiddleware
from typing import List

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
    sentiment: str
    sentiment_score: float
    tags: List[str]

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
    You are an AI assistant specialized in text analysis. Given the following text, provide a comprehensive analysis including:

    1. A concise summary (2-3 sentences)
    2. Classification into one of these categories: Business, Technology, Health, Entertainment, Education, Politics, Sports, Science, Arts, Others
    3. Sentiment analysis (Positive, Negative, Neutral) with a confidence score between -1.0 and 1.0
    4. Key tags/topics extracted from the text (5-8 relevant tags)

    Text to analyze:
    {req.text}

    Respond **ONLY** in JSON format like this:
    {{
        "summary": "A concise summary of the text",
        "category": "One of the specified categories",
        "sentiment": "Positive/Negative/Neutral",
        "sentiment_score": 0.8,
        "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"]
    }}

    Guidelines:
    - Sentiment score: -1.0 (very negative) to 1.0 (very positive)
    - Tags should be relevant keywords or topics from the text
    - Category should be the most appropriate from the given list
    - Summary should capture the main points clearly
    """

    try:
        # Create the model object
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Generate response
        response = model.generate_content(prompt)

        # Safely extract JSON
        result = extract_json(response.text)

        return AnalyzeResponse(
            summary=result["summary"], 
            category=result["category"],
            sentiment=result["sentiment"],
            sentiment_score=result["sentiment_score"],
            tags=result["tags"]
        )

    except ValueError as ve:
        raise HTTPException(status_code=500, detail=f"Failed to parse model output: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model request failed: {e}")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Text analysis service is running"}

#Gemini Chat endpoint
class ChatRequest(BaseModel):
    text: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(req.text)

        # The Gemini response is usually text
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}