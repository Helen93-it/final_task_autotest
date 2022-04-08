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