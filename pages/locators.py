from selenium.webdriver.common.by import By

class BasePageLocators():
    MENU_ON_PRODUCT_PAGE = (By.ID, "react-burger-menu-btn")
    CART_LINK_ON_PRODUCT_PAGE = (By.CLASS_NAME, "shopping_cart_link")
    FILTER_ON_PRODUCT_PAGE = (By.CLASS_NAME, "product_sort_container")
    HEADER_ON_PRODUCT_PAGE = (By.CLASS_NAME, "header_secondary_container")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login-box")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_INPUT = (By.ID, "user-name")
    LOGIN_BUTTON = (By.ID, "login-button")
    