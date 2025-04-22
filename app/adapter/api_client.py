import requests
from domain.email import Email
from constants.config import API_URL, API_TOKEN


class APIClient:
    @staticmethod
    def get_level():
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(f"{API_URL}/app/last/{1}", headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
            if data:
                return int(data[0]["level"])

        return None

    @staticmethod
    def get_emails():
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(f"{API_URL}/email", headers=headers)

        if response.status_code == 200:
            emails_data = response.json()
            email_objects = []
            for item in emails_data:
                email_objects.append(Email(email=item["email"], name=item["name"]))
            return email_objects

        return []
