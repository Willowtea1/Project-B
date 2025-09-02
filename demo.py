#!/usr/bin/env python3
"""
Smart Recipe Analyzer Demo Script
This script demonstrates how to use the API programmatically
"""

import requests
import json
import time

def demo_recipe_analysis():
    """Demonstrate the recipe analysis functionality"""
    
    print("🍳 Smart Recipe Analyzer Demo")
    print("=" * 50)
    
    # Test ingredients
    test_cases = [
        "chicken breast, rice, tomatoes, garlic, olive oil",
        "pasta, tomato sauce, cheese, basil, garlic",
        "eggs, bread, milk, cheese, butter",
        "salmon, lemon, herbs, olive oil, vegetables"
    ]
    
    base_url = "http://localhost:8000"
    
    # Check if backend is running
    try:
        health_response = requests.get(f"{base_url}/health")
        if health_response.status_code != 200:
            print("❌ Backend is not responding properly")
            return
        print("✅ Backend is running and healthy")
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running. Please start it first.")
        print("   Run: python start_backend.py")
        return
    
    print(f"\n🌐 Backend URL: {base_url}")
    print(f"📚 API Docs: {base_url}/docs")
    print("\n" + "=" * 50)
    
    # Test each ingredient combination
    for i, ingredients in enumerate(test_cases, 1):
        print(f"\n🧪 Test Case {i}: {ingredients}")
        print("-" * 40)
        
        try:
            # Make API request
            payload = {"ingredients": ingredients}
            response = requests.post(
                f"{base_url}/analyze-recipes",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                recipes = data.get("recipes", [])
                
                print(f"✅ Generated {len(recipes)} recipes:")
                
                for j, recipe in enumerate(recipes, 1):
                    print(f"\n   Recipe {j}: {recipe.get('name', 'Unknown')}")
                    print(f"     ⏱️  Cooking Time: {recipe.get('cooking_time', 'Unknown')}")
                    print(f"     ⭐ Difficulty: {recipe.get('difficulty', 'Unknown')}")
                    print(f"     👥 Servings: {recipe.get('servings', 'Unknown')}")
                    
                    nutrition = recipe.get('nutrition', {})
                    print(f"     🥗 Nutrition (per serving):")
                    print(f"        Calories: {nutrition.get('calories', 'Unknown')}")
                    print(f"        Protein: {nutrition.get('protein', 'Unknown')}")
                    print(f"        Carbs: {nutrition.get('carbs', 'Unknown')}")
                    print(f"        Fat: {nutrition.get('fat', 'Unknown')}")
                    
                    if nutrition.get('fiber'):
                        print(f"        Fiber: {nutrition.get('fiber')}")
                    
                    print(f"     📝 Instructions ({len(recipe.get('instructions', []))} steps):")
                    for k, instruction in enumerate(recipe.get('instructions', [])[:3], 1):
                        print(f"        {k}. {instruction}")
                    if len(recipe.get('instructions', [])) > 3:
                        print(f"        ... and {len(recipe.get('instructions', [])) - 3} more steps")
                
            else:
                print(f"❌ API request failed with status {response.status_code}")
                print(f"   Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        
        # Add delay between requests to be respectful to the API
        if i < len(test_cases):
            print("\n⏳ Waiting 2 seconds before next request...")
            time.sleep(2)
    
    print("\n" + "=" * 50)
    print("🎉 Demo completed!")
    print("\n💡 Try the web interface at: http://localhost:5173")
    print("🔧 API documentation at: http://localhost:8000/docs")

def interactive_demo():
    """Interactive demo where user can input ingredients"""
    
    print("\n🎮 Interactive Demo Mode")
    print("=" * 30)
    
    base_url = "http://localhost:8000"
    
    while True:
        print("\nEnter your ingredients (or 'quit' to exit):")
        ingredients = input("🍽️  Ingredients: ").strip()
        
        if ingredients.lower() in ['quit', 'exit', 'q']:
            break
            
        if not ingredients:
            print("❌ Please enter some ingredients")
            continue
        
        try:
            payload = {"ingredients": ingredients}
            response = requests.post(
                f"{base_url}/analyze-recipes",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                recipes = data.get("recipes", [])
                
                print(f"\n🎯 Generated {len(recipes)} recipes for: {ingredients}")
                print("-" * 50)
                
                for i, recipe in enumerate(recipes, 1):
                    print(f"\n🍳 Recipe {i}: {recipe.get('name', 'Unknown')}")
                    print(f"   ⏱️  {recipe.get('cooking_time', 'Unknown')} | ⭐ {recipe.get('difficulty', 'Unknown')} | 👥 {recipe.get('servings', 'Unknown')} servings")
                    
                    nutrition = recipe.get('nutrition', {})
                    print(f"   🥗 {nutrition.get('calories', 'Unknown')} cal | P: {nutrition.get('protein', 'Unknown')} | C: {nutrition.get('carbs', 'Unknown')} | F: {nutrition.get('fat', 'Unknown')}")
                    
                    print(f"   📝 Instructions:")
                    for j, instruction in enumerate(recipe.get('instructions', []), 1):
                        print(f"      {j}. {instruction}")
                        
            else:
                print(f"❌ API request failed: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")

def main():
    """Main demo function"""
    
    print("Welcome to the Smart Recipe Analyzer Demo!")
    print("This script demonstrates the API functionality")
    
    # Run automated demo
    demo_recipe_analysis()
    
    # Ask if user wants interactive mode
    print("\n" + "=" * 50)
    response = input("Would you like to try interactive mode? (y/n): ").strip().lower()
    
    if response in ['y', 'yes']:
        interactive_demo()
    
    print("\n👋 Thanks for trying the Smart Recipe Analyzer!")
    print("🍳 Happy cooking!")

if __name__ == "__main__":
    main()
