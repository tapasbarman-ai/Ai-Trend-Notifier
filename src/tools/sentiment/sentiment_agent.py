import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from transformers import pipeline


class SentimentAgent:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze(self, text):
        try:
            result = self.analyzer(text[:512])[0]
            return {
                'sentiment_label': result['label'],
                'sentiment_score': result['score']
            }
        except Exception as e:
            print(f"Sentiment analysis error: {e}")
            return {'sentiment_label': 'NEUTRAL', 'sentiment_score': 0.5}