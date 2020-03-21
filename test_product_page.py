# import time
#
# import pytest
#
# from Stepik_final_task.pages.basket_page import BasketPage
# from Stepik_final_task.pages.login_page import LoginPage
# from Stepik_final_task.pages.product_page import ProductPage


# @pytest.mark.need_review
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
#                                   pytest.param("bugged_link", marks=pytest.mark.xfail)])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_busket_btn()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     time.sleep(1)


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser,
#                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.should_be_add_to_busket_btn()
#     page.add_to_busket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#     time.sleep(1)
#
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser,
#                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.should_be_add_to_busket_btn()
#     page.should_not_be_success_message()
#     time.sleep(1)
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser,
#                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.should_be_add_to_busket_btn()
#     page.add_to_busket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message_2()
#     time.sleep(1)


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page.go_to_login_page()
#     time.sleep(1)


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.check_basket()


import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

offer_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9", ]

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(faker.email(), faker.password())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_see_success_message_upon_opening_product_page()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link", links)
    def test_user_can_add_product_to_basket(self, browser, link: str):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket(True)
        product_page.should_be_present_in_cart()
        product_page.should_check_overall_cost()


@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link: str):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


@pytest.mark.skip
@pytest.mark.parametrize("link", offer_links)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link: str):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_can_add_non_promo_product_to_cart(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_see_success_message_upon_opening_product_page()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_contain_empty_text()
