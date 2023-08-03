#
#
# from selenium import webdriver
# import pytest
# import time
#
# from selenium.webdriver.common.by import By
#
# from Pageobject.Create_customer_roles import Create_customer_roles
# from Pageobject.LoginPage import LoginPage
# from Testcases.conftest import  setup
# from utilities.Readproperties import Readconfig
# from utilities.Logger import Logen
#
#
#
# class Test_Create_customer_roles_004():
#
#     url=Readconfig.getApplicationURL()
#     email=Readconfig.getUsermail()
#     password=Readconfig.getPassword()
#     Loger=Logen.loggen()
#
#     def test_Create_customer_roles(self,setup):
#
#         self.driver=setup
#         self.driver.get(self.url)
#
#         LoginPage_object=LoginPage(self.driver)
#         LoginPage_object.setUsername(self.email)
#         LoginPage_object.setPassword(self.password)
#         LoginPage_object.clickLogin()
#
#
#         self.Create_customer_role_object=Create_customer_roles(self.driver)
#
#         self.Create_customer_role_object.clickCustomers()
#         self.Create_customer_role_object.clickCustomerRoles()
#         time.sleep(6)
#         self.Create_customer_role_object.clickAddnew()
#         self.Create_customer_role_object.setName('akshay dafale')
#         self.Create_customer_role_object.cb_Active_xpath()
#         self.Create_customer_role_object.text_Sysname_xpath('apple')
#         self.Create_customer_role_object.link_Save_xpath()
#
#         self.msg    = self.driver.find_elements(By.TAG_NAME,'body').text()
#         self.actual = "The new customer has been added successfully"
#
#         if self.actual in self.msg:
#             assert True==True
#             self.Loger.info('****** test case pass ******')
#             self.driver.close()
#
#         elif self.actual not in self.msg:
#             assert True==False
#             self.driver.get_screenshot_as_file(".\\screenshot\\"+"test_Create_customer_roles_fail.png")
#             self.Loger.info("***** test case fail *****")
#             self.driver.close()
























