from pages.base_page import BasePage
import allure
from locators.forgot_password_locators import ForgotPasswordLocators
from config.urls import Urls


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find(ForgotPasswordLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Кликнуть на кнопку «Восстановить»")
    def click_restore_button(self):
        self.click_by_js(ForgotPasswordLocators.RESTORE_BUTTON)
        self.wait_for_url_contains(Urls.RESET_PASSWORD_PAGE)

    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_password_visibility_button(self):
        self.click_by_js(ForgotPasswordLocators.PASSWORD_VISIBILITY_BUTTON)

    @allure.step("Получить поле ввода пароля")
    def get_password_input(self):
        return self.find(ForgotPasswordLocators.PASSWORD_INPUT)