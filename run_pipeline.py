"""
Standalone script to run the pipeline once
Usage: python run_pipeline.py
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.langgraph.graph import run_pipeline
from datetime import datetime

if __name__ == "__main__":
    print(f"\n{'=' * 50}")
    print(f"Starting AI Trend Pipeline - {datetime.now()}")
    print(f"{'=' * 50}\n")

    try:
        result = run_pipeline()
        print(f"\n✅ Pipeline completed successfully!")
        print(f"Processed {len(result.get('trends', []))} trends")
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        import traceback

        traceback.print_exc()

    print(f"\n{'=' * 50}")
    print(f"Finished - {datetime.now()}")
    print(f"{'=' * 50}\n")