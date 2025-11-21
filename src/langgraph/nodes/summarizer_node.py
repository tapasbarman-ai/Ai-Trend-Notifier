# import sys
# import os
#
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
# from src.tools.summarizer.summarizer_agent import SummarizerAgent
#
#
# def summarizer_node(state):
#     """Summarize each trend using LLM"""
#     print("📝 Summarizer Node: Generating summaries...")
#
#     summarizer = SummarizerAgent()
#
#     for trend in state['trends']:
#         summary = summarizer.summarize(
#             trend['content'],
#             trend.get('enriched_data', '')
#         )
#         trend['summary'] = summary
#
#     print(f"   ✅ Summarized {len(state['trends'])} trends")
#     return state


"""
Summarizer Node for LangGraph Pipeline
Summarizes and enhances trend quality
"""

from typing import Dict, List
from src.tools.summarizer.summarizer_agent import SummarizerAgent


def summarizer_node(state: Dict) -> Dict:
    """
    Summarize enriched trends and add quality metrics

    Args:
        state: Dictionary containing 'trends' key with list of trend dicts

    Returns:
        Updated state with summarized trends
    """
    print("\n" + "=" * 60)
    print("📝 SUMMARIZER NODE - Processing trends...")
    print("=" * 60)

    trends = state.get('trends', [])

    if not trends:
        print("⚠️  No trends to summarize")
        return state

    print(f"📊 Processing {len(trends)} trends for summarization")

    try:
        # Initialize summarizer
        summarizer = SummarizerAgent()

        # Batch summarize all trends
        summarized_trends = summarizer.summarize_batch(trends)

        # Generate executive summary
        print("\n📋 Generating executive summary...")
        exec_summary = summarizer.generate_executive_summary(summarized_trends)

        # Calculate average quality score
        quality_scores = [t.get('quality_score', 0) for t in summarized_trends]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        # Update state
        state['trends'] = summarized_trends
        state['executive_summary'] = exec_summary
        state['average_quality_score'] = round(avg_quality, 2)

        # Print summary stats
        print(f"\n✅ Summarization complete!")
        print(f"   • Trends processed: {len(summarized_trends)}")
        print(f"   • Average quality score: {avg_quality:.1f}/100")
        print(f"\n📊 Executive Summary:")
        print(f"   {exec_summary}")
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"❌ Summarization error: {e}")
        state['summarization_error'] = str(e)
        # Keep original trends if summarization fails
        if 'trends' not in state:
            state['trends'] = trends

    return state


# Alternative: Enhanced version with filtering
def enhanced_summarizer_node(state: Dict) -> Dict:
    """
    Enhanced version with quality filtering
    Only keeps high-quality trends
    """
    print("\n" + "=" * 60)
    print("📝 ENHANCED SUMMARIZER NODE - Processing trends...")
    print("=" * 60)

    trends = state.get('trends', [])

    if not trends:
        print("⚠️  No trends to summarize")
        return state

    print(f"📊 Processing {len(trends)} trends")

    try:
        summarizer = SummarizerAgent()

        # Enhance each trend
        enhanced_trends = []
        for idx, trend in enumerate(trends, 1):
            print(f"   Enhancing trend {idx}/{len(trends)}...", end='\r')
            enhanced = summarizer.enhance_trend_quality(trend)
            enhanced_trends.append(enhanced)

        print(f"\n✅ Enhanced {len(enhanced_trends)} trends")

        # Filter by quality score (optional)
        quality_threshold = state.get('quality_threshold', 50)
        high_quality_trends = [
            t for t in enhanced_trends
            if t.get('quality_score', 0) >= quality_threshold
        ]

        print(f"🔍 Filtered to {len(high_quality_trends)} high-quality trends (score >= {quality_threshold})")

        # Generate executive summary
        exec_summary = summarizer.generate_executive_summary(high_quality_trends)

        # Update state
        state['trends'] = high_quality_trends
        state['all_trends'] = enhanced_trends  # Keep all for reference
        state['executive_summary'] = exec_summary
        state['filtered_count'] = len(trends) - len(high_quality_trends)

        print(f"\n📊 Executive Summary:")
        print(f"   {exec_summary}")
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"❌ Enhanced summarization error: {e}")
        state['summarization_error'] = str(e)
        state['trends'] = trends

    return state


# Quick test function
if __name__ == "__main__":
    # Test with sample state
    test_state = {
        'trends': [
            {
                'content': 'AI safety experts warn about superintelligence risks...',
                'sentiment': 'NEGATIVE',
                'enriched_data': 'Multiple experts have raised concerns'
            },
            {
                'content': 'New AI model achieves breakthrough in efficiency...',
                'sentiment': 'POSITIVE',
                'enriched_data': 'Research published in Nature'
            }
        ]
    }

    print("Testing summarizer node...")
    result = summarizer_node(test_state)

    print("\nResults:")
    for idx, trend in enumerate(result['trends'], 1):
        print(f"\n{idx}. Summary: {trend.get('summary', 'N/A')}")
        print(f"   Quality: {trend.get('quality_score', 'N/A')}/100")