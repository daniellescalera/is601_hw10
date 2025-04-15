import smtplib
from email.mime.text import MIMEText
from app.dependencies import get_settings

settings = get_settings()

def send_email(to_email: str, subject: str, body: str) -> bool:
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = settings.smtp_sender_email
        msg["To"] = to_email

        with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.sendmail(settings.smtp_sender_email, [to_email], msg.as_string())

        print("✅ Email sent successfully.")
        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        print("❌ Failed to send email.")
        return False
