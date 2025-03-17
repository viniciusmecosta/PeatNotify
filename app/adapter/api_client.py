import datetime
import requests
from domain.email import Email
from constants.config import API_URL

class APIClient:
    @staticmethod
    def get_level():
        today = datetime.datetime.now().strftime("%d%m%Y")
        response = requests.get(f"{API_URL}/distance/date/{today}")

        if response.status_code == 200:
            data = response.json()
            if data:
                most_recent = min(data, key=lambda x: x["count"])
                return int(most_recent["level"])

        return None

    @staticmethod
    def get_emails():
        response = requests.get(f"{API_URL}/email")
        if response.status_code == 200:
            emails_data = response.json()
            email_objects = []
            for item in emails_data:
                email_objects.append(Email(email=item["email"], name=item["name"]))
            return email_objects
        return []
