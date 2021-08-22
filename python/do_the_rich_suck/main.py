import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from babel.numbers import format_currency


class RichBot:
    def __init__(self):
        self.chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.user = os.environ['username']
        self.psswrd = os.environ['password']

    def get_richest(self):
        self.driver.get('https://www.forbes.com/forbes-400/#15b032877e2f')
        time.sleep(30)
        richest = self.driver.find_element_by_xpath('//*[@id="jeff-bezos"]/div[3]/div')
        richest_value = int(richest.text.split()[0].replace('$', '')) * 1_000_000_000
        return richest_value

    def get_median_worth(self):
        self.driver.get('https://www.forbes.com/advisor/investing/average-net-worth/')
        time.sleep(30)
        median = int(
            self.driver.find_element_by_xpath('//*[@id="footable_99872"]/tbody/tr[2]/td[3]/p').text.split('$')[
                1].replace(',', ''))
        return median

    def twitter_sign_in(self):
        self.driver.get('https://twitter.com/home')
        time.sleep(2)
        username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(self.user)

        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(self.psswrd)

        log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        log_in.send_keys(Keys.ENTER)

    def tweet(self):
        richest = self.get_richest()
        median = self.get_median_worth()
        time.sleep(10)
        self.twitter_sign_in()
        time.sleep(2)
        text_entry = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        text_entry.click()
        text_entry.send_keys(
            f"The richest person in the world is Jeff Bezos, and is worth {format_currency(richest, 'USD', locale='en_US')}."
            f" That's {(richest / median).__round__(0)} times more than the average American.")
        time.sleep(2)
        tweet_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_btn.click()


bot = RichBot()
bot.tweet()


