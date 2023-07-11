



import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pageobject.LoginPage import LoginPage
# from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig


class Test_Login_001():

    #url='' --shift to conftest
    email=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    Logger=LogGenerator.loggen()

    def testLoginPage(self,setup):

        self.Logger.info('test case testLoginPage started')
        self.driver=setup
        self.Logger.info('invoking browser')
        self.Logger.info('opening URL')

        act_result=self.driver.title
        exp_result='Your store. Login'

        if act_result==exp_result:
            assert True
            self.Logger.info('testLoginPage is passed')
            self.driver.close()
        else:
            assert True==False
            self.Logger.info('Test LoginHomePage Fail')
            self.driver.get_screenshot_as_file(".\\screenshot\\" + 'TestLoginHomePage_Failed.png')
            self.driver.close()

    @pytest.mark.sanity
    def test_HomePage(self,setup):
        self.Logger.info('Test_HomePage is started start')
        self.driver=setup
        self.Logger.info('invoking browser')
        self.Logger.info('opening URL')

        self.LoginPage_object=LoginPage(self.driver)
        self.LoginPage_object.setEmail(self.email)
        self.Logger.info(' entering email -->'+self.email)
        self.LoginPage_object.setPass(self.password)
        self.Logger.info(' enetring password -->'+self.password)
        self.LoginPage_object.cliclOnLogin()
        self.Logger.info('click on login')

        actual_title=self.driver.title
        expected_tiltle='Dashboard / nopCommerce administration'

        if actual_title==expected_tiltle:
            assert True
            self.Logger.info('test_HomePage passed ')
            self.LoginPage_object.cliclOnLogout()
            self.driver.close()

        else:
            assert False == True
            self.Logger.info('test_HomePage Failed')
            self.driver.get_screenshot_as_file(".\\screenshot\\"+'Test_login_Fail.png')
            self.driver.close()


## pytest -rA .\Testcases\Test_login.py --html=Reports\myhtmlreport.html -m 'sanity' -n auto

# Test case for practise


    @pytest.mark.sanity
    def test_HomePage_other(self,setup):
        self.Logger.info('Test_HomePage_other is started start')
        self.driver=setup
        self.Logger.info('invoking browser')
        self.Logger.info('opening URL')

        self.LoginPage_object=LoginPage(self.driver)
        self.LoginPage_object.setEmail(self.email)
        self.Logger.info(' entering email')
        self.LoginPage_object.setPass(self.password)
        self.Logger.info(' enetring password')
        self.LoginPage_object.cliclOnLogin()
        self.Logger.info('click on login')

        msg=self.driver.find_element(By.TAG_NAME,'body').text     # body --small letters
        title='Dashboard'

        if title in msg:
            assert True
            self.Logger.info('test_HomePage passed ')
            self.LoginPage_object.cliclOnLogout()
            self.driver.close()

        else:
            assert False == True
            self.Logger.info('test_HomePage_other Failed')
            self.driver.get_screenshot_as_file(".\\screenshot\\"+'Test_login_Fail.png')
            self.driver.close()

























