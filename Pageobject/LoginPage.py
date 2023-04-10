

from selenium import webdriver
# driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class LoginPage:                          #login is scenareo
    textbox_Username_id='Email'
    textbox_password_id='Password'
    Button_login_Xpath ='/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_Xpath  ='//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self,driver):
        self.driver=driver

    #action method
    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_Username_id).clear()
        self.driver.find_element(By.ID, self.textbox_Username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.Button_login_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_Xpath).click()

