from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import math


class ProductPage(BasePage):
    def should_be_add_to_busket_btn(self):
        if "?promo=" in self.browser.current_url:
            assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSKET_BTN), "Adding button is not presented"
        else:
            raise(AssertionError("Wrong URL"))

    def add_to_busket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


