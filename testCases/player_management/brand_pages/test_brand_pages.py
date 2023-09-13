import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PlayerManagementPage import PlayerManagementPage
from test_data.player_management_test_data import PlayerManagementData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestBrandPages:
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

        # Initialize the Player Management Page object
        self.player = PlayerManagementPage(self.driver)
        self.player.click_player_management()
        sleep(SHORT_WAIT)
        self.player.click_brand_pages()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_edit_brand_pages(self):
        self.player.edit_brand_pages(PlayerManagementData.block_status_time)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update brand pages
        perform_assertion(self.driver, self.player, self.logger, success_message, "test_edit_brand_pages")

    def test_export(self):
        self.player.click_export_brand_pages()
        sleep(SHORT_WAIT)

    def test_search_player(self):
        self.player.search_brand_page()

    def test_view_player_profile(self):
        self.player.click_view_profile_brand_pages()
        sleep(SHORT_WAIT)
        self.driver.back()
