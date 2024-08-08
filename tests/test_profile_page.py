import pytest
from pages.profile_page import ProfilePage


@pytest.mark.smoke
@pytest.mark.regression
def test_add_pet(user_auth, browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.add_pet()
    browser.save_screenshot('screenshots/added_pet.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_third_pet(user_auth, browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.delete_third_pet()
    browser.save_screenshot('screenshots/deleted_pet.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_edit_pet(browser, user_auth):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.edit_pet()
    screenshot = browser.save_screenshot('screenshots/edited_pet.png')
    current_url = browser.current_url
    assert screenshot
    assert current_url == "http://34.141.58.52:8080/#/profile?message=Your+pet+has+been+successfully+saved"
