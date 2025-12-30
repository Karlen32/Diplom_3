from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure


class FeedPage(BasePage):

    @allure.step("Кликнуть на первый заказ")
    def click_first_order(self):
        order = self.find(FeedPageLocators.ORDER_CARD_FEED_PAGE)
        order.click()

    @allure.step("Получить модальное окно заказа")
    def find_order_modal(self):
        return self.find(FeedPageLocators.ORDER_MODAL_FEED_PAGE)

    @allure.step("Получить номер заказа из страницы заказов")
    def get_order_number_from_orders_page(self):
        number = self.find(FeedPageLocators.ORDER_NUMBER_IN_FEED_PAGE)
        return number.text.replace('#', '')

    @allure.step("Получить счетчики заказов за все время")
    def get_orders_counters_all_time(self):
        number = self.find(FeedPageLocators.ORDER_COUNTER_FEED_PAGE_ALL_TIME)
        return number.text.replace('#', '')

    @allure.step("Получить счетчики заказов за сегодня")
    def get_orders_counters_today(self):
        number = self.find(FeedPageLocators.ORDER_COUNTER_FEED_PAGE_TODAY)
        return number.text.replace('#', '')

    @allure.step("Получить список заказов в процессе")
    def get_orders_in_progress(self):
        number = self.find(FeedPageLocators.ORDER_IN_PROGRESS_LIST)
        return number.text.replace('#', '')
