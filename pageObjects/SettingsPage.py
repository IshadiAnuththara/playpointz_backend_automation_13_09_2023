from locators.common_locators import CommonLocators
from locators.settings_locators import SettingsLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class Settings(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SettingsLocators()
        self.locator = CommonLocators()

    def click_settings(self):
        self.click_element("button_settings_xpath", self.locators.button_settings_xpath)

    def click_general(self):
        self.click_element("hyperlink_general_xpath", self.locators.hyperlink_general_xpath)

    def click_email_domain(self):
        self.click_element("hyperlink_email_domain_xpath", self.locators.hyperlink_email_domain_xpath)

    def click_edit_quiz_easy_level(self):
        self.find_element("tablerow_row2_xpath", self.locators.tablerow_row2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_edit2_xpath", self.locators.button_edit2_xpath)

    def click_edit_quiz_hard_level(self):
        self.find_element("tablerow_row1_xpath", self.locators.tablerow_row1_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_edit1_xpath", self.locators.button_edit1_xpath)

    def edit_quiz_lower_bound(self, lower_bound):
        self.clear_fields("input_quiz_lower_bound_xpath", self.locators.input_quiz_lower_bound_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(lower_bound, "input_quiz_lower_bound_xpath",
                                  self.locators.input_quiz_lower_bound_xpath)

    def edit_quiz_upper_bound(self, upper_bound):
        self.clear_fields("input_quizUpperBound_xpath", self.locators.input_quiz_upper_bound_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(upper_bound, "input_quiz_upper_bound_xpath",
                                  self.locators.input_quiz_upper_bound_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_create_email(self):
        self.click_element("button_create_email_xpath", self.locators.button_create_email_xpath)

    def set_allowed_email(self, email):
        self.send_keys_to_element(email, "input_allowed_email_xpath", self.locators.input_allowed_email_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def edit_email(self, email):
        self.clear_fields("input_allowed_email_xpath", self.locators.input_allowed_email_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(email, "input_allowed_email_xpath", self.locators.input_allowed_email_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def search(self, email):
        self.send_keys_to_element(email, "input_search_xpath", self.locators.input_search_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def set_quiz_limit(self, limit):
        settings = self.find_element("heading_settings_xpath", self.locators.heading_settings_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", settings)
        sleep(SHORT_WAIT)
        self.clear_fields("input_quizLimit_xpath", self.locators.input_quiz_limit_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(limit, "input_quiz_limit_xpath", self.locators.input_quiz_limit_xpath)

    def set_daily_pointz_easy(self, daily_pointz):
        self.clear_fields("input_daily_pointz_easy_xpath", self.locators.input_daily_pointz_easy_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(daily_pointz, "input_daily_pointz_easy_xpath",
                                  self.locators.input_daily_pointz_easy_xpath)

    def set_minus_pointz_easy(self, minus_pointz):
        self.clear_fields("input_minus_pointz_easy_xpath", self.locators.input_minus_pointz_easy_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(minus_pointz, "input_minus_pointz_easy_xpath",
                                  self.locators.input_minus_pointz_easy_xpath)

    def set_daily_pointz_hard(self, daily_pointz):
        self.clear_fields("input_daily_pointz_hard_xpath", self.locators.input_daily_pointz_hard_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(daily_pointz, "input_daily_pointz_hard_xpath",
                                  self.locators.input_daily_pointz_hard_xpath)

    def set_minus_pointz_hard(self, minus_pointz):
        self.clear_fields("input_minus_pointz_hard_xpath", self.locators.input_minus_pointz_hard_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(minus_pointz, "input_minus_pointz_hard_xpath",
                                  self.locators.input_minus_pointz_hard_xpath)

    def set_join_pointz(self, join_pointz):
        self.clear_fields("input_join_pointz_xpath", self.locators.input_join_pointz_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(join_pointz, "input_join_pointz_xpath",
                                  self.locators.input_join_pointz_xpath)

    def set_referral_pointz(self, referral_pointz):
        self.clear_fields("input_referral_pointz_xpath", self.locators.input_referral_pointz_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(referral_pointz, "input_referral_pointz_xpath",
                                  self.locators.input_referral_pointz_xpath)

    def set_recent_winner_count(self, winner_count):
        self.clear_fields("input_recent_winner_count_xpath", self.locators.input_recent_winner_count_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(winner_count, "input_recent_winner_count_xpath",
                                  self.locators.input_recent_winner_count_xpath)

    def set_schedule_expire(self, schedule_expire):
        self.clear_fields("input_schedule_expire_xpath", self.locators.input_schedule_expire_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(schedule_expire, "input_schedule_expire_xpath",
                                  self.locators.input_schedule_expire_xpath)

    def setLogo(self, image_path):
        self.send_keys_to_element(image_path, "input_logo_xpath", self.locators.input_logo_xpath)

    def preview_logo(self):
        self.click_element("span_preview_logo_xpath", self.locators.span_preview_logo_xpath)

    def close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def settings_save(self):
        appLogo = self.find_element("heading_app_logo_xpath", self.locators.heading_app_logo_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", appLogo)
        sleep(SHORT_WAIT)
        self.click_element("button_settings_save_xpath", self.locators.button_settings_save_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_email_domain(self, email):
        self.click_create_email()
        sleep(SHORT_WAIT)
        self.set_allowed_email(email)
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_email_domain(self, email):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.edit_email(email)
        sleep(SHORT_WAIT)
        self.click_save()

    def search_email_domain(self, name_1, name_2):
        self.search(name_1)
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)
        self.search(name_2)
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

