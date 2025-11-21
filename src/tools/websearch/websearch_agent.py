import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tavily import TavilyClient
from src.config.settings import TAVILY_API_KEY


class WebSearchAgent:
    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def search(self, query, max_results=3):
        try:
            results = self.client.search(query, max_results=max_results)
            enriched = []
            for r in results.get('results', []):
                enriched.append({
                    'title': r.get('title'),
                    'url': r.get('url'),
                    'snippet': r.get('content', '')[:200]
                })
            return enriched
        except Exception as e:
            print(f"Web search error: {e}")
            return []