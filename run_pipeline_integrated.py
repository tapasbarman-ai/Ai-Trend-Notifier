import sys
import os
import sqlite3
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.langgraph.graph import run_pipeline
from backend.database import SQLALCHEMY_DATABASE_URL
from groq import Groq
from src.config.settings import GROQ_API_KEY

def generate_title_from_summary(summary, groq_client):
    """Generate a catchy newsletter title from the summary using LLM"""
    try:
        prompt = f"""Generate a short, catchy newsletter title (max 8 words) for this AI trend:

{summary}

Title should be:
- Concise and attention-grabbing
- Highlight the key innovation or topic
- Professional but engaging
- No quotes or extra punctuation

Just output the title, nothing else."""

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=50
        )
        
        title = response.choices[0].message.content.strip()
        # Remove quotes if LLM added them
        title = title.strip('"').strip("'")
        return title
    except Exception as e:
        print(f"Error generating title: {e}")
        return None

def save_trends_to_new_db(trends):
    # Parse the URL to get the file path
    db_path = SQLALCHEMY_DATABASE_URL.replace("sqlite:///", "")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Initialize Groq client for title generation
    groq_client = None
    if GROQ_API_KEY:
        groq_client = Groq(api_key=GROQ_API_KEY)
    
    saved_count = 0
    for trend in trends:
        try:
            summary = trend.get('summary', '')
            
            # Generate title using LLM
            if groq_client and summary:
                title = generate_title_from_summary(summary, groq_client)
                if not title:
                    # Fallback: use first 60 chars of summary
                    title = summary[:60] + "..." if len(summary) > 60 else summary
            else:
                # Fallback: use first 60 chars of summary
                title = summary[:60] + "..." if len(summary) > 60 else summary
            
            # Get sentiment - check multiple possible keys
            sentiment = (
                trend.get('sentiment_label') or 
                trend.get('sentiment') or 
                'Neutral'
            )
            
            # Normalize sentiment to match expected values
            sentiment_map = {
                'POSITIVE': 'Positive',
                'NEGATIVE': 'Negative',
                'NEUTRAL': 'Neutral',
                'positive': 'Positive',
                'negative': 'Negative',
                'neutral': 'Neutral'
            }
            sentiment = sentiment_map.get(sentiment, sentiment)
            
            content = f"{trend.get('content', '')}\n\nEnriched Data:\n{trend.get('enriched_data', '')}"
            
            cursor.execute('''
                INSERT INTO newsletters (title, summary, content, sentiment, published_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, summary, content, sentiment, datetime.now()))
            saved_count += 1
        except Exception as e:
            print(f"Error saving trend: {e}")
            
    conn.commit()
    conn.close()
    return saved_count

if __name__ == "__main__":
    print("Starting Integrated Pipeline...")
    try:
        # Run the existing pipeline
        result = run_pipeline()
        trends = result.get('trends', [])
        
        if trends:
            print(f"Pipeline found {len(trends)} trends. Saving to new database...")
            count = save_trends_to_new_db(trends)
            print(f"Successfully saved {count} newsletters to the website database.")
        else:
            print("No trends found.")
            
    except Exception as e:
        print(f"Pipeline failed: {e}")
        import traceback
        traceback.print_exc()
