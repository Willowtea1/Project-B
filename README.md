# 🍳 Smart Recipe Analyzer

A full-stack web application that uses AI to generate recipe suggestions from available ingredients. Built with Vue.js + Vuetify frontend and FastAPI backend, powered by Google Gemini AI.

## ✨ Features

- **Smart Ingredient Analysis**: Input your available ingredients and get AI-powered recipe suggestions
- **Multiple Recipe Options**: Receive 2-3 different recipe ideas for each ingredient combination
- **Detailed Instructions**: Step-by-step cooking instructions for each recipe
- **Nutritional Information**: Complete nutritional breakdown including calories, protein, carbs, and fat
- **Cooking Details**: Cooking time, difficulty level, and serving size for each recipe
- **Responsive Design**: Beautiful, mobile-friendly interface built with Vuetify
- **Copy to Clipboard**: Easy recipe sharing functionality

## 🏗️ Architecture

```
Project-B/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main API server
│   ├── requirements.txt    # Python dependencies
│   └── env_template.txt    # Environment variables template
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── views/         # Page components
│   │   │   ├── HomeView.vue
│   │   │   └── RecipeAnalyzerView.vue
│   │   ├── App.vue        # Main app component
│   │   └── main.js        # App entry point
│   └── package.json       # Node.js dependencies
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ and pip
- Node.js 18+ and npm
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Backend Setup

1. **Navigate to backend directory:**

   ```bash
   cd backend
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   ```bash
   # Copy the template and add your API key
   cp env_template.txt .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

5. **Start the backend server:**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**

   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:5173`

## 🔧 API Endpoints

### Recipe Analysis

- **POST** `/analyze-recipes`
  - **Request Body:**
    ```json
    {
      "ingredients": "chicken breast, rice, tomatoes, garlic"
    }
    ```
  - **Response:**
    ```json
    {
      "recipes": [
        {
          "name": "Garlic Butter Chicken with Rice",
          "ingredients": [
            "chicken breast",
            "rice",
            "garlic",
            "butter",
            "salt",
            "pepper"
          ],
          "instructions": [
            "Season chicken...",
            "Cook rice...",
            "Sauté garlic..."
          ],
          "cooking_time": "25 minutes",
          "difficulty": "Easy",
          "nutrition": {
            "calories": 450,
            "protein": "35g",
            "carbs": "45g",
            "fat": "18g",
            "fiber": "3g"
          },
          "servings": 2
        }
      ]
    }
    ```

### Health Check

- **GET** `/health` - API health status
- **GET** `/` - API information and available endpoints

## 🎯 Usage Examples

### Example 1: Basic Ingredients

**Input:** `chicken, rice, vegetables`
**Result:** Multiple recipe suggestions including stir-fry, rice bowls, and soup variations

### Example 2: Pantry Staples

**Input:** `pasta, tomato sauce, cheese, garlic`
**Result:** Classic pasta dishes, baked pasta, and quick pasta salads

### Example 3: Breakfast Ingredients

**Input:** `eggs, bread, milk, cheese`
**Result:** French toast, scrambled eggs, breakfast sandwiches, and quiches

## 🛠️ Development

### Backend Development

- **Framework:** FastAPI with Pydantic models
- **AI Integration:** Google Gemini 1.5 Flash model
- **Validation:** Request/response validation with Pydantic
- **Error Handling:** Comprehensive error handling with user-friendly messages

### Frontend Development

- **Framework:** Vue 3 with Composition API
- **UI Library:** Vuetify 3 with Material Design
- **State Management:** Vue reactive system
- **HTTP Client:** Axios for API communication

### Code Structure

- **Components:** Reusable Vue components with proper props and events
- **Views:** Page-level components with routing
- **API Service:** Centralized API communication layer
- **Error Handling:** User-friendly error messages and loading states

## 🚀 Deployment

### Backend Deployment

- **Platform:** Railway, Fly.io, or Heroku
- **Environment Variables:** Set `GOOGLE_API_KEY` in production
- **Requirements:** Install from `requirements.txt`

### Frontend Deployment

- **Platform:** Vercel, Netlify, or GitHub Pages
- **Build Command:** `npm run build`
- **Output Directory:** `dist/`

## 🔒 Security Considerations

- **API Key Protection:** Never commit API keys to version control
- **Input Validation:** All user inputs are validated on both frontend and backend
- **CORS Configuration:** Properly configured for development and production
- **Rate Limiting:** Consider implementing rate limiting for production use

## 🧪 Testing

### Backend Testing

```bash
cd backend
python -m pytest test_*.py
```

### Frontend Testing

```bash
cd frontend
npm run test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the AI capabilities
- **Vuetify** for the beautiful Material Design components
- **FastAPI** for the high-performance backend framework
- **Vue.js** for the progressive frontend framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section below
2. Review the API documentation at `/docs` when the backend is running
3. Open an issue on GitHub

## 🔧 Troubleshooting

### Common Issues

**Backend won't start:**

- Ensure Python virtual environment is activated
- Check that all dependencies are installed
- Verify your `.env` file has the correct API key

**Frontend won't start:**

- Ensure Node.js version is 18+ or 20+
- Delete `node_modules` and run `npm install` again
- Check for any console errors

**API calls failing:**

- Verify backend is running on port 8000
- Check CORS configuration
- Ensure Google Gemini API key is valid

**Recipe generation issues:**

- Check API key has sufficient quota
- Verify ingredient input format
- Review backend logs for detailed error messages

---

**Happy Cooking! 🍳✨**
