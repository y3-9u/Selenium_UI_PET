import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_login()
    page.input_psw()
    page.submit_btn()
    browser.save_screenshot('screenshots/profile_page.png')
