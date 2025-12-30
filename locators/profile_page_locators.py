from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_CARD_PROFILE_PAGE = (By.XPATH,"//li[contains(@class,'OrderHistory_listItem')]//a[contains(@class,'OrderHistory_link')]")
    ORDER_NUMBER_PROFILE_PAGE = (
        By.XPATH,
        "//ul[contains(@class,'OrderHistory_list')]"
        "/li[last()]"
        "//div[contains(@class,'OrderHistory_textBox')]"
        "/p[starts-with(text(),'#')]"
    )