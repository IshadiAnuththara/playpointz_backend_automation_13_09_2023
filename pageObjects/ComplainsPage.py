from pageObjects.BasePage import BasePage
from locators.complains_locators import ComplainsLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class Complains(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ComplainsLocators()
        self.locator = CommonLocators()

    def click_complains(self):
        self.click_element("hyperlink_complains_xpath", self.locators.hyperlink_complains_xpath)

    def view_profile(self):
        self.click_element("hyperlink_view_profile_xpath", self.locators.hyperlink_view_profile_xpath)
        sleep(SHORT_WAIT)
        self.quit()

    def view_complain(self):
        self.click_element("button_complain_xpath", self.locators.button_complain_xpath)

    def take_action_ban_user(self):
        self.click_element("option_ban_user_xpath", self.locators.option_ban_user_xpath)

    def take_action_delete_post(self):
        self.click_element("option_delete_post_xpath", self.locators.option_delete_post_xpath)

    def take_action_ignore(self):
        self.click_element("option_ignore_xpath", self.locators.option_ignore_xpath)

    def click_cancel(self):
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)

    def click_delete_cancel(self):
        self.click_element("button_delete_cancel_xpath", self.locators.button_delete_cancel_xpath)

    def search_by_reporter(self, reporter):
        self.send_keys_to_element(reporter, "input_search_reporter_xpath", self.locators.input_search_reporter_xpath)

    def search_by_status_all(self):
        self.click_element("option_status_all_xpath", self.locators.option_status_all_xpath)

    def search_by_status_not_resolved(self):
        self.click_element("option_status_not_resolved_xpath", self.locators.option_status_not_resolved_xpath)

    def search_by_status_resolved(self):
        self.click_element("option_status_resolved_xpath", self.locators.option_status_resolved_xpath)

    def search_by_date_from(self, date_from):
        self.send_keys_to_element(date_from, "input_date_from_xpath", self.locators.input_date_from_xpath)

    def search_by_date_to(self, date_to):
        self.send_keys_to_element(date_to, "input_date_to_xpath", self.locators.input_date_to_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_ignore(self):
        self.click_element("button_ignore_xpath", self.locators.button_ignore_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_ignore_xpath", self.locators.button_accept_ignore_xpath)

    def click_advanced_filter(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def search_complains(self, reporter, date_from, date_to):
        self.search_by_reporter(reporter)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_all()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_not_resolved()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_resolved()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_date_from(date_from)
        sleep(SHORT_WAIT)
        self.search_by_date_to(date_to)
        self.search_and_refresh()

    def take_action(self):
        self.view_complain()
        sleep(SHORT_WAIT)
        self.take_action_ban_user()
        sleep(SHORT_WAIT)
        self.click_cancel()
        sleep(SHORT_WAIT)
        self.view_complain()
        sleep(SHORT_WAIT)
        self.take_action_delete_post()
        sleep(SHORT_WAIT)
        self.click_cancel()
        sleep(SHORT_WAIT)
        self.view_complain()
        sleep(SHORT_WAIT)
        self.take_action_ignore()
        sleep(SHORT_WAIT)
        self.click_cancel()
