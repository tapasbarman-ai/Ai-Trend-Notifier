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

    def calculate_quality_score(self, post):
        """Calculate quality score based on engagement metrics"""
        # Weighted scoring: upvotes (60%), comments (30%), upvote ratio (10%)
        upvote_score = min(post.score / 100, 10) * 0.6  # Max 6 points
        comment_score = min(post.num_comments / 20, 10) * 0.3  # Max 3 points
        ratio_score = post.upvote_ratio * 10 * 0.1  # Max 1 point
        
        return upvote_score + comment_score + ratio_score

    def fetch_trends(self, max_results=30, min_score=10, min_comments=3):
        """
        Fetch high-quality AI trends from Reddit
        
        Args:
            max_results: Maximum number of posts to return (default 30)
            min_score: Minimum upvote score (default 10)
            min_comments: Minimum number of comments (default 3)
        
        Returns:
            List of trend dictionaries sorted by quality score
        """
        try:
            # Curated AI-focused subreddits
            subreddits = [
                "MachineLearning",    # ML research papers / breakthroughs
                "Artificial",         # AI discussions
                "DeepLearning",       # Deep learning papers & models
                "OpenAI",             # OpenAI updates
                "LocalLLaMA",         # Open source LLMs
                "Singularity",        # AGI / future AI
                "ArtificialIntelligence",  # General AI news
            ]

            results = []

            for sub in subreddits:
                try:
                    # Fetch from hot (trending) posts
                    for post in self.reddit.subreddit(sub).hot(limit=20):
                        # Filter out low-quality posts
                        if post.score < min_score or post.num_comments < min_comments:
                            continue
                        
                        # Skip stickied posts (usually announcements)
                        if post.stickied:
                            continue
                        
                        # Calculate quality score
                        quality_score = self.calculate_quality_score(post)
                        
                        # Combine title + selftext snippet
                        content = f"{post.title}"
                        if post.selftext and len(post.selftext) > 50:
                            content += f" - {post.selftext[:400].strip()}"
                        
                        results.append({
                            'source': 'reddit',
                            'content': content,
                            'timestamp': post.created_utc,
                            'quality_score': quality_score,
                            'upvotes': post.score,
                            'comments': post.num_comments,
                            'url': post.url,
                            'subreddit': sub
                        })
                except Exception as e:
                    print(f"Error fetching from r/{sub}: {e}")
                    continue

            # Sort by quality score (highest first)
            results.sort(key=lambda x: x['quality_score'], reverse=True)
            
            # Return top results
            top_results = results[:max_results]
            
            print(f"✅ Fetched {len(top_results)} high-quality Reddit posts (from {len(results)} total)")
            return top_results

        except Exception as e:
            print(f"❌ Reddit API error: {e}")
            return []
