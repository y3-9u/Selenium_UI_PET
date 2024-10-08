from .base_page import BasePage
from .locators import LoginPageLocators
import time
from config import Credentials


class LoginPage(BasePage):
    def input_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(Credentials.valid_email)
        time.sleep(2)

    def input_psw(self):
        login_psw = self.browser.find_element(*LoginPageLocators.LOGIN_PSW)
        login_psw.send_keys(Credentials.valid_psw)
        time.sleep(2)

    def submit_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
        time.sleep(2)
