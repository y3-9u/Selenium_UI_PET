from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    return driver
