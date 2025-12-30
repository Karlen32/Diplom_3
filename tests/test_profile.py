import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from config.urls import Urls


class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_go_to_profile_page(self, logged_in_user):
        driver = logged_in_user
        main = MainPage(driver)

        main.main_page_loading_wait()
        main.click_account_button()

        assert main.is_url_contains(Urls.PROFILE_PAGE)

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history_page(self, logged_in_user):
        driver = logged_in_user
        main = MainPage(driver)
        profile = ProfilePage(driver)

        main.click_account_button()
        profile.click_order_history_link()

        assert profile.is_url_contains(Urls.ORDER_HISTORY_PAGE)

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_user):
        driver = logged_in_user
        main = MainPage(driver)
        profile = ProfilePage(driver)

        main.click_account_button()
        profile.click_logout_button()

        assert profile.is_url_contains(Urls.LOGIN_PAGE)