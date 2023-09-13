import pytest
import self as self
from pageObjects.ItemsPage import ItemsPage
from pageObjects.LoginPage import LoginPage
from test_data.item_test_data import ItemData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


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
        self.lp = LoginPage(self.driver)
        self.lp.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        # Initialize the Item Page object
        self.categories = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.categories.click_main_items()
        sleep(SHORT_WAIT)
        self.categories.click_categories()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_categories(self):
        self.categories.create_new_category(ItemData.create_category)
        # Define the expected success message
        success_message = 'Successfully Created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate category creation
        perform_assertion(self.driver, self.categories, self.logger, success_message, "test_create_categories")

    def test_edit_category(self):
        self.categories.edit_category(ItemData.edit_category)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update category
        perform_assertion(self.driver, self.categories, self.logger, success_message, "test_edit_category")

    def test_search_categories(self, setup):
        self.categories.search_categories(ItemData.search_category)
        sleep(SHORT_WAIT)
        self.categories.click_refresh()
