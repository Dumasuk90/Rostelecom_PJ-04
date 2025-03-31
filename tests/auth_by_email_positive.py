import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')

    yield driver
    driver.quit()

def test_auth_by_email_positive(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys('dimasiks5700@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('Dumasuk0209')

    driver.find_element(By.ID, 'kc-login').click()

    time.sleep(3)
    current_url = driver.current_url
    if 'account' in current_url or 'lk.rt.ru' in current_url:
        print('Авторизация прошла успешно: пользователь зашёл в личный кабинет.')
    else:
        print('Авторизация не удалась: пользователь не зашёл в ЛК.')