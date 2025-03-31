import webbrowser
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
@pytest.fixture()
def driver():
    executable_path = 'C:/PycharmProjects/ROSTELECOM(PJ-04)/chromedriver.exe'
    WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()