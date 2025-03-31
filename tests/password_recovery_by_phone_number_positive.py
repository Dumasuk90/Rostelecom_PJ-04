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

def test_password_recovery_by_phone_number_positive(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).clear()
    driver.find_element(By.ID, 'username').send_keys('+79803670881')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'captcha')))

    #Вводим тест с картинки вручную
    time.sleep(20)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reset'))).click()

    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@inputmode="numeric"]')))

    #Вводим СМС код вручную
    time.sleep(20)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-new')))
    driver.find_element(By.ID, 'password-new').send_keys('Dumasuk0209!!')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    driver.find_element(By.ID, 'password-confirm').send_keys('Dumasuk0209!!')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-reset-pass'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    print('Пароль успешно восстановлен, клиент вернулся на страницу авторизации.')