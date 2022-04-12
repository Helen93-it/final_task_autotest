from .base_page import BasePage
from .locators import AddProductToBasket

class BasketPage(BasePage):

    def should_message_of_empty_baste(self):
        assert self.is_element_present(*AddProductToBasket.BASKET_EMPTY), \
            "The basket isn`t empty"

    def should_basket_has_not_items(self):
        assert not self.is_element_present(*AddProductToBasket.BASKET_ITEMS), \
            "The basket has items"