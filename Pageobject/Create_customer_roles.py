from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class Create_customer_roles():
    link_Customer_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p'
    link_Customer_role_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[2]/a/p'
    link_AddNew_xpath='/html/body/div[3]/div[1]/div/div/a'
    text_Name_xpath='//*[@id="Name"]'
    cb_Active_xpath='//*[@id="Active"]'
    text_Sysname_xpath='//*[@id="SystemName"]'
    link_Save_xpath='/html/body/div[3]/div[1]/form/div/div/button[1]'

    def __init__(self,driver):
        self.driver=driver


    def clickCustomers(self):
        self.driver.find_element(By.XPATH,self.link_Customer_xpath).click()

    def clickCustomerRoles(self):
        self.driver.find_element(By.XPATH,self.link_Customer_role_xpath).click()

    def clickAddnew(self):
        self.driver.find_element(By.LINK_TEXT,'Add new').click()

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.link_Customer_xpath).send_keys(name)

    def enableCheckbor(self):
        self.driver.find_element(By.XPATH, self.cb_Active_xpath).click()





































