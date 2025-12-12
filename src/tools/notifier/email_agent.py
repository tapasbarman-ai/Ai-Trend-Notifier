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
        
        # Initialize LLM for headline generation
        try:
            from src.tools.summarizer.summarizer_agent import SummarizerAgent
            self.summarizer = SummarizerAgent()
            self.use_llm_headlines = True
            print("✅ LLM headline generation enabled")
        except Exception as e:
            print(f"⚠️ LLM headline generation disabled: {e}")
            self.summarizer = None
            self.use_llm_headlines = False

    def get_dynamic_gif(self):
        """Rotate GIFs based on day of month - 15+ premium AI/tech themed animations"""
        day = datetime.now().day
        gifs = [
            # AI Brain & Neural Networks
            "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",  # AI Brain
            "https://media.giphy.com/media/xUPGcdhiQf0vS1fX5a/giphy.gif",  # Neural Network
            "https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif",  # Tech Animation
            
            # Robots & Technology
            "https://media.giphy.com/media/26BRQTezZrKak4BeE/giphy.gif",  # Robot
            "https://media.giphy.com/media/26BRzozg4TCBXv6QU/giphy.gif",  # Tech
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",  # AI Animation
            
            # Data & Analytics
            "https://media.giphy.com/media/JqmupuTVZYaQX5s094/giphy.gif",  # Data Flow
            "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif",  # Analytics
            "https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif",  # Processing
            
            # Futuristic & Digital
            "https://media.giphy.com/media/3oKIPlifLxdigaD2Y8/giphy.gif",  # Rocket/Launch
            "https://media.giphy.com/media/citBl9yPwnUOs/giphy.gif",  # Code/Matrix
            "https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif",  # Digital
            
            # Innovation & Growth
            "https://media.giphy.com/media/KJ1f5iTl4Oo7u/giphy.gif",  # Innovation
            "https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif",  # Star/Success
            "https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif",  # Tech Wave
        ]
        return gifs[day % len(gifs)]
    
    def get_header_gif(self):
        """Get header GIF based on time of day"""
        hour = datetime.now().hour
        if hour < 12:
            # Morning - energetic, bright
            return "https://media.giphy.com/media/3oKIPlifLxdigaD2Y8/giphy.gif"
        elif hour < 18:
            # Afternoon - productive, focused
            return "https://media.giphy.com/media/JqmupuTVZYaQX5s094/giphy.gif"
        else:
            # Evening - calm, analytical
            return "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif"
    
    def get_sentiment_gif(self, sentiment):
        """Get sentiment-specific GIF"""
        sentiment_gifs = {
            'POSITIVE': "https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif",  # Star/Success
            'NEGATIVE': "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",  # Alert/Warning
            'NEUTRAL': "https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif"  # Information
        }
        return sentiment_gifs.get(sentiment, sentiment_gifs['NEUTRAL'])
    
    def get_divider_gif(self):
        """Get animated divider GIF"""
        dividers = [
            "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
            "https://media.giphy.com/media/xUPGcdhiQf0vS1fX5a/giphy.gif",
        ]
        return dividers[datetime.now().day % len(dividers)]

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
        Render professional HTML email with clean, attractive design

        Args:
            trends: List of trend dictionaries
            executive_summary: Optional executive summary

        Returns:
            HTML string
        """
        # Professional color scheme
        sentiment_config = {
            'POSITIVE': {
                'emoji': '✓', 
                'icon': '🟢',
                'color': '#059669', 
                'bg': '#ECFDF5', 
                'border': '#10B981',
                'light': '#D1FAE5'
            },
            'NEGATIVE': {
                'emoji': '✗', 
                'icon': '🔴',
                'color': '#DC2626', 
                'bg': '#FEF2F2', 
                'border': '#EF4444',
                'light': '#FEE2E2'
            },
            'NEUTRAL': {
                'emoji': '●', 
                'icon': '🔵',
                'color': '#2563EB', 
                'bg': '#EFF6FF', 
                'border': '#3B82F6',
                'light': '#DBEAFE'
            }
        }

        # Count sentiments
        sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
        for trend in trends:
            sentiment = trend.get('sentiment', trend.get('sentiment_label', 'NEUTRAL')).upper()
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

        # Build professional trend cards
        trends_html = ""
        for idx, trend in enumerate(trends[:10], 1):
            sentiment = trend.get('sentiment', trend.get('sentiment_label', 'NEUTRAL')).upper()
            config = sentiment_config.get(sentiment, sentiment_config['NEUTRAL'])

            # Extract info
            summary = trend.get('summary', trend.get('content', 'No summary available'))
            source = trend.get('source', 'Unknown').capitalize()
            title = self._extract_title(summary, idx)

            trends_html += f"""
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 24px;">
                <tr>
                    <td>
                        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                            
                            <!-- Card Header -->
                            <tr>
                                <td style="padding: 20px 24px; border-bottom: 1px solid #E5E7EB; background: {config['bg']};">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tr>
                                            <td style="vertical-align: middle; width: 40px;">
                                                <div style="width: 36px; height: 36px; background: {config['color']}; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: 700;">
                                                    {idx}
                                                </div>
                                            </td>
                                            <td style="vertical-align: middle; padding-left: 16px;">
                                                <h3 style="margin: 0; color: #111827; font-size: 18px; font-weight: 600; line-height: 1.4;">
                                                    {title}
                                                </h3>
                                            </td>
                                            <td style="vertical-align: middle; text-align: right; padding-left: 16px;">
                                                <span style="display: inline-block; padding: 4px 12px; background: {config['color']}; color: white; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border-radius: 4px;">
                                                    {source}
                                                </span>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            
                            <!-- Card Body -->
                            <tr>
                                <td style="padding: 24px;">
                                    <p style="margin: 0 0 20px 0; color: #4B5563; font-size: 15px; line-height: 1.7; font-weight: 400;">
                                        {summary}
                                    </p>
                                    
                                    <table cellpadding="0" cellspacing="0" border="0">
                                        <tr>
                                            <td style="padding: 8px 16px; background: {config['light']}; border-left: 3px solid {config['color']}; border-radius: 4px;">
                                                <span style="color: #6B7280; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Sentiment:</span>
                                                <span style="color: {config['color']}; font-size: 14px; font-weight: 700; margin-left: 8px;">
                                                    {config['icon']} {sentiment}
                                                </span>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            
                        </table>
                    </td>
                </tr>
            </table>
            """

        # Executive summary section
        exec_section = ""
        if executive_summary:
            exec_section = f"""
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 32px;">
                <tr>
                    <td style="background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%); padding: 32px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                                <td style="text-align: center; padding-bottom: 16px;">
                                    <div style="font-size: 48px;">📊</div>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <h2 style="margin: 0 0 16px 0; color: #FFFFFF; font-size: 24px; font-weight: 700; text-align: center; letter-spacing: -0.5px;">
                                        Executive Summary
                                    </h2>
                                    <p style="margin: 0; color: #DBEAFE; font-size: 16px; line-height: 1.7; text-align: center; font-weight: 400;">
                                        {executive_summary}
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            """

        # Professional stats section
        stats_html = f"""
        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 32px;">
            <tr>
                <td style="padding: 24px; background: #F9FAFB; border: 1px solid #E5E7EB; border-radius: 8px;">
                    <h3 style="margin: 0 0 20px 0; color: #111827; font-size: 18px; font-weight: 600; text-align: center;">
                        📈 Today's Overview
                    </h3>
                    <table width="100%" cellpadding="12" cellspacing="0" border="0">
                        <tr>
                            <td align="center" style="width: 25%; padding: 12px;">
                                <div style="background: #FFFFFF; padding: 16px; border-radius: 6px; border: 1px solid #E5E7EB;">
                                    <div style="font-size: 32px; font-weight: 700; color: #1F2937; margin-bottom: 4px;">
                                        {len(trends)}
                                    </div>
                                    <div style="color: #6B7280; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
                                        Total
                                    </div>
                                </div>
                            </td>
                            <td align="center" style="width: 25%; padding: 12px;">
                                <div style="background: #ECFDF5; padding: 16px; border-radius: 6px; border: 1px solid #10B981;">
                                    <div style="font-size: 32px; font-weight: 700; color: #059669; margin-bottom: 4px;">
                                        {sentiment_counts.get('POSITIVE', 0)}
                                    </div>
                                    <div style="color: #047857; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
                                        Positive
                                    </div>
                                </div>
                            </td>
                            <td align="center" style="width: 25%; padding: 12px;">
                                <div style="background: #FEF2F2; padding: 16px; border-radius: 6px; border: 1px solid #EF4444;">
                                    <div style="font-size: 32px; font-weight: 700; color: #DC2626; margin-bottom: 4px;">
                                        {sentiment_counts.get('NEGATIVE', 0)}
                                    </div>
                                    <div style="color: #B91C1C; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
                                        Negative
                                    </div>
                                </div>
                            </td>
                            <td align="center" style="width: 25%; padding: 12px;">
                                <div style="background: #EFF6FF; padding: 16px; border-radius: 6px; border: 1px solid #3B82F6;">
                                    <div style="font-size: 32px; font-weight: 700; color: #2563EB; margin-bottom: 4px;">
                                        {sentiment_counts.get('NEUTRAL', 0)}
                                    </div>
                                    <div style="color: #1D4ED8; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
                                        Neutral
                                    </div>
                                </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        """

        # Get dynamic GIF
        current_date = datetime.now().strftime('%B %d, %Y')
        day_of_week = datetime.now().strftime('%A')
        gif_url = self.get_dynamic_gif()

        # Professional HTML template
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Trends Report - {current_date}</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #F3F4F6;">
    
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #F3F4F6; padding: 40px 20px;">
        <tr>
            <td align="center">
                
                <!-- Main Container -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: 680px; background-color: #FFFFFF; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%); padding: 40px 32px; text-align: center;">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="text-align: center;">
                                        <div style="font-size: 64px; margin-bottom: 16px;">🤖</div>
                                        <h1 style="margin: 0 0 8px 0; color: #FFFFFF; font-size: 32px; font-weight: 700; letter-spacing: -0.5px;">
                                            AI Trends Report
                                        </h1>
                                        <p style="margin: 0; color: #BFDBFE; font-size: 16px; font-weight: 500;">
                                            {day_of_week}, {current_date}
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                    <!-- Banner GIF -->
                    <tr>
                        <td style="background: #1F2937; padding: 0; border-top: 3px solid #3B82F6; border-bottom: 3px solid #3B82F6;">
                            <img src="{gif_url}" alt="AI Technology" style="width: 100%; display: block; max-width: 680px; height: auto;">
                        </td>
                    </tr>
                    
                    <!-- Main Content -->
                    <tr>
                        <td style="padding: 40px 32px;">
                            
                            <!-- Welcome Message -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 32px;">
                                <tr>
                                    <td style="padding: 20px 24px; background: #F9FAFB; border-left: 4px solid #3B82F6; border-radius: 6px;">
                                        <p style="margin: 0; color: #374151; font-size: 15px; line-height: 1.7; font-weight: 400;">
                                            <strong style="color: #111827; font-weight: 600;">Welcome to your daily AI intelligence briefing.</strong> 
                                            We've curated the most significant developments in artificial intelligence to keep you informed and ahead of the curve.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            {exec_section}
                            
                            {stats_html}
                            
                            <!-- Section Divider -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 32px 0;">
                                <tr>
                                    <td style="text-align: center;">
                                        <div style="font-size: 40px; margin-bottom: 12px;">📰</div>
                                        <h2 style="margin: 0 0 8px 0; color: #111827; font-size: 24px; font-weight: 700;">
                                            Today's Key Insights
                                        </h2>
                                        <div style="width: 60px; height: 3px; background: #3B82F6; margin: 0 auto; border-radius: 2px;"></div>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Trend Cards -->
                            {trends_html}
                            
                            <!-- Divider -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 40px 0 32px 0;">
                                <tr>
                                    <td style="border-top: 2px solid #E5E7EB;"></td>
                                </tr>
                            </table>
                            
                            <!-- Footer CTA -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="padding: 24px; background: #FFFBEB; border: 1px solid #FCD34D; border-radius: 6px; text-align: center;">
                                        <div style="font-size: 32px; margin-bottom: 12px;">💡</div>
                                        <h3 style="margin: 0 0 8px 0; color: #92400E; font-size: 18px; font-weight: 600;">
                                            Stay Ahead of the Curve
                                        </h3>
                                        <p style="margin: 0; color: #78350F; font-size: 14px; line-height: 1.6;">
                                            Questions or feedback? We'd love to hear from you.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background: #F9FAFB; padding: 32px; text-align: center; border-top: 1px solid #E5E7EB;">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="text-align: center;">
                                        <p style="margin: 0 0 8px 0; color: #6B7280; font-size: 14px; font-weight: 500;">
                                            AI Trends Analyzer
                                        </p>
                                        <p style="margin: 0 0 16px 0; color: #9CA3AF; font-size: 13px;">
                                            Powered by Advanced AI • {current_date}
                                        </p>
                                        <div style="border-top: 1px solid #E5E7EB; padding-top: 16px; margin-top: 16px;">
                                            <p style="margin: 0; color: #D1D5DB; font-size: 12px;">
                                                © 2025 AI Trends Analyzer. All rights reserved.
                                            </p>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                </table>
                
            </td>
        </tr>
    </table>
    
</body>
</html>
        """

        return html

    def _extract_title(self, summary: str, idx: int) -> str:
        """Generate an engaging title using LLM or fallback to extraction"""
        
        # Try to use LLM for headline generation
        if self.use_llm_headlines and self.summarizer:
            try:
                headline = self.summarizer.generate_headline(summary)
                if headline and headline != "AI Trend Update":
                    return headline
            except Exception as e:
                print(f"⚠️ LLM headline generation failed: {e}")
        
        # Fallback: extract from summary
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