import time
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from pageObjects.BasePage import BasePage
from locators.player_management_locators import PlayerManagementLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class PlayerManagementPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PlayerManagementLocators
        self.locator = CommonLocators

    def click_player_management(self):
        self.click_element("hyperlink_player_management_xpath", self.locators.hyperlink_player_management_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def search_by_user_name(self, username):
        self.send_keys_to_element(username, "input_search_username_xpath", self.locators.input_search_username_xpath)

    def search_pointz_from(self, pointz_from):
        self.send_keys_to_element(pointz_from, "input_search_point_from_xpath",
                                  self.locators.input_search_point_from_xpath)

    def search_pointz_to(self, pointz_to):
        self.send_keys_to_element(pointz_to, "input_search_point_to_xpath", self.locators.input_search_point_to_xpath)

    def search_by_date_from(self, date_from):
        self.send_keys_to_element(date_from, "input_search_reg_date_from_xpath",
                                  self.locators.input_search_reg_date_from_xpath)

    def search_by_date_to(self, date_to):
        self.send_keys_to_element(date_to, "input_search_reg_date_to_xpath",
                                  self.locators.input_search_reg_date_to_xpath)

    def search_by_pointz_sorting_default(self):
        self.click_element("option_pointz_default", self.locators.option_pointz_default)

    def search_by_pointz_sorting_ascending(self):
        self.click_element("option_pointz_ascending", self.locators.option_pointz_ascending)

    def search_by_pointz_sorting_descending(self):
        self.click_element("option_pointz_descending", self.locators.option_pointz_descending)

    def search_by_status_all(self):
        self.click_element("option_status_all", self.locators.option_status_all)

    def search_by_status_blocked(self):
        self.click_element("option_status_blocked", self.locators.option_status_blocked)

    def search_by_status_active(self):
        self.click_element("option_status_active", self.locators.option_status_active)

    def search_by_verify_status_all(self):
        self.click_element("option_verify_status_all", self.locators.option_verify_status_all)

    def search_by_verify_status_verified(self):
        self.click_element("option_verify_status_verified", self.locators.option_verify_status_verified)

    def search_by_verify_status_not_verified(self):
        self.click_element("option_verify_status_not_verified", self.locators.option_verify_status_not_verified)

    def search_by_referral_status_all(self):
        self.click_element("option_referral_status_all", self.locators.option_referral_status_all)

    def search_by_referral_status_by_referral(self):
        self.click_element("option_referral_status_by_referral", self.locators.option_referral_status_by_referral)

    def search_by_referral_status_direct(self):
        self.click_element("option_referral_status_direct", self.locators.option_referral_status_direct)

    def search_by_active_status_all(self):
        self.click_element("option_active_status_all", self.locators.option_active_status_all)

    def search_by_active_status_active(self):
        self.click_element("option_active_status_active", self.locators.option_active_status_active)

    def search_by_active_status_de_active(self):
        self.click_element("option_active_status_de_active", self.locators.option_active_status_de_active)

    def view_profile(self):
        self.click_element("hyperlink_view_profile_xpath", self.locators.hyperlink_view_profile_xpath)

    def view_profile_see_more(self):
        self.click_element("button_view_profile_see_more_xpath", self.locators.button_view_profile_see_more_xpath)
        sleep(SHORT_WAIT)
        self.driver.back()
        sleep(SHORT_WAIT)
        self.click_element("button_view_profile_see_more_again_xpath",
                           self.locators.button_view_profile_see_more_again_xpath)
        sleep(SHORT_WAIT)

    def delete_post(self):
        self.click_element("button_delete_post_xpath", self.locators.button_delete_post_xpath)
        sleep(SHORT_WAIT)
        # self.click_element("button_acceptDeletePost_xpath", self.locators.button_acceptDeletePost_xpath)
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)
        self.driver.back()
        sleep(SHORT_WAIT)
        self.driver.back()

    def edit_player(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)
        sleep(SHORT_WAIT)

    def select_purchase_block_block(self):
        self.click_element("option_purchase_block_xpath", self.locators.option_purchase_block_xpath)
        sleep(SHORT_WAIT)

    def select_purchase_block_unblock(self):
        self.click_element("option_purchase_unblock_xpath", self.locators.option_purchase_unblock_xpath)
        sleep(SHORT_WAIT)

    def select_player_block_status_block(self):
        self.click_element("option_block_xpath", self.locators.option_block_xpath)

    def select_player_block_status_unblock(self):
        self.click_element("option_unblock_xpath", self.locators.option_unblock_xpath)

    def set_purchase_block_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_purchase_block_end_date_xpath",
                                  self.locators.input_purchase_block_end_date_xpath)

    def set_purchase_block_end_time(self, end_time):
        self.set_element_value_with_tab("input_purchase_block_end_date_xpath",
                                        self.locators.input_purchase_block_end_date_xpath, end_time)

    def set_block_end_date(self, end_date):
        self.clear_fields("input_block_end_date_xpath", self.locators.input_block_end_date_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(end_date, "input_block_end_date_xpath", self.locators.input_block_end_date_xpath)

    def set_block_end_time(self, end_time):
        self.set_element_value_with_tab("input_block_end_date_xpath",
                                        self.locators.input_block_end_date_xpath, end_time)

    def click_take_action(self):
        self.click_element("button_take_action_xpath", self.locators.button_take_action_xpath)

    def click_cancel(self):
        self.click_element("button_edit_block_status_xpath", self.locators.button_edit_block_status_xpath)
        sleep(SHORT_WAIT)
        block_status = self.get_element_attribute("select_status_block_xpath",
                                                  self.locators.select_status_block_xpath, "value")
        sleep(SHORT_WAIT)
        if block_status == "true":
            sleep(SHORT_WAIT)
            self.click_element("option_unblock_xpath", self.locators.option_unblock_xpath)
            sleep(SHORT_WAIT)
        elif block_status == "false":
            self.click_element("option_block_xpath", self.locators.option_block_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def click_export(self):
        self.click_element("button_export_xpath", self.locators.button_export_xpath)

    def click_page_7(self):
        self.click_element("list_page_7_xpath", self.locators.list_page_7_xpath)

    def click_advanced_filter(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def click_advanced_filter_brand_pages(self):
        self.click_element("button_advanced_filter_brand_pages_xpath",
                           self.locators.button_advanced_filter_brand_pages_xpath)

    def click_brand_pages(self):
        self.click_element("button_brand_pages_xpath", self.locators.button_brand_pages_xpath)

    def search_by_brand_page_name(self, brand_page_name):
        self.send_keys_to_element(brand_page_name, "input_search_brand_page_name_xpath",
                                  self.locators.input_search_brand_page_name_xpath)

    def search_brand_page(self):
        self.click_element("button_search_brand_page_xpath", self.locators.button_search_brand_page_xpath)

    def click_refresh_brand_pages(self):
        self.click_element("button_refresh_brand_pages_xpath", self.locators.button_refresh_brand_pages_xpath)

    def search_by_date_from_brand_pages(self, date_from):
        self.send_keys_to_element(date_from, "input_search_reg_date_from_brand_pages_xpath",
                                  self.locators.input_search_reg_date_from_brand_pages_xpath)

    def search_by_date_to_brand_pages(self, date_to):
        self.send_keys_to_element(date_to, "input_search_reg_date_to_brand_pages_xpath",
                                  self.locators.input_search_reg_date_to_brand_pages_xpath)

    def search_by_verify_status_all_brand_pages(self):
        self.click_element("option_verify_status_all_brand_pages_xpath",
                           self.locators.option_verify_status_all_brand_pages_xpath)

    def search_by_verify_status_verified_brand_pages(self):
        self.click_element("option_verify_status_verified_brand_pages_xpath",
                           self.locators.option_verify_status_verified_brand_pages_xpath)

    def search_by_verify_status_not_verified_brand_pages(self):
        self.click_element("option_verify_status_not_verified_brand_pages_xpath",
                           self.locators.option_verify_status_not_verified_brand_pages_xpath)

    def search_by_status_all_brand_pages(self):
        self.click_element("option_status_all_brand_pages_xpath", self.locators.option_status_all_brand_pages_xpath)

    def search_by_status_blocked_brand_pages(self):
        self.click_element("option_status_blocked_brand_pages_xpath",
                           self.locators.option_status_blocked_brand_pages_xpath)

    def search_by_status_active_brand_pages(self):
        self.click_element("option_status_active_brand_pages_xpath",
                           self.locators.option_status_active_brand_pages_xpath)

    def search_by_referral_status_all_brand_pages(self):
        self.click_element("option_referral_status_all_brand_pages_xpath",
                           self.locators.option_referral_status_all_brand_pages_xpath)

    def search_by_referral_status_by_referral_brand_pages(self):
        self.click_element("option_referral_status_by_referral_brand_pages_xpath",
                           self.locators.option_referral_status_by_referral_brand_pages_xpath)

    def search_by_referral_status_direct_brand_pages(self):
        self.click_element("option_referral_status_direct_brand_pages_xpath",
                           self.locators.option_referral_status_direct_brand_pages_xpath)

    def search_by_active_status_all_brand_pages(self):
        self.click_element("option_active_status_all_brand_pages_xpath",
                           self.locators.option_active_status_all_brand_pages_xpath)

    def search_by_active_status_active_brand_pages(self):
        self.click_element("option_active_status_active_brand_pages_xpath",
                           self.locators.option_active_status_active_brand_pages_xpath)

    def search_by_active_status_de_active_brand_pages(self):
        self.click_element("option_active_status_de_active_brand_pages_xpath",
                           self.locators.option_active_status_de_active_brand_pages_xpath)

    def click_export_brand_pages(self):
        self.click_element("button_export_brand_pages_xpath", self.locators.button_export_brand_pages_xpath)

    def click_view_profile_brand_pages(self):
        self.click_element("hyperlink_view_profile_brand_pages_xpath",
                           self.locators.hyperlink_view_profile_brand_pages_xpath)

    def click_edit(self):
        self.click_element("button_edit_brand_pages_xpath", self.locators.button_edit_brand_pages_xpath)

    def set_block_status(self, end_date):
        self.click_element("select_block_status_brand_page_xpath", self.locators.select_block_status_brand_page_xpath)
        dropdown = Select(self.find_element("select_block_status_brand_page_xpath",
                                            self.locators.select_block_status_brand_page_xpath))
        current_value = dropdown.first_selected_option.get_attribute("value")
        if current_value == "true":
            dropdown.select_by_visible_text("Unblock")
        elif current_value == "false":
            dropdown.select_by_visible_text("Block")
            sleep(SHORT_WAIT)
            self.send_keys_to_element(end_date, "input_block_end_date_brand_page_xpath",
                                      self.locators.input_block_end_date_brand_page_xpath)
            sleep(SHORT_WAIT)
            self.send_keys_to_element(Keys.ARROW_RIGHT, "input_block_end_date_brand_page_xpath",
                                      self.locators.input_block_end_date_brand_page_xpath)
            sleep(SHORT_WAIT)
            self.send_keys_to_element(end_date, "input_block_end_date_brand_page_xpath",
                                      self.locators.input_block_end_date_brand_page_xpath)
            sleep(SHORT_WAIT)

    def set_verify_status(self):
        self.click_element("select_verify_status_brand_pages_xpath",
                           self.locators.select_verify_status_brand_pages_xpath)
        dropdown = Select(self.find_element("select_verify_status_brand_pages_xpath",
                                            self.locators.select_verify_status_brand_pages_xpath))
        current_value = dropdown.first_selected_option.get_attribute("value")
        if current_value == "true":
            dropdown.select_by_visible_text("Not Verified")
        elif current_value == "false":
            dropdown.select_by_visible_text("Verified")
            time.sleep(SHORT_WAIT)

    def set_active_status(self):
        self.click_element("select_active_status_brand_pages_xpath",
                           self.locators.select_active_status_brand_pages_xpath)
        dropdown = Select(self.find_element("select_active_status_brand_pages_xpath",
                                            self.locators.select_active_status_brand_pages_xpath))
        current_value = dropdown.first_selected_option.get_attribute("value")
        if current_value == "true":
            dropdown.select_by_visible_text("De Activate")
        elif current_value == "false":
            dropdown.select_by_visible_text("Active")
            time.sleep(SHORT_WAIT)

    def click_take_action_brand_pages(self):
        self.click_element("button_take_action_brand_pages_xpath", self.locators.button_take_action_brand_pages_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def edit_brand_pages(self, block_status_time):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_block_status(block_status_time)
        sleep(SHORT_WAIT)
        self.set_verify_status()
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.click_take_action_brand_pages()
        sleep(SHORT_WAIT)

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.search_brand_page()
        sleep(SHORT_WAIT)
        self.click_refresh_brand_pages()
        sleep(SHORT_WAIT)

    def search_brand_pages(self, name, date_from, date_to):
        self.search_by_brand_page_name(name)
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_date_from_brand_pages(date_from)
        sleep(SHORT_WAIT)
        self.search_by_date_to_brand_pages(date_to)
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_all_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_verified_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_not_verified_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_status_all_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_status_blocked_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_status_active_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_all_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_by_referral_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_direct_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_active_status_all_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_active_status_active_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)
        self.search_by_active_status_de_active_brand_pages()
        self.search_and_refresh()
        self.click_advanced_filter_brand_pages()
        sleep(SHORT_WAIT)

    def search_players(self, name, points_from, points_to, date_from, date_to):
        self.search_by_user_name(name)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_pointz_from(points_from)
        sleep(SHORT_WAIT)
        self.search_pointz_to(points_to)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_date_from(date_from)
        sleep(SHORT_WAIT)
        self.search_by_date_to(date_to)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_pointz_sorting_default()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_pointz_sorting_ascending()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_pointz_sorting_descending()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_blocked()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_status_active()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_verified()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_verify_status_not_verified()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_by_referral()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_referral_status_direct()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_active_status_all()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_active_status_active()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)
        self.search_by_active_status_de_active()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_filter()
        sleep(SHORT_WAIT)

    def edit_player_block_status_block(self, name, end_date, end_time):
        self.search_by_user_name(name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.edit_player()
        sleep(SHORT_WAIT)
        self.select_player_block_status_block()
        sleep(SHORT_WAIT)
        self.set_block_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_block_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_take_action()
        sleep(SHORT_WAIT)

    def edit_player_block_status_unblock(self, name):
        self.search_by_user_name(name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.edit_player()
        sleep(SHORT_WAIT)
        self.select_player_block_status_unblock()
        sleep(SHORT_WAIT)
        self.click_take_action()
        sleep(SHORT_WAIT)

    def edit_player_purchase_block_status_block(self, name, end_date, end_time):
        self.search_by_user_name(name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.edit_player()
        sleep(MEDIUM_WAIT)
        self.select_purchase_block_block()
        sleep(SHORT_WAIT)
        self.set_purchase_block_end_date(end_date)
        sleep(SHORT_WAIT)
        self.set_purchase_block_end_time(end_time)
        sleep(SHORT_WAIT)
        self.click_take_action()
        sleep(SHORT_WAIT)

    def edit_player_purchase_block_status_unblock(self, name):
        self.search_by_user_name(name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.edit_player()
        sleep(SHORT_WAIT)
        self.select_purchase_block_unblock()
        sleep(SHORT_WAIT)
        self.click_take_action()
        sleep(SHORT_WAIT)
