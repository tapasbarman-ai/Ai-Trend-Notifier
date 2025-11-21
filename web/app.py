import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.langgraph.graph import run_pipeline

# Page config
st.set_page_config(
    page_title="AI Trends Newsletter",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }

    /* Newsletter card */
    .newsletter-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Trend card */
    .trend-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #764ba2;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }

    .trend-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Sentiment badges */
    .sentiment-positive {
        background: #10b981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }

    .sentiment-negative {
        background: #ef4444;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }

    .sentiment-neutral {
        background: #6b7280;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }

    /* Source badges */
    .source-badge {
        background: #667eea;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
    }

    /* Subscriber form */
    .subscribe-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

DB_PATH = "data/db/trends.db"
NEWSLETTER_DB = "data/db/newsletter.db"


# Initialize newsletter database
def init_newsletter_db():
    conn = sqlite3.connect(NEWSLETTER_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            active INTEGER DEFAULT 1
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sent_newsletters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            recipient_count INTEGER
        )
    ''')
    conn.commit()
    conn.close()


init_newsletter_db()

# Sidebar navigation
with st.sidebar:
    st.markdown("# 🤖 AI Trends")
    st.markdown("### Newsletter Platform")
    st.markdown("---")

    page = st.radio(
        "Navigate",
        ["📰 Newsletter", "📊 Analytics", "👥 Subscribers", "⚙️ Settings"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    if st.button("🔄 Fetch New Trends", use_container_width=True):
        with st.spinner("Running pipeline..."):
            try:
                run_pipeline()
                st.success("✅ Trends updated!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    # Quick stats
    try:
        conn = sqlite3.connect(NEWSLETTER_DB)
        sub_count = pd.read_sql_query("SELECT COUNT(*) as count FROM subscribers WHERE active=1", conn)
        conn.close()

        st.markdown("---")
        st.metric("📬 Subscribers", sub_count['count'].iloc[0])
    except:
        pass


# Fetch data
@st.cache_data(ttl=300)
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM trends ORDER BY created_at DESC", conn)
    conn.close()
    return df


# =======================
# NEWSLETTER PAGE
# =======================
if page == "📰 Newsletter":
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Trends Newsletter</h1>
        <p style="font-size: 1.1rem; margin-top: 0.5rem;">
            Your daily dose of AI innovation, research, and industry insights
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Two column layout
    col1, col2 = st.columns([2, 1])

    with col1:
        try:
            df = load_data()

            if df.empty:
                st.info("📭 No trends available yet. Click 'Fetch New Trends' to get started!")
            else:
                # Latest newsletter preview
                st.markdown("## 📬 Latest Edition")
                st.markdown(f"*Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")

                # Top metrics
                col_m1, col_m2, col_m3 = st.columns(3)
                with col_m1:
                    st.metric("📊 Total Trends", len(df))
                with col_m2:
                    positive = len(df[df['sentiment_label'] == 'POSITIVE'])
                    st.metric("😊 Positive", positive, delta=f"{positive / len(df) * 100:.0f}%")
                with col_m3:
                    avg_sentiment = df['sentiment'].mean()
                    st.metric("🎯 Avg Score", f"{avg_sentiment:.2f}")

                st.markdown("---")

                # Display trends as newsletter cards
                st.markdown("### 🔥 Today's Top AI Trends")

                for idx, row in df.head(10).iterrows():
                    sentiment_class = f"sentiment-{row['sentiment_label'].lower()}"

                    st.markdown(f"""
                    <div class="trend-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                            <div>
                                <span class="source-badge">{row['source'].upper()}</span>
                                <span class="{sentiment_class}">{row['sentiment_label']}</span>
                            </div>
                            <span style="color: #6b7280; font-size: 0.85rem;">{row['created_at']}</span>
                        </div>
                        <h4 style="margin: 0.5rem 0; color: #1f2937;">
                            {row['content'][:100]}...
                        </h4>
                        <p style="color: #4b5563; margin: 1rem 0;">
                            {row['summary']}
                        </p>
                        <div style="color: #6b7280; font-size: 0.85rem;">
                            Sentiment Score: {row['sentiment']:.2f}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error loading trends: {e}")

    with col2:
        # Subscribe form
        st.markdown("""
        <div class="subscribe-box">
            <h3 style="margin-top: 0;">📬 Subscribe</h3>
            <p>Get AI trends delivered to your inbox daily</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("subscribe_form"):
            name = st.text_input("Your Name", placeholder="John Doe")
            email = st.text_input("Email Address", placeholder="john@example.com")
            agree = st.checkbox("I agree to receive daily AI trend updates")

            submit = st.form_submit_button("🚀 Subscribe Now", use_container_width=True)

            if submit:
                if name and email and agree:
                    conn = sqlite3.connect(NEWSLETTER_DB)
                    cursor = conn.cursor()
                    try:
                        cursor.execute(
                            "INSERT INTO subscribers (name, email) VALUES (?, ?)",
                            (name, email)
                        )
                        conn.commit()
                        st.success(f"✅ Welcome aboard, {name}!")
                        st.balloons()
                    except sqlite3.IntegrityError:
                        st.warning("⚠️ This email is already subscribed!")
                    finally:
                        conn.close()
                else:
                    st.error("Please fill all fields and agree to terms")

        st.markdown("---")

        # Why subscribe
        st.markdown("### ✨ Why Subscribe?")
        st.markdown("""
        - 🤖 Daily AI trend summaries
        - 🎯 Sentiment analysis insights
        - 🔍 Curated from Twitter & Reddit
        - 📊 Key metrics and analytics
        - 🚀 Delivered at 9 AM daily
        """)

# =======================
# ANALYTICS PAGE
# =======================
elif page == "📊 Analytics":
    st.markdown("# 📊 Analytics Dashboard")

    try:
        df = load_data()

        if df.empty:
            st.info("No data to analyze yet.")
        else:
            # Metrics row
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("📰 Total Trends", len(df))
            with col2:
                positive = len(df[df['sentiment_label'] == 'POSITIVE'])
                st.metric("😊 Positive", positive, delta=f"+{positive / len(df) * 100:.0f}%")
            with col3:
                negative = len(df[df['sentiment_label'] == 'NEGATIVE'])
                st.metric("😞 Negative", negative)
            with col4:
                avg_sentiment = df['sentiment'].mean()
                delta_color = "normal" if avg_sentiment > 0.5 else "inverse"
                st.metric("🎯 Avg Sentiment", f"{avg_sentiment:.2f}")

            st.markdown("---")

            # Charts
            col_c1, col_c2 = st.columns(2)

            with col_c1:
                st.subheader("📈 Sentiment Distribution")
                fig = px.pie(
                    df,
                    names='sentiment_label',
                    color='sentiment_label',
                    color_discrete_map={
                        'POSITIVE': '#10b981',
                        'NEGATIVE': '#ef4444',
                        'NEUTRAL': '#6b7280'
                    },
                    hole=0.4
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig, use_container_width=True)

            with col_c2:
                st.subheader("📊 Source Distribution")
                source_counts = df['source'].value_counts()
                fig2 = px.bar(
                    x=source_counts.index,
                    y=source_counts.values,
                    labels={'x': 'Source', 'y': 'Count'},
                    color=source_counts.values,
                    color_continuous_scale='Purples'
                )
                st.plotly_chart(fig2, use_container_width=True)

            # Timeline
            st.subheader("📅 Trends Timeline")
            df['created_at'] = pd.to_datetime(df['created_at'])
            daily_counts = df.groupby(df['created_at'].dt.date).agg({
                'id': 'count',
                'sentiment': 'mean'
            }).reset_index()
            daily_counts.columns = ['date', 'count', 'avg_sentiment']

            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(
                x=daily_counts['date'],
                y=daily_counts['count'],
                mode='lines+markers',
                name='Trend Count',
                line=dict(color='#667eea', width=3),
                marker=dict(size=8)
            ))
            fig3.update_layout(
                title='Daily Trend Activity',
                xaxis_title='Date',
                yaxis_title='Number of Trends'
            )
            st.plotly_chart(fig3, use_container_width=True)

            # Sentiment timeline
            st.subheader("🎭 Sentiment Over Time")
            fig4 = go.Figure()
            fig4.add_trace(go.Scatter(
                x=daily_counts['date'],
                y=daily_counts['avg_sentiment'],
                mode='lines+markers',
                name='Avg Sentiment',
                line=dict(color='#764ba2', width=3),
                marker=dict(size=8),
                fill='tozeroy'
            ))
            fig4.update_layout(
                xaxis_title='Date',
                yaxis_title='Average Sentiment Score'
            )
            st.plotly_chart(fig4, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

# =======================
# SUBSCRIBERS PAGE
# =======================
elif page == "👥 Subscribers":
    st.markdown("# 👥 Subscriber Management")

    # Password protection
    password = st.text_input("Admin Password", type="password")

    if password == "admin123":  # Change this!
        st.success("✅ Access Granted")

        conn = sqlite3.connect(NEWSLETTER_DB)
        subscribers = pd.read_sql_query("SELECT * FROM subscribers ORDER BY subscribed_at DESC", conn)
        conn.close()

        # Stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total Subscribers", len(subscribers))
        with col2:
            active = len(subscribers[subscribers['active'] == 1])
            st.metric("✅ Active", active)
        with col3:
            today = datetime.now().date()
            new_today = len(subscribers[pd.to_datetime(subscribers['subscribed_at']).dt.date == today])
            st.metric("🆕 New Today", new_today, delta=f"+{new_today}")

        st.markdown("---")

        # Subscriber list
        st.subheader("📋 All Subscribers")

        if not subscribers.empty:
            # Format dates
            subscribers['subscribed_at'] = pd.to_datetime(subscribers['subscribed_at']).dt.strftime('%Y-%m-%d %H:%M')

            st.dataframe(
                subscribers[['name', 'email', 'subscribed_at', 'active']],
                use_container_width=True,
                hide_index=True
            )

            # Download button
            csv = subscribers.to_csv(index=False)
            st.download_button(
                "📥 Download Subscriber List (CSV)",
                csv,
                "subscribers.csv",
                "text/csv",
                use_container_width=True
            )
        else:
            st.info("No subscribers yet!")

    elif password:
        st.error("❌ Incorrect password")

# =======================
# SETTINGS PAGE
# =======================
elif page == "⚙️ Settings":
    st.markdown("# ⚙️ Settings")

    tab1, tab2, tab3 = st.tabs(["📧 Email", "🤖 Pipeline", "🗄️ Database"])

    with tab1:
        st.subheader("Email Configuration")
        st.info("Configure your SMTP settings in the `.env` file")

        st.code("""
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@gmail.com
        """, language="bash")

        st.markdown("📖 [How to setup Gmail App Password](https://support.google.com/accounts/answer/185833)")

    with tab2:
        st.subheader("Pipeline Configuration")

        schedule_time = st.time_input("Daily Run Time", value=datetime.strptime("09:00", "%H:%M").time())

        st.info(f"Pipeline will run daily at {schedule_time}")

        if st.button("🧪 Test Pipeline Now"):
            with st.spinner("Testing pipeline..."):
                try:
                    run_pipeline()
                    st.success("✅ Pipeline test successful!")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    with tab3:
        st.subheader("Database Management")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔄 Reset Trends Database", use_container_width=True):
                if st.checkbox("I understand this will delete all trends"):
                    conn = sqlite3.connect(DB_PATH)
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM trends")
                    conn.commit()
                    conn.close()
                    st.success("✅ Trends database reset")
                    st.rerun()

        with col2:
            try:
                conn = sqlite3.connect(DB_PATH)
                trend_count = pd.read_sql_query("SELECT COUNT(*) as count FROM trends", conn)
                conn.close()
                st.metric("📊 Total Trends", trend_count['count'].iloc[0])
            except:
                st.metric("📊 Total Trends", 0)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 2rem 0;'>
    <p style='margin: 0;'>Made with ❤️ using Streamlit & LangGraph</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.85rem;'>
        © 2025 AI Trends Newsletter | Powered by AI
    </p>
</div>
""", unsafe_allow_html=True)