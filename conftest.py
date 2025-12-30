import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers.login_helper import login_via_ui
from helpers.api_user_helper import ApiUserHelper
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
    login_via_ui(
        driver,
        user_data["email"],
        user_data["password"]
    )
    return driver


@pytest.fixture
def logged_in_feed_user(driver):
    login_via_ui(
        driver,
        Utils.EMAIL,
        Utils.PASSWORD
    )
    return driver



