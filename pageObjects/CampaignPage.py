from pageObjects.BasePage import BasePage
from locators.campaigns_locators import CampaignsLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class CampaignPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CampaignsLocators()
        self.locator = CommonLocators()

    def click_campaigns(self):
        self.click_element("hyperlink_campaigns_xpath", self.locators.hyperlink_campaigns_xpath)

    def click_create_campaign(self):
        self.click_element("button_create_campaign_xpath", self.locators.button_create_campaign_xpath)

    def set_campaign_name(self, name):
        self.send_keys_to_element(name, "input_campaign_name_xpath", self.locators.input_campaign_name_xpath)

    def set_headline(self, headline):
        self.send_keys_to_element(headline, "input_headline_xpath", self.locators.input_headline_xpath)

    def set_sponsor(self, sponsor):
        self.send_keys_to_element(sponsor, "input_sponsor_xpath", self.locators.input_sponsor_xpath)

    def select_placement(self):
        self.click_element("option_placement_xpath", self.locators.option_placement_xpath)

    def select_campaign_type(self):
        self.click_element("option_campaign_type_xpath", self.locators.option_campaign_type_xpath)

    def click_upload(self):
        self.click_element("button_upload_image_xpath", self.locators.button_upload_image_xpath)

    def choose_new_image(self):
        self.perform_click_and_image_upload("button_choose_image_xpath",
                                            self.locators.button_choose_image_xpath, self.locators.image_path)

    def click_add(self):
        self.click_element("button_add_xpath", self.locators.button_add_xpath)

    def set_website(self, website):
        self.send_keys_to_element(website, "input_website_xpath", self.locators.input_website_xpath)

    def click_schedule(self):
        self.click_element("button_schedule_xpath", self.locators.button_schedule_xpath)

    def schedule_date(self):
        self.click_element("td_start_date_xpath", self.locators.td_start_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("td_end_date_xpath", self.locators.td_end_date_xpath)

    def schedule_time(self):
        self.click_element("option_start_hour_xpath", self.locators.option_start_hour_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_start_minute_xpath", self.locators.option_start_minute_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_start_am_xpath", self.locators.option_start_am_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_end_hour_xpath", self.locators.option_end_hour_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_end_minute_xpath", self.locators.option_end_minute_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_end_pm_xpath", self.locators.option_end_pm_xpath)
        sleep(SHORT_WAIT)

    def click_apply(self):
        self.click_element("button_apply_xpath", self.locators.button_apply_xpath)

    def click_publish(self):
        self.click_element("button_publish_xpath", self.locators.button_publish_xpath)

    def click_edit(self, message):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_campaign_type_text_xpath", self.locators.option_campaign_type_text_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("textarea_primary_text_xpath", self.locators.textarea_primary_text_xpath)
        self.send_keys_to_element(message, "textarea_primary_text_xpath", self.locators.textarea_primary_text_xpath)

    def click_delete(self):
        sleep(MEDIUM_WAIT)
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def search_campaign_name(self, name):
        self.send_keys_to_element(name, "input_search_campaign_xpath", self.locators.input_search_campaign_xpath)

    def search_active_status_all(self):
        self.click_element("option_active_status_all_xpath", self.locators.option_active_status_all_xpath)

    def search_active_status_active(self):
        self.click_element("option_active_status_active_xpath", self.locators.option_active_status_active_xpath)

    def search_active_status_inactive(self):
        self.click_element("option_active_status_inactive_xpath", self.locators.option_active_status_inactive_xpath)

    def search_sponsor_all(self):
        self.click_element("option_sponsor_all_xpath", self.locators.option_sponsor_all_xpath)

    def search_sponsor_bairaha(self):
        self.click_element("option_sponsor_bairaha_xpath", self.locators.option_sponsor_bairaha_xpath)

    def search_sponsor_beverly_hills_polo_club(self):
        self.click_element("option_sponsor_beverly_hills_polo_club_xpath",
                           self.locators.option_sponsor_beverly_hills_polo_club_xpath)

    def search_sponsor_fadna_shape_up_tea(self):
        self.click_element("option_sponsor_fadna_shape_up_tea_xpath",
                           self.locators.option_sponsor_fadna_shape_up_tea_xpath)

    def search_sponsor_stesafe(self):
        self.click_element("option_sponsor_stesafe_xpath", self.locators.option_sponsor_stesafe_xpath)

    def search_sponsor_fadna_tummy_tea(self):
        self.click_element("option_sponsor_fadna_tummy_tea_xpath", self.locators.option_sponsor_fadna_tummy_tea_xpath)

    def search_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_start_date_xpath", self.locators.input_start_date_xpath)

    def search_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_end_date_xpath", self.locators.input_end_date_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_export(self):
        self.click_element("button_export_xpath", self.locators.button_export_xpath)

    def click_advanced_filter(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def upload_image(self):
        self.click_upload()
        sleep(SHORT_WAIT)
        self.choose_new_image()
        sleep(SHORT_WAIT)
        self.click_add()

    def schedule_new_campaign(self):
        self.click_schedule()
        sleep(SHORT_WAIT)
        self.schedule_date()
        sleep(SHORT_WAIT)
        self.schedule_time()
        sleep(SHORT_WAIT)
        self.click_apply()

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def create_new_campaign(self, name, headline, sponsor, website):
        self.click_create_campaign()
        sleep(SHORT_WAIT)
        self.set_campaign_name(name)
        sleep(SHORT_WAIT)
        self.set_headline(headline)
        sleep(SHORT_WAIT)
        self.set_sponsor(sponsor)
        sleep(SHORT_WAIT)
        self.select_placement()
        sleep(SHORT_WAIT)
        self.select_campaign_type()
        sleep(SHORT_WAIT)
        self.upload_image()
        sleep(SHORT_WAIT)
        self.set_website(website)
        sleep(SHORT_WAIT)
        self.schedule_new_campaign()
        sleep(SHORT_WAIT)
        self.click_publish()
        sleep(SHORT_WAIT)

    def search_campaigns(self, campaign_name, start_date, end_date):
        self.search_campaign_name(campaign_name)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_active_status_all()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_active_status_active()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_active_status_inactive()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_all()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_bairaha()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_beverly_hills_polo_club()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_fadna_shape_up_tea()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_stesafe()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_sponsor_fadna_tummy_tea()
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_start_date(start_date)
        sleep(SHORT_WAIT)
        self.search_end_date(end_date)
        self.search_and_refresh()

    def edit_campaigns(self, primary_text):
        self.click_edit(primary_text)
        sleep(SHORT_WAIT)
        self.click_publish()
