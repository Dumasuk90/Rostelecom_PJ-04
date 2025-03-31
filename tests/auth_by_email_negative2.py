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

def test_auth_by_email_negative2(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys('dimasiks0@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('@@@Dumasuk0209@')

    driver.find_element(By.ID, 'kc-login').click()

    time.sleep(3)
    error_block = driver.find_element(By.ID, 'form-error-message')
    if 'неверный логин или пароль' in error_block.text.lower():
        print('Форма об ошибке авторизации отображается корректно.')
    else:
        print('Форма об ошибке авторизации не отображается.')

    forgot_pass_link = driver.find_element(By.ID, 'forgot_password')
    color = forgot_pass_link.value_of_css_property('color')
    print(f'Цвет ссылки "Забыл пароль": {color}')

    if 'rgba(255, 79, 18)' in color or 'rgb(255, 79, 18)' in color:
        print('Элемент "Забыл пароль" перекрасился в оранжевый.')
    else:
        print('Цвет элемента не изменился.')