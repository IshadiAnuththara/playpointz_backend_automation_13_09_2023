import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.UserManagementPage import UserManagement
from test_data.user_role_test_data import UserRoleTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestUserRole:
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
        self.user_role = UserManagement(self.driver)
        self.user_role.click_user_role()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_add_user_role(self):
        self.user_role.add_new_user_role(UserRoleTestData.user_role, UserRoleTestData.add_permission)
        # Define the expected success message
        success_message = 'Successfully Created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new user role creation
        perform_assertion(self.driver, self.user_role, self.logger, success_message, "test_add_user_role")

    def test_edit_user_role(self):
        self.user_role.edit_user_permission(UserRoleTestData.edit_permission)
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit user role
        perform_assertion(self.driver, self.user_role, self.logger, success_message, "test_edit_user_role")

    def test_remove_permission(self):
        self.user_role.remove_permissions()
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit user role
        perform_assertion(self.driver, self.user_role, self.logger, success_message, "test_remove_permission")
