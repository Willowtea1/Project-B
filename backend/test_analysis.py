#!/usr/bin/env python3
"""
Test script for the text analysis backend
"""

import requests
import json

def test_analysis_endpoint():
    """Test the /analyze endpoint with sample text"""
    
    # Test data
    test_text = """
    Artificial intelligence is transforming the way we live and work. 
    From virtual assistants to autonomous vehicles, AI technologies are 
    becoming increasingly integrated into our daily lives. Companies are 
    investing heavily in AI research and development, recognizing its 
    potential to drive innovation and efficiency across various industries.
    """
    
    # API endpoint
    url = "http://127.0.0.1:8000/analyze"
    
    try:
        # Make request
        response = requests.post(url, json={"text": test_text})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Analysis successful!")
            print(f"Summary: {result['summary']}")
            print(f"Category: {result['category']}")
            print(f"Sentiment: {result['sentiment']}")
            print(f"Sentiment Score: {result['sentiment_score']}")
            print(f"Tags: {', '.join(result['tags'])}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Make sure the backend server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def test_health_endpoint():
    """Test the /health endpoint"""
    
    url = "http://127.0.0.1:8000/health"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Health check successful!")
            print(f"Status: {result['status']}")
            print(f"Message: {result['message']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Make sure the backend server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    print("🧪 Testing Text Analysis Backend")
    print("=" * 40)
    
    print("\n1. Testing health endpoint...")
    test_health_endpoint()
    
    print("\n2. Testing analysis endpoint...")
    test_analysis_endpoint()
    
    print("\n" + "=" * 40)
    print("Test completed!")
