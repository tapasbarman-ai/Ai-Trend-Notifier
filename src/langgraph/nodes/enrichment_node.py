import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from src.tools.websearch.websearch_agent import WebSearchAgent


def enrichment_node(state):
    """Enrich trends with web search results"""
    print("🔍 Enrichment Node: Searching web for context...")

    search = WebSearchAgent()

    for trend in state['trends']:
        query = trend['content'][:100]
        enriched = search.search(query)
        trend['enriched_data'] = str(enriched)

    print(f"   ✅ Enriched {len(state['trends'])} trends")
    return state