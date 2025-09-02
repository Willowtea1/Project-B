# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

load_dotenv()

app = FastAPI(title="Smart Recipe Analyzer API", version="1.0.0")

origins = [
    "http://localhost:5173",
    "http://localhost:3000"
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

# Request model for recipe analysis
class RecipeRequest(BaseModel):
    ingredients: str

# Nutritional information model
class NutritionInfo(BaseModel):
    calories: int
    protein: str
    carbs: str
    fat: str
    fiber: Optional[str] = None

# Recipe model
class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    instructions: List[str]
    cooking_time: str
    difficulty: str
    nutrition: NutritionInfo
    servings: int = 2

# Response model
class RecipeResponse(BaseModel):
    recipes: List[Recipe]

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

# Recipe analysis endpoint
@app.post("/analyze-recipes", response_model=RecipeResponse)
async def analyze_recipes(req: RecipeRequest):
    if not req.ingredients.strip():
        raise HTTPException(status_code=400, detail="Ingredients list cannot be empty")

    prompt = f"""
    You are a professional chef and nutritionist. Given the following ingredients, decides if it is a valid cooking ingredient, if not then fallback to error. If it is a valid cooking ingredient, then create 3 delicious recipe suggestions.
    
    Available ingredients: {req.ingredients}
    
    For each recipe, provide:
    1. A creative recipe name
    2. List of ingredients needed (including the provided ingredients plus any common pantry staples)
    3. Step-by-step cooking instructions
    4. Estimated cooking time
    5. Difficulty level (Easy, Medium, Hard)
    6. Nutritional information per serving
    7. Number of servings
    
    Respond **ONLY** in this exact JSON format:
    {{
        "recipes": [
            {{
                "name": "Recipe Name",
                "ingredients": ["ingredient1", "ingredient2", "ingredient3"],
                "instructions": ["Step 1", "Step 2", "Step 3"],
                "cooking_time": "X minutes",
                "difficulty": "Easy/Medium/Hard",
                "nutrition": {{
                    "calories": 350,
                    "protein": "15g",
                    "carbs": "45g",
                    "fat": "12g",
                    "fiber": "5g"
                }},
                "servings": 2
            }}
        ]
    }}
    
    Guidelines:
    - Use the provided ingredients as the main components
    - Add common pantry staples (salt, pepper, oil, etc.) as needed
    - Make instructions clear and beginner-friendly
    - Ensure nutritional info is realistic and balanced
    - Cooking time should be reasonable for home cooking
    - Difficulty should match the complexity of the recipe
    """

    try:
        # Create the model object
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Generate response
        response = model.generate_content(prompt)

        # Safely extract JSON
        result = extract_json(response.text)

        # Validate the response structure
        if "recipes" not in result or not isinstance(result["recipes"], list):
            raise ValueError("Invalid response structure: missing recipes array")

        # Convert to RecipeResponse
        recipes = []
        for recipe_data in result["recipes"]:
            try:
                recipe = Recipe(**recipe_data)
                recipes.append(recipe)
            except Exception as e:
                print(f"Error parsing recipe: {e}")
                continue

        if not recipes:
            raise ValueError("No valid recipes could be parsed from the response")

        return RecipeResponse(recipes=recipes)

    except ValueError as ve:
        raise HTTPException(status_code=500, detail=f"Failed to parse model output: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model request failed: {e}")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Smart Recipe Analyzer API is running"}

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Smart Recipe Analyzer API",
        "version": "1.0.0",
        "endpoints": {
            "analyze_recipes": "/analyze-recipes",
            "health": "/health"
        }
    }