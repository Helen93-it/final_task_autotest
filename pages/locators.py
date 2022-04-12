from selenium.webdriver.common.by import By

class MainPaiglocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class AddProductToBasket():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default:nth-child(1)")


