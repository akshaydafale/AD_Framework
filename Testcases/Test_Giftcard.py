import time

import pytest
import faker
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.Readproperties import Readconfig
from utilities.Logger import LogGenerator
from Pageobject.LoginPage import LoginPage
from Pageobject.GiftCard import GiftCard


class Test_Giftcard():
    url = Readconfig.getApplicationURL()
    email = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    loger = LogGenerator.loggen()


    def test_giftcard(self,setup):     # setup is parameter

        self.driver = setup
        self.loger.info('Launching chrome browser')
        self.driver.get(self.url)
        self.loger.info('opening url')
        self.driver.maximize_window()

        lp_object = LoginPage(self.driver)
        lp_object.setEmail(self.email)
        self.loger.info('enter email-->' + self.email)
        lp_object.setPass(self.password)
        self.loger.info('enter password-->' + self.password)
        lp_object.cliclOnLogin()
        self.loger.info('click on login')
        self.loger.info('Login succesfull')

        gc_Object = GiftCard(self.driver) # object naver need self
        gc_Object.clickOnSales()
        self.loger.info('click on sales')

        time.sleep(3)

        gc_Object.clickOnGiftcard()
        self.loger.info('click on gift card')

        time.sleep(3)

        gc_Object.clickOnAddNew()
        self.loger.info('click on add new')

        time.sleep(3)

        gc_Object.setgiftCardType('Physical')
        self.loger.info('select option from gift card type')

        time.sleep(3)

        # self.GiftCard_Object.setInitialValue('10')
        # self.loger.info('enterd initial value')

        time.sleep(3)

        gc_Object.giftCardActivated()
        self.loger.info('click on check box')

        time.sleep(3)

        gc_Object.generateCouponCode()
        self.loger.info('generate coupoun code')

        time.sleep(3)

        fake=Faker()
        random_name=fake.name()

        # n='akshay dafale'
        gc_Object.setRecipientName(random_name)
        self.loger.info('enter recipient name')

        time.sleep(3)

        # gc_Object.setRecipientEmail('akshay@gmail.com')
        # self.loger.info('enter recipient Email')
        #
        # time.sleep(3)

        gc_Object.clickOnSave()
        self.loger.info('click on save')

        time.sleep(3)

        msg = 'The new gift card has been added successfully.'
        body = self.driver.find_element(By.TAG_NAME, 'body').text
        self.loger.info('verifying test Test_Giftcard')

        self.loger.info('verifying msg in body')
        if msg in body:
            self.loger.info('verified msg in body')
            list_of_name=self.driver.find_elements(By.XPATH,'//*[@id="giftcards-grid"]/tbody/tr/td')
            for name in list_of_name:
                if name.text==random_name:
                    # print(n)
                    self.loger.info(random_name)
                    assert True
                    self.loger.info('Test case giftCard is passed')
                    # self.driver.get_screenshot_as_png()
                    self.driver.close()
                    self.loger.info('driver closed')
                    break
            else:
                self.loger.info('Test case is failed')
                self.driver.get_screenshot_as_file('.\\screenshot\\' + 'TestCase_giftcard_failed.png')
                self.driver.close()
                self.loger.info('driver closed')
                assert True == False

        else:
            self.loger.info('Test case is failed')
            self.driver.get_screenshot_as_file('.\\screenshot\\' + 'TestCase_giftcard_failed.png')
            self.loger.info('sceenshot has been saved')
            assert True == False  # if this will write at start then after that not execute so it will write at last
            self.driver.close()
            self.loger.info('driver closed')


            # asserttion error means test case fail


