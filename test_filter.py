import pytest
from pages.product_page import ProductPage


@pytest.mark.main_test
class TestLoginFormProductPage():
    
    def test_guest_add_to_cart_filtered_items(self, browser):
        
        link = "https://www.saucedemo.com/inventory.html"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.filtered_items_by_low_price()
        self.page.add_to_cart()
