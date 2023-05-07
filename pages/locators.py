from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_BUSKET = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
