import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PlayerSupportPage import PlayerSupportPage
from test_data.player_support_test_data import PlayerSupportData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_assertion


class TestPlayerSupport:
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

        # Initialize the PlayerSupportPage object and navigate to single quiz creation
        self.player_support = PlayerSupportPage(self.driver)
        self.player_support.click_player_support()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_search_support_details(self, setup):
        self.player_support.search_player_support(PlayerSupportData.name,
                                                  PlayerSupportData.start_date,
                                                  PlayerSupportData.end_date)

    def test_send_reply_support_message(self, setup):
        self.player_support.reply_support_message(PlayerSupportData.subject, PlayerSupportData.comment)
        # Define the expected success message
        success_message = 'Successfully sent.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate send reply support message
        perform_assertion(self.driver, self.player_support, self.logger, success_message,
                          "test_send_reply_support_message")

    def test_view_player_profile(self):
        sleep(MEDIUM_WAIT)
        self.player_support.click_view()
        sleep(SHORT_WAIT)
        self.player_support.click_view_profile()
        sleep(SHORT_WAIT)
