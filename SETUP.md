# Quick Setup Guide

This guide will help you get the AI Text Analysis application up and running in minutes.

## Prerequisites

- **Python 3.8+** installed on your system
- **Node.js 18+** installed on your system
- **Google Gemini API Key** (free tier available)

## Step 1: Get Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key (you'll need it for the backend)

## Step 2: Backend Setup

### Option A: Using the startup script (Recommended)

**Windows:**

```bash
start_backend.bat
```

**Linux/Mac:**

```bash
python start_backend.py
```

### Option B: Manual setup

1. **Navigate to backend directory:**

   ```bash
   cd backend
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**

   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file:**
   Create a file named `.env` in the backend directory with:

   ```
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

6. **Start the server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Step 3: Frontend Setup

1. **Open a new terminal and navigate to frontend directory:**

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

## Step 4: Access the Application

1. **Backend API:** http://127.0.0.1:8000
2. **API Documentation:** http://127.0.0.1:8000/docs
3. **Frontend Application:** http://localhost:5173

## Testing the Setup

### Test Backend

```bash
cd backend
python test_analysis.py
```

### Test Frontend

1. Open http://localhost:5173 in your browser
2. Navigate to the Text Analysis page
3. Enter some text and click "Analyze Text"

## Troubleshooting

### Common Issues

**1. "Module not found" errors**

- Make sure you're in the correct directory
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**2. "Connection refused" errors**

- Check if the backend server is running on port 8000
- Verify the frontend is trying to connect to the correct URL

**3. "API key not found" errors**

- Ensure the `.env` file exists in the backend directory
- Check that the API key is correctly formatted
- Verify the API key is valid in Google AI Studio

**4. Frontend not loading**

- Check if Node.js is installed: `node --version`
- Ensure all dependencies are installed: `npm install`
- Check the console for any error messages

### Getting Help

If you encounter issues:

1. Check the console/terminal for error messages
2. Verify all prerequisites are installed
3. Ensure both backend and frontend are running
4. Check the API documentation at http://127.0.0.1:8000/docs

## Next Steps

Once everything is working:

1. Explore the different analysis features
2. Try the advanced Text Analysis tool
3. Check out the API documentation
4. Customize the application for your needs

## Development

For development:

- Backend auto-reloads on file changes
- Frontend hot-reloads on file changes
- API documentation updates automatically
- Check the console for detailed error messages
