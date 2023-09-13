import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.QuizPage import QuizPage
from pageObjects.SchedulePage import SchedulePage
from test_data.schedule_test_data import ScheduleTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import SHORT_WAIT, sleep, perform_create_quiz_schedule_negative_testing_assertion


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

        # Initialize the Quiz Schedule Page object for negative testing
        self.scheduler = SchedulePage(self.driver)
        self.quiz = QuizPage(self.driver)
        self.quiz.click_quizzes()
        sleep(SHORT_WAIT)
        self.scheduler.click_normal_quiz_scheduler()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create quiz schedule - Without fill any field
    def test_negative_testing_001(self):
        self.scheduler.create_quiz_schedule_without_fill_any_field_negative_testing()
        # Define the expected success message
        success_message = 'Quiz Category required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quiz_schedule_negative_testing_assertion(self.driver, self.scheduler, self.logger,
                                                                success_message, "test_negative_testing_001")
        sleep(SHORT_WAIT)

    # Create quiz schedule - Only enter quiz category
    def test_negative_testing_002(self):
        self.scheduler.create_quiz_schedule_only_enter_quiz_category_negative_testing(
            ScheduleTestData.category_name
        )
        # Define the expected success message
        success_message = 'Quiz Level required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quiz_schedule_negative_testing_assertion(self.driver, self.scheduler, self.logger,
                                                                success_message, "test_negative_testing_002")
        sleep(SHORT_WAIT)

    # Create quiz schedule - Without enter start time
    def test_negative_testing_003(self):
        self.scheduler.create_quiz_schedule_without_enter_start_time(
            ScheduleTestData.category_name
        )
        # Define the expected success message
        success_message = 'Start Time required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quiz_schedule_negative_testing_assertion(self.driver, self.scheduler, self.logger,
                                                                success_message, "test_negative_testing_003")
        sleep(SHORT_WAIT)
