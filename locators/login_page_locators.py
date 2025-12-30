from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH,"//div[label[text()='Email']]//input")
    PASSWORD_INPUT = (By.XPATH,"//div[label[text()='Пароль']]//input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")