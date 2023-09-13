import time
from locators.common_locators import CommonLocators
from locators.user_management_locators import UserManagementLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class UserManagement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.list_permission = None
        self.locators = UserManagementLocators
        self.locator = CommonLocators

    def click_user_management(self):
        self.click_element("button_users_xpath", self.locators.button_users_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_user_management_xpath", self.locators.hyperlink_user_management_xpath)

    def click_add_member(self):
        self.click_element("button_add_member_xpath", self.locators.button_add_member_xpath)

    def set_name(self, username):
        self.send_keys_to_element(username, "input_username_xpath", self.locators.input_username_xpath)

    def generate_password(self):
        self.click_element("button_generate_password_xpath", self.locators.button_generate_password_xpath)

    def set_email(self, email):
        self.send_keys_to_element(email, "input_email_xpath", self.locators.input_email_xpath)

    def set_first_name(self, first_name):
        self.send_keys_to_element(first_name, "input_first_name_xpath", self.locators.input_first_name_xpath)

    def set_last_name(self, last_name):
        self.send_keys_to_element(last_name, "input_last_name_xpath", self.locators.input_last_name_xpath)

    def set_role(self):
        self.click_element("option_role_xpath", self.locators.option_role_xpath)

    def set_active_status(self):
        self.click_element("option_status_active_xpath", self.locators.option_status_active_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def edit_member(self):
        self.click_element("button_edit_2_xpath", self.locators.button_edit_2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_status_inactive_xpath", self.locators.option_status_inactive_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def set_search_user(self, user):
        self.send_keys_to_element(user, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_user_role(self):
        self.click_element("button_users_xpath", self.locators.button_users_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_user_role_xpath", self.locators.hyperlink_user_role_xpath)

    def click_add_user_role(self):
        self.click_element("button_add_role_xpath", self.locators.button_add_role_xpath)

    def add_user_role(self, role_name):
        self.send_keys_to_element(role_name, "input_role_name_xpath", self.locators.input_role_name_xpath)
        sleep(SHORT_WAIT)

    def add_permission(self, permission):
        self.send_keys_to_element(permission, "input_permission_xpath", self.locators.input_permission_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_permission_xpath", self.locators.span_permission_xpath)

    def click_edit_user_role(self):
        self.click_element("button_edit_user_role_xpath", self.locators.button_edit_user_role_xpath)

    def edit_permission(self, permission):
        self.click_element("input_permission_xpath", self.locators.input_permission_xpath)
        time.sleep(5)
        if permission == 'User Reportings':
            self.list_permission = self.find_element("span_user_reporting_xpath",
                                                     self.locators.span_user_reporting_xpath)
        self.driver.execute_script("arguments[0].click();", self.list_permission)

    def remove_permission(self):
        self.click_element("span_remove_permission_xpath", self.locators.span_remove_permission_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_user(self, name, email, first_name, last_name):
        self.click_add_member()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.generate_password()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_first_name(first_name)
        sleep(SHORT_WAIT)
        self.set_last_name(last_name)
        sleep(SHORT_WAIT)
        self.set_role()
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def search_user(self, name):
        self.set_search_user(name)
        sleep(SHORT_WAIT)
        self.click_search()

    def add_new_user_role(self, user_role, add_permission):
        self.click_add_user_role()
        sleep(SHORT_WAIT)
        self.add_user_role(user_role)
        sleep(SHORT_WAIT)
        self.add_permission(add_permission)
        time.sleep(5)
        self.click_save()
        sleep(SHORT_WAIT)

    def edit_user_permission(self, edit_permission):
        self.click_edit_user_role()
        sleep(SHORT_WAIT)
        self.edit_permission(edit_permission)
        sleep(SHORT_WAIT)
        self.click_save()

    def remove_permissions(self):
        self.click_edit_user_role()
        sleep(SHORT_WAIT)
        self.remove_permission()
        sleep(SHORT_WAIT)
        self.click_save()
