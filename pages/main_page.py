from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def filter_by_cat(self):
        filter_dropdown = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable(MainPageLocators.FILTER_BY_TYPE)
        )
        filter_dropdown.click()
        time.sleep(1)

        wait.until(
            EC.visibility_of_element_located(MainPageLocators.FILTER_BY_CAT)
        )
        cat_select = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(MainPageLocators.FILTER_BY_CAT)
        )
        cat_select.click()
        time.sleep(3)

    def filter_by_name(self):
        name_enter = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        name_enter.send_keys('Bunny')
        name_enter.send_keys(Keys.ENTER)
        time.sleep(2)

    def show_bunny_details(self):
        bunny_details = self.browser.find_element(*MainPageLocators.BUNNY_DETAILS)
        bunny_details.click()
        time.sleep(2)

    def go_to_last_page(self):
        last_page = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LAST_PAGE_BTN)
        )
        last_page.click()
        time.sleep(2)

    def put_like(self):
        bunny_like = self.browser.find_element(*MainPageLocators.BUNNY_LIKE)
        bunny_like.click()
        time.sleep(2)

    def add_comment(self):
        bunny_details = self.browser.find_element(*MainPageLocators.BUNNY_DETAILS)
        bunny_details.click()
        bunny_comment = self.browser.find_element(*MainPageLocators.COMMENT_FIELD_ACTIVATION)
        bunny_comment.send_keys('Beauty')
        comment_save = self.browser.find_element(*MainPageLocators.COMMENT_SAVE)
        comment_save.click()
        time.sleep(3)

    def enlarge_pet_photo(self):
        bunny_details = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNNY_DETAILS)
        )
        bunny_details.click()
        time.sleep(5)

        enlarge_pet_photo = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(MainPageLocators.ENLARGE_PET_PHOTO)
        )
        enlarge_pet_photo.click()
        time.sleep(5)
