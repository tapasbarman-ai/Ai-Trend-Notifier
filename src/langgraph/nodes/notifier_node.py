# import sys
# import os
#
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
# import sqlite3
# from src.config.settings import DB_PATH
# from src.tools.notifier.email_agent import EmailAgent
#
#
# def notifier_node(state):
#     """Save trends to database and send email notification"""
#     print("💾 Notifier Node: Saving to database and sending email...")
#
#     # Save to database
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#
#     for trend in state['trends']:
#         cursor.execute('''
#             INSERT INTO trends (source, content, sentiment, sentiment_label, enriched_data, summary)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (
#             trend['source'],
#             trend['content'],
#             trend.get('sentiment_score', 0.5),
#             trend.get('sentiment_label', 'NEUTRAL'),
#             trend.get('enriched_data', ''),
#             trend.get('summary', '')
#         ))
#
#     conn.commit()
#     conn.close()
#
#     print(f"   ✅ Saved {len(state['trends'])} trends to database")
#
#     # Send email
#     try:
#         email = EmailAgent()
#         email.send_summary(state['trends'])
#         print("   ✅ Email notification sent")
#     except Exception as e:
#         print(f"   ⚠️  Email sending failed: {e}")
#
#     return state
#
#

"""
Fixed Notifier Node - Works with updated EmailAgent
Place at: src/langgraph/nodes/notifier_node.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import sqlite3
from typing import Dict
from datetime import datetime
from src.config.settings import DB_PATH
from src.tools.notifier.email_agent import EmailAgent


def notifier_node(state: Dict) -> Dict:
    """
    Save trends to database and send beautiful HTML email notification

    Args:
        state: Dictionary containing 'trends' and optionally 'executive_summary'

    Returns:
        Updated state with database and email status
    """
    print("\n" + "=" * 60)
    print("💾 NOTIFIER NODE - Saving & Sending...")
    print("=" * 60)

    trends = state.get('trends', [])

    if not trends:
        print("⚠️  No trends to process")
        state['db_saved'] = False
        state['email_sent'] = False
        return state

    # Initialize status tracking
    db_success = False
    email_success = False

    # ============================================================
    # PART 1: Save to Database
    # ============================================================
    try:
        print(f"\n💾 Saving {len(trends)} trends to database...")

        from backend.database import SessionLocal
        from backend.models import Trend

        session = SessionLocal()
        saved_count = 0

        for trend in trends:
            try:
                new_trend = Trend(
                    source=trend.get('source', 'unknown'),
                    content=trend.get('content', ''),
                    sentiment=trend.get('sentiment_score', 0.5),
                    sentiment_label=trend.get('sentiment', 'NEUTRAL'),
                    enriched_data=trend.get('enriched_data', ''),
                    summary=trend.get('summary', ''),
                    created_at=datetime.now()
                )
                session.add(new_trend)
                saved_count += 1
            except Exception as e:
                print(f"   ⚠️  Error processing trend for database: {e}")
                continue

        session.commit()
        session.close()

        print(f"✅ Successfully saved {saved_count}/{len(trends)} trends to database")
        db_success = True
        state['db_saved'] = True
        state['saved_count'] = saved_count

    except Exception as e:
        print(f"❌ Database error: {e}")
        state['db_saved'] = False
        state['db_error'] = str(e)
        db_success = False

    # ============================================================
    # PART 2: Send HTML Email
    # ============================================================
    try:
        print(f"\n📧 Preparing HTML email notification...")

        email_agent = EmailAgent()

        # Get executive summary if available
        executive_summary = state.get('executive_summary', None)

        # 1. Fetch subscribers from the unified database using SQLAlchemy
        subscribers = []
        try:
            from backend.database import SessionLocal
            from backend.models import Subscriber

            session = SessionLocal()
            active_subs = session.query(Subscriber).filter(Subscriber.is_active == True).all()
            subscribers = [sub.email for sub in active_subs]
            session.close()
            print(f"   Found {len(subscribers)} active subscribers in DB.")
        except Exception as db_err:
             print(f"   ⚠️ Error fetching subscribers: {db_err}")
             # Fallback
             if email_agent.recipient:
                 subscribers = [email_agent.recipient]

        # Ensure we at least have the default recipient if list is empty (for testing)
        if not subscribers and email_agent.recipient:
             print("   No subscribers found in DB, using default RECIPIENT_EMAIL.")
             subscribers = [email_agent.recipient]
        
        # Remove duplicates
        subscribers = list(set(subscribers))

        # 2. Send to all subscribers
        sent_count = 0
        failed_count = 0
        
        print(f"   Sending to {len(subscribers)} recipients...")
        
        for sub_email in subscribers:
            if email_agent.send_email(
                to_email=sub_email,
                trends=trends,
                executive_summary=executive_summary
            ):
                sent_count += 1
            else:
                failed_count += 1

        if sent_count > 0:
            print(f"✅ HTML email sent successfully to {sent_count} recipients ({failed_count} failed)")
            email_success = True
            state['email_sent'] = True
        else:
            print("❌ Failed to send any emails")
            state['email_sent'] = False

    except Exception as e:
        print(f"❌ Email error: {e}")
        state['email_sent'] = False
        state['email_error'] = str(e)
        email_success = False


    # ============================================================
    # PART 3: Summary & Status
    # ============================================================
    print("\n" + "=" * 60)
    print("📊 NOTIFIER SUMMARY")
    print("=" * 60)
    print(f"✓ Trends processed: {len(trends)}")
    print(f"✓ Database saved: {'✅ Yes' if db_success else '❌ No'}")
    print(f"✓ Email sent: {'✅ Yes' if email_success else '❌ No'}")

    if executive_summary:
        print(f"✓ Executive summary included: ✅ Yes")

    if state.get('average_quality_score'):
        print(f"✓ Average quality score: {state['average_quality_score']}/100")

    print("=" * 60 + "\n")

    return state


# Test function
if __name__ == "__main__":
    test_state = {
        'trends': [
            {
                'source': 'reddit',
                'content': 'AI safety breakthrough announced...',
                'sentiment': 'POSITIVE',
                'sentiment_score': 0.8,
                'summary': 'Major AI safety breakthrough.',
                'enriched_data': 'Published in Nature.'
            }
        ],
        'executive_summary': 'Test executive summary'
    }

    print("Testing notifier node...")
    result = notifier_node(test_state)
    print(f"\nResults: DB={result.get('db_saved')}, Email={result.get('email_sent')}")
