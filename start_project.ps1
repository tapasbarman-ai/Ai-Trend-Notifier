# AI Trend Notifier Startup Script
# PowerShell version

Write-Host "Starting AI Trend Notifier..." -ForegroundColor Cyan
Write-Host ""

# Start Backend (FastAPI)
Write-Host "[1/2] Starting Backend Server (FastAPI)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot'; uvicorn backend.main:app --reload"

# Wait a moment for backend to initialize
Start-Sleep -Seconds 3

# Start Frontend (Next.js)
Write-Host "[2/2] Starting Frontend Server (Next.js)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\frontend'; npm run dev"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   AI Trend Notifier is starting!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to exit this window..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
