import time

from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys


class DataEntryBot:
    def __init__(self):
        chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        form = 'https://forms.gle/DT1HkZzmXrAcCyeF7'
        self.driver.get(form)

    def enter_data(self, data: list):
        for val in data:
            for i in val.values():
                address = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                time.sleep(1)
                address.send_keys(i['address'])
                link.send_keys(i['link'])
                price.send_keys(i['price'])
                time.sleep(1)
                submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
                submit.click()
                time.sleep(2)
                another = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                another.click()
                time.sleep(1)

