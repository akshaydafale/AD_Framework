

import configparser

object_config=configparser.RawConfigParser()
object_config.read(".\\Configuration\\config.ini")

class Readconfig():

    @staticmethod
    def getApplicationURL():
        baseURL=object_config.get('common info','baseURL')
        return baseURL

    @staticmethod
    def getUsermail():
        useremail= object_config.get('common info', 'username')
        return useremail

    @staticmethod
    def getPassword():
        password = object_config.get('common info', 'password')
        return password









