
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_busket()          # выполняем метод страницы — добавляем в корзину товар
    page.should_be_price_the_same()
    page.should_be_name_the_same()

