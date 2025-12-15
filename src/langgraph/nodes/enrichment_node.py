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
        # Use json.dumps to ensure valid JSON format that is easy to parse
        import json
        trend['enriched_data'] = json.dumps(enriched)

    print(f"   ✅ Enriched {len(state['trends'])} trends")
    return state