import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.UserManagementPage import UserManagement
from test_data.user_management_test_data import UserManagementTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestUserManagement:
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

        # Initialize the User Management object
        self.user_management = UserManagement(self.driver)
        self.user_management.click_user_management()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_add_user(self):
        self.user_management.create_user(UserManagementTestData.name,
                                         UserManagementTestData.email,
                                         UserManagementTestData.first_name,
                                         UserManagementTestData.last_name)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new user creation
        perform_assertion(self.driver, self.user_management, self.logger, success_message, "test_add_user")

    def test_search_member(self):
        self.user_management.search_user(UserManagementTestData.search_user)

    def test_edit_member(self):
        self.user_management.edit_member()
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate user update
        perform_assertion(self.driver, self.user_management, self.logger, success_message, "test_edit_member")
