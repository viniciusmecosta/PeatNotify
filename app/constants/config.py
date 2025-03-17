import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "defaultEMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS", "defaultPASS")
API_URL = os.getenv("API_URL", "defaultURL")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465