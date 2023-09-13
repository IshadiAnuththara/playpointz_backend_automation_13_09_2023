import self as self
from pageObjects.Dashboard import Dashboard
from pageObjects.LoginPage import LoginPage
from test_data.dashboard_test_data import DashboardData
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestDashboard:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_get_report(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.dashboard = Dashboard(self.driver)
        sleep(SHORT_WAIT)
        self.dashboard.get_report_by_date_range(DashboardData.start_date, DashboardData.end_date)
        sleep(SHORT_WAIT)
        self.dashboard.get_report()
        sleep(SHORT_WAIT)
        self.dashboard.click_notification()
        sleep(SHORT_WAIT)
        self.driver.close()
