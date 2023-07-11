#
#
# import pytest
# from Pageobject.LoginPage import LoginPage
# from utilities.Logger import LogGenerator
# from utilities.Readproperties import Readconfig
# from utilities.XLutils import ReadData
#
# class Test_login_ddt():
#
#     url=Readconfig.getApplicationURL()
#     Logger=LogGenerator.loggen()
#
#
#     def test_login_ddt(self,setup):
#         driver=setup
#         driver.get(self.url)
#
#         path='C:\\Users\\prati\\OneDrive\\Desktop\\IDPASS.xlsx'
#         self.rowcount=ReadData.getRowCount(path,'Sheet1')
#
#         List=[]
#         for r in range(2,self.rowcount+1):
#
#             id=ReadData.readData(path,'Sheet1',r,1)
#             password=ReadData.readData(path,'Sheet1',r,2)
#             expected=ReadData.readData(path,'Sheet1',r,3)
#
#
#             Login_object=LoginPage(driver)
#             Login_object.setEmail(id)
#             Login_object.setPass(password)
#             Login_object.cliclOnLogin()
#
#
#             driver.get(self.url)
#             actual_result=driver.title
#             expected_result='Dashboard / nopCommerce administration'
#
#             if actual_result==expected_result:
#                 if expected=='Pass':                 ## this for valid id and password
#                     assert True==True
#                     List.append('Pass')
#                     Login_object.cliclOnLogout()
#
#                 elif expected !='Pass':             ## this for invalid id and password
#                     assert False==False
#                     List.append('Fail')
#                     Login_object.cliclOnLogout()
#
#             elif actual_result!=expected_result:         ## this for invalid id and password
#                 if expected=='Fail':
#                     assert True==True
#                     List.append('Pass')
#
#                 if expected!='Fail':               ## this for valid id and password
#                     assert False==False
#                     List.append('Fail')
#
#         print(List)
#         if 'Fail' not in List:
#             assert True==True
#             self.Logger.info('*** test_login_ddt Passed **** ')
#             driver.close()
#         elif 'Fail' in List:
#             assert False==True
#             self.Logger.info('*** test_login_ddt Failed **** ')
#             driver.close()



from selenium import webdriver
import pytest
from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from utilities.XLutils import ReadData
from Pageobject.LoginPage import LoginPage  # always remember we have to import CLASS


class Test_login_DDT_002():

    logger=LogGenerator.loggen()

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
            driver.get_screenshot_as_file(".\\screenshot\\" + 'testLoginDDT_Failed.png')































































