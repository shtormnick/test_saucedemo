from selenium.webdriver.common.by import By

class BasePageLocators():
    MENU = (By.ID, "react-burger-menu-btn")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    FILTER = (By.CLASS_NAME, "product_sort_container")
    HEADER_TEXT_ON_PRODUCT_PAGE = (By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login-box")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_INPUT = (By.ID, "user-name")
    LOGIN_BUTTON = (By.ID, "login-button")

class CartPageLocators():
    HEADER_TEXT_ON_CART_PAGE = (By.CLASS_NAME, "title")
    CART_LIST_ON_CART_PAGE = (By.CLASS_NAME, "cart_list")
    CART_ITEM_ON_CART_PAGE = (By.CLASS_NAME, "cart_item")
    