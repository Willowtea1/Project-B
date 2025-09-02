# 🚀 Smart Recipe Analyzer - Setup Guide

This guide will walk you through setting up the Smart Recipe Analyzer application step by step.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** with pip
- **Node.js 18+** with npm
- **Git** (for cloning the repository)
- **Google Gemini API Key** ([Get one here](https://makersuite.google.com/app/apikey))

## 🏗️ Project Structure

```
Project-B/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main API server
│   ├── requirements.txt    # Python dependencies
│   ├── env_template.txt    # Environment variables template
│   └── test_recipe_analyzer.py  # Backend tests
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── views/         # Page components
│   │   ├── App.vue        # Main app component
│   │   └── main.js        # App entry point
│   └── package.json       # Node.js dependencies
├── start_backend.bat      # Windows backend startup
├── start_backend.py       # Cross-platform backend startup
├── start_frontend.bat     # Windows frontend startup
└── README.md              # Main documentation
```

## 🔧 Step-by-Step Setup

### Step 1: Clone and Navigate to Project

```bash
# Navigate to your desired directory
cd /path/to/your/projects

# Clone the repository (if not already done)
git clone <repository-url>
cd Project-B
```

### Step 2: Backend Setup

#### 2.1 Navigate to Backend Directory

```bash
cd backend
```

#### 2.2 Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

#### 2.3 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2.4 Set Up Environment Variables

```bash
# Copy the template
cp env_template.txt .env

# Edit .env file and add your Google Gemini API key
# Replace 'your_google_gemini_api_key_here' with your actual API key
```

**Important:** Never commit your `.env` file to version control!

#### 2.5 Test Backend Installation

```bash
# Test if everything is working
python test_recipe_analyzer.py
```

### Step 3: Frontend Setup

#### 3.1 Navigate to Frontend Directory

```bash
cd ../frontend
```

#### 3.2 Install Dependencies

```bash
npm install
```

#### 3.3 Verify Frontend Setup

```bash
# Check if all dependencies are installed
npm list --depth=0
```

### Step 4: Start the Application

#### Option A: Using Startup Scripts (Recommended)

**For Backend:**

```bash
# Windows
start_backend.bat

# Cross-platform
python start_backend.py
```

**For Frontend:**

```bash
# Windows
start_frontend.bat

# Manual
npm run dev
```

#### Option B: Manual Startup

**Backend (Terminal 1):**

```bash
cd backend
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # macOS/Linux

uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend (Terminal 2):**

```bash
cd frontend
npm run dev
```

## 🌐 Access Points

Once both services are running:

- **Frontend Application:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

## 🧪 Testing the Setup

### Backend Test

```bash
cd backend
python test_recipe_analyzer.py
```

### Frontend Test

1. Open http://localhost:5173 in your browser
2. Navigate to the recipe analyzer
3. Enter some test ingredients (e.g., "chicken, rice, tomatoes")
4. Click "Find Recipes" to test the AI integration

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Backend Issues

**"Module not found" errors:**

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall requirements
pip install -r requirements.txt
```

**"Port already in use" error:**

```bash
# Kill process using port 8000
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**API key errors:**

- Verify your `.env` file exists and contains the correct API key
- Check that the API key is valid and has sufficient quota
- Ensure the `.env` file is in the `backend/` directory

#### Frontend Issues

**"Module not found" errors:**

```bash
# Remove node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**"Port already in use" error:**

```bash
# Kill process using port 5173
# Windows
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5173 | xargs kill -9
```

**CORS errors:**

- Ensure backend is running on port 8000
- Check that CORS is properly configured in `backend/main.py`

### Debug Mode

**Backend Debug:**

```bash
# Add debug logging
export DEBUG=true  # macOS/Linux
set DEBUG=true     # Windows

# Or modify main.py to include debug logging
```

**Frontend Debug:**

```bash
# Check browser console for errors
# Check terminal for build errors
npm run build  # Test production build
```

## 🚀 Production Deployment

### Backend Deployment

1. Set production environment variables
2. Use production ASGI server (e.g., Gunicorn)
3. Configure reverse proxy (e.g., Nginx)
4. Set up SSL certificates

### Frontend Deployment

1. Build production version: `npm run build`
2. Deploy `dist/` folder to your hosting service
3. Configure environment variables for production API endpoints

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vue.js Documentation](https://vuejs.org/)
- [Vuetify Documentation](https://vuetifyjs.com/)
- [Google Gemini API Documentation](https://ai.google.dev/)

## 🆘 Getting Help

If you encounter issues:

1. **Check the troubleshooting section above**
2. **Review the logs** in both terminal windows
3. **Check the API documentation** at http://localhost:8000/docs
4. **Open an issue** on the project repository
5. **Check the browser console** for frontend errors

## ✅ Verification Checklist

- [ ] Python virtual environment created and activated
- [ ] Backend dependencies installed
- [ ] Google Gemini API key configured in `.env`
- [ ] Backend server running on port 8000
- [ ] Frontend dependencies installed
- [ ] Frontend server running on port 5173
- [ ] Backend health check passes
- [ ] Frontend loads without errors
- [ ] Recipe analysis endpoint working
- [ ] AI generates recipe suggestions

---

**🎉 Congratulations!** Your Smart Recipe Analyzer is now set up and ready to use!

**Next Steps:**

1. Try the application with different ingredients
2. Explore the API documentation
3. Customize the UI or add new features
4. Deploy to production when ready

**Happy Cooking! 🍳✨**
