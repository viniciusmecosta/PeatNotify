import smtplib
from utils.body_email import BodyEmail
from constants.config import EMAIL_SENDER, SMTP_SERVER, SMTP_PORT, EMAIL_PASS
from utils.logger import logger

class EmailSender:
    def __init__(self):
        self.body = BodyEmail()
    def send(self, name, email, level):
        try:
            logger.log("Iniciando envio de e-mail...")
            logger.log(f"Conectando ao servidor SMTP: {SMTP_SERVER}:465")
            
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                logger.log("Conexão segura estabelecida com SMTP_SSL.")

                server.login(EMAIL_SENDER, EMAIL_PASS)
                logger.log("Login realizado com sucesso.")

                message = self.body.createBody(name,email,level)

                server.sendmail(EMAIL_SENDER, email, message)
                logger.log(f"E-mail enviado com sucesso para {name} ({email})")
                return True

        except smtplib.SMTPException as e:
            logger.log(f"Erro SMTP ao enviar para {name} ({email}): {e}")
        except Exception as e:
            logger.log(f"Erro inesperado ao enviar para {name} ({email}): {e}")
        return False