from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPaiglocators
from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPaiglocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPaiglocators.LOGIN_LINK), "Login link is not presented"