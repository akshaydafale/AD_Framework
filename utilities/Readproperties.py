

import configparser # it is a library

object_config=configparser.RawConfigParser()
object_config.read("C:\\Users\\prati\\PycharmProjects\\CT10\\AD_framework\\configuration\\config.ini")

class Readconfig():

    @staticmethod
    def getApplicationURL():
        baseURL=object_config.get('login info','baseURL')
        return baseURL

    @staticmethod
    def getUsermail():
        useremail= object_config.get('login info', 'username')
        return useremail

    @staticmethod
    def getPassword():
        password = object_config.get('login info', 'password')
        return password






