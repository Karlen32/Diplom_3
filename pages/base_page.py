import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from config.urls import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(Urls.BASE_URL)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу через JS")
    def click_by_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ждём, пока элемент исчезнет")
    def wait_for_element_hide(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ждём, что URL содержит часть")
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )

    @allure.step("Ждём, что URL НЕ содержит часть")
    def wait_for_url_not_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part not in d.current_url
        )

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)