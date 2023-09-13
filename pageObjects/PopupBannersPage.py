from selenium.webdriver import Keys
from pageObjects.BasePage import BasePage
from locators.pop_up_banners_locators import PopupBannersLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class PopupBannersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PopupBannersLocators
        self.locator = CommonLocators

    def click_popup_banners(self):
        self.click_element("hyperlink_popup_banners_xpath", self.locators.hyperlink_popup_banners_xpath)

    def create_popup_banners(self):
        self.click_element("button_create_xpath", self.locators.button_create_xpath)

    def click_insert_image(self):
        self.perform_click_and_image_upload("button_image_xpath", self.locators.button_image_xpath,
                                            self.locators.image_path)

    # def set_schedule_start_date(self, start_date):
    #     self.set_date("input_schedule_start_time_xpath", self.locators.input_schedule_start_time_xpath, start_date)
    def set_schedule_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_schedule_start_time_xpath",
                                  self.locators.input_schedule_start_time_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(Keys.ARROW_RIGHT, "input_schedule_start_time_xpath",
                                  self.locators.input_schedule_start_time_xpath)

    def set_schedule_start_time(self, start_time):
        self.send_keys_to_element(start_time, "input_schedule_start_time_xpath",
                                  self.locators.input_schedule_start_time_xpath)
        sleep(SHORT_WAIT)

    def set_schedule_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_schedule_end_time_xpath",
                                  self.locators.input_schedule_end_time_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(Keys.ARROW_RIGHT, "input_schedule_end_time_xpath",
                                  self.locators.input_schedule_end_time_xpath)

    def set_schedule_end_time(self, end_time):
        self.send_keys_to_element(end_time, "input_schedule_end_time_xpath", self.locators.input_schedule_end_time_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_cancel(self):
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_new_popup_banners(self, start_date, start_time, end_date, end_time):
        self.click_insert_image()
        sleep(SHORT_WAIT)
        self.set_schedule_start_date(start_date)
        sleep(SHORT_WAIT)
        self.set_schedule_start_time(start_time)
        sleep(SHORT_WAIT)
        self.set_schedule_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_schedule_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def edit_popup_banners(self, start_date, start_time, end_date, end_time):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_schedule_start_date(start_date)
        sleep(SHORT_WAIT)
        self.set_schedule_start_time(start_time)
        sleep(SHORT_WAIT)
        self.set_schedule_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_schedule_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_without_fill_any_field_negative_testing(self):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_only_add_image_negative_testing(self):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.click_insert_image()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_only_add_schedule_end_time(self, end_date, end_time):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_schedule_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_only_add_schedule_start_time(self, start_date, start_time):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.set_schedule_start_date(start_date)
        sleep(SHORT_WAIT)
        self.set_schedule_start_time(start_time)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_without_set_schedule_end_date(self, start_date, start_time):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.click_insert_image()
        sleep(SHORT_WAIT)
        self.set_schedule_start_date(start_date)
        sleep(SHORT_WAIT)
        self.set_schedule_start_time(start_time)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_popup_banners_without_set_schedule_start_date(self, end_date, end_time):
        self.create_popup_banners()
        sleep(SHORT_WAIT)
        self.click_insert_image()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_schedule_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_save()


