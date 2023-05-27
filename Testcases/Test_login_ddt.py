#
# from selenium import webdriver
# import pytest
# from utilities.log_generation import Logen
# from utilities.Readproperties import Readconfig
# from Pageobject.LoginPage import LoginPage
# from utilities import XLutils
#
# class Test_login_ddt():
#
#     url=Readconfig.getApplicationURL()
#     path='C:\\Users\\prati\\OneDrive\\Desktop\\IDPASS.xlsx'
#     logger=Logen.loggen()
#
#
#     def test_login_ddt(self,setup):
#         self.driver=setup
#         self.driver.get(self.url)
#         self.login_page_object=LoginPage(self.driver)
#
#         self.rowCount=XLutils.getRowCount(self.path,'Sheet1')
#
#         List_status=[]
#
#         for r in range(2,self.rowCount+1):
#             self.id=XLutils.readData(self.path,'Sheet1',r,1)
#             self.password=XLutils.readData(self.path,'Sheet1',r,2)
#             self.Expected=XLutils.readData(self.path,'Sheet1',r,3)
#
#
#             self.login_page_object.setUsername(self.id)
#             self.login_page_object.setPassword(self.password)
#             self.login_page_object.clickLogin()
#
#             actual_result=self.driver.title
#             expected_result='Dashboard / nopCommerce administration'
#
#             if actual_result==expected_result:
#                 if self.Expected=='Pass':
#                     assert True==True
#                     List_status.append('Pass')
#                     self.login_page_object.clickLogout()
#
#                 elif self.Expected=='Fail':
#                     assert False==False
#                     List_status.append('Fail')
#                     self.login_page_object.clickLogout()
#
#             elif actual_result!=expected_result:
#                 if self.Expected=='Fail':
#                     assert True==True
#                     List_status.append('Pass')
#
#                 elif self.Expected=='Pass':
#                     assert False == False
#                     List_status.append('Fail')
#
#
#
#         if 'Fail' in List_status:
#             assert True==False
#             self.logger.info('***** test case failed *****') # test case pased or fail zali ki driver close lrne must i.
#             self.driver.close()
#
#         elif 'Fail' not in List_status:
#             assert True==True
#             self.logger.info('***** test case passed ****')
#             self.driver.close()


##----------------------------------------------------------------------------------------------------------------------

import pytest
from Pageobject.LoginPage import LoginPage
from utilities.log_generation import Logen
from utilities.Readproperties import Readconfig
from utilities import XLutils

class Test_login_ddt():

    url=Readconfig.getApplicationURL()
    Logger=Logen.loggen()


    def test_login_ddt(self,setup):
        self.driver=setup
        self.driver.get(self.url)

        path='C:\\Users\\prati\\OneDrive\\Desktop\\IDPASS.xlsx'
        self.rowcount=XLutils.getRowCount(path,'Sheet1')

        List=[]
        for r in range(2,self.rowcount+1):

            self.id=XLutils.readData(path,'Sheet1',r,1)
            self.password=XLutils.readData(path,'Sheet1',r,2)
            self.expected=XLutils.readData(path,'Sheet1',r,3)


            self.Login_object=LoginPage(self.driver)
            self.Login_object.setEmail(self.id)
            self.Login_object.setPass(self.password)
            self.Login_object.cliclOnLogin()

            self.driver.get(self.url)
            actual_result=self.driver.title
            expected_result='Dashboard / nopCommerce administration'

            if actual_result==expected_result:
                if self.expected=='Pass':                 ## this for valid id and password
                    assert True==True
                    List.append('Pass')
                    self.Login_object.cliclOnLogout()

                elif self.expected !='Pass':             ## this for invalid id and password
                    assert False==False
                    List.append('Fail')
                    self.Login_object.cliclOnLogout()


            elif actual_result!=expected_result:         ## this for invalid id and password
                if self.expected=='Fail':
                    assert True==True
                    List.append('Pass')


                if self.expected!='Fail':               ## this for valid id and password
                    assert False==False
                    List.append('Fail')

        print(List)
        if 'Fail' not in List:
            assert True==True
            self.Logger.info('*** test_login_ddt Passed **** ')
            self.driver.close()
        elif 'Fail' in List:
            assert False==False
            self.Logger.info('*** test_login_ddt Failed **** ')
            self.driver.close()















































