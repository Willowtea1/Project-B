#!/usr/bin/env python3
"""
Simple test script for the Smart Recipe Analyzer backend
"""

import requests
import json
import time

def test_health_endpoint():
    """Test the health check endpoint"""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed with status {response.status_code}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    print("\n🏠 Testing root endpoint...")
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            print("✅ Root endpoint working!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Root endpoint failed with status {response.status_code}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False

def test_recipe_analysis():
    """Test the recipe analysis endpoint"""
    print("\n🍳 Testing recipe analysis endpoint...")
    
    test_ingredients = "chicken breast, rice, tomatoes, garlic, olive oil"
    payload = {"ingredients": test_ingredients}
    
    try:
        print(f"   Testing with ingredients: {test_ingredients}")
        response = requests.post(
            "http://localhost:8000/analyze-recipes",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Recipe analysis successful!")
            data = response.json()
            recipes = data.get("recipes", [])
            print(f"   Generated {len(recipes)} recipes:")
            
            for i, recipe in enumerate(recipes, 1):
                print(f"   Recipe {i}: {recipe.get('name', 'Unknown')}")
                print(f"     Cooking time: {recipe.get('cooking_time', 'Unknown')}")
                print(f"     Difficulty: {recipe.get('difficulty', 'Unknown')}")
                print(f"     Calories: {recipe.get('nutrition', {}).get('calories', 'Unknown')}")
                
        elif response.status_code == 500:
            print("❌ Recipe analysis failed (server error)")
            print(f"   Error: {response.text}")
        else:
            print(f"❌ Recipe analysis failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            
        return response.status_code == 200
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Smart Recipe Analyzer Backend Tests")
    print("=" * 50)
    
    # Wait a moment for backend to be ready
    print("⏳ Waiting for backend to be ready...")
    time.sleep(2)
    
    # Run tests
    health_ok = test_health_endpoint()
    root_ok = test_root_endpoint()
    recipe_ok = test_recipe_analysis()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"   Health Check: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"   Root Endpoint: {'✅ PASS' if root_ok else '❌ FAIL'}")
    print(f"   Recipe Analysis: {'✅ PASS' if recipe_ok else '❌ FAIL'}")
    
    if all([health_ok, root_ok, recipe_ok]):
        print("\n🎉 All tests passed! Backend is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the backend logs for details.")
    
    print("\n💡 To test manually:")
    print("   - Health: http://localhost:8000/health")
    print("   - API Docs: http://localhost:8000/docs")
    print("   - Frontend: http://localhost:5173")

if __name__ == "__main__":
    main()
