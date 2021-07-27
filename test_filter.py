import pytest
from pages.product_page import ProductPage


@pytest.mark.main_test
class TestLoginFormProductPage():
    @pytest.mark.checker
    def test_guest_can_see_title(self, browser, setup):
        link = "https://www.saucedemo.com/inventory.html"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.go_to_cart_page()
        self.page.should_be_correct_title()

    def test_guest_can_add_item_to_cart(self, browser, setup):
        link = "https://www.saucedemo.com/inventory.html"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_to_cart()

    def test_guest_add_to_cart_filtered_by_low_price_items(self, browser, setup):
        link = "https://www.saucedemo.com/inventory.html"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.filtered_items_by_low_price()

    def test_guest_add_to_cart_filtered_by_high_price_items(self, browser, setup):
        link = "https://www.saucedemo.com/inventory.html"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.filtered_items_by_high_price()
