from pageObjects.BasePage import BasePage
from locators.dashboard_locators import DashboardLocators
from utilities.test_utils import sleep, SHORT_WAIT


class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardLocators()

    def set_start_date(self, start_date):
        self.send_keys_to_element(start_date, "input_startDate_xpath", self.locator.input_start_date_xpath)

    def set_end_date(self, end_date):
        self.send_keys_to_element(end_date, "input_endDate_xpath", self.locator.input_end_date_xpath)

    def click_get_report(self):
        self.click_element("button_getReport_xpath", self.locator.button_get_report_xpath)

    def get_report_by_date_range(self, start_date_txt, end_date_txt):
        self.set_start_date(start_date_txt)
        sleep(SHORT_WAIT)
        self.set_end_date(end_date_txt)
        sleep(SHORT_WAIT)
        return self.click_get_report()

    def get_report_daily(self):
        self.click_element("label_daily_xpath", self.locator.label_daily_xpath)

    def get_report_monthly(self):
        self.click_element("label_monthly_xpath", self.locator.label_monthly_xpath)

    def get_report_yearly(self):
        self.click_element("label_yearly_xpath", self.locator.label_yearly_xpath)

    def get_report(self):
        self.get_report_daily()
        sleep(SHORT_WAIT)
        self.get_report_monthly()
        sleep(SHORT_WAIT)
        self.get_report_yearly()

    def click_notification(self):
        self.click_element("button_notification_xpath", self.locator.button_notification_xpath)

    def click_mark_all_as_read(self):
        self.click_element("button_markAllAsRead_xpath", self.locator.button_mark_all_as_read_xpath)
