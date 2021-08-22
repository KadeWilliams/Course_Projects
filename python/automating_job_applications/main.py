import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r'C:\Users\kadew\Desktop\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

site = 'https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=103644278&keywords=software%20engineer&location=United%20States'
# site = 'https://www.linkedin.com/jobs/search/'
driver.get(site)

sign_in = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
sign_in.click()

time.sleep(2)

username = driver.find_element_by_id('username')
username.send_keys('kadewilliams0@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('iwMK8U0kl8JC')

sign_in_btn = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()

time.sleep(2)
remember = driver.find_element_by_css_selector('.btn__primary--large')
remember.click()

time.sleep(5)

# search = driver.find_element_by_css_selector('.jobs-search-box__text-input')
# search.send_keys('software engineer')
# search.send_keys(Keys.ENTER)


listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in listings:
    value = 0
    job.click()
    time.sleep(2)
    apply_button = driver.find_element_by_css_selector('.jobs-apply-button')
    apply_button.click()
    time.sleep(1)
    try:

        submit_button = driver.find_element_by_css_selector("footer button")
        submit_button.click()
        while value < 3:
            submit_button = driver.find_element_by_css_selector("footer button")
            submit_button.click()
            time.sleep(2)
            value += 1
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()


    except NoSuchElementException:
        print("No application button, skipped.")
        continue
        # review = driver.find_element_by_id('#ember2121')
        # review.click()
        # time.sleep(1)
        # submit = driver.find_element_by_id('#ember2131')

