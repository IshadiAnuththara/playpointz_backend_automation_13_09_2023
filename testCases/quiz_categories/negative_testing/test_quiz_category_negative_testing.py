import pytest
import self as self
from test_data.categories_test_data import CategoriesTestData
from utilities.custom_logger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from pageObjects.CategoriesPage import CategoryPage
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_quiz_categories_negative_testing_assertion


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

        # Initialize the Quiz Category Page object for negative testing
        self.quiz_categories = CategoryPage(self.driver)
        sleep(SHORT_WAIT)
        self.quiz_categories.click_categories()
        yield
        self.driver.close()

    # Create quiz category - Without fill category name
    def test_negative_testing_001(self):
        self.quiz_categories.create_category_without_fill_category_name_negative_testing()
        # Define the expected success message
        success_message = 'Category Name Required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quiz_categories_negative_testing_assertion(self.driver, self.quiz_categories,
                                                                  self.logger, success_message,
                                                                  "test_negative_testing_001")
        sleep(SHORT_WAIT)

    # Create quiz category - Enter exist category
    def test_negative_testing_002(self):
        self.quiz_categories.create_category_enter_exist_category_negative_testing(
            CategoriesTestData.exist_category_negative_testing
        )
        # Define the expected success message
        success_message = 'That Quiz category already exists.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_quiz_categories_negative_testing_assertion(self.driver, self.quiz_categories,
                                                                  self.logger, success_message,
                                                                  "test_negative_testing_002")
        sleep(SHORT_WAIT)
