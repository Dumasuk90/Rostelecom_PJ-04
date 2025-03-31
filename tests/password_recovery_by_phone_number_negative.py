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

def test_password_recovery_by_phone_number_negative(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).clear()
    driver.find_element(By.ID, 'username').send_keys('+70000000000')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'captcha')))

    # Вводим капчу вручную
    time.sleep(20)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reset'))).click()

    # Вводим в поле для ввода кода некорректный код
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'rt-code-input')))
    driver.find_element(By.ID, 'rt-code-input').send_keys('111111')

    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))
    expected_text = 'Неверный код. Повторите попытку'
    assert expected_text in error_message.text, f'Ожидали "{expected_text}", но получили "{error_message.text}"'

    print('Тест успешно пройден: некорректный номер не позволяет восстановить пароль.')