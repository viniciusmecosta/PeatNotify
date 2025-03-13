import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('PeatNotify')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log(self, message: str):
        self.logger.info(message)

logger = Logger()
