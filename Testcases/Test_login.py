# from utilities.Readproperties import Readconfig
# from utilities.log_generation import Logen
# from Pageobject.LoginPage import LoginPage
# import pytest
#
#
# class Test_login_002:
#     url = Readconfig.getApplicationURL()
#     email = Readconfig.getUsermail()
#     password = Readconfig.getPassword()
#     logger = Logen.loggen()
#
#     @pytest.mark.sanity               # custome marker
#     def test_login(self,setup):
#
#         self.driver = setup
#         self.logger.info('***** Test_login start verifying *****')
#
#         self.driver.get(self.url)
#         self.loginpage_object = LoginPage(self.driver)
#         self.loginpage_object.setUsername(self.email)
#         self.loginpage_object.setPassword(self.password)
#         self.loginpage_object.clickLogin()
#
#         actual_title = self.driver.title
#         expected_title = 'Dashboard / nopCommerce administration'
#
#         if actual_title == expected_title:
#             assert True == True
#             self.logger.info('***** Test_login test case passed *****')
#             self.driver.get_screenshot_as_file(".\\screenshot\\"+"test_login_Passed.png")
#             self.driver.close()
#
#         else:
#             assert True == False
#             self.logger.info('***** Test_login test case Failed *****')
#             self.driver.get_screenshot_as_file('.\\screenshot\test_login_failed.png')
#             self.driver.close()


#-----------------------------------------------------------------------------------------------------------------------
## Date : 26May2023

import pytest
from Pageobject.LoginPage import LoginPage
from utilities.Readproperties import Readconfig
from utilities.log_generation import Logen

class Test_Login_001():

    url=Readconfig.getApplicationURL()
    email=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    Logger=Logen.loggen()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.Logger.info('****** Test_login_001 start verifying ******')
        self.driver=setup

        self.driver.get(self.url)
        self.LoginPage_object=LoginPage(self.driver)
        self.LoginPage_object.setEmail(self.email)
        self.LoginPage_object.setPass(self.password)
        self.LoginPage_object.cliclOnLogin()

        self.Logger.info('**** Login succesfull *****')

        actual_title=self.driver.title
        expected_tiltle='Dashboard / nopCommerce administration'

        if actual_title==expected_tiltle:
            assert True==True
            self.Logger.info('**** test_Login passed *****')
            self.driver.get_screenshot_as_file(".\\screenshot\\" + 'Test_login_Pass.png')
            self.driver.close()

        if actual_title != expected_tiltle:
            assert True == False
            self.Logger.info('**** test_Login passed *****')
            self.driver.get_screenshot_as_file(".\\screenshot\\"+'Test_login_Fail.png')
            self.driver.close()



















