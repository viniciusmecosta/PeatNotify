import smtplib
from constants.config import EMAIL_SENDER, SMTP_SERVER, SMTP_PORT, EMAIL_PASS
from utils.logger import logger

class EmailSender:
    def send(self, name, email, level):
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_SENDER, EMAIL_PASS)

                subject = "Alerta: Baixo nível no comedouro!"
                body = f"Olá {name},\n\nO nível do comedouro está em {level}%. Por favor, reabasteça o comedouro.\n\nAtenciosamente,\nEquipe Peat"
                message = f"Subject: {subject}\n\n{body}"

                server.sendmail(EMAIL_SENDER, email, message)
                logger.log(f"E-mail enviado para {name} ({email})")
                return True

        except Exception as e:
            logger.log(f"Erro ao enviar para {name} ({email}): {e}")
            return False
