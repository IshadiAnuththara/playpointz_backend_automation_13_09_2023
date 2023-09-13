import pytest
import self as self
from pageObjects.QuizPage import QuizPage
from test_data.quiz_test_data import QuizTestData
from utilities.custom_logger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_quiz_assertion, \
    perform_edit_quiz_assertion, perform_delete_quiz_assertion


class TestSingleQuizzes:
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

        # Initialize the QuizPage object and navigate to single quiz creation
        self.single_quiz = QuizPage(self.driver)
        self.single_quiz.click_single_quiz()
        sleep(SHORT_WAIT)
        self.single_quiz.click_single_quiz_pool()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_quiz(self):
        self.single_quiz.create_image_type_single_quiz(QuizTestData.type_image_quiz_name,
                                                       QuizTestData.type_image_plus_points,
                                                       QuizTestData.type_image_minus_points,
                                                       QuizTestData.type_image_description,
                                                       QuizTestData.type_image_category,
                                                       QuizTestData.type_image_answer_1,
                                                       QuizTestData.type_image_answer_2,
                                                       QuizTestData.type_image_answer_3,
                                                       QuizTestData.type_image_answer_4)

        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate quiz creation
        perform_create_quiz_assertion(self.driver, self.single_quiz, self.logger, success_message)

    def test_create_quiz_type_video(self):
        self.single_quiz.create_video_type_single_quiz(QuizTestData.type_video_quiz_name,
                                                       QuizTestData.type_video_plus_points,
                                                       QuizTestData.type_video_minus_points,
                                                       QuizTestData.video_path,
                                                       QuizTestData.type_video_description,
                                                       QuizTestData.type_video_category,
                                                       QuizTestData.type_video_answer_1,
                                                       QuizTestData.type_video_answer_2,
                                                       QuizTestData.type_video_answer_3,
                                                       QuizTestData.type_video_answer_4)

        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate quiz creation
        perform_create_quiz_assertion(self.driver, self.single_quiz, self.logger, success_message)

    def test_create_quiz_type_youtube_video(self):
        self.single_quiz.create_youtube_video_type_single_quiz(QuizTestData.type_youtube_quiz_name,
                                                               QuizTestData.type_youtube_plus_points,
                                                               QuizTestData.type_youtube_minus_points,
                                                               QuizTestData.youtube_video_link,
                                                               QuizTestData.type_youtube_description,
                                                               QuizTestData.type_youtube_category,
                                                               QuizTestData.type_youtube_answer_1,
                                                               QuizTestData.type_youtube_answer_2,
                                                               QuizTestData.type_youtube_answer_3,
                                                               QuizTestData.type_youtube_answer_4)

        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate quiz creation
        perform_create_quiz_assertion(self.driver, self.single_quiz, self.logger, success_message)

    def test_search_quizzes(self):
        self.single_quiz.search_quizzes(QuizTestData.quiz_name)

    def test_edit_quizzes(self):
        self.single_quiz.edit_single_quiz(QuizTestData.edit_quiz_name, QuizTestData.edit_quiz_plus_pointz,
                                          QuizTestData.edit_quiz_minus_pointz)

        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate update quiz
        perform_edit_quiz_assertion(self.driver, self.single_quiz, self.logger, success_message)

    def test_delete_quizzes(self, setup):
        self.single_quiz.delete_quiz(QuizTestData.delete_quiz_name)

        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate delete quiz
        perform_delete_quiz_assertion(self.driver, self.single_quiz, self.logger, success_message)
