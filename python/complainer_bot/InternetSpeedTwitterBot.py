import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 15
        self.up = 1
        self.chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.user = os.environ['user']
        self.psswrd = os.environ['password']

    def get_internet_speed(self) -> tuple:
        self.driver.get('https://www.speedtest.net/')
        time.sleep(10)
        start = self.driver.find_element_by_css_selector('.js-start-test')
        start.click()
        time.sleep(50)
        download_speed = float(self.driver.find_element_by_css_selector('.download-speed').text)
        upload_speed = float(self.driver.find_element_by_css_selector('.upload-speed').text)
        return download_speed, upload_speed

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
        speeds = self.get_internet_speed()
        time.sleep(10)
        self.twitter_sign_in()
        time.sleep(2)
        text_entry = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        text_entry.click()
        text_entry.send_keys(
            f"My ISP promised {self.down} and {self.up}, but I'm only getting {speeds[0]} and {speeds[1]}, this is ridiculous")
        time.sleep(2)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
# speeds = bot.get_internet_speed()
bot.tweet()
