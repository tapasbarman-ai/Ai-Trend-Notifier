import sqlite3
import os

# Create directory
os.makedirs('data/db', exist_ok=True)

# Connect and create tables
conn = sqlite3.connect('data/db/trends.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    content TEXT NOT NULL,
    sentiment REAL,
    sentiment_label TEXT,
    enriched_data TEXT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_created_at ON trends(created_at)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_sentiment ON trends(sentiment)')

conn.commit()
conn.close()

print("✅ Database initialized successfully!")