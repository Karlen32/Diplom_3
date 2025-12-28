from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    OVERLAY = (By.XPATH, ".//div[contains(@class,'Modal_modal_overlay')]/parent::div")
    ACCOUNT_BUTTON = (By.XPATH,"//a[@href='/account' and .//p[text()='Личный Кабинет']]")
    CONSTRUCTOR_LINK = (By.XPATH,"//p[text()='Конструктор']/parent::a")
    ORDERS_FEED_LINK = (By.XPATH,"//p[text()='Лента Заказов']/parent::a")
    INGREDIENT_MODAL = (By.XPATH,"//div[contains(@class,'Modal_modal__contentBox')]")
    MODAL_CLOSE_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_IMAGE = (By.XPATH,".//img[contains(@class,'BurgerIngredient_ingredient__image')]")
    INGREDIENT_COUNTER_VALUE = (By.XPATH,".//p[contains(@class,'counter_counter__num')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH,"//div[contains(@class,'Modal_modal__contentBox')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")
    BASKET_ITEM = (By.XPATH,"//li[contains(@class,'BurgerConstructor_basket__listItem')]")