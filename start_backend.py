#!/usr/bin/env python3
"""
Smart Recipe Analyzer Backend Startup Script
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def main():
    print("🍳 Starting Smart Recipe Analyzer Backend...")
    print()
    
    # Change to backend directory
    backend_dir = Path(__file__).parent / "backend"
    os.chdir(backend_dir)
    
    # Check if virtual environment exists
    venv_path = backend_dir / ".venv"
    if not venv_path.exists():
        print("📦 Virtual environment not found. Creating one...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
    
    # Activate virtual environment and install dependencies
    if platform.system() == "Windows":
        activate_script = venv_path / "Scripts" / "activate.bat"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    # Install requirements
    print("📥 Installing dependencies...")
    subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
    
    print()
    print("🚀 Starting FastAPI server...")
    print("🌐 API will be available at: http://localhost:8000")
    print("📚 API docs will be available at: http://localhost:8000/docs")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    
    # Start the server
    uvicorn_path = venv_path / "Scripts" / "uvicorn.exe" if platform.system() == "Windows" else venv_path / "bin" / "uvicorn"
    subprocess.run([
        str(uvicorn_path),
        "main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
