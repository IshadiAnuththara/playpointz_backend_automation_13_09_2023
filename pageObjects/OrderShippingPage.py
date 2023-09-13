from pageObjects.BasePage import BasePage
from locators.order_shipping_locators import OrderShippingLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class OrderShippingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderShippingLocators()
        self.locator = CommonLocators()

    def click_order_and_shipping(self):
        self.click_element("hyperlink_order_shipping_xpath", self.locators.hyperlink_order_shipping_xpath)

    def search_item_by_name(self, item_name):
        self.send_keys_to_element(item_name, "input_search_xpath", self.locators.input_search_xpath)
        sleep(SHORT_WAIT)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def search_item_by_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_start_date_xpath", self.locators.input_start_date_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def search_item_by_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_end_date_xpath", self.locators.input_end_date_xpath)

    def click_option(self):
        self.click_element("select_status_xpath", self.locators.select_status_xpath)

    def click_option_placed(self):
        self.click_element("option_placed_xpath", self.locators.option_placed_xpath)

    def click_option_processing(self):
        self.click_element("option_processing_xpath", self.locators.option_processing_xpath)

    def click_option_shipped(self):
        self.click_element("option_shipped_xpath", self.locators.option_shipped_xpath)

    def click_option_delivered(self):
        self.click_element("option_delivered_xpath", self.locators.option_delivered_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def edit_order(self):
        self.click_element("hyperlink_page_xpath", self.locators.hyperlink_page_xpath)

    def click_export(self):
        self.click_element("button_export_xpath", self.locators.button_export_xpath)

    def click_page(self):
        self.click_element("hyperlink_page_xpath", self.locators.hyperlink_page_xpath)

    def set_option_delivered(self):
        self.click_element("option_delivered_edit_xpath", self.locators.option_delivered_edit_xpath)

    def set_option_shipped(self):
        self.click_element("option_shipped_edit_xpath", self.locators.option_shipped_edit_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_advanced_path(self):
        self.click_element("button_advanced_filter_xpath", self.locators.button_advanced_filter_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def search_orders(self, name, start_date, end_date):
        self.search_item_by_name(name)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)
        self.search_item_by_start_date(start_date)
        sleep(SHORT_WAIT)
        self.search_item_by_end_date(end_date)
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)
        self.click_option_placed()
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)
        self.click_option_processing()
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)
        self.click_option_shipped()
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)
        self.click_option_delivered()
        self.search_and_refresh()
        self.click_advanced_path()
        sleep(SHORT_WAIT)

    def edit_orders(self):
        self.click_page()
        sleep(SHORT_WAIT)
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_option_delivered()
        sleep(SHORT_WAIT)
        self.click_save()
