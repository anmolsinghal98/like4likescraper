import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import ConfigParser

setting_file="config/config.txt"
config=ConfigParser.ConfigParser()
config.readfp(open(setting_file))

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.

driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)  # Optional argument, if not specified will search path.
driver.get('https://www.like4like.org/login/')

username_id = driver.find_element_by_id("username")
password_id = driver.find_element_by_id("password")
username_id.send_keys(username)
password_id.send_keys(password)
login = driver.find_element_by_link_text("Submit").click()


# driver.quit()