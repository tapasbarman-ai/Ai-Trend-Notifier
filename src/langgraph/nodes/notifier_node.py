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

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        saved_count = 0

        for trend in trends:
            try:
                cursor.execute('''
                    INSERT INTO trends (
                        source, 
                        content, 
                        sentiment, 
                        sentiment_label, 
                        enriched_data, 
                        summary,
                        created_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    trend.get('source', 'unknown'),
                    trend.get('content', ''),
                    trend.get('sentiment_score', 0.5),
                    trend.get('sentiment', 'NEUTRAL'),
                    trend.get('enriched_data', ''),
                    trend.get('summary', ''),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                saved_count += 1

            except sqlite3.IntegrityError:
                continue
            except Exception as e:
                print(f"   ⚠️  Error saving trend: {e}")
                continue

        conn.commit()
        conn.close()

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

        # Send email using send_summary (reads RECIPIENT_EMAIL from settings)
        email_success = email_agent.send_summary(
            trends=trends,
            executive_summary=executive_summary
        )

        if email_success:
            print(f"✅ HTML email sent successfully to {email_agent.recipient}")
            state['email_sent'] = True
        else:
            print("❌ Failed to send email")
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
