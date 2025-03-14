from adapter.api_client import APIClient
from utils.logger import logger
from service.email_service import EmailService

class LevelService:
    def __init__(self):
        self.email_service = EmailService()

    def check_and_notify(self):
        logger.log("Verificando nível do comedouro...")
        level = APIClient.get_level()

        if level is None:
            logger.log("Erro ao obter nível.")
            return

        logger.log(f"Nível atual: {level}%")

        if level > 20:
            logger.log("Nível está OK. Nenhum e-mail necessário.")
            return

        emails = APIClient.get_emails()
        if not emails:
            logger.log("Nenhum e-mail cadastrado para notificação.")
            return

        success, failure = self.email_service.send_notifications(emails, level)
        logger.log(f"Envios concluídos. Sucesso: {success}, Falhas: {failure}")
