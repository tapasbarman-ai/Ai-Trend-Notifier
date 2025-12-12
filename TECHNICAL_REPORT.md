# AI Trend Notifier - Technical Report

## 1. Project Overview
**AI Trend Notifier** is a full-stack automated platform designed to monitor, analyze, and report on Artificial Intelligence trends. It leverages advanced AI agents to scrape social media, analyze sentiment, enrich data with web research, and generate professional email newsletters using LLMs.

## 2. Technology Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Icons**: Lucide React

### Backend & API
- **Framework**: FastAPI
- **Language**: Python 3.10+
- **Server**: Uvicorn
- **ORM**: SQLAlchemy (likely used via direct DB interactions or similar)
- **Validation**: Pydantic

### AI & Machine Learning
- **Orchestration**: LangChain, LangGraph
- **LLM Inference**: Groq (Llama 3.1)
- **Sentiment Analysis**: HuggingFace Transformers (DistilBERT)
- **Web Search**: Tavily API

### Data & Storage
- **Database**: SQLite (`ai_trend_notifier.db`)
- **Data Processing**: Pandas

### DevOps & Tools
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git
- **Package Management**: npm, pip

## 3. System Architecture

The system follows a **Node-Based Agentic Architecture** orchestrated by LangGraph:

1.  **Ingestion Node**: Fetches raw data from Twitter and Reddit APIs.
2.  **Sentiment Node**: Analyzes text using DistilBERT to determine emotional tone (Positive/Negative/Neutral).
3.  **Enrichment Node**: Uses Tavily Search API to find related news and context for each trend.
4.  **Summarizer Node**: Uses Groq (Llama 3) to generate concise summaries, headlines, and executive insights.
5.  **Notifier Node**: Formats the final content into an HTML email and sends it via SMTP.
6.  **Web Dashboard**: A Next.js interface to view trends, manage settings, and control the pipeline.

## 4. Key Features
-   **Multi-Source Ingestion**: Unified trend collection from Twitter and Reddit.
-   **AI-Powered Analysis**: Sentiment classification and intelligent summarization.
-   **Smart Enrichment**: Automatic verification and context addition via web search.
-   **Professional Reporting**: Automated generation of HTML newsletters with dynamic content (GIFs, stats).
-   **Interactive Dashboard**: Real-time view of running pipelines and trend analytics.

## 5. Configuration
The system relies on environment variables defined in `.env`:
-   **Social**: `TWITTER_BEARER_TOKEN`, `REDDIT_CLIENT_ID`
-   **AI**: `GROQ_API_KEY`, `TAVILY_API_KEY`
-   **Email**: `SMTP_SERVER`, `SMTP_PASSWORD`

## 6. Installation
The project requires **Python 3.10+** and **Node.js 18+**.
-   **Backend**: `pip install -r requirements.txt` followed by `python init_db.py`.
-   **Frontend**: `npm install` inside the `frontend` directory.
-   Run using `start_project.bat`.
