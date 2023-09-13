import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.QuizPage import QuizPage
from pageObjects.SchedulePage import SchedulePage
from test_data.schedule_test_data import ScheduleTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import SHORT_WAIT, sleep, perform_assertion


class TestQuizSchedulerSingleQuiz:
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

        # Initialize the User Role object
        self.scheduler = SchedulePage(self.driver)
        self.quiz = QuizPage(self.driver)
        self.quiz.click_quizzes()
        sleep(SHORT_WAIT)
        self.scheduler.click_single_quiz_scheduler()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_quiz_schedule(self):
        self.scheduler.create_new_schedule_normal_quiz(ScheduleTestData.quiz_name)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new quiz schedule creation
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_create_quiz_schedule")

    def test_edit_quiz_schedule(self):
        self.scheduler.edit_schedule_normal_quiz()
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit quiz schedule
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_edit_quiz_schedule")

    def test_delete_quiz_schedule(self, setup):
        self.scheduler.delete_schedule_normal_quiz()
        # Define the expected success message
        success_message = 'Successfully Deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete quiz schedule
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_delete_quiz_schedule")
