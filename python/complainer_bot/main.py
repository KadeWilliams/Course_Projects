from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

PROMISED_DOWN = 15
PROMISED_UP = 2

TWITTER_USERNAME = '32ahteak@gmail.com'
TWITTER_PASSWORD = '#91InlAX*hy76Tti!BTW5QHt'


