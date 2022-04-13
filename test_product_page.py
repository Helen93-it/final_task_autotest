import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param(7, marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket()

@pytest.mark.xfail(reason="Bug is fixing now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Bug is fixing now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_disappeared()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_message_of_empty_baste()
    basket_page.should_basket_has_not_items()

@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse = True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, "vfcbrvjq1820")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_add_product_in_basket()
        page.solve_quiz_and_get_code()
        page.should_be_add_to_basket()