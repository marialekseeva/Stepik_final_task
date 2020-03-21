import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

main_page_link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, main_page_link)
        main_page.open()
        main_page.go_to_login_page()
        main_page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, main_page_link)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()
        basket_page.should_contain_empty_text()

# тесты из домашнего задания №1

link = "http://selenium1py.pythonanywhere.com/ru/"


class TestForHomeWorkNumberOne:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(faker.email(), faker.password())
        login_page.should_be_authorized_user()

    @pytest.mark.need_review_custom_scenarios
    def test_find_book(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.find_book()
        main_page.add_to_cart()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.go_to_checkout()
        shipping_stage = BasketPage(browser, browser.current_url)
        shipping_stage.shipping()
        shipping_stage_next = BasketPage(browser, browser.current_url)
        shipping_stage_next.payment()
        last_stage = BasketPage(browser, browser.current_url)
        last_stage.confirm()
        last_stage.success_order()
