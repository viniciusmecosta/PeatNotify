from constants.config import EMAIL_SENDER
from utils.logger import logger

class BodyEmail():
    def __init__(self):
        pass
    def createBody(name:str, email:str, level:int) -> str:
        logger.log(f"Enviando e-mail para {name} ({email})...")
        subject = "Alerta: Baixo nível no comedouro!"
        body = f"Olá {name},\n\nO nível do comedouro está em {level}%. Por favor, reabasteça o comedouro.\n\nAtenciosamente,\nEquipe Peat"
        
        message = f"From: {EMAIL_SENDER}\nTo: {email}\nSubject: {subject}\n\n{body}"
        return message