import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from constants.config import EMAIL_SENDER, SMTP_SERVER, SMTP_PORT, EMAIL_PASS
from utils.body_email import BodyEmail
from utils.logger import logger

class EmailSender:
    def __init__(self):
        self.body = BodyEmail()

    def send(self, name, email, level):
        
        body, subject = self.body.createBody(name, level)

        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.login(EMAIL_SENDER, EMAIL_PASS)
                smtp.send_message(msg)
                logger.log(f"Email successfully sent to {name} ({email})")
                return True
        except smtplib.SMTPException as e:
            logger.log(f"SMTP error while sending to {name} ({email}): {e}")
        except Exception as e:
            logger.log(f"Unexpected error while sending to {name} ({email}): {e}")
        return False