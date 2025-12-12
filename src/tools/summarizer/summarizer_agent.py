# import sys
# import os
#
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
# from langchain_groq import ChatGroq
# from src.config.settings import GROQ_API_KEY
#
#
# class SummarizerAgent:
#     def __init__(self):
#         self.llm = ChatGroq(
#             api_key=GROQ_API_KEY,
#             model="llama-3.1-8b-instant"
#         )
#
#     def summarize(self, content, enriched_data):
#         try:
#             context = f"Content: {content}\n\nRelated Info: {enriched_data}"
#             prompt = f"Summarize this AI trend in 2-3 sentences:\n{context}"
#             response = self.llm.invoke(prompt)
#             return response.content
#         except Exception as e:
#             print(f"Summarization error: {e}")
#             return "Summary unavailable"

"""
Enhanced Summarizer Agent with structured output
Place at: src/tools/summarizer/summarizer_agent.py
"""

import sys
import os
from typing import Dict, List, Optional

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from langchain_groq import ChatGroq
from src.config.settings import GROQ_API_KEY


class SummarizerAgent:
    """Enhanced AI trend summarizer with better prompt engineering"""

    def __init__(self):
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0.3  # Lower for more focused summaries
        )

    def summarize(self, content: str, enriched_data: Optional[str] = None) -> str:
        """
        Summarize a single trend with context

        Args:
            content: Main trend content
            enriched_data: Additional context from web search

        Returns:
            Clean, concise summary string
        """
        try:
            # Build context
            if enriched_data:
                context = f"Main Content: {content}\n\nAdditional Context: {enriched_data}"
            else:
                context = content

            # Improved prompt for better summaries
            prompt = f"""You are an AI trends analyst. Summarize this AI trend clearly and concisely.

Content to summarize:
{context}

Requirements:
- Write 2-3 clear, informative sentences
- Focus on the key facts and implications
- Avoid speculation or filler words
- Be objective and factual
- Make it engaging but professional

Summary:"""

            response = self.llm.invoke(prompt)
            summary = response.content.strip()

            # Clean up common issues
            summary = self._clean_summary(summary)

            return summary

        except Exception as e:
            print(f"⚠️  Summarization error: {e}")
            # Fallback to truncated original
            return self._fallback_summary(content)

    def summarize_batch(self, trends: List[Dict]) -> List[Dict]:
        """
        Summarize multiple trends efficiently

        Args:
            trends: List of trend dictionaries with 'content' and optionally 'enriched_data'

        Returns:
            List of trends with added 'summary' field
        """
        print(f"📝 Summarizing {len(trends)} trends...")

        summarized_trends = []

        for idx, trend in enumerate(trends, 1):
            try:
                print(f"   Processing trend {idx}/{len(trends)}...", end='\r')

                summary = self.summarize(
                    content=trend.get('content', ''),
                    enriched_data=trend.get('enriched_data', '')
                )

                trend['summary'] = summary
                summarized_trends.append(trend)

            except Exception as e:
                print(f"\n⚠️  Error on trend {idx}: {e}")
                trend['summary'] = self._fallback_summary(trend.get('content', ''))
                summarized_trends.append(trend)

        print(f"\n✅ Summarized {len(summarized_trends)} trends successfully")
        return summarized_trends

    def generate_executive_summary(self, trends: List[Dict]) -> str:
        """
        Generate an overall executive summary of all trends

        Args:
            trends: List of trend dictionaries

        Returns:
            Executive summary string
        """
        try:
            # Prepare trend summaries
            summaries = []
            for idx, trend in enumerate(trends[:10], 1):  # Limit to top 10
                summary = trend.get('summary', trend.get('content', ''))
                sentiment = trend.get('sentiment', 'NEUTRAL')
                summaries.append(f"{idx}. [{sentiment}] {summary[:200]}")

            all_summaries = "\n".join(summaries)

            prompt = f"""You are an AI trends analyst. Create a brief executive summary of today's AI trends.

Today's Trends:
{all_summaries}

Write a 3-4 sentence executive summary that:
- Identifies the main themes or patterns
- Highlights the most significant developments
- Notes the overall sentiment/direction
- Is clear and actionable for business leaders

Executive Summary:"""

            response = self.llm.invoke(prompt)
            return response.content.strip()

        except Exception as e:
            print(f"⚠️  Executive summary error: {e}")
            return "Unable to generate executive summary at this time."

    def generate_headline(self, summary: str) -> str:
        """
        Generate a catchy, concise headline from a trend summary
        
        Args:
            summary: The trend summary text
            
        Returns:
            A short, engaging headline (max 80 characters)
        """
        try:
            prompt = f"""You are a professional headline writer. Create a catchy, concise headline for this AI trend.

Trend Summary:
{summary}

Requirements:
- Maximum 80 characters
- Clear and engaging
- Professional tone
- No clickbait
- Focus on the key insight
- No quotes or special formatting

Headline:"""

            response = self.llm.invoke(prompt)
            headline = response.content.strip()
            
            # Clean up
            headline = headline.replace('"', '').replace("'", "").strip()
            
            # Truncate if too long
            if len(headline) > 80:
                headline = headline[:77] + "..."
                
            return headline
            
        except Exception as e:
            print(f"⚠️  Headline generation error: {e}")
            # Fallback: use first sentence of summary
            return self._extract_title_fallback(summary)
    
    def _extract_title_fallback(self, summary: str) -> str:
        """Fallback title extraction from summary"""
        sentences = summary.split('.')
        if sentences and len(sentences[0]) > 10:
            title = sentences[0].strip()
            if len(title) > 80:
                title = title[:77] + "..."
            return title
        return "AI Trend Update"

    def _clean_summary(self, summary: str) -> str:
        """Clean up common summary issues"""
        # Remove common prefixes
        prefixes = [
            "Summary:", "Here's a summary:", "Here is a summary:",
            "The summary is:", "In summary:", "To summarize:"
        ]

        for prefix in prefixes:
            if summary.lower().startswith(prefix.lower()):
                summary = summary[len(prefix):].strip()

        # Remove markdown formatting
        summary = summary.replace("**", "").replace("*", "")

        # Ensure it ends with proper punctuation
        if summary and summary[-1] not in '.!?':
            summary += '.'

        return summary

    def _fallback_summary(self, content: str, max_length: int = 200) -> str:
        """Fallback summary when LLM fails"""
        if not content:
            return "No content available for summarization."

        # Truncate and add ellipsis
        if len(content) > max_length:
            return content[:max_length].rsplit(' ', 1)[0] + "..."
        return content

    def enhance_trend_quality(self, trend: Dict) -> Dict:
        """
        Enhance a single trend with better summarization and metadata

        Args:
            trend: Trend dictionary

        Returns:
            Enhanced trend with summary and quality score
        """
        try:
            # Generate summary
            trend['summary'] = self.summarize(
                content=trend.get('content', ''),
                enriched_data=trend.get('enriched_data', '')
            )

            # Calculate quality score (0-100)
            quality_score = self._calculate_quality_score(trend)
            trend['quality_score'] = quality_score

            # Extract key entities (optional)
            if trend.get('content'):
                trend['key_points'] = self._extract_key_points(trend['content'])

            return trend

        except Exception as e:
            print(f"⚠️  Enhancement error: {e}")
            return trend

    def _calculate_quality_score(self, trend: Dict) -> int:
        """
        Calculate trend quality score based on various factors

        Returns: Score from 0-100
        """
        score = 50  # Base score

        # Check for content length (not too short, not too long)
        content = trend.get('content', '')
        if 100 <= len(content) <= 1000:
            score += 10
        elif len(content) > 50:
            score += 5

        # Check for enriched data
        if trend.get('enriched_data'):
            score += 15

        # Check for sentiment
        if trend.get('sentiment') in ['POSITIVE', 'NEGATIVE']:
            score += 10

        # Check for summary
        if trend.get('summary') and len(trend['summary']) > 50:
            score += 15

        return min(100, score)

    def _extract_key_points(self, content: str) -> List[str]:
        """Extract key points from content (simple version)"""
        # Split into sentences
        sentences = [s.strip() for s in content.split('.') if s.strip()]

        # Return first 2-3 key sentences
        return sentences[:min(3, len(sentences))]


# Test function
if __name__ == "__main__":
    # Test the summarizer
    agent = SummarizerAgent()

    test_trend = {
        'content': 'AI safety experts are warning about the potential risks of artificial intelligence surpassing human intelligence, which could lead to catastrophic consequences. A notable example is the concept of an AI deciding to eliminate slower-witted humans, highlighting the need for caution and regulation in AI development.',
        'sentiment': 'NEGATIVE',
        'enriched_data': 'Dr. Roman and other experts have been warning about these risks for decades.'
    }

    print("Testing summarization...")
    summary = agent.summarize(test_trend['content'], test_trend['enriched_data'])
    print(f"\nOriginal: {test_trend['content'][:100]}...")
    print(f"\nSummary: {summary}")

    print("\n" + "=" * 50)
    print("Testing batch summarization...")
    trends = [test_trend] * 3
    results = agent.summarize_batch(trends)
    print(f"\nProcessed {len(results)} trends")

    print("\n" + "=" * 50)
    print("Testing executive summary...")
    exec_summary = agent.generate_executive_summary(results)
    print(f"\nExecutive Summary:\n{exec_summary}")