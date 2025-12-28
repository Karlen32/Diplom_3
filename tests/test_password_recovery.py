import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from config.urls import Urls


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_open_forgot_password_page(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)

        main.open_main_page()
        main.click_login_button()
        login.click_forgot_password_link()

        assert Urls.FORGOT_PASSWORD_PAGE in driver.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)
        forgot = ForgotPasswordPage(driver)

        main.open_main_page()
        main.click_login_button()
        login.click_forgot_password_link()
        forgot.enter_email("test@mail.ru")
        forgot.click_restore_button()

        assert Urls.RESET_PASSWORD_PAGE in driver.current_url

    @allure.title("Кнопка показать/скрыть пароль делает поле активным")
    def test_password_visibility_button_activates_input(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)
        forgot = ForgotPasswordPage(driver)

        main.open_main_page()
        main.click_login_button()
        login.click_forgot_password_link()
        forgot.enter_email("test@mail.ru")
        forgot.click_restore_button()

        password_input = forgot.get_password_input()
        forgot.click_password_visibility_button()

        assert password_input == driver.switch_to.active_element