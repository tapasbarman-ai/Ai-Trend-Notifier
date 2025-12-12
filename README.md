<div align="center">

# 🤖 AI Trend Notifier

![AI Animation](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)

### *Your Intelligent AI Trend Analysis & Newsletter Platform*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Stay ahead of the AI curve with automated trend monitoring, sentiment analysis, and intelligent summaries delivered straight to your inbox.**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-usage) • [🎨 Features](#-key-features) • [🤝 Contributing](#-contributing)

</div>

---

## 📺 Demo

<div align="center">

### Watch the Full Walkthrough

**[▶️ View Demo on YouTube](https://youtu.be/p9FM-yghvfs)**

*See the system in action: data ingestion, sentiment analysis, web enrichment, and newsletter generation*

</div>

---

## 🎯 What is AI Trend Notifier?

AI Trend Notifier is an **autonomous agentic AI system** that monitors Twitter and Reddit for trending AI topics, analyzes sentiment using state-of-the-art NLP models, enriches content with web research, and delivers beautiful newsletters with actionable insights.

<div align="center">

![Features](https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif)

</div>

### Why Use This?

- ✅ **Save Time**: Automated monitoring replaces hours of manual research
- ✅ **Stay Informed**: Never miss important AI developments
- ✅ **Data-Driven**: Sentiment analysis reveals market emotions
- ✅ **Context-Rich**: Web enrichment provides comprehensive understanding
- ✅ **Professional**: Beautiful newsletter format ready to share

---

## ✨ Key Features

### 🔄 **Multi-Platform Data Collection**
Automatically scrapes and aggregates AI trends from Twitter and Reddit using official APIs

### 🎭 **Advanced Sentiment Analysis**
Powered by HuggingFace's DistilBERT transformer model for accurate emotion detection (Positive/Negative/Neutral)

### 🔍 **Intelligent Web Enrichment**
Uses Tavily API to search the web and add context, related news, and deeper insights to each trend

### 🤖 **AI-Powered Summarization**
Groq's Llama 3.1 model generates concise, readable summaries from raw social media data

### 📊 **Interactive Dashboard**
Beautiful Streamlit interface with:
- Real-time analytics and metrics
- Sentiment distribution charts
- Timeline visualizations
- Subscriber management
- Admin control panel

### 📧 **Automated Email Newsletters**
Daily digest emails sent to subscribers with top trends, summaries, and sentiment scores

### ⏰ **Smart Scheduling**
Python-based scheduler runs the pipeline automatically at customizable times

### 🔒 **Secure & Private**
Local SQLite database, password-protected admin panel, and secure email configuration

---

## 🏗️ Architecture

<div align="center">

![Architecture](https://media.giphy.com/media/JqmupuTVZYaQX5s094/giphy.gif)

</div>

### System Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                         AI TREND NOTIFIER                            │
│                     (LangGraph Orchestration)                        │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌──────────────────┐         ┌──────────────────┐
          │  INGESTION NODE  │         │   DATA SOURCES   │
          │  (Multi-source)  │◄────────│  • Twitter API   │
          └────────┬─────────┘         │  • Reddit API    │
                   │                   └──────────────────┘
                   ▼
          ┌──────────────────┐
          │ SENTIMENT NODE   │
          │  (DistilBERT)    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ ENRICHMENT NODE  │
          │  (Tavily API)    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ SUMMARIZER NODE  │
          │  (Groq/Llama)    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐         ┌──────────────────┐
          │  NOTIFIER NODE   │────────►│   • SQLite DB    │
          │  (Save & Send)   │         │   • Email SMTP   │
          └──────────────────┘         └──────────────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ STREAMLIT UI     │
          │  (Dashboard)     │
          └──────────────────┘
```

### Technology Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Purpose</th>
</tr>
<tr>
<td><b>Orchestration</b></td>
<td>LangGraph + LangChain</td>
<td>Agentic workflow management</td>
</tr>
<tr>
<td><b>Scheduling</b></td>
<td>Python Schedule</td>
<td>Automated daily execution</td>
</tr>
<tr>
<td><b>Social APIs</b></td>
<td>Tweepy + PRAW</td>
<td>Twitter & Reddit data collection</td>
</tr>
<tr>
<td><b>NLP/ML</b></td>
<td>Transformers + PyTorch</td>
<td>Sentiment analysis (DistilBERT)</td>
</tr>
<tr>
<td><b>Web Search</b></td>
<td>Tavily API</td>
<td>Content enrichment & context</td>
</tr>
<tr>
<td><b>LLM</b></td>
<td>Groq API (Llama 3.1)</td>
<td>Text summarization</td>
</tr>
<tr>
<td><b>Database</b></td>
<td>SQLite</td>
<td>Trends & subscriber storage</td>
</tr>
<tr>
<td><b>Frontend</b></td>
<td>Streamlit</td>
<td>Interactive dashboard & newsletter UI</td>
</tr>
<tr>
<td><b>Email</b></td>
<td>SMTP (smtplib)</td>
<td>Newsletter delivery</td>
</tr>
</table>

---

## 🚀 Quick Start

<div align="center">

![Rocket](https://media.giphy.com/media/3oKIPlifLxdigaD2Y8/giphy.gif)

</div>

### Prerequisites

- **Python 3.10.11** or higher
- **pip** package manager
- **Git** for cloning

### Installation (5 Minutes)

**Step 1: Clone the Repository**
```bash
git clone https://github.com/tapasbarman-ai/ai-trend-notifier.git
cd ai-trend-notifier
```

**Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3.1: Install Frontend Dependencies**
```bash
cd frontend
npm install
cd ..
```

**Step 4: Setup Project Structure**
```bash
python setup_project.py
```

**Step 5: Initialize Database**
```bash
python init_db.py
```

**Step 6: Configure Environment Variables**

Create a `.env` file in the project root:

```env
# Social Media APIs
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=AITrendNotifier/1.0

# AI Services
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password_here
RECIPIENT_EMAIL=recipient@example.com

# Database
DB_PATH=data/db/trends.db
```

### 🔑 Getting API Keys

| Service | Link | Free Tier |
|---------|------|-----------|
| **Twitter API** | [developer.twitter.com](https://developer.twitter.com/) | ✅ Yes |
| **Reddit API** | [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) | ✅ Yes |
| **Tavily API** | [tavily.com](https://tavily.com/) | ✅ 1,000 searches/month |
| **Groq API** | [console.groq.com](https://console.groq.com/) | ✅ Yes |
| **Gmail App Password** | [Google Account](https://myaccount.google.com/apppasswords) | ✅ Free |

---

## 📖 Usage

<div align="center">

![Usage](https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif)

</div>

### 🚀 Quick Run (Recommended)

Use the provided startup scripts to launch both the **FastAPI Backend** and **Next.js Frontend** simultaneously.

**Windows (Command Prompt)**
```cmd
start_project.bat
```

**Windows (PowerShell)**
```powershell
.\start_project.ps1
```

## 🎨 Dashboard Features

<div align="center">

![Dashboard](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

</div>

### 📰 Newsletter Page
- Beautiful card-based trend display
- Real-time subscriber count
- Email subscription form
- Latest edition preview
- Quick statistics overview

### 📊 Analytics Dashboard
- **Sentiment Distribution** - Interactive pie chart
- **Trends Timeline** - Daily trend counts over time
- **Source Breakdown** - Twitter vs Reddit distribution
- **Key Metrics** - Total trends, positive/negative counts

### 👥 Subscriber Management (Admin)
- Complete subscriber list with join dates
- CSV export functionality
- Subscriber growth analytics
- Bulk email broadcasting
- Activation/deactivation controls

### ⚙️ Settings Panel (Admin)
- Email configuration testing
- Pipeline manual trigger
- Database management tools
- System health checks
- Password-protected access

---

## 📁 Project Structure

```
ai-trend-notifier/
│
├── 📂 backend/                    # FastAPI Backend 
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── 📂 routers/
│
├── 📂 frontend/                   # Next.js Frontend 
│   ├── 📂 app/
│   ├── 📂 components/
│   ├── 📂 utils/
│   ├── package.json
│   └── tsconfig.json
│
├── 📂 src/                        # Core Agent Logic
│   ├── 📂 config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── 📂 langgraph/              # Orchestration
│   │   ├── 📂 nodes/
│   │   └── graph.py
│   │
│   ├── 📂 orchestrator/           # Scheduling
│   │   └── simple_scheduler.py
│   │
│   └── 📂 tools/                  # Agent Tools
│       ├── 📂 twitter/
│       ├── 📂 reddit/
│       ├── 📂 sentiment/
│       ├── 📂 websearch/
│       ├── 📂 summarizer/
│       └── 📂 notifier/
│
├── 📂 web/                        # Streamlit Dashboard (Original)
│   ├── app.py
│   └── trends.db
│
├── 📂 data/
│   └── 📂 db/
│
├── 📄 .env
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 ai_trend_notifier.db
├── 📄 docker-compose.yml
├── 📄 init_db.py
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 run_pipeline_integrated.py
├── 📄 start_project.bat
└── 📄 start_project.ps1
```

---

## 🔧 Configuration

### Customize Pipeline Schedule

Edit `src/orchestrator/simple_scheduler.py`:

```python
# Change execution time
schedule.every().day.at("09:00").do(job)  # 9:00 AM
schedule.every().day.at("18:00").do(job)  # 6:00 PM

# Or multiple times per day
schedule.every(6).hours.do(job)  # Every 6 hours

# Or specific days
schedule.every().monday.at("09:00").do(job)
```

### Modify Trend Sources

Edit `src/langgraph/nodes/ingestion_node.py`:

```python
# Change Twitter search query
twitter_trends = twitter.fetch_trends(
    query="AI OR machine learning OR deep learning OR LLM"
)

# Change Reddit parameters
reddit_trends = reddit.fetch_trends(
    subreddit="MachineLearning+artificial+technology",
    limit=20
)
```

### Adjust Sentiment Model

Edit `src/tools/sentiment/sentiment_agent.py`:

```python
# Use different model
self.analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"  # Twitter-specific
)
```

---

## 🗄️ Database Schema

### Trends Table
```sql
CREATE TABLE trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,                    -- 'twitter' or 'reddit'
    content TEXT NOT NULL,                   -- Original post content
    sentiment REAL,                          -- Sentiment score (-1 to 1)
    sentiment_label TEXT,                    -- 'POSITIVE', 'NEGATIVE', 'NEUTRAL'
    enriched_data TEXT,                      -- Web search results (JSON)
    summary TEXT,                            -- AI-generated summary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Subscribers Table
```sql
CREATE TABLE subscribers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active INTEGER DEFAULT 1                 -- 1 = active, 0 = unsubscribed
);
```

---

## 🧪 Testing

<div align="center">

![Testing](https://media.giphy.com/media/citBl9yPwnUOs/giphy.gif)

</div>

### Test Pipeline Execution
```bash
python run_pipeline.py
```

### Test Database
```bash
sqlite3 data/db/trends.db "SELECT COUNT(*) FROM trends;"
```

### Test Email Configuration
```bash
python -c "from src.tools.notifier.email_agent import EmailAgent; EmailAgent().send_summary([{'content': 'Test trend', 'summary': 'Test summary', 'sentiment_label': 'POSITIVE'}])"
```

### Test Individual Agents
```bash
# Test Twitter agent
python -c "from src.tools.twitter.twitter_agent import TwitterAgent; print(TwitterAgent().fetch_trends())"

# Test sentiment analysis
python -c "from src.tools.sentiment.sentiment_agent import SentimentAgent; print(SentimentAgent().analyze('AI is amazing!'))"
```

---

## 🐛 Troubleshooting

### Common Issues

**Import Errors**
```bash
# Solution: Ensure all __init__.py files exist
python setup_project.py
```

**Database Not Found**
```bash
# Solution: Initialize database
python init_db.py
```

**API Rate Limits**
- Twitter: 500k tweets/month (Free tier)
- Reddit: 60 requests/minute
- Solution: Reduce fetch frequency or upgrade API tier

**Email Not Sending**
- Verify Gmail App Password (not regular password)
- Check SMTP settings in `.env`
- Test with: `telnet smtp.gmail.com 587`

---

## 🤝 Contributing

<div align="center">

![Contributing](https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif)

</div>

We welcome contributions! Here's how to get started:

### Contribution Process

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/ai-trend-notifier.git`
3. **Create** a branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes
5. **Test** thoroughly
6. **Commit**: `git commit -m 'Add amazing feature'`
7. **Push**: `git push origin feature/amazing-feature`
8. **Submit** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Include unit tests for new features
- Update README if needed
- Keep commits atomic and well-documented

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Additional tests
- 🌐 Internationalization

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 AI Trend Notifier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

Special thanks to these amazing projects:

- **[LangChain](https://langchain.com/)** & **[LangGraph](https://github.com/langchain-ai/langgraph)** - Agentic AI framework
- **[Streamlit](https://streamlit.io/)** - Beautiful dashboards made easy
- **[HuggingFace](https://huggingface.co/)** - Transformers and NLP models
- **[Groq](https://groq.com/)** - Lightning-fast LLM inference
- **[Tavily](https://tavily.com/)** - Intelligent web search API

---

## 👥 Authors & Contributors

<div align="center">

**Tapas Barman** - *Creator & Lead Developer*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tapasbarman-ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tapas-barman-2661161a0/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tapasb.dev@gmail.com)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/tapasbarman)
[![Portfolio](https://img.shields.io/badge/Portfolio-Host-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://portfolio-tapas000s-projects.vercel.app)

</div>

---

## 📞 Support & Contact

<table>
<tr>
<td>

### 💬 Get Help

- 📧 Email: tapasb.dev@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/tapasbarman-ai/ai-trend-notifier/issues)
- 💡 Discussions: [GitHub Discussions](https://github.com/tapasbarman-ai/ai-trend-notifier/discussions)

</td>
<td>

### 🌐 Connect

- � LinkedIn: [Tapas Barman](https://www.linkedin.com/in/tapas-barman-2661161a0/)
- � GitHub: [tapasbarman-ai](https://github.com/tapasbarman-ai)
- 🏆 Kaggle: [tapasbarman](https://www.kaggle.com/tapasbarman)
- 🌍 Portfolio: [portfolio-tapas000s-projects.vercel.app](https://portfolio-tapas000s-projects.vercel.app)
- 📞 Phone: 7363971909

</td>
</tr>
</table>

---

## 🔮 Roadmap & Future Enhancements

<div align="center">

![Future](https://media.giphy.com/media/3oKIPlifLxdigaD2Y8/giphy.gif)

</div>

### Version 2.0 (Q1 2024)
- [ ] LinkedIn and HackerNews integration
- [ ] Real-time WebSocket updates
- [ ] Advanced filtering and personalization
- [ ] Mobile app (React Native)

### Version 2.5 (Q2 2024)
- [ ] Multi-language support (i18n)
- [ ] Trend prediction using LSTM/GRU
- [ ] Webhook notifications (Slack, Discord, Teams)
- [ ] REST API endpoints

### Version 3.0 (Q3 2024)
- [ ] User authentication and profiles
- [ ] Custom alert rules engine
- [ ] Historical trend comparison
- [ ] Export to PDF/PowerPoint
- [ ] Cloud deployment (AWS/GCP)

---

## 📊 Project Statistics

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/tapasbarman-ai/ai-trend-notifier?style=social)
![GitHub forks](https://img.shields.io/github/forks/tapasbarman-ai/ai-trend-notifier?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/tapasbarman-ai/ai-trend-notifier?style=social)

![GitHub issues](https://img.shields.io/github/issues/tapasbarman-ai/ai-trend-notifier)
![GitHub pull requests](https://img.shields.io/github/issues-pr/tapasbarman-ai/ai-trend-notifier)
![GitHub last commit](https://img.shields.io/github/last-commit/tapasbarman-ai/ai-trend-notifier)
![GitHub code size](https://img.shields.io/github/languages/code-size/tapasbarman-ai/ai-trend-notifier)

</div>

---

## 🎓 Learn More

### Documentation
- [Full API Documentation](docs/API.md)
- [Architecture Deep Dive](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing Guidelines](CONTRIBUTING.md)

### Tutorials
- [Setting Up Your First Pipeline](docs/tutorials/first-pipeline.md)
- [Customizing Sentiment Models](docs/tutorials/custom-sentiment.md)
- [Building Custom Agents](docs/tutorials/custom-agents.md)

---

<div align="center">

![Thank You](https://media.giphy.com/media/KJ1f5iTl4Oo7u/giphy.gif)

### ⭐️ If you found this project helpful, please give it a star!

### 📧 Subscribe to get daily AI trends delivered to your inbox!

![Star](https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif)

---

**Made with ❤️ by the AI Trend Notifier Team**

*Keeping you informed, one trend at a time* 🚀

</div>
