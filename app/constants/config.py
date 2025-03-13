import os

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "default@gmail.com")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_PASS = os.getenv("EMAIL_PASS", "defaltpass")
EMAIL_SUBJECT = "Periodic Email"
EMAIL_BODY = "This is the body of the email."
API_URL = "http://127.0.0.1:8002"
