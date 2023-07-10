

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    textbox_Username_id='Email'
    textbox_password_id='Password'
    btn_login_xpath='/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_xpath='//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.textbox_Username_id).clear()
        self.driver.find_element(By.ID, self.textbox_Username_id).send_keys(email)

    def setPass(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def cliclOnLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def cliclOnLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()


##----------------------------------------------------------------------------------------------------------------------



















