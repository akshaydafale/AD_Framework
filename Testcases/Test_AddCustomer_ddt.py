
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.Readproperties import Readconfig
from utilities.Logger import Logen
from Pageobject.LoginPage import LoginPage
from Pageobject.AddCustomer import AddCustomer
import random
from Testcases.conftest import setup
from utilities import XLutils


class Test_AddCustomer_ddt_005:

    url = Readconfig.getApplicationURL()
    email = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger = Logen.loggen()

    def test_AddCustomer_ddt(self,setup):

        self.driver=setup

        self.driver.get(self.url)
        LoginPage_object=LoginPage(self.driver)
        LoginPage_object.setUsername(self.email)
        LoginPage_object.setPassword(self.password)
        LoginPage_object.clickLogin()

        self.logger.info('******* Login test_AddCustomer_ddt succesful ******')

        self.Add_customer_object = AddCustomer(self.driver)
        self.Add_customer_object.clickOnCustomerMainMenu()
        self.Add_customer_object.clickOnCustomerSubMenu()
        self.Add_customer_object.clickonAddNew()

        self.path='C:\\Users\\prati\\OneDrive\\Desktop\\test_addcustomer_ddt.xlsx'

        self.rowcount=XLutils.getRowCount(self.path,'Sheet1')


        for r in range(2,self.rowcount+1):

            self.email=XLutils.readData(self.path,'Sheet1',r,1)
            self.password=XLutils.readData(self.path,'Sheet1',r,2)
            self.Firstname = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.Lastname = XLutils.readData(self.path, 'Sheet1', r, 4)
            self.gender = XLutils.readData(self.path, 'Sheet1', r, 5)
            # self.Dob = XLutils.readData(self.path, 'Sheet1', r, 6)
            self.Company_name = XLutils.readData(self.path, 'Sheet1', r, 7)
            # self.Customer_role = XLutils.readData(self.path, 'Sheet1', r, 8)
            self.Vendor = XLutils.readData(self.path, 'Sheet1', r, 9)

            self.logger.info('***** Provide Customer information  *****')

            self.Add_customer_object.setEmail(self.email)
            time.sleep(2)
            self.Add_customer_object.setPassword(self.password)
            time.sleep(2)
            self.Add_customer_object.setFirstName(self.Firstname)
            time.sleep(2)
            self.Add_customer_object.setLastName(self.Lastname)
            time.sleep(2)
            self.Add_customer_object.setGender(self.gender)
            time.sleep(2)
            # self.Add_customer_object.setdob(self.Dob)  # Format: D/MM/YYY
            time.sleep(2)
            self.Add_customer_object.setCompanyName(self.Company_name)
            time.sleep(2)
            self.Add_customer_object.setCustomerRoles('Registered')
            time.sleep(2)
            self.Add_customer_object.setManagerOfVendor(self.Vendor)
            time.sleep(2)
            self.Add_customer_object.clickOnSave()
            time.sleep(2)
            self.logger.info('***** Customer information saved *****')

            self.msg = self.driver.find_element_by_tag_name("body").text
            self.line = "The new customer has been added successfully"

            if self.line in self.msg:
                assert True == True
                self.logger.info('***** test_Addcustomer_ddt_005 is Passed *****')
                self.driver.close()         # make sure test should closed after test pass or fail

            else:
                assert False == False
                self.logger.error('***** test_Addcustomer_ddt_005 is Failed *****')
                self.driver.get_screenshot_as_file(".\\screenshot\\" + "test_Addcustomer_ddt_005_failed.png")  # .\\ means own directory
                self.driver.close()























































