from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
from selenium.webdriver.common.by import By
import time

driver.get("https://3click.com/")
driver.find_elements(By.CLASS_NAME,'location-btn')[0].click()
time.sleep(1)
search = driver.find_element(By.ID,'input-150').send_keys("ist")
time.sleep(1)
result = driver.find_elements(By.CLASS_NAME,'mr-1')
for i in range(1,4,1):
    print(result[i].text)
print(result[3].text)
ist = driver.find_elements(By.CLASS_NAME,'text-truncate')[0].text
print(ist)
assert ist == 'استانبول'
time.sleep(5)


