import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.SettingsPage import Settings
from test_data.settings_test_data import SettingsTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestSettingsEmailDomain:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):

        # Initialize the WebDriver and navigate to the application
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Initialize the LoginPage object and perform login
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        # Initialize the Settings Page object
        self.settings = Settings(self.driver)
        self.settings.click_settings()
        sleep(SHORT_WAIT)
        self.settings.click_email_domain()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_email_domain(self):
        self.settings.create_email_domain(SettingsTestData.email)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate create new email domain
        perform_assertion(self.driver, self.settings, self.logger, success_message,
                          "test_create_email_domain")

    def test_edit_email_domain(self):
        self.settings.edit_email_domain(SettingsTestData.edit_email)
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit email domain
        perform_assertion(self.driver, self.settings, self.logger, success_message, "test_edit_email_domain")

    def test_search_email_domain(self):
        self.settings.search_email_domain(SettingsTestData.search_email_1, SettingsTestData.search_email_2)

    def test_delete_email_domain(self):
        self.settings.click_delete()
        # Define the expected success message
        success_message = 'Successfully Deleted'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete email domain
        perform_assertion(self.driver, self.settings, self.logger, success_message, "test_delete_email_domain")
