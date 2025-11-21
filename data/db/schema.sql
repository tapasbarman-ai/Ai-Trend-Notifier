
CREATE TABLE IF NOT EXISTS trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    content TEXT NOT NULL,
    sentiment REAL,
    sentiment_label TEXT,
    enriched_data TEXT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_created_at ON trends(created_at);
CREATE INDEX IF NOT EXISTS idx_sentiment ON trends(sentiment);
