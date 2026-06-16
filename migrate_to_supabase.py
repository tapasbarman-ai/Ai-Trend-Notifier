import os
import sqlite3
from datetime import datetime
from backend.database import engine, Base, SessionLocal
from backend.models import User, Subscriber, Newsletter, Trend

def setup_supabase_tables():
    print("[INFO] Ensuring all tables exist in Supabase PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    print("[INFO] Tables initialized.")

def migrate_users():
    local_db = 'ai_trend_notifier.db'
    if not os.path.exists(local_db):
        print(f"[WARNING] Local database {local_db} not found. Skipping users migration.")
        return

    print("[INFO] Migrating users...")
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, email, hashed_password, is_admin FROM users")
        rows = cursor.fetchall()
        
        session = SessionLocal()
        migrated = 0
        for row in rows:
            user_id, email, hashed_password, is_admin = row
            # Check if user already exists on Supabase
            existing = session.query(User).filter(User.email == email).first()
            if not existing:
                new_user = User(
                    email=email,
                    hashed_password=hashed_password,
                    is_admin=bool(is_admin)
                )
                session.add(new_user)
                migrated += 1
        
        session.commit()
        session.close()
        print(f"[SUCCESS] Migrated {migrated}/{len(rows)} users successfully.")
    except Exception as e:
        print(f"[ERROR] Error migrating users: {e}")
    finally:
        conn.close()

def migrate_subscribers():
    local_db = 'ai_trend_notifier.db'
    if not os.path.exists(local_db):
        print(f"[WARNING] Local database {local_db} not found. Skipping subscribers migration.")
        return

    print("[INFO] Migrating subscribers...")
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, email, subscribed_at, is_active FROM subscribers")
        rows = cursor.fetchall()
        
        session = SessionLocal()
        migrated = 0
        for row in rows:
            sub_id, email, subscribed_at_str, is_active = row
            # Check if subscriber already exists
            existing = session.query(Subscriber).filter(Subscriber.email == email).first()
            if not existing:
                try:
                    subscribed_at = datetime.fromisoformat(subscribed_at_str)
                except Exception:
                    subscribed_at = datetime.now()
                
                new_sub = Subscriber(
                    email=email,
                    subscribed_at=subscribed_at,
                    is_active=bool(is_active)
                )
                session.add(new_sub)
                migrated += 1
        
        session.commit()
        session.close()
        print(f"[SUCCESS] Migrated {migrated}/{len(rows)} subscribers successfully.")
    except Exception as e:
        print(f"[ERROR] Error migrating subscribers: {e}")
    finally:
        conn.close()

def migrate_newsletters():
    local_db = 'ai_trend_notifier.db'
    if not os.path.exists(local_db):
        print(f"[WARNING] Local database {local_db} not found. Skipping newsletters migration.")
        return

    print("[INFO] Migrating newsletters...")
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, title, summary, content, sentiment, published_at FROM newsletters")
        rows = cursor.fetchall()
        
        session = SessionLocal()
        migrated = 0
        for row in rows:
            nl_id, title, summary, content, sentiment, published_at_str = row
            # Check if newsletter already exists (by title)
            existing = session.query(Newsletter).filter(Newsletter.title == title).first()
            if not existing:
                try:
                    published_at = datetime.fromisoformat(published_at_str)
                except Exception:
                    published_at = datetime.now()
                
                new_nl = Newsletter(
                    title=title,
                    summary=summary,
                    content=content,
                    sentiment=sentiment,
                    published_at=published_at
                )
                session.add(new_nl)
                migrated += 1
        
        session.commit()
        session.close()
        print(f"[SUCCESS] Migrated {migrated}/{len(rows)} newsletters successfully.")
    except Exception as e:
        print(f"[ERROR] Error migrating newsletters: {e}")
    finally:
        conn.close()

def migrate_trends():
    local_db = 'data/db/trends.db'
    if not os.path.exists(local_db):
        print(f"[WARNING] Local database {local_db} not found. Skipping trends migration.")
        return

    print("[INFO] Migrating raw trends...")
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, source, content, sentiment, sentiment_label, enriched_data, summary, created_at FROM trends")
        rows = cursor.fetchall()
        
        session = SessionLocal()
        migrated = 0
        for row in rows:
            tr_id, source, content, sentiment, sentiment_label, enriched_data, summary, created_at_str = row
            # Check if trend already exists (by content snippet / source)
            existing = session.query(Trend).filter(
                Trend.source == source, 
                Trend.content.like(f"{content[:50]}%")
            ).first()
            
            if not existing:
                try:
                    created_at = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S')
                except Exception:
                    created_at = datetime.now()
                
                new_trend = Trend(
                    source=source,
                    content=content,
                    sentiment=sentiment,
                    sentiment_label=sentiment_label,
                    enriched_data=enriched_data,
                    summary=summary,
                    created_at=created_at
                )
                session.add(new_trend)
                migrated += 1
        
        session.commit()
        session.close()
        print(f"[SUCCESS] Migrated {migrated}/{len(rows)} raw trends successfully.")
    except Exception as e:
        print(f"[ERROR] Error migrating trends: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("=== STARTING SUPABASE DATABASE MIGRATION ===")
    setup_supabase_tables()
    migrate_users()
    migrate_subscribers()
    migrate_newsletters()
    migrate_trends()
    print("=== MIGRATION COMPLETED SUCCESSFULY ===")
