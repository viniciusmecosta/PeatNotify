from constants.config import EMAIL_SENDER
from utils.logger import logger

class BodyEmail():
    def __init__(self):
        pass
    def createBody(self, name:str, level:int) -> str:
        subject = "O Comedouro Pet Do IFCE está com capacidade crítica"
        body = f"Olá {name},\n\nO nível do comedouro localizado no IFCE CAMPUS FORTALEZA está em {level}%. Por favor, reabasteça o comedouro.\n\nAtenciosamente,\nEquipe Peat"
        
        return body, subject