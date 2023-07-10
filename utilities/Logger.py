import inspect
import logging

class LogGenerator:

    @staticmethod
    def loggen():

        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        file=logging.FileHandler("C:\\Users\\prati\\PycharmProjects\\CT10\\AD_framework\\Logs\\NopCommerse.log")
        format=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(lineno)s:%(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger



