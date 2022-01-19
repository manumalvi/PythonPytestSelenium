import inspect
import logging


class BaseClass:
    def getLogger(self):
        # __name__ will capture your filename so that its easy to know from which file you are getting log
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('log1file.log')
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger