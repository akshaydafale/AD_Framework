from utilities.Readproperties import Readconfig
from utilities.log_generation import Logen
from Pageobject.LoginPage import LoginPage



class Test_login_002:
    url = Readconfig.getApplicationURL()
    email = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger = Logen.loggen()

    def test_login(self,setup):

        self.driver = setup
        self.logger.info('***** Test_login start verifying *****')

        self.driver.get(self.url)
        self.loginpage_object = LoginPage(self.driver)
        self.loginpage_object.setUsername(self.email)
        self.loginpage_object.setPassword(self.password)
        self.loginpage_object.clickLogin()

        actual_title = self.driver.title
        expected_title = 'Dashboard / nopCommerce administration'

        if actual_title == expected_title:
            assert True == True
            self.logger.info('***** Test_login test case passed *****')
            self.driver.get_screenshot_as_file(".\\screenshot\\"+"test_login_Passed.png")
            self.driver.close()

        else:
            assert True == False
            self.logger.info('***** Test_login test case Failed *****')
            self.driver.get_screenshot_as_file('.\\screenshot\test_login_failed.png')
            self.driver.close()
