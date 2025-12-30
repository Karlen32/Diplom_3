import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

class TestFeed:
    @allure.title("Модальное окно заказа открывается при клике на заказ")
    def test_order_modal_opens_on_click(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.click_orders_feed_link()
        feed.click_first_order()

        assert feed.find_order_modal().is_displayed()

    @allure.title("Заказы из «История заказов» отображаются в «Лента заказов»")
    def test_user_orders_visible_in_feed(self, logged_in_feed_user):
        driver = logged_in_feed_user
        profile = ProfilePage(driver)
        feed = FeedPage(driver)
        main = MainPage(driver)

        main.main_page_loading_wait()
        main.click_account_button()
        profile.click_order_history_link()
        order_number = profile.get_last_order_number()
        main.click_orders_feed_link()
        order_number_in_feed = feed.get_order_number_from_orders_page()

        assert order_number == order_number_in_feed

    @allure.title("Счетчики заказов за все время увеличиваются после оформления заказа")
    def test_orders_counters_increase_after_order(self, logged_in_feed_user):
        driver = logged_in_feed_user
        main = MainPage(driver)
        feed = FeedPage(driver)

        main.main_page_loading_wait()
        main.click_orders_feed_link()
        all_time_before = feed.get_orders_counters_all_time()

        main.open_main_page()
        main.add_first_ingredient_to_basket()
        main.click_order_button()
        main.close_order_modal()
        main.click_orders_feed_link()
        all_time_now = feed.get_orders_counters_all_time()

        assert all_time_before < all_time_now

    @allure.title("Счетчики заказов за сегодня увеличиваются после оформления заказа")
    def test_orders_counters_today_increase_after_order(self, logged_in_feed_user):
        driver = logged_in_feed_user
        main = MainPage(driver)
        feed = FeedPage(driver)

        main.main_page_loading_wait()
        main.click_orders_feed_link()
        today_before = feed.get_orders_counters_today()

        main.open_main_page()
        main.add_first_ingredient_to_basket()
        main.click_order_button()
        main.close_order_modal()
        main.click_orders_feed_link()
        today_now = feed.get_orders_counters_today()

        assert today_before < today_now

    @allure.title("Заказ появляется в списке в работе")
    def test_order_appears_in_progress(self, logged_in_feed_user):
        driver = logged_in_feed_user
        main = MainPage(driver)
        feed = FeedPage(driver)
        profile = ProfilePage(driver)

        main.open_main_page()
        main.main_page_loading_wait()
        main.add_first_ingredient_to_basket()
        main.click_order_button()
        main.close_order_modal()
        main.click_account_button()
        profile.click_order_history_link()
        order_number_in_history = profile.get_last_order_number()

        main.click_orders_feed_link()
        order_number_in_feed = feed.get_orders_in_progress()

        assert order_number_in_history == order_number_in_feed