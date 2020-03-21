# from .base_page import BasePage
# from .locators import BasketPageLocators


# class BasketPage(BasePage):
#     def check_basket(self):
#         assert self.is_element_present(*BasketPageLocators.EMPTY_BOX), "Basket is empty"

from .base_page import BasePage
from .locators import BasketPageLocators, SellRegistration


class BasketPage(BasePage):
    def should_be_empty(self):
        self.is_not_element_present(*BasketPageLocators.CART_ELEMENT)

    def should_contain_empty_text(self):
        empty_text = "Your basket is empty"
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT_ELEMENT
        ), "Cart empty warning element is not present on the page"
        assert self.is_text_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT_ELEMENT, empty_text
        ), f"The text '{empty_text}' is not present in the empty basket warning element"

    # для домашнего задания №1
    def go_to_checkout(self):
        assert self.is_element_present(*SellRegistration.LINK_TO_BOOK), "No link to book"
        assert self.is_element_present(*SellRegistration.CONFIRM_BTN), "No checkout link"
        self.browser.find_element(*SellRegistration.CONFIRM_BTN).click()

    def shipping(self):
        self.browser.find_element(*SellRegistration.FIRST_NAME).send_keys("Mar")
        self.browser.find_element(*SellRegistration.LAST_NAME).send_keys("Al")
        self.browser.find_element(*SellRegistration.ADDRESS).send_keys("ets")
        self.browser.find_element(*SellRegistration.CITY).send_keys("ets")
        self.browser.find_element(*SellRegistration.POSTCODE).send_keys("620034")
        self.browser.find_element(*SellRegistration.COUNTRY).send_keys("Rus")
        self.browser.find_element(*SellRegistration.CONTINUE).click()

    def payment(self):
        self.browser.find_element(*SellRegistration.CONTINUE_TO_PREVIEW).click()

    def confirm(self):
        self.browser.find_element(*SellRegistration.PLACE_ORDER).click()

    def success_order(self):
        assert self.is_element_present(*SellRegistration.PRINT_PAGE), "Order FAILD HAHA"
