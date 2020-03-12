import self as self
from selenium.common.exceptions import NoSuchElementException
from urllib3.util import timeout


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   #команда для неявного ожидания, значение по умолчанию 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True