from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.com/")

web_element = driver.find_element(By.NAME, 'search')
web_element.send_keys("Python" + Keys.ENTER)

time.sleep(30)