import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import praw
from src.config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT


class RedditAgent:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )

    def fetch_trends(self, subreddit=None, limit=10):
        try:
            default_subreddits = [
                "MachineLearning",    # ML research papers / breakthroughs
                "Artificial",         # AI discussions
                "DeepLearning",       # Deep learning papers & models
                "OpenAI",             # OpenAI updates
                "Singularity",        # AGI / future AI
                "Computervision",     # Vision models
                "LanguageTechnology", # NLP / LLM tech
            ]

            # If user passes a subreddit use it, otherwise use the optimized list
            subreddits_to_scan = [subreddit] if subreddit else default_subreddits

            results = []

            for sub in subreddits_to_scan:
                for post in self.reddit.subreddit(sub).hot(limit=limit):
                    # Combine title + selftext snippet (clean)
                    content = f"{post.title} - {post.selftext[:300].strip()}" if post.selftext else post.title

                    results.append({
                        'source': 'reddit',
                        'content': content,
                        'timestamp': post.created_utc
                    })

            return results

        except Exception as e:
            print(f"Reddit API error: {e}")
            return []
