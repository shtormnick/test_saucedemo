from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """
    LoginPage class describe tests which connected with functional and visual elements on current page
    """

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_password_imput()
        self.should_be_login_input()
        self.should_be_login_button()

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is absent on Login page"

    def should_be_password_imput(self):
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_INPUT
        ), "Password imput is absent on Login page"

    def should_be_login_imput(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_INPUT
        ), "Login input imput is absent on Login page"

    def should_be_login_button(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BUTTON), "Button is not present at Login page"

    def register_new_user(self, name, password):
        self.browser.find_element(
            *LoginPageLocators.LOGIN_INPUT).send_keys(name)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
