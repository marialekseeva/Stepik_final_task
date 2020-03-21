# from .locators import ProductPageLocators
# from .base_page import BasePage
# from selenium.common.exceptions import NoAlertPresentException
# import math
#
#
# class ProductPage(BasePage):
#     def should_be_add_to_busket_btn(self):
#         if "?promo=" in self.browser.current_url:
#             assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Adding button is not presented"
#         else:
#             raise(AssertionError("Wrong URL"))
#
#     def add_to_cart(self, is_promo=False):
#         self.browser.find_element(
#             *ProductPageLocators.BUTTON_ADD_TO_CART).click()
#
#         if is_promo:
#             self.solve_quiz_and_get_code()
#
#     def solve_quiz_and_get_code(self):
#         alert = self.browser.switch_to.alert
#         x = alert.text.split(" ")[2]
#         answer = str(math.log(abs((12 * math.sin(float(x))))))
#         alert.send_keys(answer)
#         alert.accept()
#         try:
#             alert = self.browser.switch_to.alert
#             alert_text = alert.text
#             print(f"Your code: {alert_text}")
#             alert.accept()
#         except NoAlertPresentException:
#             print("No second alert presented")


from .base_page import BasePage
from .locators import ProductPageLocators, SellRegistration


class ProductPage(BasePage):
    def add_to_basket(self, is_promo=False):
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_CART).click()

        if is_promo:
            self.solve_quiz_and_get_code()

    def should_be_present_in_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_CART
        ), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def should_check_overall_cost(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS
                                       ), "No alert with cart status"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"

    def should_not_see_success_message_after_adding_to_cart(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDING_SUCCESS
        ), "Success element is visible for an user"

    def should_not_see_success_message_upon_opening_product_page(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDING_SUCCESS
        ), "Success element is visible for an user"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_SUCCESS), "Success message has not disappeared"

    # для домашнего задания №1


