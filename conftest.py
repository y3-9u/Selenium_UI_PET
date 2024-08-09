import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def user_auth(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_login()
    page.input_psw()
    page.submit_btn()
