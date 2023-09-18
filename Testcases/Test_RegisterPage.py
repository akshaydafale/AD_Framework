

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pageobject.LoginPage import LoginPage
from Pageobject.RegisterPage import RegisterPage
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig
from utilities.XLutils import ReadData


class Test_RegisterPage():

    url=Readconfig.getApplicationURL()
    email=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    loger=LogGenerator.loggen()

    def test_RegisterPage_001(self,setup):

        self.driver=setup
        self.loger.info('Launching Crome browser')

        # self.driver.get(self.url)
        # self.loger.info('opening url')

        self.driver.get('https://www.nopcommerce.com/en/training?utm_source=admin-panel&utm_medium=menu&utm_campaign=course&utm_content=help')

        self.driver.maximize_window()

        # lp_object=LoginPage(self.driver)
        # lp_object.setEmail(self.email)
        # self.loger.info('Enter Email -->'+self.email)         # remember in logeer self.loger.info('Enter Email -->',self.email)-->,gives error use +
        # lp_object.setPass(self.password)
        # self.loger.info('Enter Password -->'+self.password)
        # lp_object.cliclOnLogin()
        # self.loger.info('Login succesfull')

        time.sleep(3)
        self.loger.info('Verifying test_RegisterPage_001 start')
        rp_object=RegisterPage(self.driver)
        self.loger.info('rp_object is created from class RegisterPage() ')

        # time.sleep(2)
        # rp_object.clickOn_mainMenu_Help()
        # self.loger.info('ClickedOn_mainMenu_Help')
        # time.sleep(2)
        #
        # rp_object.clickOn_subMenu_Traning()
        # self.loger.info('ClickOn_subMenu_Traning')
        # time.sleep(2)
        #
        # all_windows_list=self.driver.window_handles
        # self.loger.info(all_windows_list)
        # new_window=all_windows_list[-1]
        # time.sleep(3)

        # self.driver.switch_to(new_window)
        # self.loger.info('switched to new window')
        # time.sleep(3)

        time.sleep(5)
        rp_object.clickOn_topMenu_english()
        self.loger.info('ClickOn_topMenu_english')
        time.sleep(10)

        rp_object.clickOn_userActionIcon()
        self.loger.info('ClickOn_userActionIcon')
        time.sleep(3)

        














































































































