from locators.common_locators import CommonLocators
from locators.player_support_locators import PlayerSupportLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class PlayerSupportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PlayerSupportLocators
        self.locator = CommonLocators

    def click_player_support(self):
        self.click_element("hyperlink_player_support_xpath", self.locators.hyperlink_player_support_xpath)

    def search_by_name(self, name):
        self.send_keys_to_element(name, "input_search_by_name_xpath", self.locators.input_search_by_name_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_advanced_filter(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def set_action_all(self):
        self.click_element("option_access_all_xpath", self.locators.option_access_all_xpath)

    def set_action_action_taken(self):
        self.click_element("option_access_action_taken_xpath", self.locators.option_access_action_taken_xpath)

    def set_action_action_required(self):
        self.click_element("option_access_action_required_xpath", self.locators.option_access_action_required_xpath)

    def set_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_start_date_xpath", self.locators.input_start_date_xpath)

    def set_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_end_date_xpath", self.locators.input_end_date_xpath)

    def click_view(self):
        self.click_element("hyperlink_page_11_xpath", self.locators.hyperlink_page_11_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_view_xpath", self.locators.button_view_xpath)

    def edit_solution_resolved(self):
        resolved = self.find_element("select_status_xpath", self.locators.select_status_xpath)
        if resolved == "Resolved":
            self.click_element("option_not_resolved_xpath", self.locators.option_not_resolved_xpath)
        else:
            self.click_element("option_resolved_xpath", self.locators.option_resolved_xpath)

    def click_take_action(self):
        self.click_element("button_take_action_xpath", self.locators.button_take_action_xpath)

    def click_view_profile(self):
        self.click_element("hyperlink_view_profile_xpath", self.locators.hyperlink_view_profile_xpath)

    def set_subject(self, subject):
        self.clear_fields("input_subject_xpath", self.locators.input_subject_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(subject, "input_subject_xpath", self.locators.input_subject_xpath)

    def set_comment(self, comment):
        self.clear_fields("paragraph_comment_xpath", self.locators.paragraph_comment_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(comment, "paragraph_comment_xpath", self.locators.paragraph_comment_xpath)

    def click_reset(self):
        self.click_element("button_reset_xpath", self.locators.button_reset_xpath)

    def click_send(self):
        self.click_element("button_send_xpath", self.locators.button_send_xpath)

    def select_image(self):
        self.perform_click_and_image_upload("button_choose_image_xpath", self.locators.button_choose_image_xpath,
                                            self.locators.image_path)

    def click_mark_as_resolved(self):
        self.click_element("button_mark_as_resolved_xpath", self.locators.button_mark_as_resolved_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_xpath", self.locators.button_accept_xpath)

    def select_type(self):
        self.click_element("select_type_xpath", self.locators.select_type_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_image_xpath", self.locators.option_image_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def search_and_refresh(self):
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def search_player_support(self, name, start_date, end_date):
        self.search_by_name(name)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.set_action_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.set_action_action_taken()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.set_action_action_required()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.set_start_date(start_date)
        sleep(SHORT_WAIT)
        self.set_end_date(end_date)
        sleep(SHORT_WAIT)
        self.search_and_refresh()

    def reply_support_message(self, subject, comment):
        self.click_view()
        sleep(SHORT_WAIT)
        self.set_subject(subject)
        sleep(SHORT_WAIT)
        self.set_comment(comment)
        sleep(SHORT_WAIT)
        self.select_type()
        sleep(SHORT_WAIT)
        self.select_image()
        sleep(SHORT_WAIT)
        self.click_reset()
        sleep(SHORT_WAIT)
        self.set_subject(subject)
        sleep(SHORT_WAIT)
        self.set_comment(comment)
        sleep(SHORT_WAIT)
        self.select_type()
        sleep(SHORT_WAIT)
        self.select_image()
        sleep(SHORT_WAIT)
        self.click_send()
        sleep(SHORT_WAIT)
