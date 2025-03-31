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

def test_registration_positive(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'firstName').send_keys('Дмитрий')
    driver.find_element(By.NAME, 'lastName').send_keys('Шуметов')

    region_input = driver.find_element(By.CLASS_NAME, 'rt-select__input')
    region_input.click()
    region_input.send_keys('Москва г')

    try:
        suggestions = driver.find_elements(By.CLASS_NAME, 'rt-select__list-item')
        if suggestions:
            suggestions[0].click()
    except Exception as e:
        print('Не удалось выбрать регион:', e)

    driver.find_element(By.ID, 'address').send_keys('+79803670881')
    driver.find_element(By.ID, 'password').send_keys('Dumasuk0209')
    driver.find_element(By.ID, 'password-confirm').send_keys('Dumasuk0209')

    driver.find_element(By.NAME, 'register').click()

    time.sleep(3)
    page_text = driver.page_source.lower()
    if 'код подтверждения' in page_text or 'подтверждение' in page_text:
        print('Регистрация прошла успешно: форма подтверждения отображается')
    else:
        print('Не удалось найти форму подтверждения')