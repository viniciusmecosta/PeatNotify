import time
from service.level_service import LevelService
from utils.logger import logger

class App:
    def __init__(self):
        self.level_service = LevelService()

    def run(self):
        while True:
            logger.log("Vefiricando Level do comedouro...")
            self.level_service.check_and_notify()
            time.sleep(60)

if __name__ == "__main__":
    app = App()
    app.run()