# from .base_page import BasePage
# from .locators import MainPageLocators, LoginPageLocators
#
#
# class LoginPage(BasePage):
#     def register_new_user(self, email: str, password: str):
#         self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(
#             email)
#         self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
#             password)
#         self.browser.find_element(
#             *LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
#         self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
#
#     def should_be_login_page(self):
#         self.should_be_login_url()
#         self.should_be_login_form()
#         self.should_be_register_form()
#
#     def should_be_login_url(self):
#         if "login" in self.browser.current_url:
#             assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
#
#     def should_be_login_form(self):
#         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login option"
#
#     def should_be_register_form(self):
#         assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is np registration option"

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(
            email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            password)
        self.browser.find_element(
            *LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"No login substring in the {current_url}"

    def should_be_login_form(self):
        # есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), f"Login form is not present on the {self.browser.current_url}"

    def should_be_register_form(self):
        # есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), f"Register form is not present on the {self.browser.current_url} page"
