from pages.base_page import BasePage
import allure
from locators.profile_page_locators import ProfilePageLocators
from config.urls import Urls


class ProfilePage(BasePage):
    @allure.step("Кликнуть на ссылку «История заказов»")
    def click_order_history_link(self):
        self.click_by_js(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_for_url_contains(Urls.ORDER_HISTORY_PAGE)

    @allure.step("Кликнуть на кнопку «Выход»")
    def click_logout_button(self):
        self.click_by_js(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_url_contains(Urls.LOGIN_PAGE)
    
    @allure.step("Получить номер последнего заказа")
    def get_last_order_number(self) -> str:
        number = self.find(ProfilePageLocators.ORDER_NUMBER_PROFILE_PAGE)
        return number.text.replace('#', '')