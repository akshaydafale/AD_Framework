

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()


class RegisterPage:

    mainMenu_Help_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[10]/a/p'
    subMenu_Traning_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[10]/ul/li[1]/a/p'
    topMenu_english_xpath='//*[@id="training-page"]/body/header/nav/div[3]/div/ul[2]/li/span'
    subMenu_english_xpath='//*[@id="training-page"]/body/header/nav/div[3]/div/ul[2]/li/ul/li[1]/a/span'
    userActionIcon_xpath='//*[@id="training-page"]/body/header/nav/ul/li[3]/span/span/svg'
    linkRegisterPage_xpath='//*[@id="register-page"]/body/div[7]/header/nav/ul/li[3]/ul/li[2]/a/span'
    textbox_FirstName_xpath='//*[@id="FirstName"]'
    textbox_LastName_xpath='//*[@id="LastName"]'
    textbox_Email_xpath='//*[@id="Email"]'
    textbox_ConfirmEmail_xpath='//*[@id="ConfirmEmail"]'
    textbox_Username_xpath='//*[@id="Username"]'
    button_CheckAvailibility_xpath='//*[@id="check-availability-button"]'
    dd_Country_xpath='//*[@id="CountryId"]'
    cb_Newsletter_xpath='//*[@id="register-page"]/body/div[7]/section/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div[8]/div/label'
    textbox_Password_xpath='//*[@id="Password"]'
    textbox_ConfirmPassword_xpath='//*[@id="Password"]'
    dd_MyCompanyPrimarily_xpath='//*[@id="Details_CompanyIndustryId"]'
    dd_MyMainActivity_xpath='//*[@id="Details_CompanyRoleId"]'
    dd_HowManyPeople_xpath='//*[@id="Details_CompanySizeId"]'
    btn_Register_xpath='//*[@id="register-button"]'

    def __init__(self,driver):
        self.driver=driver

    def ClickOn_mainMenu_Help(self):
        driver.find_element(By.XPATH,self.mainMenu_Help_xpath).click()

    def ClickOn_subMenu_Traning(self):
        driver.find_element(By.XPATH,self.subMenu_Traning_xpath).click()

    def ClickOn_topMenu_english(self):

        Top_englishElement=driver.find_element(By.XPATH,self.topMenu_english_xpath)
        Sub_englishElement = driver.find_element(By.XPATH, self.subMenu_english_xpath)

        ActionChain_object=ActionChains(driver)
        ActionChain_object.move_to_element(Top_englishElement).move_to_element(Sub_englishElement)


    def ClickOn_userActionIcon(self):

        ActionChain_object = ActionChains(driver)
        ActionChain_object.move_to_element(driver.find_element(By.XPATH,self.userActionIcon_xpath)).move_to_element(driver.find_element(By.XPATH,self.linkRegisterPage_xpath))

    def Set_firstName(self,firstName):
        driver.find_element(By.XPATH,self.textbox_FirstName_xpath).clear()
        driver.find_element(By.XPATH, self.textbox_FirstName_xpath).send_keys(firstName)


    def Set_lastName(self,lastName):
        driver.find_element(By.XPATH,self.textbox_LastName_xpath).clear()
        driver.find_element(By.XPATH,self.textbox_LastName_xpath).send_keys(lastName)

    def Set_Email(self,Email):
        driver.find_element(By.XPATH,self.textbox_Email_xpath).clear()
        driver.find_element(By.XPATH,self.textbox_Email_xpath).send_keys(Email)


    def Set_ConfirmEmail(self,ConfirmEmail):
        driver.find_element(By.XPATH,self.textbox_ConfirmEmail_xpath).clear()
        driver.find_element(By.XPATH,self.textbox_ConfirmEmail_xpath).send_keys(ConfirmEmail)


    def Set_Username(self,Username):
        driver.find_element(By.XPATH,self.textbox_Username_xpath).clear()
        driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(Username)

    def ClickOn_CheckAvailibility(self):
        driver.find_element(By.XPATH,self.button_CheckAvailibility_xpath).click()


    def Set_Country(self,Country):

        dd_Country_object=Select(driver.find_element(By.XPATH,self.dd_Country_xpath))
        dd_Country_object.select_by_visible_text(Country)


    def Click0n_Newsletter(self):
        driver.find_element(By.XPATH,self.cb_Newsletter_xpath).click()


    def Set_Password(self,password):
        driver.find_element(By.XPATH, self.textbox_Password_xpath).send_keys(password)


    def Set_ConfirmPassword(self,conf_password):
        driver.find_element(By.XPATH, self.textbox_ConfirmPassword_xpath).send_keys(conf_password)


    def Set_MyCompanyPrimarily(self,option):

        dd_MyCompanyPrimarily_object=Select(driver.find_element(By.XPATH,self.dd_MyCompanyPrimarily_xpath))
        dd_MyCompanyPrimarily_object.select_by_visible_text(option)


    def Set_MyMainActivity(self,Activity):

        dd_MyMainActivity_object=Select(driver.find_element(By.XPATH,self.dd_MyMainActivity_xpath))
        dd_MyMainActivity_object.select_by_visible_text(Activity)

    def Set_HowManyPeople(self, number):
        dd_HowManyPeople_xpath=Select(driver.find_element(By.XPATH,self.dd_HowManyPeople_xpath))
        dd_HowManyPeople_xpath.select_by_visible_text(number)


    def ClickOn_Register(self):
        driver.find_element(By.XPATH,self.btn_Register_xpath).click()






