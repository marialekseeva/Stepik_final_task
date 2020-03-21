from .base_page import BasePage
from .locators import SellRegistration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # для домашнего задания №1
    def find_book(self):
        self.browser.find_element(*SellRegistration.SEARCH).send_keys("Applied cryptography")
        self.browser.find_element(*SellRegistration.BUTTON_SEARCH).click()

    def add_to_cart(self):
        assert self.is_element_present(
            *SellRegistration.IMG), "Book not found"
        self.browser.find_element(*SellRegistration.ADD_TO_BASKET).click()
        self.browser.find_element(*SellRegistration.GO_TO_BASKET).click()

