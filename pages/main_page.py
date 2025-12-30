import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from config.urls import Urls


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(Urls.BASE_URL)

    @allure.step("Ждём загрузки главной страницы")
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликнуть на кнопку «Войти в аккаунт»")
    def click_login_button(self):
        self.click_by_js(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть на кнопку «Личный кабинет»")
    def click_account_button(self):
        self.click_by_js(MainPageLocators.ACCOUNT_BUTTON)
        self.wait_for_url_contains(Urls.PROFILE_PAGE)

    @allure.step("Кликнуть на ссылку «Конструктор»")
    def click_constructor_link(self):
        self.click_by_js(MainPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_url_contains(Urls.BASE_URL)

    @allure.step("Кликнуть на ссылку «Лента заказов»")
    def click_orders_feed_link(self):
        self.click_by_js(MainPageLocators.ORDERS_FEED_LINK)
        self.wait_for_url_contains(Urls.ORDER_FEED_PAGE)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_by_js(MainPageLocators.INGREDIENT_IMAGE)

    @allure.step("Получить модальное окно ингредиента")
    def find_ingredient_modal(self):
        return self.find(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Кликнуть на кнопку закрытия модального окна ингредиента")
    def click_modal_close_button(self):
        self.click_by_js(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Добавить первый ингредиент в корзину")
    def add_first_ingredient_to_basket(self):
        self.main_page_loading_wait()
        ingredient = self.find(MainPageLocators.INGREDIENT_IMAGE)
        basket = self.find(MainPageLocators.BASKET_ITEM)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step("Ждём, пока счетчик ингредиентов увеличится")
    def wait_for_ingredient_counter_not_zero(self, timeout=10):
        self.wait_until(
            lambda _: int(
                self.get_text(
                    MainPageLocators.INGREDIENT_COUNTER_VALUE
                ) or 0
            ) > 0,
            timeout=timeout
        )

    @allure.step("Получить значение счетчика ингредиентов")
    def find_ingredient_counter_value(self):
        return self.find(MainPageLocators.INGREDIENT_COUNTER_VALUE)

    @allure.step("Кликнуть на кнопку «Оформить заказ»")
    def click_order_button(self):
        self.click_by_js(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получить модальное окно заказа")
    def find_order_modal(self):
        return self.find(MainPageLocators.ORDER_MODAL)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_by_js(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)