# import sys
# import os
#
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
# import tweepy
# from src.config.settings import TWITTER_BEARER_TOKEN
#
#
# class TwitterAgent:
#     def __init__(self):
#         self.client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
#
#     def fetch_trends(self, query="AI OR artificial intelligence", max_results=10):
#         try:
#             tweets = self.client.search_recent_tweets(
#                 query=query,
#                 max_results=max_results,
#                 tweet_fields=['created_at', 'public_metrics']
#             )
#
#             results = []
#             if tweets.data:
#                 for tweet in tweets.data:
#                     results.append({
#                         'source': 'twitter',
#                         'content': tweet.text,
#                         'timestamp': tweet.created_at
#                     })
#             return results
#         except Exception as e:
#             print(f"Twitter API error: {e}")
#             return []

"""
Fixed Twitter Agent with Shorter Query
Place at: src/tools/twitter/twitter_agent.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import requests
from src.config.settings import TWITTER_BEARER_TOKEN


class TwitterAgent:
    """Fetch AI trends from Twitter using API v2"""

    def __init__(self):
        self.bearer_token = TWITTER_BEARER_TOKEN
        self.base_url = "https://api.twitter.com/2/tweets/search/recent"

    def fetch_trends(self, max_results=50):
        """
        Fetch recent AI-related tweets

        Args:
            max_results: Number of tweets to fetch (10-100, default 50)

        Returns:
            List of trend dictionaries
        """
        if not self.bearer_token:
            print("⚠️  Twitter Bearer Token not configured")
            return []

        try:
            # FIXED: Shorter query that fits within 512 character limit
            # Old query was 650 characters, new is ~380 characters
            query = (
                '("AI research" OR "new AI model" OR LLM OR "large language model" OR '
                '"transformer" OR "multimodal" OR "AI breakthrough" OR "research paper" OR '
                'arxiv OR "SOTA" OR "state-of-the-art" OR benchmark OR "model release" OR '
                'AGI OR "deep learning" OR "generative AI" OR OpenAI OR DeepMind OR '
                'Anthropic OR "Meta AI" OR Mistral OR Gemini OR "scaling law" OR '
                '"alignment research" OR "neural network" OR "diffusion model" OR '
                '"foundation model") lang:en -is:retweet -is:reply'
            )

            # Verify query length
            print(f"🔍 Query length: {len(query)}/512 characters")

            if len(query) > 512:
                print("⚠️  WARNING: Query still too long, using minimal query")
                # Fallback to minimal query
                query = '("AI" OR "artificial intelligence" OR "machine learning") lang:en -is:retweet'

            headers = {
                "Authorization": f"Bearer {self.bearer_token}",
                "Content-Type": "application/json"
            }

            params = {
                "query": query,
                "max_results": min(max_results, 100),  # API max is 100
                "tweet.fields": "created_at,public_metrics,author_id",
                "expansions": "author_id",
                "user.fields": "username,name"
            }

            print(f"🐦 Fetching {max_results} tweets from Twitter...")
            response = requests.get(self.base_url, headers=headers, params=params)

            if response.status_code == 429:
                print("⚠️  Twitter API rate limit reached. Try again later.")
                return []

            if response.status_code != 200:
                print(f"Twitter API error: {response.status_code} {response.reason}")
                print(response.text)
                return []

            data = response.json()

            if "data" not in data or not data["data"]:
                print("⚠️  No tweets found")
                return []

            # Parse tweets
            tweets = data.get("data", [])
            users = {user["id"]: user for user in data.get("includes", {}).get("users", [])}

            trends = []
            for tweet in tweets:
                author = users.get(tweet.get("author_id"), {})

                trends.append({
                    "source": "twitter",
                    "content": tweet.get("text", ""),
                    "author": author.get("username", "unknown"),
                    "author_name": author.get("name", "Unknown"),
                    "created_at": tweet.get("created_at", ""),
                    "metrics": tweet.get("public_metrics", {}),
                    "tweet_id": tweet.get("id", "")
                })

            print(f"✅ Fetched {len(trends)} tweets from Twitter")
            return trends

        except requests.exceptions.RequestException as e:
            print(f"❌ Twitter request error: {e}")
            return []
        except Exception as e:
            print(f"❌ Twitter error: {e}")
            return []


# Alternative queries if you need even shorter ones
QUERY_VARIANTS = {
    # MINIMAL - 98 characters (most reliable)
    "minimal": '("AI" OR "artificial intelligence" OR "machine learning") lang:en -is:retweet',

    # SHORT - 215 characters
    "short": (
        '("AI research" OR "new AI model" OR LLM OR "AI breakthrough" OR '
        'OpenAI OR DeepMind OR Anthropic OR Gemini) lang:en -is:retweet -is:reply'
    ),

    # MEDIUM - 380 characters (current default)
    "medium": (
        '("AI research" OR "new AI model" OR LLM OR "large language model" OR '
        '"transformer" OR "multimodal" OR "AI breakthrough" OR "research paper" OR '
        'arxiv OR "SOTA" OR "state-of-the-art" OR benchmark OR "model release" OR '
        'AGI OR "deep learning" OR "generative AI" OR OpenAI OR DeepMind OR '
        'Anthropic OR "Meta AI" OR Mistral OR Gemini OR "scaling law" OR '
        '"alignment research" OR "neural network" OR "diffusion model" OR '
        '"foundation model") lang:en -is:retweet -is:reply'
    ),

    # FOCUSED - 245 characters (good balance)
    "focused": (
        '("AI model" OR "LLM" OR "GPT" OR "Claude" OR "Gemini" OR "Llama" OR '
        '"AI research" OR "ML research" OR "deep learning" OR OpenAI OR DeepMind OR '
        'Anthropic OR "Meta AI") lang:en -is:retweet -is:reply'
    )
}


class TwitterAgentConfigurable(TwitterAgent):
    """Twitter agent with configurable query presets"""

    def __init__(self, query_type="medium"):
        """
        Initialize with query preset

        Args:
            query_type: One of 'minimal', 'short', 'medium', 'focused'
        """
        super().__init__()
        self.query_type = query_type
        self.query = QUERY_VARIANTS.get(query_type, QUERY_VARIANTS["medium"])

        print(f"📝 Using '{query_type}' query preset ({len(self.query)} chars)")

    def fetch_trends(self, max_results=50):
        """Fetch trends using preset query"""
        if not self.bearer_token:
            print("⚠️  Twitter Bearer Token not configured")
            return []

        try:
            headers = {
                "Authorization": f"Bearer {self.bearer_token}",
                "Content-Type": "application/json"
            }

            params = {
                "query": self.query,
                "max_results": min(max_results, 100),
                "tweet.fields": "created_at,public_metrics,author_id",
                "expansions": "author_id",
                "user.fields": "username,name"
            }

            print(f"🐦 Fetching {max_results} tweets from Twitter...")
            response = requests.get(self.base_url, headers=headers, params=params)

            if response.status_code == 429:
                print("⚠️  Twitter API rate limit reached. Try again later.")
                return []

            if response.status_code != 200:
                print(f"Twitter API error: {response.status_code} {response.reason}")
                print(response.text)
                return []

            data = response.json()

            if "data" not in data or not data["data"]:
                print("⚠️  No tweets found")
                return []

            tweets = data.get("data", [])
            users = {user["id"]: user for user in data.get("includes", {}).get("users", [])}

            trends = []
            for tweet in tweets:
                author = users.get(tweet.get("author_id"), {})

                trends.append({
                    "source": "twitter",
                    "content": tweet.get("text", ""),
                    "author": author.get("username", "unknown"),
                    "author_name": author.get("name", "Unknown"),
                    "created_at": tweet.get("created_at", ""),
                    "metrics": tweet.get("public_metrics", {}),
                    "tweet_id": tweet.get("id", "")
                })

            print(f"✅ Fetched {len(trends)} tweets from Twitter")
            return trends

        except requests.exceptions.RequestException as e:
            print(f"❌ Twitter request error: {e}")
            return []
        except Exception as e:
            print(f"❌ Twitter error: {e}")
            return []


# Test function
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Testing Twitter Agent")
    print("=" * 60)

    # Test default agent
    print("\n1. Testing default (medium) query:")
    agent = TwitterAgent()
    trends = agent.fetch_trends(max_results=10)

    if trends:
        print(f"\n✅ Success! Got {len(trends)} tweets")
        print("\nSample tweet:")
        print(f"  Author: @{trends[0]['author']}")
        print(f"  Content: {trends[0]['content'][:100]}...")
    else:
        print("\n⚠️  No results. Trying focused query...")

        # Try with focused query
        agent2 = TwitterAgentConfigurable(query_type="focused")
        trends2 = agent2.fetch_trends(max_results=10)

        if trends2:
            print(f"\n✅ Success with focused query! Got {len(trends2)} tweets")
        else:
            print("\n⚠️  Still no results. Check your Twitter API credentials.")

    print("\n" + "=" * 60)
    print("💡 TIP: If queries fail, try different presets:")
    print("  - 'minimal': Broadest search, most reliable")
    print("  - 'focused': Company names and model names")
    print("  - 'short': Key AI terms only")
    print("  - 'medium': Default, balanced coverage")
    print("=" * 60)