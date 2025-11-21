@echo off
cd /d C:\Users\tb619\PycharmProjects\ai-trend-notifier
call .venv\Scripts\activate
echo Starting AI Trend Scheduler...
python -m src.orchestrator.simple_scheduler