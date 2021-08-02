from .base_page import BasePage
import re
from .locators import BasePageLocators, CartPageLocators, ProductPageLocators


class ProductPage(BasePage):
    """
    ProductPage class describe tests which connected with functional and visual elements on current page 
    """

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.should_be_add_to_cart()
        self.should_be_correct_title()

    def should_be_correct_title(self):
        assert self.is_element_present(
            *ProductPageLocators.HEADER_TEXT_ON_PRODUCT_PAGE), "Title is incorrect or absent op page"

    def should_be_add_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART), "Add to Cart is absent"

    def add_to_cart_one_item(self):
        # this variable contains name of item which we add to cart in (string)
        item_name = self.browser.find_element(*ProductPageLocators.NAME).text
        # this variable contains price of neded item (string)
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        self.browser.find_element(*BasePageLocators.CART_LINK).click()
        # this variable contains items price which displayed on cart page (str)
        cart_price = self.browser.find_element(
            *CartPageLocators.CART_ITEM_PRICE).text
        # this variable contains items name which displayed on cart page (str)
        cart_item_name = self.browser.find_element(
            *CartPageLocators.CART_ITEM_NAME).text
        assert price == cart_price, "Cart price and price is not match"
        assert item_name == cart_item_name, "Cart item name and item name is not match"

    def filtered_items_by_low_price(self):
        """Filters by price ascending

        This function takes a price of items on page and compare sorted and converted list of equal prices
        """
        self.browser.find_element(
            *ProductPageLocators.FILTER_LOW_PRICE).click()
        # this variable contains list of items which displayed on page (list of string)
        list_of_items = self.browser.find_element(
            *ProductPageLocators.INVENTORY_LIST).text
        # regular expression that which cuts off all not needed data from list
        price = r"\d[0-9]*\.[0-9]*\d"
        # list of prices on page (str)
        list_of_items = re.findall(price, list_of_items)
        # convert str to float
        list_of_items = list(map(float, list_of_items))
        # copy list
        sorted_list_of_items = list_of_items[:]
        # sort copied list
        sorted_list_of_items.sort()
        # compare actual list of price taker on page with sorted and reversed list of prices
        assert list_of_items == sorted_list_of_items, "Filter sorted by ASC price"

    def filtered_items_by_high_price(self):
        """Filters by price decending

        This function takes a price of items on page and compare sorted list of equal prices
        """
        self.browser.find_element(
            *ProductPageLocators.FILTER_HIGH_PRICE).click()
        # this variable contains list of items which displayed on page (list of string)
        list_of_items = self.browser.find_element(
            *ProductPageLocators.INVENTORY_LIST).text
        # regular expression that which cuts off all not needed data from list
        price = r"\d[0-9]*\.[0-9]*\d"
        # list of prices on page (str)
        list_of_items = re.findall(price, list_of_items)
        # convert str to float
        list_of_items = list(map(float, list_of_items))
        # copy list
        sorted_list_of_items = list_of_items[:]
        # sort copied list and reverse
        sorted_list_of_items.sort(reverse=True)
        assert list_of_items == sorted_list_of_items, "Filter sorted by Desc price"
