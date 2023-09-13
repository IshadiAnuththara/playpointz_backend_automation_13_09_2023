import pytest
import self as self
from test_data.categories_test_data import CategoriesTestData
from utilities.custom_logger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from pageObjects.CategoriesPage import CategoryPage
from utilities.test_utils import SHORT_WAIT, sleep, perform_assertion


class TestCategories:
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

        # Initialize the Category Page object
        self.categories = CategoryPage(self.driver)
        self.categories.click_categories()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_category(self):
        self.categories.create_new_category(CategoriesTestData.category_name)
        # Define the expected success message
        success_message = 'Successfully Created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new quiz category creation
        perform_assertion(self.driver, self.categories, self.logger, success_message, "test_create_category")

    def test_edit_categories(self):
        self.categories.edit_quiz_category(CategoriesTestData.edit_category_name)
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit quiz category
        perform_assertion(self.driver, self.categories, self.logger, success_message, "test_edit_categories")

    def test_search_category(self):
        self.categories.search_quiz_category(
            CategoriesTestData.search_category_name
        )
