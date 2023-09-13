from pageObjects.BasePage import BasePage
from locators.announcement_locators import AnnouncementPageLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class AnnouncementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AnnouncementPageLocators()
        self.locator = CommonLocators()

    def click_announcement(self):
        self.click_element("hyperlink_announcement_xpath", self.locators.hyperlink_announcement_xpath)

    def click_new_announcement(self):
        self.click_element("button_new_announcement_xpath", self.locators.button_new_announcement_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_announcement_name_xpath", self.locators.input_announcement_name_xpath)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "textarea_description_xpath", self.locators.textarea_description_xpath)

    def set_type(self):
        self.click_element("option_type_image_xpath", self.locators.option_type_image_xpath)

    def select_image_announcement(self):
        self.perform_click_and_image_upload("button_choose_image_xpath",
                                            self.locators.button_choose_image_xpath, self.locators.image_path)

    def set_redirect(self):
        self.click_element("option_redirect_store_xpath", self.locators.option_redirect_store_xpath)

    def set_schedule(self):
        self.click_element("button_schedule_xpath", self.locators.button_schedule_xpath)

    def set_start_date(self):
        self.click_element("td_start_date_xpath", self.locators.td_start_date_xpath)

    def set_end_date(self):
        self.click_element("td_end_date_xpath", self.locators.td_end_date_xpath)

    def set_start_time_hour(self):
        self.click_element("option_start_time_hour_xpath", self.locators.option_start_time_hour_xpath)

    def set_start_time_minute(self):
        self.click_element("option_start_time_minute_xpath", self.locators.option_start_time_minute_xpath)

    def set_start_am(self):
        self.click_element("option_start_am_xpath", self.locators.option_start_am_xpath)

    def set_end_time_hour(self):
        self.click_element("option_end_time_hour_xpath", self.locators.option_end_time_hour_xpath)

    def set_end_time_minute(self):
        self.click_element("option_end_time_minute_xpath", self.locators.option_end_time_minute_xpath)

    def set_end_pm(self):
        self.click_element("option_end_pm_xpath", self.locators.option_end_pm_xpath)

    def click_apply(self):
        self.click_element("button_apply_xpath", self.locators.button_apply_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_page(self):
        self.click_element("hyperlink_page_xpath", self.locators.hyperlink_page_xpath)

    def click_edit(self):
        self.click_element("hyperlink_page22_xpath", self.locators.hyperlink_page22_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("textarea_description_xpath", self.locators.textarea_description_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def search_announcement(self, announcement):
        self.send_keys_to_element(announcement, "input_search_announcement_xpath",
                                  self.locators.input_search_announcement_xpath)

    def search_status_all(self):
        self.click_element("option_active_status_all_xpath", self.locators.option_active_status_all_xpath)

    def search_status_active(self):
        self.click_element("option_active_status_active_xpath", self.locators.option_active_status_active_xpath)

    def search_status_inactive(self):
        self.click_element("option_active_status_inactive_xpath", self.locators.option_active_status_inactive_xpath)

    def search_type_all(self):
        self.click_element("option_type_all_xpath", self.locators.option_type_all_xpath)

    def search_type_text(self):
        self.click_element("option_type_text_xpath", self.locators.option_type_text_xpath)

    def search_type_image(self):
        self.click_element("option_type_search_image_xpath", self.locators.option_type_search_image_xpath)

    def search_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_start_date_xpath", self.locators.input_start_date_xpath)

    def search_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_end_date_xpath", self.locators.input_end_date_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_advanced_filter(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_schedule(self):
        self.set_schedule()
        sleep(SHORT_WAIT)
        self.set_start_date()
        sleep(SHORT_WAIT)
        self.set_end_date()
        sleep(SHORT_WAIT)
        self.set_start_time_hour()
        sleep(SHORT_WAIT)
        self.set_start_time_minute()
        sleep(SHORT_WAIT)
        self.set_start_am()
        sleep(SHORT_WAIT)
        self.set_end_time_hour()
        sleep(SHORT_WAIT)
        self.set_end_time_minute()
        sleep(SHORT_WAIT)
        self.set_end_pm()
        sleep(SHORT_WAIT)
        self.click_apply()
        sleep(SHORT_WAIT)

    def create_new_announcement(self, name, desc):
        self.click_new_announcement()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.set_redirect()
        sleep(SHORT_WAIT)
        self.set_type()
        sleep(SHORT_WAIT)
        self.select_image_announcement()
        sleep(SHORT_WAIT)
        self.create_schedule()
        sleep(SHORT_WAIT)
        self.click_save()

    def search_and_refresh(self):
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def search_announcements(self, announcement, start_date, end_date):
        self.search_announcement(announcement)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_status_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_status_active()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_status_inactive()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_type_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_type_text()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_type_image()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_start_date(start_date)
        sleep(SHORT_WAIT)
        self.search_end_date(end_date)
        sleep(SHORT_WAIT)
        self.search_and_refresh()

    def edit_announcements(self, desc):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_description(desc)
        self.click_save()

    def delete_announcement(self, name):
        self.search_announcement(name)
        sleep(SHORT_WAIT)
        self.click_search()
        self.click_delete()
