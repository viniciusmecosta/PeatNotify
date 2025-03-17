from adapter.api_client import APIClient
from utils.logger import logger
from service.email_service import EmailService

class LevelService:
    def __init__(self):
        self.email_service = EmailService()

    def check_and_notify(self):
        message = "Current level do comedouro: "
        level = APIClient.get_level()

        if level is None:
            logger.log("Error getting level.")
            return

        

        if level > 20:
            logger.log(f"{message}{level}% - No send emails.")
            return
        logger.log(f"{message}{level}% - Send emails.")
        emails = APIClient.get_emails()
        if not emails:
            logger.log("No emails registered for notification.")
            return

        success, failure = self.email_service.send_notifications(emails, level)
        logger.log(f"Sends completed. Success: {success}, Failures: {failure}")
