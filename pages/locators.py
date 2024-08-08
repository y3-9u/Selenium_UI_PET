from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.CSS_SELECTOR, "div.p-dropdown-trigger")
    FILTER_BY_CAT = (By.ID, "pv_id_2_1")
    FILTER_BY_NAME = (By.ID, "petName")
    BUNNY_DETAILS = (By.XPATH, "//div[contains(@class, 'product-grid-item-content') and .//div[text("
                               ")='Bunny']]/following-sibling::div[contains(@class, "
                               "'product-grid-item-bottom')]//span[text()='Details']")
    LAST_PAGE_BTN = (By.CSS_SELECTOR, "button.p-paginator-last.p-paginator-element.p-link")
    BUNNY_LIKE = (By.XPATH, "//div[contains(@class, 'product-grid-item-content') and .//div[text("
                            ")='Bunny']]//following-sibling::div[contains(@class, 'product-grid-item-bottom')]//i["
                            "contains(@class, 'pi pi-thumbs-up')]")
    COMMENT_FIELD_ACTIVATION = (By.XPATH, "//div[@id='app']/main/div[2]/div/div/div[3]/form/div/div/div[2]/div/p")
    COMMENT_EDIT = (By.XPATH, "//div[@id='app']/main/div[2]/div/div/div[3]/form/div/div/div[2]/div")
    COMMENT_SAVE = (By.XPATH, "//div[@id='app']/main/div[2]/div/div/div[3]/form/div/button/span[2]")
    ENLARGE_PET_PHOTO = (By.XPATH, "//div[@id='app']/main/div/div/div/div/div[2]/span/div/i")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PSW = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    EDIT_PET = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div/div/div/div[2]/button/span[2]")
    EDIT_PET_NAME = (By.XPATH, "//*[@id='name']")
    SAVE_EDITED_PET = (By.XPATH, "//div[@id='app']/main/div/form/div/div[2]/div[3]/button/span")
    ADD_PET_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div/div/div/button/span")
    ADD_PET_NAME = (By.XPATH, "//input[@id='name']")
    ADD_TYPE_DROPDOWN = (By.XPATH, "//*[@id='typeSelector']")
    ADD_TYPE_DROPDOWN_PARROT = (By.XPATH, "//li[@aria-label='parrot']")
    ADD_PET_SUBMIT_BTN = (By.XPATH, "//div[@id='app']/main/div/div/form/div/div[2]/div[3]/button/span[2]")
    CHOOSE_PHOTO_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div[2]/div/span/span[2]")
    INPUT_PHOTO = (By.XPATH, "//*[@id='app']/main/div/div/div[2]/div[2]/div/span/input")
    ADD_PHOTO_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div[2]/div/span/span[2]")
    DELETE_PET_BTN = (By.XPATH, "//*[@id='app']/main/div/div/div[2]/div/div[3]/div/div[2]/button[2]/span[2]")
    DELETE_PET_CONFIRM = (By.XPATH, "//div[3]/div[2]/button[2]/span")
