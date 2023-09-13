from self import self
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, perform_assertion, SHORT_WAIT


class TestLogin:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        # Define the expected success message
        success_message = 'Successfully logged in.'
        # Call the assertion function to validate login
        perform_assertion(self.driver, self.login_page, self.logger, success_message,
                          "test_login_with_valid_credentials")
        sleep(SHORT_WAIT)
        self.login_page.click_logout()
        self.driver.close()
