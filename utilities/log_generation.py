

import logging

class Logen():

    @staticmethod
    def loggen():             # (PWD) present folder -- file name
        logging.basicConfig(filename=".\\Logs\Automation.logs",
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S')

        logger = logging.getLogger()
        return logger
