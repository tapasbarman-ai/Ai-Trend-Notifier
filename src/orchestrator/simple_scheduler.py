import schedule
import time
from datetime import datetime
from src.langgraph.graph import run_pipeline


def job():
    print(f"\n{'=' * 60}")
    print(f"🤖 Starting AI Trend Pipeline - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 60}\n")

    try:
        result = run_pipeline()
        trends_count = len(result.get('trends', []))
        print(f"\n✅ Pipeline completed successfully!")
        print(f"📊 Processed {trends_count} trends")
        print(f"⏰ Next run scheduled for tomorrow at 9:00 AM\n")
    except Exception as e:
        print(f"\n❌ Pipeline error: {e}\n")


# Schedule daily at 9 AM
schedule.every().day.at("09:00").do(job)

# Optional: Run immediately on start
print("🚀 Scheduler started!")
print("📅 Pipeline scheduled to run daily at 9:00 AM")
print("🔄 Press Ctrl+C to stop\n")

# Uncomment to run immediately on startup:
# print("▶️  Running pipeline now...")
# job()

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute