import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from src.tools.twitter.twitter_agent import TwitterAgent
from src.tools.reddit.reddit_agent import RedditAgent


def ingestion_node(state):
    """Fetch trends from Twitter and Reddit"""
    print("📥 Ingestion Node: Fetching trends...")

    twitter = TwitterAgent()
    reddit = RedditAgent()

    trends = []
    trends.extend(twitter.fetch_trends())
    trends.extend(reddit.fetch_trends())

    print(f"   ✅ Fetched {len(trends)} trends")
    state['trends'] = trends
    return state