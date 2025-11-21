# import sys
# import os
#
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from src.config.settings import SMTP_SERVER, SMTP_PORT, SMTP_EMAIL, SMTP_PASSWORD, RECIPIENT_EMAIL
#
#
# class EmailAgent:
#     def __init__(self):
#         self.smtp_server = SMTP_SERVER
#         self.smtp_port = SMTP_PORT
#         self.smtp_email = SMTP_EMAIL
#         self.smtp_password = SMTP_PASSWORD
#         self.recipient = RECIPIENT_EMAIL
#
#     def send_summary(self, trends):
#         try:
#             msg = MIMEMultipart()
#             msg['From'] = self.smtp_email
#             msg['To'] = self.recipient
#             msg['Subject'] = "Daily AI Trends Summary"
#
#             body = "Daily AI Trends:\n\n"
#             for i, trend in enumerate(trends[:5], 1):
#                 body += f"{i}. {trend.get('summary', 'No summary')}\n"
#                 body += f"   Sentiment: {trend.get('sentiment_label', 'N/A')}\n\n"
#
#             msg.attach(MIMEText(body, 'plain'))
#
#             with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
#                 server.starttls()
#                 server.login(self.smtp_email, self.smtp_password)
#                 server.send_message(msg)
#
#             return True
#         except Exception as e:
#             print(f"Email error: {e}")
#             return False

"""
Fixed Email Agent with Embedded HTML Template
Place at: src/tools/notifier/email_agent.py
"""

"""
Complete Fixed Email Agent with Embedded HTML Template
Place at: src/tools/notifier/email_agent.py
"""

"""
Complete Fixed Email Agent - Final Version
Place at: src/tools/notifier/email_agent.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from typing import List, Dict

# Import from your settings (FIXED: Using correct variable names)
from src.config.settings import SMTP_SERVER, SMTP_PORT, SMTP_EMAIL, SMTP_PASSWORD, RECIPIENT_EMAIL


class EmailAgent:
    """Enhanced email agent with beautiful HTML newsletter"""

    def __init__(self):
        # FIXED: Use correct variable names from your settings
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.email_address = SMTP_EMAIL  # Changed from EMAIL_ADDRESS
        self.email_password = SMTP_PASSWORD  # Changed from EMAIL_PASSWORD
        self.recipient = RECIPIENT_EMAIL

        # Better validation
        if not self.email_address or not self.email_password:
            raise ValueError("⚠️ ERROR: SMTP_EMAIL or SMTP_PASSWORD missing in .env file!")

    def get_dynamic_gif(self):
        """Rotate GIFs based on day of month"""
        day = datetime.now().day
        gifs = [
            "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
            "https://media.giphy.com/media/xUPGcdhiQf0vS1fX5a/giphy.gif",
            "https://media.giphy.com/media/26BRQTezZrKak4BeE/giphy.gif",
            "https://media.giphy.com/media/26BRzozg4TCBXv6QU/giphy.gif",
            "https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif",
        ]
        return gifs[day % len(gifs)]

    def send_summary(self, trends: List[Dict], executive_summary: str = None) -> bool:
        """
        Send HTML email with trends (main entry point for pipeline)

        Args:
            trends: List of trend dictionaries
            executive_summary: Optional executive summary

        Returns:
            True if successful, False otherwise
        """
        try:
            return self.send_email(self.recipient, trends, executive_summary)
        except Exception as e:
            print(f"❌ Email error: {e}")
            return False

    def send_email(self, to_email: str, trends: List[Dict], executive_summary: str = None) -> bool:
        """
        Send beautiful HTML email

        Args:
            to_email: Recipient email address
            trends: List of trend dictionaries
            executive_summary: Optional executive summary

        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\n📧 Preparing email for {to_email}...")

            # Render HTML content
            html_content = self.render_email(trends, executive_summary)

            # Create MIME message
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"🤖 Daily AI Trends Report - {datetime.now().strftime('%B %d, %Y')}"
            msg["From"] = self.email_address
            msg["To"] = to_email

            # Attach HTML
            msg.attach(MIMEText(html_content, "html"))

            # Send via SMTP
            print(f"📤 Connecting to {self.smtp_server}:{self.smtp_port}...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.sendmail(self.email_address, to_email, msg.as_string())
            server.quit()

            print(f"✅ Email sent successfully to {to_email}")
            return True

        except smtplib.SMTPAuthenticationError:
            print("❌ SMTP Authentication failed! Check your email and password.")
            return False
        except Exception as e:
            print(f"❌ Email sending failed: {e}")
            return False

    def render_email(self, trends: List[Dict], executive_summary: str = None) -> str:
        """
        Render HTML email with embedded template

        Args:
            trends: List of trend dictionaries
            executive_summary: Optional executive summary

        Returns:
            HTML string
        """
        # Sentiment configuration
        sentiment_config = {
            'POSITIVE': {'emoji': '🟢', 'color': '#10B981', 'bg': '#D1FAE5', 'border': '#34D399'},
            'NEGATIVE': {'emoji': '🔴', 'color': '#EF4444', 'bg': '#FEE2E2', 'border': '#F87171'},
            'NEUTRAL': {'emoji': '🟡', 'color': '#F59E0B', 'bg': '#FEF3C7', 'border': '#FBBF24'}
        }

        # Count sentiments
        sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
        for trend in trends:
            # FIXED: Handle both 'sentiment' and 'sentiment_label' keys
            sentiment = trend.get('sentiment', trend.get('sentiment_label', 'NEUTRAL')).upper()
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

        # Build trend cards
        trends_html = ""
        for idx, trend in enumerate(trends[:10], 1):
            # FIXED: Handle both 'sentiment' and 'sentiment_label' keys
            sentiment = trend.get('sentiment', trend.get('sentiment_label', 'NEUTRAL')).upper()
            config = sentiment_config.get(sentiment, sentiment_config['NEUTRAL'])

            # Extract info
            summary = trend.get('summary', trend.get('content', 'No summary available'))
            source = trend.get('source', 'Unknown').capitalize()
            title = self._extract_title(summary, idx)

            trends_html += f"""
            <div style="background: white; margin-bottom: 25px; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 5px solid {config['border']};">

                <div style="background: linear-gradient(135deg, {config['bg']} 0%, white 100%); padding: 20px 25px; border-bottom: 1px solid #E5E7EB;">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                            <td style="vertical-align: middle;">
                                <h3 style="color: #111827; margin: 0; font-size: 20px; font-weight: 700; line-height: 1.3;">
                                    <span style="color: {config['color']};">#{idx}</span> {title}
                                </h3>
                            </td>
                            <td style="vertical-align: middle; text-align: right; white-space: nowrap; padding-left: 15px;">
                                <span style="background: {config['color']}; color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; display: inline-block;">
                                    {source}
                                </span>
                            </td>
                        </tr>
                    </table>
                </div>

                <div style="padding: 25px;">
                    <p style="color: #374151; line-height: 1.8; margin: 0 0 20px 0; font-size: 16px;">
                        {summary}
                    </p>

                    <div style="display: inline-block; background: {config['bg']}; border: 2px solid {config['color']}; border-radius: 8px; padding: 10px 18px;">
                        <strong style="color: #111827; font-size: 13px; font-weight: 600; letter-spacing: 0.3px;">SENTIMENT:</strong>
                        <span style="color: {config['color']}; font-weight: 700; font-size: 15px; margin-left: 8px;">
                            {config['emoji']} {sentiment}
                        </span>
                    </div>
                </div>

            </div>
            """

        # Executive summary section
        exec_section = ""
        if executive_summary:
            exec_section = f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; margin-bottom: 35px; border-radius: 16px; box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);">
                <div style="text-align: center; margin-bottom: 15px;">
                    <span style="font-size: 48px;">📊</span>
                </div>
                <h2 style="margin: 0 0 20px 0; font-size: 26px; color: white; text-align: center; font-weight: 700; letter-spacing: 0.5px;">
                    Executive Summary
                </h2>
                <p style="margin: 0; line-height: 1.9; font-size: 17px; color: #F3F4F6; text-align: center; font-weight: 400;">
                    {executive_summary}
                </p>
            </div>
            """

        # Stats dashboard
        stats_html = f"""
        <div style="background: linear-gradient(135deg, #F3F4F6 0%, #E5E7EB 100%); padding: 30px; border-radius: 16px; margin-bottom: 35px;">
            <h3 style="color: #111827; margin: 0 0 20px 0; font-size: 20px; font-weight: 700; text-align: center;">
                📈 Today's Analytics
            </h3>
            <table width="100%" cellpadding="15" cellspacing="0" border="0">
                <tr>
                    <td align="center" style="min-width: 120px;">
                        <div style="font-size: 36px; font-weight: 800; color: #4F46E5; margin-bottom: 5px;">
                            {len(trends)}
                        </div>
                        <div style="color: #6B7280; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                            Total Trends
                        </div>
                    </td>
                    <td align="center" style="min-width: 120px;">
                        <div style="font-size: 36px; font-weight: 800; color: #10B981; margin-bottom: 5px;">
                            {sentiment_counts.get('POSITIVE', 0)}
                        </div>
                        <div style="color: #6B7280; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                            🟢 Positive
                        </div>
                    </td>
                    <td align="center" style="min-width: 120px;">
                        <div style="font-size: 36px; font-weight: 800; color: #EF4444; margin-bottom: 5px;">
                            {sentiment_counts.get('NEGATIVE', 0)}
                        </div>
                        <div style="color: #6B7280; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                            🔴 Negative
                        </div>
                    </td>
                    <td align="center" style="min-width: 120px;">
                        <div style="font-size: 36px; font-weight: 800; color: #F59E0B; margin-bottom: 5px;">
                            {sentiment_counts.get('NEUTRAL', 0)}
                        </div>
                        <div style="color: #6B7280; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                            🟡 Neutral
                        </div>
                    </td>
                </tr>
            </table>
        </div>
        """

        # Current date
        current_date = datetime.now().strftime('%B %d, %Y')
        day_of_week = datetime.now().strftime('%A')
        gif_url = self.get_dynamic_gif()

        # Complete HTML template
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily AI Trends Report</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 20px;">

    <div style="max-width: 680px; margin: 0 auto; background-color: #FFFFFF; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.3);">

        <!-- Hero Header -->
        <div style="background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); padding: 50px 40px; text-align: center;">
            <div style="font-size: 72px; margin-bottom: 15px;">🤖</div>
            <h1 style="color: #FFFFFF; margin: 0 0 12px 0; font-size: 38px; font-weight: 800; letter-spacing: -0.5px; text-shadow: 0 2px 10px rgba(0,0,0,0.2);">
                Daily AI Trends
            </h1>
            <p style="color: #E0E7FF; margin: 0 0 8px 0; font-size: 18px; font-weight: 600;">
                {day_of_week}, {current_date}
            </p>
            <div style="display: inline-block; background: rgba(255,255,255,0.2); border-radius: 20px; padding: 8px 20px; margin-top: 10px;">
                <span style="color: white; font-size: 14px; font-weight: 600; letter-spacing: 1px;">
                    🔥 CURATED FOR YOU
                </span>
            </div>
        </div>

        <!-- Animated GIF Banner -->
        <div style="background: #1F2937; text-align: center; border-top: 4px solid #7C3AED; border-bottom: 4px solid #7C3AED;">
            <img src="{gif_url}" 
                 alt="AI Animation" 
                 style="width: 100%; max-width: 680px; display: block; margin: 0;">
        </div>

        <!-- Main Content -->
        <div style="padding: 45px 40px;">

            <!-- Welcome Message -->
            <div style="background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%); padding: 25px; border-radius: 12px; margin-bottom: 35px; border-left: 5px solid #4F46E5;">
                <p style="color: #1E1B4B; font-size: 17px; line-height: 1.8; margin: 0; font-weight: 500;">
                    👋 <strong>Welcome back!</strong> Here are today's most important developments in artificial intelligence, 
                    carefully curated and analyzed just for you. Stay ahead of the curve with insights from across the AI landscape.
                </p>
            </div>

            {exec_section}

            {stats_html}

            <!-- Section Header -->
            <div style="text-align: center; margin: 40px 0 35px 0;">
                <div style="font-size: 48px; margin-bottom: 15px;">📰</div>
                <h2 style="color: #111827; font-size: 32px; margin: 0; font-weight: 800; letter-spacing: -0.5px;">
                    Today's Top Trends
                </h2>
                <div style="width: 80px; height: 4px; background: linear-gradient(90deg, #4F46E5, #7C3AED); margin: 15px auto 0; border-radius: 2px;"></div>
            </div>

            <!-- Trend Cards -->
            {trends_html}

            <!-- Divider -->
            <div style="height: 2px; background: linear-gradient(90deg, transparent, #E5E7EB, transparent); margin: 50px 0;"></div>

            <!-- Call to Action -->
            <div style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); padding: 30px; border-radius: 16px; text-align: center; border: 2px solid #F59E0B;">
                <div style="font-size: 42px; margin-bottom: 12px;">💡</div>
                <h3 style="color: #78350F; margin: 0 0 12px 0; font-size: 22px; font-weight: 700;">
                    Stay Informed, Stay Ahead
                </h3>
                <p style="color: #92400E; font-size: 15px; margin: 0; line-height: 1.6;">
                    Want to customize your trends? Let us know what topics interest you most!
                </p>
            </div>

        </div>

        <!-- Footer -->
        <div style="background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 100%); padding: 40px; text-align: center; border-top: 2px solid #E5E7EB;">
            <div style="font-size: 36px; margin-bottom: 15px;">💌</div>
            <p style="color: #6B7280; font-size: 16px; margin: 0 0 12px 0; font-weight: 600;">
                Sent automatically by your AI Trend Analyzer
            </p>
            <p style="color: #9CA3AF; font-size: 14px; margin: 0 0 20px 0;">
                Powered by LangGraph & Claude AI • Generated on {current_date}
            </p>
            <div style="border-top: 1px solid #E5E7EB; padding-top: 20px; margin-top: 20px;">
                <p style="color: #D1D5DB; font-size: 12px; margin: 0;">
                    © 2025 AI Trends Analyzer. All rights reserved.
                </p>
            </div>
        </div>

    </div>

</body>
</html>
        """

        return html

    def _extract_title(self, summary: str, idx: int) -> str:
        """Extract or generate an engaging title from summary"""
        sentences = summary.split('.')
        if sentences and len(sentences[0]) > 10:
            title = sentences[0].strip()
            if len(title) > 80:
                title = title[:77] + "..."
            return title
        return f"AI Trend #{idx}"

    def test_email(self):
        """Send a test email"""
        test_trends = [
            {
                'source': 'reddit',
                'summary': 'Researchers develop new AI safety techniques for ensuring alignment with human values, potentially preventing risks from advanced AI systems.',
                'sentiment': 'POSITIVE',
            },
            {
                'source': 'twitter',
                'summary': 'Industry experts raise concerns about the rapid development of GPT-5 without proper safety testing and evaluation protocols.',
                'sentiment': 'NEGATIVE',
            },
            {
                'source': 'reddit',
                'summary': 'New AI diagnostic system achieves 95% accuracy in early cancer detection across multiple cancer types in clinical trials.',
                'sentiment': 'POSITIVE',
            }
        ]

        exec_summary = "Today's AI landscape shows a mix of exciting breakthroughs in healthcare and safety, alongside important concerns about responsible development."

        return self.send_summary(test_trends, exec_summary)


# Test function
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Testing Email Agent")
    print("=" * 60)

    try:
        agent = EmailAgent()
        success = agent.test_email()

        if success:
            print("\n✅ Test email sent successfully!")
            print(f"📬 Check your inbox: {agent.recipient}")
        else:
            print("\n❌ Failed to send test email")
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease ensure your .env file has:")
        print("  SMTP_EMAIL=your-email@gmail.com")
        print("  SMTP_PASSWORD=your-app-password")
        print("  RECIPIENT_EMAIL=recipient@example.com")