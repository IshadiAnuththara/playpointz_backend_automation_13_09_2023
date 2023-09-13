import pytest
import self as self
from utilities.custom_logger import LogGen
from pageObjects.QuizPage import QuizPage
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion
from test_data.quiz_test_data import QuizTestData


class TestNormalQuizzes:
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
        self.normal_quiz = QuizPage(self.driver)
        self.normal_quiz.click_quizzes()
        sleep(SHORT_WAIT)
        self.normal_quiz.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_quiz_type_image(self):
        self.normal_quiz.create_image_type_normal_quiz(QuizTestData.type_image_normal_quiz_name,
                                                       QuizTestData.type_image_normal_quiz_plus_points,
                                                       QuizTestData.type_image_normal_quiz_minus_points,
                                                       QuizTestData.type_image_normal_quiz_description,
                                                       QuizTestData.type_image_normal_quiz_quiz_category,
                                                       QuizTestData.type_image_normal_quiz_answer_1,
                                                       QuizTestData.type_image_normal_quiz_answer_2,
                                                       QuizTestData.type_image_normal_quiz_answer_3,
                                                       QuizTestData.type_image_normal_quiz_answer_4)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate quiz creation
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message,
                          "test_create_quiz_type_image")

    def test_create_quiz_type_text(self):
        self.normal_quiz.create_text_type_normal_quiz(QuizTestData.type_text_normal_quiz_name,
                                                      QuizTestData.type_text_normal_quiz_plus_pointz,
                                                      QuizTestData.type_text_normal_quiz_minus_pointz,
                                                      QuizTestData.type_text_normal_quiz_text_area,
                                                      QuizTestData.type_text_normal_quiz_category,
                                                      QuizTestData.type_text_normal_quiz_answers_1,
                                                      QuizTestData.type_text_normal_quiz_answers_2,
                                                      QuizTestData.type_text_normal_quiz_answers_3,
                                                      QuizTestData.type_text_normal_quiz_answers_4)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate quiz creation
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message,
                          "test_create_quiz_type_text")

    def test_create_quiz_type_video(self):
        self.normal_quiz.create_video_type_normal_quiz(QuizTestData.type_video_normal_quiz_name,
                                                       QuizTestData.type_video_normal_quiz_plus_pointz,
                                                       QuizTestData.type_video_normal_quiz_minus_pointz,
                                                       QuizTestData.video_path,
                                                       QuizTestData.type_video_normal_quiz_text_area,
                                                       QuizTestData.type_video_normal_quiz_category,
                                                       QuizTestData.type_video_normal_quiz_answers_1,
                                                       QuizTestData.type_video_normal_quiz_answers_2,
                                                       QuizTestData.type_video_normal_quiz_answers_3,
                                                       QuizTestData.type_video_normal_quiz_answers_4)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate quiz creation
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message,
                          "test_create_quiz_type_video")

    def test_create_quiz_type_youtube_video(self):
        self.normal_quiz.create_youtube_video_type_normal_quiz(QuizTestData.type_youtube_video_normal_quiz_name,
                                                               QuizTestData.type_youtube_video_normal_quiz_plus_pointz,
                                                               QuizTestData.type_youtube_video_normal_quiz_minus_pointz,
                                                               QuizTestData.youtube_video_link,
                                                               QuizTestData.type_youtube_video_normal_quiz_text_area,
                                                               QuizTestData.type_youtube_video_normal_quiz_category,
                                                               QuizTestData.type_youtube_video_normal_quiz_answers_1,
                                                               QuizTestData.type_youtube_video_normal_quiz_answers_2,
                                                               QuizTestData.type_youtube_video_normal_quiz_answers_3,
                                                               QuizTestData.type_youtube_video_normal_quiz_answers_4)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate quiz creation
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message,
                          "test_create_quiz_type_youtube_video")

    def test_edit_quizzes(self):
        self.normal_quiz.edit_normal_quiz(QuizTestData.edit_quiz_name_normal_quiz,
                                          QuizTestData.edit_plus_points,
                                          QuizTestData.edit_minus_points)
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update quiz
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message, "test_edit_quizzes")

    def test_search_quizzes(self):
        self.normal_quiz.search_quizzes(QuizTestData.search_quiz_name)

    def test_delete_quizzes(self):
        self.normal_quiz.delete_quiz(QuizTestData.delete_quiz_name)
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete quiz
        perform_assertion(self.driver, self.normal_quiz, self.logger, success_message, "test_delete_quizzes")
