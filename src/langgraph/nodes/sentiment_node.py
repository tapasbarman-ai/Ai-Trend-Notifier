import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from src.tools.sentiment.sentiment_agent import SentimentAgent


def sentiment_node(state):
    """Analyze sentiment of each trend"""
    print("🎭 Sentiment Node: Analyzing sentiment...")

    analyzer = SentimentAgent()

    for trend in state['trends']:
        sentiment = analyzer.analyze(trend['content'])
        trend.update(sentiment)

    print(f"   ✅ Analyzed {len(state['trends'])} trends")
    return state