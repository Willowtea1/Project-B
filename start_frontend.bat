@echo off
echo Starting Smart Recipe Analyzer Frontend...
echo.

cd frontend

echo Installing dependencies...
if not exist node_modules (
    npm install
)

echo.
echo Starting Vue development server...
echo Frontend will be available at: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo.

npm run dev

pause
