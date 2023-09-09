
import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pageobject.LoginPage import LoginPage
# from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig


class Test_Login_001():

    #url='' --shift to conftest
    url=Readconfig.getApplicationURL()
    email=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    Logger=LogGenerator.loggen()


    # @allure.title('nopcommerce_login')
    def testLoginPage(self,setup):

        self.Logger.info('test case testLoginPage started')
        self.driver=setup
        self.Logger.info('invoking browser')

        self.driver.get(self.url)
        self.Logger.info('opening URL')

        act_result=self.driver.title
        exp_result='Your store. Login'

        if act_result==exp_result:
            assert True
            self.Logger.info('Test testLoginPage passed')
            # allure.attach(self.driver.get_screenshot_as_png(),name="testLoginPagePassed",Attachment_type=AttachmentType) # screenshor for allure reports
            self.driver.close()
        else:
            self.Logger.info('Test LoginHomePage Fail')
            # allure.attach(self.driver.get_screenshot_as_png(),name="testLoginPageFailed",Attachment_type=AttachmentType) # screenshor for allure reports
            self.driver.get_screenshot_as_file(".\\screenshot\\" + 'TestLoginHomePage_Failed.png')
            assert True == False
            self.driver.close()

    # @allure.title('nopcommerce_login')
    # @pytest.mark.sanity
    def test_HomePage(self,setup):      # for 1 method opening 1 browser
        self.Logger.info('Test_HomePage is started start')
        self.driver=setup
        self.Logger.info('invoking browser')

        self.driver.get(self.url)
        self.Logger.info('opening URL')

        self.LoginPage_object=LoginPage(self.driver)
        self.LoginPage_object.setEmail(self.email)
        self.Logger.info(' entering email -->'+self.email)
        self.LoginPage_object.setPass(self.password)
        self.Logger.info(' entering password -->'+self.password)
        self.LoginPage_object.cliclOnLogin()
        self.Logger.info('click on login')

        actual_title=self.driver.title
        expected_tiltle='Dashboard /nopCommerce administration'

        if actual_title==expected_tiltle:
            assert True
            self.Logger.info('test_HomePage passed ')
            # allure.attach(self.driver.get_screenshot_as_png(),name="test_HomePagePassed",Attachment_type=AttachmentType) # screenshor for allure reports
            self.LoginPage_object.cliclOnLogout()
            self.driver.close()

        else:

            self.Logger.info('test_HomePage Failed')
            # allure.attach(self.driver.get_screenshot_as_png(),name="test_HomePageFailed",Attachment_type=AttachmentType) # screenshor for allure reports
            self.driver.get_screenshot_as_file(".\\screenshot\\"+'Test_login_Fail.png')
            assert False == True
            self.driver.close()


## pytest -rA .\Testcases\Test_login.py --html=Reports\myhtmlreport.html -m 'sanity' -n auto
#
# # Test case for practise
#
#     @allure.title('nopcommerce_login')
#     @pytest.mark.sanity
#     def test_HomePage_other(self,setup):
#         self.Logger.info('Test_HomePage_other is started start')
#         self.driver=setup
#         self.Logger.info('invoking browser')
#         self.Logger.info('opening URL')
#
#         self.LoginPage_object=LoginPage(self.driver)
#         self.LoginPage_object.setEmail(self.email)
#         self.Logger.info(' entering email')
#         self.LoginPage_object.setPass(self.password)
#         self.Logger.info(' enetring password')
#         self.LoginPage_object.cliclOnLogin()
#         self.Logger.info('click on login')
#
#         msg=self.driver.find_element(By.TAG_NAME,'body').text     # body --small letters
#         title='Dashboard'
#
#         if title in msg:
#             assert True
#             self.Logger.info('test_HomePage passed ')
#             allure.attach(self.driver.get_screenshot_as_png(),name="test_HomePage_otherPassed",Attachment_type=AttachmentType) # screenshor for allure reports
#             self.LoginPage_object.cliclOnLogout()
#             self.driver.close()
#
#         else:
#             assert False == True
#             self.Logger.info('test_HomePage_other Failed')
#             allure.attach(self.driver.get_screenshot_as_png(),name="test_HomePage_otherFailed",Attachment_type=AttachmentType) # screenshor for allure reports
#             # self.driver.get_screenshot_as_file(".\\screenshot\\"+'Test_login_Fail.png')
#             self.driver.close()
#
#























