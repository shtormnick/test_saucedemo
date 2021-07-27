from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():
    '''
        This class describs common functions than we can use on any page 
    '''
    def __init__(self, brouser, url):
        self.brouser = brouser
        self.url = url
    
    def open(self):
        self.brouser.get(self.url)

    def go_to_cart_page(self):
        button = self.browser.find_element(*BasePageLocators.CART_LINK_ON_PRODUCT_PAGE)
        button.click()
        assert "cart" in self.browser.current_url, "Wrong page (not a Cart page)"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
