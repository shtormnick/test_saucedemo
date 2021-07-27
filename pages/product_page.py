from .base_page import BasePage
from .locators import BasePageLocators, CartPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def __init__(self):
       self.should_be_add_to_cart()
    
    def should_be_add_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART), "Add to Cart is abcent"
    
    def add_to_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME).text()
        price = self.browser.find_element(*ProductPageLocators.PRICE).text()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        self.browser.find_element(*BasePageLocators.CART_LINK).click()
        cart_price = self.browser.find_element(*CartPageLocators.CART_ITEM_PRICE).text()
        cart_item_name = self.browser.find_element(*CartPageLocators.CART_ITEM_NAME).text()
        assert price == cart_price, "Cart prise and price is not match"
        assert item_name == cart_item_name, "Cart item name and item name is not match"
    
    def filtered_items_by_low_price(self):
        self.browser.find_element(*ProductPageLocators.FILTER_HIGH_PRICE).click()
        list_of_items = self.browser.find_element(*ProductPageLocators.INVENTORY_LIST)
        inventory_item = self.browser.find_element(*ProductPageLocators.ITEM)
        price_list = []
        for inventory_item in list_of_items:
            price_item = self.browser.find_element(*ProductPageLocators.PRICE).text()[1:]
            price_list.append(price_item)
            for i in price_list:
                if price_list[i] <= price_item[i+1]:
                    return True
        
            