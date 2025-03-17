import time
from service.level_service import LevelService
from utils.logger import logger

class App:
    def __init__(self):
        self.level_service = LevelService()

    def run(self):
        while True:
            self.level_service.check_and_notify()
            logger.log("Standing by for 1 hour")
            time.sleep(3600)

if __name__ == "__main__":
    app = App()
    app.run()