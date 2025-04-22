import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "defaultEMAIL")
API_TOKEN = os.getenv("API_TOKEN", "defaultTOKEN")
EMAIL_PASS = os.getenv("EMAIL_PASS", "defaultPASS")
API_URL = os.getenv("API_URL", "defaultURL")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465