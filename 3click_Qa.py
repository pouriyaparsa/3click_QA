import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
driver.maximize_window()
threeclick = "https://3click.com/"
driver.get(threeclick)
# from time import sleep
# sleep(1)
print(driver.title)
print(driver.current_url)
from selenium.webdriver.common.by import By
# banner = driver.find_element(By.CLASS_NAME,'banner').click()
# print(driver.title)
# print(driver.current_url)
# driver.back()
flight = driver.find_elements(By.CLASS_NAME, 'nav__item')[0].click()
print(driver.title)
print(driver.current_url)
# driver.back()
# flight = driver.find_elements(By.CLASS_NAME, 'nav__item')[1].click()
# print(driver.title)
# print(driver.current_url)
# driver.back()
# flight = driver.find_elements(By.CLASS_NAME, 'nav__item')[2].click()
# print(driver.title)
# print(driver.current_url)
# driver.back()
# flight = driver.find_elements(By.CLASS_NAME, 'nav__item')[3].click()
# print(driver.title)
# print(driver.current_url)
# driver.back()
# flight = driver.find_elements(By.CLASS_NAME, 'nav__item')[4].click()
# print(driver.title)
# print(driver.current_url)
# checkbox_roundtrip = driver.find_elements(By.CLASS_NAME, 'trip-type__item')[1].click()
# time.sleep(2)
# origin = driver.find_elements(By.CLASS_NAME,'location-btn')[0]
# origin.click()
# time.sleep(1)
# origin_city = driver.find_elements(By.CLASS_NAME,'justify-center.v-list-item.v-list-item--link.theme--light')[0]
# origin_city.click()
# destination = driver.find_elements(By.CLASS_NAME,'location-btn')[1]
# destination.click()
# time.sleep(1)
# destination_city = driver.find_elements(By.CLASS_NAME, 'justify-center.v-list-item.v-list-item--link.theme--light')[28]
# destination_city.click()
date = driver.find_elements(By.CLASS_NAME,'pb-3')[0]
date.click()
set_date = driver.find_elements(By.CLASS_NAME,'calendar__days--day')[31]
set_date.click()
passangers = driver.find_elements(By.CLASS_NAME,'pb-3')[1]
passangers.click()
