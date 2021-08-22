import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FollowBot:
    def __init__(self):self.chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys('art_follow_111')
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys('8FM4nQ5hCTUtdhw')
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(1)
        now_not = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        now_not.click()

    def find_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/')
        time.sleep(2)
        followers_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()
        people_to_follow = []
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        while True:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(2)

    def follow(self):
        self.find_followers('banksy')
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = FollowBot()
bot.follow()

