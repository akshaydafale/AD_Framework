import string
from selenium import webdriver
from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from Pageobject.LoginPage import LoginPage
from Pageobject.AddCustomer import AddCustomer
import random
from Testcases.conftest import setup


class Test_Addcustomer_002():
    url = Readconfig.getApplicationURL()
    email = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger = LogGenerator.loggen()

    def test_addcustomer(self, setup):

        self.logger.info('*****test_Addcustomer_001*****')

        self.driver = setup
        self.driver.get(self.url)

        LoginPage_object = LoginPage(self.driver)
        LoginPage_object.setUsername(self.email)
        LoginPage_object.setPassword(self.password)
        LoginPage_object.clickLogin()
        self.logger.info('***** Login succesfull *****')

        self.logger.info('***** test_Addcustomer_start *****')

        self.Add_customer_object = AddCustomer(self.driver)
        self.Add_customer_object.clickOnCustomerMainMenu()
        self.Add_customer_object.clickOnCustomerSubMenu()
        self.Add_customer_object.clickonAddNew()

        self.logger.info('***** Provide Customer information  *****')
        self.email = random_generator() + "@gmail.com"
        self.Add_customer_object.setEmail(self.email)
        self.Add_customer_object.setPassword("test123")
        self.Add_customer_object.setFirstName("Pavan")
        self.Add_customer_object.setLastName("Kumar")
        self.Add_customer_object.setGender("Male")
        self.Add_customer_object.setdob("7/05/1985")  # Format: D/MM/YYY
        self.Add_customer_object.setCustomerRoles("Guests")
        self.Add_customer_object.setManagerOfVendor("Vendor 2")
        self.Add_customer_object.clickOnSave()
        self.logger.info('***** Customer information saved *****')

        self.msg = self.driver.find_element_by_tag_name("body").text
        self.line = "The new customer has been added successfully"

        if self.line in self.msg:
            assert True == True
            self.logger.info('***** test_Addcustomer_002 is Passed *****')
            self.driver.close()

        else:
            assert True == False
            self.logger.error('***** test_Addcustomer_002 is Failed *****')
            self.driver.get_screenshot_as_file(".\\screenshot\\"+"Test_AddNewcustomer_failed.png")  # .\\ means own directory
            self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
