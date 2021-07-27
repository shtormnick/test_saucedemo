from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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

    def should_be_login_button():
