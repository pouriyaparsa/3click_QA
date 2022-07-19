from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def log_event(message, log_console=True, log_to_file=True):
    if log_console:
        print(message)

    if log_to_file:
        with open('search.txt', 'a', encoding='utf-8') as f:
            f.write(message)


class find_site:
    URL_Base = ("https://3click.com/")
    driver.get(URL_Base)
    driver.maximize_window()


class Action:
    origin_element = driver.find_elements(By.CLASS_NAME, 'location-btn')[0]
    origin_element.click()
    time.sleep(1.5)
    Enter_text = driver.find_element(By.ID, 'input-150')
    search_dict = {'ist': 'استانبول',
                   'thr': 'تهران',
                   'mhd': 'مشهد',
                   'lax': 'لس آنجلس',
                   'swa': 'صبیحا'
                   }
    for keyword in search_dict.keys():
        log_event(f'       >>>> The searched word is equal to {keyword}', log_console=False, log_to_file=True)
        Enter_text.send_keys(keyword)
        time.sleep(2)
        total_result = driver.find_elements(By.CLASS_NAME, 'v-item-group')
        for result in range(len(total_result) - 1):
            result_text = total_result[result].text
            log_event(result_text)
            if search_dict.get(keyword) in result_text:
                log_event(search_dict.get(keyword))
                log_event("وجود دارد")
            else:
                log_event(search_dict.get(keyword))
                log_event('ندارد')
        Enter_text.send_keys(Keys.CONTROL + "a")
        Enter_text.send_keys(Keys.DELETE)
    driver.quit()
