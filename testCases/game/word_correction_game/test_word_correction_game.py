import pytest
import self as self
from pageObjects.GamesPage import GamePage
from pageObjects.LoginPage import LoginPage
from test_data.game_test_data import WordCorrectionGameData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import SHORT_WAIT, sleep, perform_assertion


class TestWordCorrectionGame:
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

        # Initialize the Game Page object
        self.games = GamePage(self.driver)
        sleep(SHORT_WAIT)
        self.games.click_games()
        sleep(SHORT_WAIT)
        self.games.click_word_correction()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_game(self, setup):
        self.games.create_word_correction_game(WordCorrectionGameData.word,
                                               WordCorrectionGameData.plus_pointz,
                                               WordCorrectionGameData.minus_pointz)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_create_game")

    def test_searchGame(self, setup):
        self.games.search_game(WordCorrectionGameData.search_word)

    def test_edit_game(self, setup):
        self.games.edit_word_correction_game(WordCorrectionGameData.edit_plus_pointz,
                                             WordCorrectionGameData.edit_minus_pointz)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update game
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_edit_game")

    def test_delete_game(self, setup):
        self.games.delete_game()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete game
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_delete_game")

    def test_game_setting(self, setup):
        self.games.click_settings(WordCorrectionGameData.settings_hours)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update game settings
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_game_setting")
