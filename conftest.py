import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from helpers.api_user_helper import ApiUserHelper
from config.urls import Urls
from config.utils import Utils

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def api_user():
    user_data, token = ApiUserHelper.create_user()
    yield user_data, token
    ApiUserHelper.delete_user(token)


@pytest.fixture
def logged_in_user(driver, api_user):
    user_data, _ = api_user

    base = BasePage(driver)
    main = MainPage(driver)
    login = LoginPage(driver)

    main.open_main_page()
    main.click_login_button()
    login.login(user_data["email"], user_data["password"])

    base.wait_for_url_not_contains(Urls.LOGIN_PAGE)

    main.open_main_page()
    main.main_page_loading_wait()

    return driver


@pytest.fixture(scope="session")
def feed_user_credentials():
    return {
        "email": Utils.EMAIL,
        "password": Utils.PASSWORD
    }


@pytest.fixture
def logged_in_feed_user(driver, feed_user_credentials):
    user_data = feed_user_credentials

    base = BasePage(driver)
    main = MainPage(driver)
    login = LoginPage(driver)

    main.open_main_page()
    main.click_login_button()
    login.login(user_data["email"], user_data["password"])

    base.wait_for_url_not_contains(Urls.LOGIN_PAGE)

    main.open_main_page()
    main.main_page_loading_wait()

    return driver
