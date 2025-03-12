from logging import log
import time

from app.service import emailservice

class App:
    def __init__(self):
        self.emailService = emailservice
    
    def run(self):
        while True:
            log("Send E-mails")
            self.emailService.process()
            time.sleep(3600)
