import time

from locators.common_locators import CommonLocators
from locators.push_notifications_locators import PushNotificationsLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class PushNotificationsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PushNotificationsLocators
        self.locator = CommonLocators

    def click_push_notifications(self):
        self.click_element("hyperlink_push_notifications_xpath", self.locators.hyperlink_push_notifications_xpath)

    def click_create_notifications(self):
        self.click_element("button_create_notifications_xpath", self.locators.button_create_notifications_xpath)

    def set_title(self, title):
        self.send_keys_to_element(title, "input_title_xpath", self.locators.input_title_xpath)

    def set_message(self, message):
        self.send_keys_to_element(message, "textarea_message_xpath", self.locators.textarea_message_xpath)

    def set_date_time(self, date):
        self.set_date(date, "input_date_time_xpath", self.locators.input_date_time_xpath)

    def set_time(self, schedule_time):
        self.send_keys_to_element(schedule_time, "input_date_time_xpath", self.locators.input_date_time_xpath)

    def click_send(self):
        self.click_element("button_send_xpath", self.locators.button_send_xpath)

    def click_edit_notification(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def edit_message(self, message):
        self.clear_fields("textarea_message_xpath", self.locators.textarea_message_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(message, "textarea_message_xpath", self.locators.textarea_message_xpath)

    def delete_notification(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_cancel(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def search_title(self, title):
        self.send_keys_to_element(title, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_resend(self):
        self.click_element("button_resend_xpath", self.locators.button_resend_xpath)
        time.sleep(SHORT_WAIT)
        self.click_element("button_accept_resend_xpath", self.locators.button_accept_resend_xpath)

    def create_new_push_notification(self, title, message, date, time):
        self.click_create_notifications()
        sleep(SHORT_WAIT)
        self.set_title(title)
        sleep(SHORT_WAIT)
        self.set_message(message)
        sleep(SHORT_WAIT)
        self.set_date_time(date)
        sleep(SHORT_WAIT)
        self.set_time(time)
        sleep(SHORT_WAIT)
        self.click_send()

    def edit_push_notifications(self, message, date, time):
        self.click_edit_notification()
        sleep(SHORT_WAIT)
        self.edit_message(message)
        sleep(SHORT_WAIT)
        self.set_date_time(date)
        sleep(SHORT_WAIT)
        self.set_time(time)
        sleep(SHORT_WAIT)
        self.click_send()
        sleep(SHORT_WAIT)

    def search_push_notifications(self, title):
        self.search_title(title)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)
