from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class find_site:
    URL_Base = ("https://3click.com/")
    driver.get(URL_Base)
    driver.maximize_window()

class import_text:
    element_field = driver.find_elements(By.CLASS_NAME, 'location-btn')[0]
    element_field.click()
    time.sleep(2)
    element_text = driver.find_element(By.ID, 'input-150')
    Text = ('پار', 'ika', 'bkk','mhd','lax','thr','kih')
    patterns_dict = {}
    for t in Text:
        patterns_dict[t] = []
    for pattern in Text:
        print(f'>> The searched word is equal to === {pattern}')
        element_text.send_keys(pattern)
        time.sleep(2)
        element_result = driver.find_elements(By.CLASS_NAME, 'mr-1')
        for result in range(1, len(element_result) - 1):
            subject_element = element_result[result].text
            does_contain = len(re.findall(pattern, subject_element)) > 0
            patterns_dict[pattern].append(does_contain)
            print(f'> {subject_element}: {does_contain}')
            element_text.send_keys(Keys.CONTROL + "a")
            element_text.send_keys(Keys.DELETE)
    driver.quit()

