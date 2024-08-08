from pages.main_page import MainPage
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('screenshots/login_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_filter_by_cat(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_cat()
    browser.save_screenshot('screenshots/filter_by_cat.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    browser.save_screenshot('screenshots/filter_by_name.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_show_bunny_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    browser.maximize_window()
    page.show_bunny_details()
    browser.save_screenshot('screenshots/bunny_details.png')


@pytest.mark.regression
def test_go_to_last_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_last_page()
    browser.save_screenshot('screenshots/last_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_put_like(user_auth, browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.put_like()
    browser.save_screenshot('screenshots/put_like.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_add_comment(user_auth, browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.add_comment()
    browser.save_screenshot('screenshots/add_comment.png')


@pytest.mark.regression
def test_enlarge_pet_photo(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.enlarge_pet_photo()
    browser.save_screenshot('screenshots/enlarge_pet_photo.png')
