from selenium import webdriver
## step 1 >import selenium
from selenium import webdriver
## step 2.1  > import web driver manual
# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
## step 2.2 > import web driver automate
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
## step 3 > import time sleep
from time import sleep
## browser action 1 > open website
url1 = "https://www.google.com/"
driver.get(url1)
## browser action 2 > find search_field
search_field = driver.find_element("name", "q")
# browser action 3 > imput text
search_field.send_keys("3click")
## step 3 > import keys
from selenium.webdriver.common.keys import Keys
## browser action 4 > inter text
search_field.send_keys(Keys.RETURN)
## step 4 > new URL
url2 = "https://3click.com/"
driver.get(url2)
## browser action 5 > clickables
driver.find_element('id', 'js-link-box-en').click()
## browser action 6 > checked text imputed
# check1 = driver.find_element('id', 'Welcome_to_Wikipedia').text
# assert check1 == 'Welcome to Wikipedia'
# print(check1)
## dependency vabastegi ha for exaple library
