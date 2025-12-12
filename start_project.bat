@echo off
echo Starting AI Trend Notifier...
echo.

REM Start Backend (FastAPI)
echo [1/2] Starting Backend Server (FastAPI)...
start "Backend Server" cmd /k "cd /d %~dp0 && uvicorn backend.main:app --reload"

REM Wait a moment for backend to initialize
timeout /t 3 /nobreak >nul

REM Start Frontend (Next.js)
echo [2/2] Starting Frontend Server (Next.js)...
start "Frontend Server" cmd /k "cd /d %~dp0\frontend && npm run dev"

echo.
echo ========================================
echo   AI Trend Notifier is starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to exit this window...
pause >nul
