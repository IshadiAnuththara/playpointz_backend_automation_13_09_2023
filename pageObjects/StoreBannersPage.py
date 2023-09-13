from locators.common_locators import CommonLocators
from locators.store_banners_locators import StoreBannersLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class StoreBanners(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StoreBannersLocators
        self.locator = CommonLocators

    def access_store_banners(self):
        self.click_element("hyperlink_store_banners_xpath", self.locators.hyperlink_store_banners_xpath)

    def create_store_banners(self):
        self.click_element("button_create_store_banners_xpath", self.locators.button_create_store_banners_xpath)

    def set_redirect_url(self, url):
        self.send_keys_to_element(url, "input_redirect_url_xpath", self.locators.input_redirect_url_xpath)

    def click_choose_image(self):
        self.perform_click_and_image_upload("button_image_xpath", self.locators.button_image_xpath,
                                            self.locators.image_path)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "textarea_description_xpath", self.locators.textarea_description_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)

    def click_accept_delete(self):
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_edit(self, url):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_redirect_url_xpath", self.locators.input_redirect_url_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(url, "input_redirect_url_xpath", self.locators.input_redirect_url_xpath)

    def select_sequence(self):
        self.click_element("select_sequence_xpath", self.locators.select_sequence_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_value_six_xpath", self.locators.option_value_six_xpath)

    def select_existing_sequence(self):
        self.click_element("select_sequence_xpath", self.locators.select_sequence_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_value_six_xpath", self.locators.option_value_six_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_new_store_banner(self, redirect_url, description):
        self.create_store_banners()
        sleep(SHORT_WAIT)
        self.set_redirect_url(redirect_url)
        sleep(SHORT_WAIT)
        self.click_choose_image()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def delete_store_banners(self):
        self.click_delete()
        sleep(SHORT_WAIT)
        self.click_accept_delete()
        sleep(SHORT_WAIT)

    def create_store_banners_negative_testing(self):
        self.create_store_banners()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_store_banners_only_add_description_negative_testing(self, description):
        self.create_store_banners()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_store_banners_only_add_image_negative_testing(self):
        self.create_store_banners()
        sleep(SHORT_WAIT)
        self.click_choose_image()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_store_banners_only_fill_redirect_url_negative_testing(self, redirect_url):
        self.create_store_banners()
        sleep(SHORT_WAIT)
        self.set_redirect_url(redirect_url)
        sleep(SHORT_WAIT)
        self.click_save()


