import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException 
from .locators import ProductPageLocators

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
        link = self.browser.find_element(*ProductPageLocators.BUSKET)
        link.click()

    def should_be_price_the_same(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        name2 = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        assert name == name2, "Name is not the same"

    def should_be_name_the_same(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BUSKET).text
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price == price2, "Price is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_IN_MESSAGE), \
       "Success message is presented, but should not be"
        
    def should_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_IN_MESSAGE), \
       "Success message is disappeared"
