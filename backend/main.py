# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai 
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()


# class Ask(BaseModel):
#     text: str

origins = [
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

# Initialize the Gemini model
GEMINI_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.post("/summarize")
async def summarize(input: TextInput):
    prompt = f"Summarize the following text in bullet points:\n\n{input.text}"
    try:
        response = model.generate_content(prompt)
        return {"summary": response.text}
    except Exception as e:
        return {"error": str(e)}

# ## --- Google Gemini ---
# GEMINI_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GEMINI_KEY)

# @app.post("/api/ask/gemini")
# def ask_gemini(req: Ask):
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     resp = model.generate_content(req.text)
#     return {"reply": resp.text}


# ## --- OpenRouter (multi-provider) ---
# OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

# @app.post("/api/ask/openrouter")
# def ask_openrouter(req: Ask):
#     resp = requests.post(
#         "https://openrouter.ai/api/v1/chat/completions",
#         headers={
#             "Authorization": f"Bearer {OPENROUTER_KEY}",
#             "HTTP-Referer": "http://localhost:5173",  
#             "X-Title": "Project-A",
#         },
#         json={
#             "model": "deepseek/deepseek-r1:free", 
#             "messages": [{"role": "user", "content": req.text}],
#         },
#         timeout=60
#     ).json()
#     return {"reply": resp["choices"][0]["message"]["content"]}


# ## --- OpenAI (commented out) ---
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# @app.post("/api/ask/openai")
# async def ask_openai(prompt: Ask):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt.text}]
#     )
#     return {"reply": response.choices[0].message.content}

# ## --- Anthropic Claude (commented out) ---
# import anthropic
# claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
# @app.post("/api/ask/claude")
# async def ask_claude(prompt: Ask):
#     msg = claude.messages.create(
#         model="claude-3-5-sonnet-latest",
#         max_tokens=512,
#         messages=[{"role": "user", "content": prompt.text}]
#     )
#     return {"reply": msg.content[0].text}
