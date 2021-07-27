from .locators import CartPageLocators, BasePageLocators
from .base_page import BasePage


class CartPage(BasePage):

    def cart_shuld_be_empty(self):
        assert self.element_is_not_present(
            *CartPageLocators.CART_ITEM), "Cart is not empty"

    def cart_bage_have_not_counter(self):
        assert self.element_is_not_present(
            *BasePageLocators.CART_BADGE), "Cart counter is not Null"

    def cart_should_have_item(self):
        assert self.is_element_present(
            *CartPageLocators.CART_ITEM), "Cart have no item"
