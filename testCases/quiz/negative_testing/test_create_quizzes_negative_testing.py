import pytest
import self as self
from pageObjects.QuizPage import QuizPage
from test_data.quiz_test_data import QuizTestData
from utilities.custom_logger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_quizzes_negative_testing_assertion


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
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        # Initialize the Quiz Page object for negative testing
        self.quiz = QuizPage(self.driver)
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create quiz - Without fill any field

    def test_negative_testing_001(self):
        self.quiz.create_quiz_without_enter_any_field_negative_testing()

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_001")
        sleep(SHORT_WAIT)

    # Create quiz - Only add answers

    def test_negative_testing_002(self):
        self.quiz.create_quiz_only_add_answers_negative_testing(QuizTestData.answer_5_negative_testing,
                                                                QuizTestData.answer_6_negative_testing,
                                                                QuizTestData.answer_7_negative_testing,
                                                                QuizTestData.answer_8_negative_testing)

        # Define the expected success message
        success_message = 'Quiz Title / ID required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_002")
        sleep(SHORT_WAIT)

    # Create quiz - Only add wrong answers

    def test_negative_testing_003(self):
        self.quiz.create_quiz_only_add_wrong_answers_negative_testing(QuizTestData.answer_5_negative_testing,
                                                                      QuizTestData.answer_6_negative_testing,
                                                                      QuizTestData.answer_7_negative_testing,
                                                                      QuizTestData.answer_8_negative_testing)

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_003")
        sleep(SHORT_WAIT)

    # Create quiz - Only enter category

    def test_negative_testing_004(self):
        self.quiz.create_quiz_only_enter_category_negative_testing(
            QuizTestData.category_negative_testing
        )

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_004")
        sleep(SHORT_WAIT)

    # Create quiz - Only enter description

    def test_negative_testing_005(self):
        self.quiz.create_quiz_only_enter_description_negative_testing(
            QuizTestData.description_negative_testing
        )

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_005")
        sleep(SHORT_WAIT)

    # Create quiz - Only enter minus points

    def test_negative_testing_006(self):
        self.quiz.create_quiz_only_enter_minus_points_negative_testing(
            QuizTestData.minus_points_negative_testing
        )

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_006")
        sleep(SHORT_WAIT)

    # Create quiz - Only enter plus points

    def test_negative_testing_007(self):
        self.quiz.create_quiz_only_enter_plus_points_negative_testing(
            QuizTestData.plus_points_negative_testing
        )

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_007")
        sleep(SHORT_WAIT)

    # Create quiz - Only enter quiz name

    def test_negative_testing_008(self):
        self.quiz.create_quiz_only_enter_quiz_name_negative_testing(
            QuizTestData.quiz_name_negative_testing
        )

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_008")
        sleep(SHORT_WAIT)

    # Create quiz - Only select quiz level

    def test_negative_testing_009(self):
        self.quiz.create_quiz_only_select_quiz_level_negative_testing()

        # Define the expected success message
        success_message = 'Correct answer required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_009")
        sleep(SHORT_WAIT)

    # Create quiz - Without enter description

    def test_negative_testing_010(self):
        self.quiz.create_quiz_without_enter_description_negative_testing(QuizTestData.quiz_name_negative_testing,
                                                                         QuizTestData.plus_points_negative_testing,
                                                                         QuizTestData.minus_points_negative_testing,
                                                                         QuizTestData.category_negative_testing,
                                                                         QuizTestData.answer_1_negative_testing,
                                                                         QuizTestData.answer_2_negative_testing,
                                                                         QuizTestData.answer_3_negative_testing,
                                                                         QuizTestData.answer_4_negative_testing)

        # Define the expected success message
        success_message = 'Quiz required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_010")
        sleep(SHORT_WAIT)

    # Create quiz - Without select approval

    def test_negative_testing_011(self):
        self.quiz.create_quiz_without_select_approval_negative_testing(QuizTestData.quiz_name_negative_testing,
                                                                       QuizTestData.plus_points_negative_testing,
                                                                       QuizTestData.minus_points_negative_testing,
                                                                       QuizTestData.description_negative_testing,
                                                                       QuizTestData.category_negative_testing,
                                                                       QuizTestData.answer_1_negative_testing,
                                                                       QuizTestData.answer_2_negative_testing,
                                                                       QuizTestData.answer_3_negative_testing,
                                                                       QuizTestData.answer_4_negative_testing)

        # Define the expected success message
        success_message = 'Successfully created.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_011")
        sleep(SHORT_WAIT)

    # Create quiz - Without select quiz level

    def test_negative_testing_012(self):
        self.quiz.create_quiz_without_select_quiz_level_negative_testing(QuizTestData.quiz_name_negative_testing,
                                                                         QuizTestData.plus_points_negative_testing,
                                                                         QuizTestData.minus_points_negative_testing,
                                                                         QuizTestData.description_negative_testing,
                                                                         QuizTestData.category_negative_testing,
                                                                         QuizTestData.answer_1_negative_testing,
                                                                         QuizTestData.answer_2_negative_testing,
                                                                         QuizTestData.answer_3_negative_testing,
                                                                         QuizTestData.answer_4_negative_testing)

        # Define the expected success message
        success_message = 'Quiz Level required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_012")
        sleep(SHORT_WAIT)

    # Create quiz - Without select quiz category

    def test_negative_testing_013(self):
        self.quiz.create_quiz_without_select_quiz_category_negative_testing(QuizTestData.quiz_name_negative_testing,
                                                                            QuizTestData.plus_points_negative_testing,
                                                                            QuizTestData.minus_points_negative_testing,
                                                                            QuizTestData.description_negative_testing,
                                                                            QuizTestData.answer_1_negative_testing,
                                                                            QuizTestData.answer_2_negative_testing,
                                                                            QuizTestData.answer_3_negative_testing,
                                                                            QuizTestData.answer_4_negative_testing)

        # Define the expected success message
        success_message = 'Quiz Category required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_013")
        sleep(SHORT_WAIT)

    # Create quiz - Existing_quiz

    def test_negative_testing_014(self):
        self.quiz.create_quiz_existing_quiz_negative_testing(QuizTestData.quiz_name_single_quiz_negative_testing,
                                                             QuizTestData.plus_points_negative_testing,
                                                             QuizTestData.minus_points_negative_testing,
                                                             QuizTestData.description_single_quiz_negative_testing,
                                                             QuizTestData.category_negative_testing,
                                                             QuizTestData.answers_9_negative_testing,
                                                             QuizTestData.answers_10_negative_testing,
                                                             QuizTestData.answers_11_negative_testing,
                                                             QuizTestData.answers_12_negative_testing)

        # Define the expected success message
        success_message = 'That Quiz already exists.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quizzes_negative_testing_assertion(self.driver, self.quiz, self.logger, success_message,
                                                          "test_negative_testing_014")
        sleep(SHORT_WAIT)
