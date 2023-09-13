from test_data.complains_test_data import ComplainsData
import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.ComplainsPage import Complains
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class Test_Complains:
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
        self.lp = LoginPage(self.driver)
        self.lp.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        # Initialize the Complaints Page object
        self.complain = Complains(self.driver)
        sleep(SHORT_WAIT)
        self.complain.click_complains()
        sleep(SHORT_WAIT)

    def test_ignore_complains(self):
        self.complain.click_ignore()
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate ignore complains
        perform_assertion(self.driver, self.complain, self.logger, success_message, "test_ignore_complains")
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_search_complains(self):
        self.complain.search_complains(ComplainsData.reporter, ComplainsData.date_from, ComplainsData.date_to)
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_take_action(self):
        self.complain.take_action()
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_view_profile(self):
        self.complain.view_profile()
