import os
import sys
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    print("[ERROR] DATABASE_URL env variable is not set in .env")
    sys.exit(1)

print("[INFO] Testing connection to database...")
try:
    engine = create_engine(db_url)
    conn = engine.connect()
    print("[SUCCESS] Successfully connected to the database!")
    conn.close()
except Exception as e:
    print(f"[ERROR] Failed to connect: {e}")
    sys.exit(1)
