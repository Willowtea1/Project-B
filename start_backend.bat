@echo off
echo 🚀 Starting Text Analysis Backend Server...
echo 📁 Working directory: %CD%\backend
echo 🌐 Server will be available at: http://127.0.0.1:8000
echo 📚 API documentation: http://127.0.0.1:8000/docs
echo ==================================================

cd backend

echo 💡 Make sure you have:
echo    1. Python virtual environment activated
echo    2. Requirements installed: pip install -r requirements.txt
echo    3. GOOGLE_API_KEY set in .env file
echo.

uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause
