from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPaiglocators
import time # в начале файла


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "This page isn't login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "The login form not exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM), "The register form not exist"

    def register_new_user(self, email, password):
        link = self.browser.find_element(*MainPaiglocators.LOGIN_LINK)
        link.click()

        self.browser.find_element(*LoginPageLocators.EMAIL_LINK_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
        self.browser.implicitly_wait(5)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)

        button_register.click()
