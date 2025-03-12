import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('EmailLogger')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)

    def log(self, message: str):
        self.logger.info(message)