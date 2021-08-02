from selenium.webdriver.common.by import By


class BasePageLocators():
    """
    BasePageLocators contains main common web elements with can identify pages
    """

    MENU = (By.ID, "react-burger-menu-btn")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    FILTER = (By.CLASS_NAME, "product_sort_container")


class LoginPageLocators():
    """
        LoginPageLocators contains main common web elements with can identify login page
    """
    LOGIN_FORM = (By.CLASS_NAME, "login-box")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_INPUT = (By.ID, "user-name")
    LOGIN_BUTTON = (By.ID, "login-button")


class CartPageLocators():
    """
        CartPageLocators contains main common web elements with can identify cart page
    """
    HEADER_TEXT = (By.CLASS_NAME, "title")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


class ProductPageLocators():
    """
        ProductPageLocators contains main common web elements with can identify product page
    """
    HEADER_TEXT_ON_PRODUCT_PAGE = (
        By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
    ADD_TO_CART = (By.XPATH, "//*[.=\"Add to cart\"]")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    ITEM = (By.CLASS_NAME, "inventory_item")
    FILTER_LOW_PRICE = (
        By.XPATH, "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[3]")
    FILTER_HIGH_PRICE = (
        By.XPATH, "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[4]")
