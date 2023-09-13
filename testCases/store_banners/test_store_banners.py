import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.StoreBannersPage import StoreBanners
from test_data.store_banners_test_data import StoreBannersTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import SHORT_WAIT, sleep, perform_assertion


class TestStoreBanners:
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

        # Initialize the Store Banners object
        self.store_banners = StoreBanners(self.driver)
        self.store_banners.access_store_banners()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_store_banners(self):

        self.store_banners.create_new_store_banner(StoreBannersTestData.redirect_url, StoreBannersTestData.description)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate store banners creation
        perform_assertion(self.driver, self.store_banners, self.logger, success_message, "test_create_store_banners")

    def test_delete_store_banners(self):
        self.store_banners.delete_store_banners()
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate store banners deletion
        perform_assertion(self.driver, self.store_banners, self.logger, success_message, "test_delete_store_banners")
