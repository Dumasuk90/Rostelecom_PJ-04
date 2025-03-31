import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    driver.get('https://lk.rt.ru/')

    yield driver
    driver.quit()

def test_auth_by_temp_code_positive(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    driver.find_element(By.ID, 'address').send_keys('+79803670881')

    driver.find_element(By.ID, 'otp_get_code').click()

    time.sleep(2)

    driver.find_element(By.ID,'otp-back').click()

    back_to_auth = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    if back_to_auth.is_displayed():
        print('Форма успешно вернулась к вводу номера.')
    else:
        print('Ошибка: Форма не обновилась.')