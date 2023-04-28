
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pytest


class AddCustomer():
    lnk_Customers_mainmenu_Xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p'
    lnk_Customers_submenu_Xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p'
    lnk_AddNew_Xpath = '/html/body/div[3]/div[1]/form[1]/div/div/a/i'

    txt_Email_Xpath='//*[@id="Email"]'
    txt_Password_Xpath='//*[@id="Password"]'
    txt_FirstName_Xpath='//*[@id="FirstName"]'
    txt_LastName_Xpath ='//*[@id="LastName"]'
    rb_Gender_Xpath_Male='//*[@id="Gender_Male"]'
    rb_Gender_Xpath_Female='//*[@id="Gender_Female"]'
    txt_DOB_Xpath='//*[@id="DateOfBirth"]'
    txt_CompanyName_Xpath='//*[@id="Company"]'
    cb_IsTaxExtemp_Xpath='//*[@id="IsTaxExempt"]'
    Newsletter_Xpath='//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div'
    txt_CustomerRole_Xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div'
    lst_CustomerRole_Administrator_Xpath='//*[@id="b460a223-9679-4d57-93f8-52c89d73ef60"]'
    lst_CustomerRole_Forum_Moderators_Xpath ='//*[@id="SelectedCustomerRoleIds_listbox"]/li[2]'
    lst_CustomerRole_Guests_Xpath ='//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]'
    lst_CustomerRole_Registered_Xpath='//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    lst_CustomerRole_Vendors_Xpath='//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'
    dd_manageOfVendor_Xpath='//*[@id="VendorId"]'
    dd_vendorPath_Xpath='//*[@id="VendorId"]'
    cb_active_Xpath='//*[@id="Active"]'
    Lnk_save_Xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMainMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_Customers_mainmenu_Xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_Customers_submenu_Xpath).click()

    def clickonAddNew(self):
        self.driver.find_element(By.XPATH,self.lnk_AddNew_Xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_Xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_Password_Xpath).send_keys(password)

    def setFirstName(self,firstName):
        self.driver.find_element(By.XPATH,self.txt_FirstName_Xpath).send_keys(firstName)

    def setLastName(self,LastName):
        self.driver.find_element(By.XPATH,self.txt_LastName_Xpath).send_keys(LastName)

    def setGender(self,gender):                    ## correctable
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rb_Gender_Xpath_Male).click()

        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rb_Gender_Xpath_Female).click()

    def setdob(self,dob):
        self.driver.find_element(By.XPATH,self.txt_DOB_Xpath).send_keys(dob)

    def setCompanyName(self, cname):
        self.driver.find_element(By.XPATH,self.txt_CompanyName_Xpath).send_keys(cname)

    def setCustomerRoles(self,Role):

        self.driver.find_element(By.XPATH,self.txt_CustomerRole_Xpath).click()
        time.sleep(2)
        if Role=='Administrator':

            self.list_item=self.driver.find_element(By.XPATH,self.lst_CustomerRole_Administrator_Xpath)

        elif Role == 'Forum_Moderators':
            self.list_item = self.driver.find_element(By.XPATH,self.lst_CustomerRole_Forum_Moderators_Xpath)

        elif Role == 'Guests':
            self.driver.find_element(By.XPATH,self.lst_CustomerRole_Administrator_Xpath).click()
            time.sleep(3)
            self.list_item = self.driver.find_element(By.XPATH,self.lst_CustomerRole_Guests_Xpath)

        elif Role == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH,self.lst_CustomerRole_Registered_Xpath)

        elif Role == 'Vendors':
            self.list_item = self.driver.find_element(By.XPATH,self.lst_CustomerRole_Vendors_Xpath)

        self.driver.execute_script("argument[0].click();",self.list_item)

    def setManagerOfVendor(self,value):
        dd=Select(self.driver.find_element(By.XPATH,self.dd_manageOfVendor_Xpath))
        dd.select_by_visible_text(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.Lnk_save_Xpath).click()
































