from app.utils.email_utils import send_email

# Adjust these values as needed
to_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent from our FastAPI application."

success = send_email(
    to_email=to_email,
    subject=subject,
    body=body
)

if success:
    print("✅ Email sent successfully!")
else:
    print("❌ Failed to send email.")
