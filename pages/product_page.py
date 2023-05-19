from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException 
import math

class Locators():
    BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_BUSKET = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    
    

class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_busket(self):
        link = self.browser.find_element(*Locators.BUSKET)
        link.click()

    def should_be_price_the_same(self):
        assert self.browser.find_element(*Locators.NAME_IN_MESSAGE).text == self.browser.find_element(*Locators.NAME_OF_BOOK).text, "name is not the same"

    def should_be_name_the_same(self):
        assert self.browser.find_element(*Locators.PRICE_IN_BUSKET).text == self.browser.find_element(*Locators.PRICE_OF_PRODUCT).text, "price is not the same"
