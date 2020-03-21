from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from .locators import BasePageLocators, MainPageLocators
# from .locators import ProductPageLocators
#
#
# class BasePage():
#     def __init__(self, browser, url, timeout=10):
#         self.browser = browser
#         self.url = url
#         self.browser.implicitly_wait(timeout)   #команда для неявного ожидания, значение по умолчанию 10
#
#     def open(self):
#         self.browser.get(self.url)
#
#     def is_element_present(self, how, what):
#         try:
#             self.browser.find_element(how, what)
#         except (NoSuchElementException):
#             return False
#         return True
#
#     def is_not_element_present(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return True
#         return False
#
#     def should_not_be_success_message(self):
#         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#             "Success message is presented, but should not be"
#
#     def is_disappeared(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException). \
#                 until_not(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return False
#         return True
#
#     def should_not_be_success_message_2(self):
#         assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
#             "Success message is presented, but should not be 2 EDITION"
#
#     def go_to_login_page(self):
#         link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
#         link.click()
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
#
#     def go_to_basket(self):
#         box_button = self.browser.find_element(*MainPageLocators.BASKET_LINK)
#         self.browser.implicitly_wait(10)
#         ActionChains(self.browser).move_to_element(box_button).click(box_button)

import math
from typing import Sequence

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   #команда для неявного ожидания, значение по умолчанию 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_text_present(self, how: str, what: str, text: str):
        return text in self.browser.find_element(how, what).text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1,
                          TimeoutException).until_not(
                              EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        self._move_to_page(BasePageLocators.LOGIN_LINK)

    def go_to_basket_page(self):
        self._move_to_page(BasePageLocators.CART_BUTTON)

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def _move_to_page(self, selector: Sequence[str]):
        link = self.browser.find_element(*selector)
        link.click()



