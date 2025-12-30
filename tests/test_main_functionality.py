import allure
from pages.main_page import MainPage
from config.urls import Urls
from locators.main_page_locators import MainPageLocators


class TestMainNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main = MainPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.click_orders_feed_link()
        main.click_constructor_link()

        assert main.is_url_contains(Urls.BASE_URL)

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_orders_feed(self, driver):
        main = MainPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.click_orders_feed_link()

        assert main.is_url_contains(Urls.ORDER_FEED_PAGE)

    @allure.title("При клике на ингредиент открывается модалка")
    def test_ingredient_modal_opens(self, driver):
        main = MainPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.click_first_ingredient()

        assert main.find_ingredient_modal().is_displayed()

    @allure.title("Модалка ингредиента закрывается")
    def test_ingredient_modal_closes(self, driver):
        main = MainPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.click_first_ingredient()
        main.find_ingredient_modal()

        main.click_modal_close_button()
        main.wait_for_element_hide(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("При добавлении ингредиента увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.add_first_ingredient_to_basket()
        main.wait_for_ingredient_counter_not_zero()

        counter_text = main.get_text(MainPageLocators.INGREDIENT_COUNTER_VALUE)
        assert int(counter_text) > 0

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, logged_in_user):
        main = MainPage(logged_in_user)

        main.main_page_loading_wait()
        main.add_first_ingredient_to_basket()
        main.add_first_ingredient_to_basket()
        main.click_order_button()

        assert main.find_order_modal().is_displayed()