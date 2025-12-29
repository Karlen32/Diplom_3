from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from config.urls import Urls


def login_via_ui(driver, email, password):
    base = BasePage(driver)
    main = MainPage(driver)
    login = LoginPage(driver)

    main.open_main_page()
    main.click_login_button()
    login.login(email, password)

    base.wait_for_url_not_contains(Urls.LOGIN_PAGE)

    main.open_main_page()
    main.main_page_loading_wait()