from os import kill
from .base_page import BasePage
import re
from .locators import BasePageLocators, CartPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
       super().__init__(browser, url)
       self.should_be_add_to_cart()
          
    def should_be_add_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART), "Add to Cart is absent"
    
    def add_to_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        self.browser.find_element(*BasePageLocators.CART_LINK).click()
        cart_price = self.browser.find_element(*CartPageLocators.CART_ITEM_PRICE).text
        cart_item_name = self.browser.find_element(*CartPageLocators.CART_ITEM_NAME).text
        assert price == cart_price, "Cart prise and price is not match"
        assert item_name == cart_item_name, "Cart item name and item name is not match"
    
    def filtered_items_by_low_price(self):
        self.browser.find_element(*ProductPageLocators.FILTER_LOW_PRICE).click()
        list_of_items = self.browser.find_element(*ProductPageLocators.INVENTORY_LIST).text
        price = r"\d[0-9]*\.[0-9]*\d"
        list_of_items = re.findall(price,list_of_items)
        list_of_items = list(map(float, list_of_items))
        sorted_list_of_items = list_of_items[:]
        sorted_list_of_items.sort()
        assert list_of_items == sorted_list_of_items, "Filter sorted by ASC price"
    
    def filtered_items_by_high_price(self):
        self.browser.find_element(*ProductPageLocators.FILTER_HIGH_PRICE).click()
        list_of_items = self.browser.find_element(*ProductPageLocators.INVENTORY_LIST).text
        price = r"\d[0-9]*\.[0-9]*\d"
        list_of_items = re.findall(price,list_of_items)
        list_of_items = list(map(float, list_of_items))
        sorted_list_of_items = list_of_items[:]
        sorted_list_of_items.sort(reverse=True)
        assert list_of_items == sorted_list_of_items, "Filter sorted by Desc price"
