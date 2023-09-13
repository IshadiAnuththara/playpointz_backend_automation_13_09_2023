import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PlayerManagementPage import PlayerManagementPage
from test_data.player_management_test_data import PlayerManagementData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestPlayers:
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
        self.player.click_player_management()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_view_player_profile(self):
        self.player.view_profile()
        sleep(SHORT_WAIT)

    def test_edit_player_block_status_block(self):
        self.player.edit_player_block_status_block(PlayerManagementData.edit_player_name,
                                                   PlayerManagementData.block_end_date,
                                                   PlayerManagementData.block_end_time)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit player block status == block
        perform_assertion(self.driver, self.player, self.logger, success_message,
                          "test_edit_player_block_status_block")

    def test_edit_player_player_block_status_unblock(self):
        self.player.edit_player_block_status_unblock(PlayerManagementData.search_player_unblock)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit player block status == unblock
        perform_assertion(self.driver, self.player, self.logger, success_message,
                          "test_edit_player_player_block_status_unblock")

    def test_edit_player_purchase_block_block(self):
        self.player.edit_player_purchase_block_status_block(PlayerManagementData.search_player_purchase_block,
                                                            PlayerManagementData.purchase_block_end_date,
                                                            PlayerManagementData.purchase_block_end_time)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit purchase block status == block
        perform_assertion(self.driver, self.player, self.logger, success_message,
                          "test_edit_player_purchase_block_block")

    def test_edit_player_purchase_block_unblock(self):
        self.player.edit_player_purchase_block_status_unblock(PlayerManagementData.search_player_purchase_unblock)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit purchase block status == unblock
        perform_assertion(self.driver, self.player, self.logger, success_message,
                          "test_edit_player_purchase_block_unblock")

    def test_Export(self):
        self.player.click_export()
        sleep(SHORT_WAIT)

    def test_searchPlayer(self, setup):
        self.player.search_players(PlayerManagementData.search_player,
                                   PlayerManagementData.search_point_from,
                                   PlayerManagementData.search_point_to,
                                   PlayerManagementData.search_date_from,
                                   PlayerManagementData.search_date_to)

    def test_viewPlayerProfile(self):
        self.player.view_profile()
        sleep(SHORT_WAIT)
        self.driver.back()
        sleep(SHORT_WAIT)

    def delete_player_posts(self):
        self.player.view_profile()
        sleep(SHORT_WAIT)
        self.player.view_profile_see_more()
        sleep(SHORT_WAIT)
        self.player.delete_post()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete player posts
        perform_assertion(self.driver, self.player, self.logger, success_message, "delete_player_posts")
