import pytest
import self as self
from test_data.game_test_data import FindingMissingCharacterGameData
from utilities.custom_logger import LogGen
from pageObjects.GamesPage import GamePage
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestFindingMissingCharacter:
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
        self.games.click_finding_missing_character()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_game(self):
        self.games.create_finding_missing_character_game(FindingMissingCharacterGameData.word,
                                                         FindingMissingCharacterGameData.plus_points,
                                                         FindingMissingCharacterGameData.minus_points,
                                                         FindingMissingCharacterGameData.answer_1,
                                                         FindingMissingCharacterGameData.answer_2,
                                                         FindingMissingCharacterGameData.answer_3,
                                                         FindingMissingCharacterGameData.answer_4)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_create_game")

    def test_edit_game(self):
        sleep(SHORT_WAIT)
        self.games.edit_game(FindingMissingCharacterGameData.edit_plus_pointz,
                             FindingMissingCharacterGameData.edit_minus_pointz)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit game
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_edit_game")

    def test_search_games(self):
        self.games.search_game(FindingMissingCharacterGameData.search_word)

    def test_delete_game(self):
        self.games.delete_game()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete game
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_delete_game")

    def test_settings(self):
        self.games.click_settings(FindingMissingCharacterGameData.setting_minutes)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update settings
        perform_assertion(self.driver, self.games, self.logger, success_message, "test_settings")
