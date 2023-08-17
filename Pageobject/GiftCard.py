

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GiftCard():
    dd_sales_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a/p'
    tab_giftcard_xpath= "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[5]/a/p"
    link_addNew_xpath='/html/body/div[3]/div[1]/div/div/a'
    dd_giftCardType_xpath='//*[@id="GiftCardTypeId"]'
    text_initialValue_xpath='//*[@id="Amount"]'
    cb_giftCardActivated_xpath='//*[@id="IsGiftCardActivated"]'
    lnk_couponCode_xpath='//*[@id="generateCouponCode"]'
    text_recipientName_xpath='//*[@id="generateCouponCode"]'
    lnk_save_xpath='/html/body/div[3]/div[1]/form/div[1]/div/button[1]'


    def __init__(self,driver):
        self.driver=driver        # if self not use --> AttributeError: 'GiftCard' object has no attribute 'driver'

    # def driver(self,driver):
    #     self.driver=driver

    def clickOnSales(self):
        self.driver.find_element(By.XPATH,self.dd_sales_xpath).click()

    def clickOnGiftcard(self):
        self.driver.find_element(By.XPATH,self.tab_giftcard_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.link_addNew_xpath).click()

    def setgiftCardType(self,option):
        dropdown=Select(self.driver.find_element(By.XPATH,self.dd_giftCardType_xpath))
        dropdown.select_by_visible_text(option)

    # def setInitialValue(self,value):
    #     # self.driver.find_element(By.XPATH, self.text_initialValue_xpath).clear()
    #     self.driver.find_element(By.XPATH,self.text_initialValue_xpath).send_keys(value)

    def giftCardActivated(self):
        self.driver.find_element(By.XPATH,self.cb_giftCardActivated_xpath).click()

    def generateCouponCode(self):
        self.driver.find_element(By.XPATH,self.lnk_couponCode_xpath).click()

    def setRecipientName(self,value):
        self.driver.find_element(By.XPATH, self.text_recipientName_xpath).send_keys(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.lnk_save_xpath).click()









































































