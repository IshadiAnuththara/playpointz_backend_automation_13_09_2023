import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.GamesPage import GamePage
from test_data.game_test_data import NegativeTestingData_WordCorrectionGame
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_game_negative_testing_assertion, \
    perform_add_item_negative_testing_assertion


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
        self.games.click_word_correction()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create a new game - Without Fill Any Field
    def test_negative_testing_1(self):
        self.games.click_create_game()
        sleep(SHORT_WAIT)
        self.games.click_save()
        sleep(SHORT_WAIT)
        # Define the expected success message
        success_message = 'Please shuffel word'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_001")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Duplicate answers
    def test_negative_testing_2(self):
        self.games.create_word_correction_game_negative_testing_duplicate_answers(
            NegativeTestingData_WordCorrectionGame.word,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz,
            NegativeTestingData_WordCorrectionGame.answer_1)
        # Define the expected success message
        success_message = 'Answers has duplicate values.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_002")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Enter Numbers
    def test_negative_testing_3(self):
        self.games.create_word_correction_game_negative_testing_enter_numbers(
            NegativeTestingData_WordCorrectionGame.numbers,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz
        )
        # Define the expected success message
        success_message = 'Maximum word limit is 10 and characters only.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_003")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Enter Symbols
    def test_negative_testing_4(self):
        self.games.create_word_correction_game_negative_testing_enter_symbols(
            NegativeTestingData_WordCorrectionGame.symbols,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz
        )
        # Define the expected success message
        success_message = 'Maximum word limit is 10 and characters only.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_004")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Fill All Field - No Shuffle
    def test_negative_testing_5(self):
        self.games.create_word_correction_game_negative_testing_no_shuffle(
            NegativeTestingData_WordCorrectionGame.word,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz
        )
        # Define the expected success message
        success_message = 'Please shuffel word'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_005")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Only Fill Word, Level, Minus Pointz and Shuffle
    def test_negative_testing_6(self):
        self.games.create_word_correction_game_negative_testing_without_plus_points(
            NegativeTestingData_WordCorrectionGame.word, NegativeTestingData_WordCorrectionGame.minus_pointz)
        # Define the expected success message
        success_message = 'Game points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_006")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Only Fill Word Level, Plus Pointz & Shuffle
    def test_negative_testing_7(self):
        self.games.create_word_correction_game_negative_testing_without_minus_points(
            NegativeTestingData_WordCorrectionGame.word,
            NegativeTestingData_WordCorrectionGame.minus_pointz)
        # Define the expected success message
        success_message = 'Game minus points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_007")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - Only Fill Word Level & Shuffle
    def test_negative_testing_8(self):
        self.games.create_word_correction_game_negative_testing_without_points(
            NegativeTestingData_WordCorrectionGame.word
        )
        # Define the expected success message
        success_message = 'Game points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_008")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - only fill word and no shuffle
    def test_negative_testing_9(self):
        self.games.create_word_correction_game_negative_testing_only_fill_word_no_shuffle(
            NegativeTestingData_WordCorrectionGame.word
        )
        # Define the expected success message
        success_message = 'Please shuffel word'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_009")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - only fill word and shuffle
    def test_negative_testing_10(self):
        self.games.create_word_correction_game_negative_testing_only_fill_word_and_shuffle(
            NegativeTestingData_WordCorrectionGame.word
        )
        # Define the expected success message
        success_message = 'Game level required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)

        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_010")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create New Game - only fill word and no shuffle
    def test_negative_testing_11(self):
        self.games.create_word_correction_game_negative_testing_without_select_status(
            NegativeTestingData_WordCorrectionGame.word,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz
        )
        # Define the expected success message
        success_message = 'Active status required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)

        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_011")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Edit game - Edit Answered Game
    def test_negative_testing_12(self):
        self.games.edit_word_correction_game_negative_testing_edit_answered_game(
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz)
        # Define the expected success message
        success_message = 'Cannot update game because some player submit answer to this game'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)

        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                    "test_012")
        self.games.click_close()
        sleep(SHORT_WAIT)

    # Create a game - Exist game
    def test_negative_testing_13(self):

        self.games.edit_word_correction_game_negative_testing_create_exist_game(
            NegativeTestingData_WordCorrectionGame.word,
            NegativeTestingData_WordCorrectionGame.plus_pointz,
            NegativeTestingData_WordCorrectionGame.minus_pointz
        )
        # Define the expected success message
        success_message = 'Successfully created.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_game_negative_testing_assertion(self.driver, self.games, self.logger, success_message,
                                                       "test_013")
        self.games.click_close()
        sleep(SHORT_WAIT)
