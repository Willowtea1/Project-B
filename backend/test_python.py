import requests

# Test Gemini endpoint
resp = requests.post(
    "http://127.0.0.1:8000/api/ask/gemini",
    json={"text": "Hello Gemini, what model are you?"}
)
print("Gemini says:", resp.json())

# Test OpenRouter endpoint
resp = requests.post(
    "http://127.0.0.1:8000/api/ask/openrouter",
    json={"text": "Hello OpenRouter, what model are you?"}
)
print("OpenRouter says:", resp.json())

# import requests
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

# OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

# response = requests.get(
#   url="https://openrouter.ai/api/v1/key",
#   headers={
#     "Authorization": f"Bearer {OPENROUTER_KEY}"
#   }
# )

# print(json.dumps(response.json(), indent=2))
