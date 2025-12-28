from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDER_CARD_FEED_PAGE = (
        By.XPATH,
        "//a[contains(@class,'OrderHistory_link')]"
    )

    ORDER_MODAL_FEED_PAGE = (
        By.XPATH,
        "//div[contains(@class,'Modal_modal__contentBox')]//p[starts-with(text(),'#')]"
    )
    ORDER_NUMBER_IN_FEED_PAGE = (
        By.XPATH,
        "//li[contains(@class,'OrderHistory_listItem')]//p[starts-with(text(),'#')]"
    )

    ORDER_COUNTER_FEED_PAGE_ALL_TIME = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']/following-sibling::p"
    )

    ORDER_COUNTER_FEED_PAGE_TODAY = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p"
    )

    ORDER_IN_PROGRESS_LIST = (
        By.XPATH,
        "//p[normalize-space()='В работе:']"
        "/following-sibling::ul[1]"
        "//li[normalize-space() and translate(text(),'0123456789','')='']"
    )
