# from selenium.webdriver.common.by import By
#
#
# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-default")
#
#
# class LoginPageLocators():
#     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#     REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
#
#
# class ProductPageLocators():
#     BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
#     ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
#
#
# class BasePageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
#
#
# class BasketPageLocators:
#     CART_ELEMENT = (By.CLASS_NAME, "basket-items")
#     BASKET_EMPTY_TEXT_ELEMENT = (By.CSS_SELECTOR, "div#content_inner > p")

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inv")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_BUTTON = (By.ID, "login_link")
    EMAIL_INPUT = (By.NAME, "registration-email")
    PASSWORD_INPUT = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR,
                           "#messages>div:first-child .alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators:
    CART_ELEMENT = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_TEXT_ELEMENT = (By.CSS_SELECTOR, "div#content_inner > p")


class SellRegistration:
    SEARCH = (By.ID, 'id_q')
    BUTTON_SEARCH = (By.CSS_SELECTOR, "input.btn")
    IMG = (By.CSS_SELECTOR, "img.thumbnail")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
    GO_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[2]/a[1]')
    LINK_TO_BOOK = (By.LINK_TEXT, "Applied cryptography")
    CONFIRM_BTN = (By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary.btn-block")
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    ADDRESS = (By.NAME, "line1")
    CITY = (By.NAME, "line4")
    POSTCODE = (By.NAME, "postcode")
    COUNTRY = (By.NAME, "country")
    CONTINUE = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    CONTINUE_TO_PREVIEW = (By.ID, "view_preview")
    PLACE_ORDER = (By.ID, "place-order")
    PRINT_PAGE = (By.CSS_SELECTOR, "a.btn.btn-primary.btn-block.btn-lg")
