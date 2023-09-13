from pageObjects.BasePage import BasePage
from locators.login_locators import LoginPageLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators()
        self.locators = CommonLocators()

    def set_username(self, username):
        self.send_keys_to_element(username, "textbox_username_id", self.locator.textbox_username_id)

    def set_password(self, password):
        self.send_keys_to_element(password, "textbox_password_id", self.locator.textbox_password_id)

    def set_invalid_username(self, username):
        self.send_keys_to_element(username, "textbox_username_id", self.locator.textbox_username_id)

    def set_invalid_password(self, password):
        self.send_keys_to_element(password, "textbox_password_id", self.locator.textbox_password_id)

    def click_login(self):
        self.click_element("button_login_xpath", self.locator.button_login_xpath)

    def clear_username(self):
        self.clear_fields("textbox_username_id", self.locator.textbox_username_id)

    def clear_password(self):
        self.clear_fields("textbox_password_id", self.locator.textbox_password_id)

    def login_to_application(self, email_address_text, password_text):
        self.set_username(email_address_text)
        self.set_password(password_text)
        return self.click_login()

    def login_with_valid_username_and_invalid_password(self, email_address_text, password_text):
        self.set_username(email_address_text)
        self.set_invalid_password(password_text)
        return self.click_login()

    def login_with_invalid_username_and_valid_password(self, email_address_text, password_text):
        self.set_invalid_username(email_address_text)
        self.set_password(password_text)
        return self.click_login()

    def login_with_invalid_username_and_invalid_password(self, email_address_text, password_text):
        self.set_invalid_username(email_address_text)
        self.set_invalid_password(password_text)
        return self.click_login()

    def login_without_enter_username_password(self):
        self.clear_username()
        self.clear_password()
        return self.click_login()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def click_logout(self):
        self.click_element("div_super_admin_xpath", self.locator.div_super_admin_xpath)
        sleep(5)
        self.click_element("button_logout_xpath", self.locator.hyperlink_logout_xpath)
        sleep(3)
        self.click_element("button_confirm_xpath", self.locator.button_confirm_xpath)
