from .base_page import BasePage
from .locators import AddProductToBasket


class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        self.should_compare_price_in_basket_and_main_paig()
        self.should_be_compare_name_book_in_basket_and_on_main_page()

    def should_add_product_in_basket(self):
        self.browser.find_element(*AddProductToBasket.ADD_BUTTON).click()

    def should_be_compare_name_book_in_basket_and_on_main_page(self):
        assert self.browser.find_element(*AddProductToBasket.NAME_PRODUCT_IN_BASKET).text == self.browser.find_element(
             *AddProductToBasket.NAME_PRODUCT).text, "Names are not equal"

    def should_compare_price_in_basket_and_main_paig(self):
        assert self.browser.find_element(*AddProductToBasket.PRICE_PRODUCT_IN_BASKET).text == self.browser.find_element(
             *AddProductToBasket.PRICE_PRODUCT).text, "Prices are not equal"
