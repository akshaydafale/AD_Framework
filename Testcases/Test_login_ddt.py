import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from utilities.XLutils import ReadData
from Pageobject.LoginPage import LoginPage  # always remember we have to import CLASS


class Test_login_DDT_002():

    logger=LogGenerator.loggen()

    @allure.title('nopcommerce_login_ddt')
    @pytest.mark.sanity
    def testLoginDDT(self,setup):
        self.logger.info('Test Test_login_DDT_002 is started')
        driver=setup
        self.logger.info('invoking browser')
        self.logger.info('opening url')

        path='C:\\Users\\prati\\OneDrive\\Desktop\\IDPASS.xlsx'
        rowcount=ReadData.getRowCount(path,'Sheet1')

        status =[]
        for r in range(2,rowcount+1):

            username=ReadData.readData(path,'Sheet1',r,1)
            password=ReadData.readData(path,'Sheet1',r,2)
            expected=ReadData.readData(path,'Sheet1',r,3)

            lp_object=LoginPage(driver)
            lp_object.setEmail(username)
            self.logger.info('enter username-->'+username)
            lp_object.setPass(password)
            self.logger.info('enter password-->' + password)
            lp_object.cliclOnLogin()
            self.logger.info('click on login button' )

            act_result=driver.title
            exp_result='Your store. Login'

            if act_result==exp_result:
                self.logger.info('login succesfull with --> '+username+'|'+password)
                if expected=='Pass':
                    status.append('Pass')
                    lp_object.cliclOnLogout()
                    driver.close()
                elif expected !='Pass':
                    status.append('Fail')
                    lp_object.cliclOnLogout()
                    driver.close()

            else:
                self.logger.info('login Failed with --> ' + username + '|' + password)
                if expected=='Fail':
                    status.append('Pass')
                    driver.close()
                elif expected !='Fail':
                    status.append('Fail')
                    driver.close()

        if 'Fail' not in status:
            assert True
            self.logger.info('testLoginDDT is Passed')
        else:
            assert False==True
            self.logger.info('testLoginDDT is Failed')
            # driver.get_screenshot_as_file(".\\screenshot\\" + 'testLoginDDT_Failed.png')
            allure.attach(driver.get_screenshot_as_png(),name="testLoginDDTFailed",Attachment_type=AttachmentType) # screenshor for allure reports
































































