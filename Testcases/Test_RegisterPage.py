

import pytest
import time
from selenium import webdriver

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

        self.driver.get(self.url)
        self.loger.info('opening url')

        lp_object=LoginPage(self.driver)
        lp_object.setEmail(self.email)
        self.loger.info('Enter Email -->'+self.email)         # remember in logeer self.loger.info('Enter Email -->',self.email)-->,gives error use +
        lp_object.setPass(self.password)
        self.loger.info('Enter Password -->'+self.password)
        lp_object.cliclOnLogin()
        self.loger.info('Login succesfull')

        self.loger.info('Verifying test_RegisterPage_001 start')

        rp_object=RegisterPage(self.driver)

        time.sleep(15)
        rp_object.ClickOn_mainMenu_Help()
        time.sleep(5)

        rp_object.ClickOn_subMenu_Traning()
        time.sleep(20)

        all_windows=self.driver.window_handles
        for window in all_windows:
            self.driver.switch_to(all_windows[-1])

        rp_object.ClickOn_topMenu_english()
        time.sleep(3)

        rp_object.ClickOn_userActionIcon()
        time.sleep(3)

        














































































































