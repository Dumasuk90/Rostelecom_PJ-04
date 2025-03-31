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

def test_password_length(driver):
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

    driver.find_element(By.ID, 'address').send_keys('+79066624456')
    driver.find_element(By.ID, 'password').send_keys('Dumasuk')
    driver.find_element(By.NAME, 'register').click()

    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta--error')))
    assert 'Длина пароля должна быть не менее 8 символов' in error_message.text, 'Ошибка не отображается!'

    print('Тест успешно пройден: короткий пароль не подошёл.')

    time.sleep(2)

    # Проверяем, что ошибка окрашена в красный цвет
    color = error_message.value_of_css_property('color')
    print('rgba(255, 12, 12)', color)
    assert '255' in color and '12' in color, 'Ошибка не окрашена в красный цвет!'
    print('Тест успешно пройден: короткий пароль не подошёл, ошибка отображается в красном цвете.')