from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH,"//div[label[text()='Email']]//input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    PASSWORD_VISIBILITY_BUTTON = (By.XPATH, "//div[label[text()='Пароль']]//div[contains(@class,'input__icon')]")
