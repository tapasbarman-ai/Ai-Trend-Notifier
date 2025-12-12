# AI Trend Notifier

**AI Trend Notifier** is a powerful full-stack automated platform designed to monitor, analyze, and report on Artificial Intelligence trends. It leverages a sophisticated multi-agent system to scrape social media, analyze sentiment, enrich data with web research, and generate professional HTML email newsletters using LLMs.

---

## 🚀 Key Features

*   **Multi-Source Ingestion**: Automatically fetches trending discussions from **Twitter** and **Reddit**.
*   **AI-Powered Analysis**: Uses **DistilBERT** for sentiment classification (Positive/Negative/Neutral) and **Groq (Llama 3)** for intelligent summarization.
*   **Smart Enrichment**: Verifies claims and adds context using **Tavily Search API**.
*   **Professional Reporting**: Generates beautiful, responsive HTML newsletters with dynamic content, stats, and GIFs.
*   **Interactive Dashboard**: A modern **Next.js** web interface to view live trends, manage settings, and control the agent pipeline.

---

## 🏗️ System Architecture

The system follows a **Node-Based Agentic Architecture** orchestrated by **LangGraph**:

1.  **Ingestion Node**: Fetches raw data from social platforms.
2.  **Sentiment Node**: Analyzes text tone and emotion.
3.  **Enrichment Node**: Searches the web for validation and additional context.
4.  **Summarizer Node**: Synthesizes data into executive summaries and headlines.
5.  **Notifier Node**: Compiles the newsletter and dispatches it via SMTP.
6.  **Web Dashboard**: Frontend for monitoring and control.

---

## 🛠️ Technology Stack

### Frontend
*   **Framework**: Next.js 14 (App Router)
*   **Language**: TypeScript
*   **Styling**: Tailwind CSS, Lucide React

### Backend & AI
*   **Framework**: FastAPI
*   **Language**: Python 3.10+
*   **Orchestration**: LangChain, LangGraph
*   **LLM Inference**: Groq (Llama 3.1)
*   **Tools**: Tavily API (Search), HuggingFace (Sentiment)

### Infrastructure
*   **Database**: SQLite
*   **Containerization**: Docker support available

---

## 📦 Installation

### Prerequisites
*   **Python 3.10+**
*   **Node.js 18+**
*   **Git**

### 1. Clone the Repository
```bash
git clone https://github.com/tapasbarman-ai/Ai-Trend-Notifier.git
cd Ai-Trend-Notifier
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Initialize Database
python init_db.py
```

### 3. Frontend Setup
```bash
cd frontend
npm install
cd ..
```

### 4. Environment Configuration
Create a `.env` file in the root directory (refer to `.env.example` if available) and add your keys:
```env
# Social Keys
TWITTER_BEARER_TOKEN=your_token
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret

# AI Keys
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key

# Email Config
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email
SMTP_PASSWORD=your_app_password
EMAIL_FROM=your_email
EMAIL_TO=recipient_email
```

---

## ▶️ How to Run

We provide convenient scripts to start both the Frontend and Backend servers simultaneously.

### Windows (Command Prompt)
Double-click `start_project.bat` or run:
```cmd
start_project.bat
```

### Windows (PowerShell)
Right-click `start_project.ps1` and select "Run with PowerShell", or run:
```powershell
.\start_project.ps1
```

Once started, access the application at:
*   **Frontend**: [http://localhost:3000](http://localhost:3000)
*   **Backend API**: [http://localhost:8000](http://localhost:8000)
*   **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```
ai-trend-notifier/
├── backend/                 # FastAPI application
├── frontend/                # Next.js application
├── src/
│   ├── agents/             # LangGraph agent definitions
│   ├── tools/              # Scrapers and utility tools
│   └── ...
├── templates/              # Email HTML templates
├── start_project.bat       # Windows Startup Script
└── start_project.ps1       # PowerShell Startup Script
```