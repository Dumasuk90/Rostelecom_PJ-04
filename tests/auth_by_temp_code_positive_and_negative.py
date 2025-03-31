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

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@inputmode="numeric"]')))

    #Ввод кода вручную
    WebDriverWait(driver, 60).until(lambda d: 'https://lk.rt.ru/' in d.current_url)
    if driver.current_url == 'https://lk.rt.ru/':
        print('Авторизация по временному коду прошла успешно.')
    else:
        print('Авторизация не выполнена или не произошло перенаправление в личный кабинет.')