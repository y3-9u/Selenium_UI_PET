import time
from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os


class ProfilePage(BasePage):
    def edit_pet(self):
        try:
            self.browser.refresh()
            wait = WebDriverWait(self.browser, 30)

            edit_pet = wait.until(EC.visibility_of_element_located(ProfilePageLocators.EDIT_PET))
            wait.until(EC.element_to_be_clickable(ProfilePageLocators.EDIT_PET))
            edit_pet.click()

            edit_pet_name = wait.until(EC.visibility_of_element_located(ProfilePageLocators.EDIT_PET_NAME))
            edit_pet_name.click()

            time.sleep(3)

            edit_pet_name.clear()
            time.sleep(3)
            edit_pet_name.send_keys('Kittie')

            save_edited_pet = wait.until(EC.element_to_be_clickable(ProfilePageLocators.SAVE_EDITED_PET))
            save_edited_pet.click()
            time.sleep(3)

            print("Pet profile updated successfully.")
        except NoSuchElementException as e:
            print(f"An error occurred: {e}")

    def add_pet(self):
        add_pet_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN)
        add_pet_btn.click()

        add_pet_name = self.browser.find_element(*ProfilePageLocators.ADD_PET_NAME)
        add_pet_name.click()
        add_pet_name.send_keys('Boo')
        add_pet_name.send_keys(Keys.ENTER)
        time.sleep(2)

        self.browser.find_element(*ProfilePageLocators.ADD_TYPE_DROPDOWN).click()
        add_type_parrot = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located
                                                                (ProfilePageLocators.ADD_TYPE_DROPDOWN_PARROT))
        add_type_parrot.click()
        time.sleep(2)

        add_pet_submit_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET_SUBMIT_BTN)
        add_pet_submit_btn.click()
        time.sleep(2)

        choose_photo_btn = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable
                                                                 (ProfilePageLocators.CHOOSE_PHOTO_BTN))
        choose_photo_btn.click()
        time.sleep(2)

        # Получаем текущую директорию
        current_dir = os.path.dirname(__file__)

        # Строим относительный путь к файлу
        relative_path = os.path.join(current_dir, '..', 'pics', 'Boo.png')

        # Преобразуем относительный путь в абсолютный
        absolute_path = os.path.abspath(relative_path)

        # Используем абсолютный путь для загрузки файла
        input_photo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.INPUT_PHOTO)
        )
        input_photo.send_keys(absolute_path)

        add_photo_btn = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ADD_PHOTO_BTN)
        )
        add_photo_btn.click()
        time.sleep(5)

    def delete_third_pet(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_BTN).click()
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_CONFIRM).click()
        time.sleep(3)
