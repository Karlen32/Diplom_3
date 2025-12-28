from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config.urls import Urls
import allure

class LoginPage(BasePage):

    @allure.step("Кликнуть на ссылку «Восстановить пароль»")
    def click_forgot_password_link(self):
        self.click_by_js(LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.wait_for_url_contains(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find(LoginPageLocators.EMAIL_INPUT).clear()
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.find(LoginPageLocators.PASSWORD_INPUT).clear()
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Кликнуть на кнопку «Войти»")
    def click_login_button(self):
        self.click_by_js(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        