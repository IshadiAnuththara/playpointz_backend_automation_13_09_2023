import pytest
import self as self
from pageObjects.GamesPage import GamePage
from pageObjects.LoginPage import LoginPage
from test_data.game_test_data import NegativeTestingData_FindingMissingCharacterGame
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import SHORT_WAIT, sleep, perform_create_game_negative_testing_assertion


class TestNegativeTesting:
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

    # Create a new game - Without Fill Any Field
    def test_negative_testing_001(self):
        self.games.click_create_game()
        sleep(SHORT_WAIT)
        self.games.click_save()
        # Define the expected success message
        success_message = 'Correct required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger,
                                                       success_message, "test_001")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Duplicate answers
    def test_negative_testing_002(self):
        self.games.create_finding_missing_character_game_negative_testing_duplicate_answers(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.answers_1,
            NegativeTestingData_FindingMissingCharacterGame.answers_2,
            NegativeTestingData_FindingMissingCharacterGame.answers_3,
            NegativeTestingData_FindingMissingCharacterGame.answers_4)

        # Define the expected success message
        success_message = 'Answers has duplicate values.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_002")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Fill All Field - No Shuffle
    def test_negative_testing_003(self):
        self.games.create__finding_missing_character_game_negative_testing_no_shuffle(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz)

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_003")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create a new game - Fill All Field - Not Add Answers
    def test_negative_testing_004(self):
        self.games.create_finding_missing_character_game_negative_testing_not_add_answers(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz)

        # Define the expected success message
        success_message = 'All answers required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_004")
        self.games.click_close()

    # Create a new game - Without Add Pointz
    def test_negative_testing_005(self):
        self.games.create_finding_missing_character_game_negative_testing_without_add_points(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.answer_1,
            NegativeTestingData_FindingMissingCharacterGame.answer_2,
            NegativeTestingData_FindingMissingCharacterGame.answer_3,
            NegativeTestingData_FindingMissingCharacterGame.answer_4)

        # Define the expected success message
        success_message = 'Game points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_005")
        self.games.click_close()

    # Create a new game - Without Enter Minus Pointz
    def test_negative_testing_006(self):
        self.games.create_finding_missing_character_game_negative_testing_without_enter_minus_points(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.answer_1,
            NegativeTestingData_FindingMissingCharacterGame.answer_2,
            NegativeTestingData_FindingMissingCharacterGame.answer_3,
            NegativeTestingData_FindingMissingCharacterGame.answer_4)
        # Define the expected success message
        success_message = 'Game minus points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_006")
        self.games.click_close()

    # Create a new game - Without Enter Plus Pointz
    def test_negative_testing_007(self):
        self.games.create_finding_missing_character_game_negative_testing_without_enter_plus_points(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.answer_1,
            NegativeTestingData_FindingMissingCharacterGame.answer_2,
            NegativeTestingData_FindingMissingCharacterGame.answer_3,
            NegativeTestingData_FindingMissingCharacterGame.answer_4)

        # Define the expected success message
        success_message = 'Game points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_007")
        self.games.click_close()

    # Create a new game - Without Select Game Level
    def test_negative_testing_008(self):
        self.games.create_finding_missing_character_game_negative_testing_without_select_game_level(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.answer_1,
            NegativeTestingData_FindingMissingCharacterGame.answer_2,
            NegativeTestingData_FindingMissingCharacterGame.answer_3,
            NegativeTestingData_FindingMissingCharacterGame.answer_4)

        # Define the expected success message
        success_message = 'Game level required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_008")
        self.games.click_close()

    # Create a new game - Without Select Status
    def test_negative_testing_009(self):
        self.games.create_finding_missing_character_game_negative_testing_without_select_status(
            NegativeTestingData_FindingMissingCharacterGame.word,
            NegativeTestingData_FindingMissingCharacterGame.plus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.minus_pointz,
            NegativeTestingData_FindingMissingCharacterGame.answer_1,
            NegativeTestingData_FindingMissingCharacterGame.answer_2,
            NegativeTestingData_FindingMissingCharacterGame.answer_3,
            NegativeTestingData_FindingMissingCharacterGame.answer_4)

        # Define the expected success message
        success_message = 'Active status required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_009")
        self.games.click_close()
