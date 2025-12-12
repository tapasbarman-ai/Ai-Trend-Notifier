import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from src.tools.twitter.twitter_agent import TwitterAgentConfigurable
from src.tools.reddit.reddit_agent import RedditAgent


def ingestion_node(state):
    """Fetch trends from Twitter and Reddit with quality filtering"""
    print("📥 Ingestion Node: Fetching high-quality trends...")

    # Configurable limits - adjust these as needed
    TWITTER_LIMIT = 20  # Top 20 tweets by engagement
    REDDIT_LIMIT = 20   # Top 20 Reddit posts by quality score
    
    # Use 'focused' query preset (245 chars) to avoid Twitter API query length errors
    twitter = TwitterAgentConfigurable(query_type="focused")
    reddit = RedditAgent()

    trends = []
    
    # Fetch from Twitter with engagement filtering
    twitter_trends = twitter.fetch_trends(
        max_results=TWITTER_LIMIT,
        min_likes=10,      # Minimum 10 likes
        min_retweets=5     # Minimum 5 retweets
    )
    trends.extend(twitter_trends)
    
    # Fetch from Reddit with quality filtering
    reddit_trends = reddit.fetch_trends(
        max_results=REDDIT_LIMIT,
        min_score=10,      # Minimum 10 upvotes
        min_comments=3     # Minimum 3 comments
    )
    trends.extend(reddit_trends)

    print(f"   ✅ Fetched {len(trends)} high-quality trends ({len(twitter_trends)} Twitter + {len(reddit_trends)} Reddit)")
    state['trends'] = trends
    return state