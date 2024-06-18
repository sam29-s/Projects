import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def auto_mail():
    sender_email = "lordwinsam21@gmail.com"
    receiver_email = input("Enter receiver's email address: ")
    password = "Samofficial@29"  # Use app password if 2FA is enabled
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  # For SSL

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "This is a test email."
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Test email sent successfully to", receiver_email)
    except Exception as e:
        print("Error sending test email:", str(e))

if __name__ == "__main__":
    auto_mail()
