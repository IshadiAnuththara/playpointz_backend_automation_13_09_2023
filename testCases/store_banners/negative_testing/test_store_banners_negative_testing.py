import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.StoreBannersPage import StoreBanners
from test_data.store_banners_test_data import StoreBannersTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_store_banners_negative_testing_assertion


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

        # Initialize the Store Banners Page object for negative testing
        self.store_banner = StoreBanners(self.driver)
        sleep(SHORT_WAIT)
        self.store_banner.access_store_banners()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create store banners - Without fill any field
    def test_negative_testing_001(self):
        self.store_banner.create_store_banners_negative_testing()
        # Define the expected success message
        success_message = 'Image required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_store_banners_negative_testing_assertion(self.driver, self.store_banner, self.logger,
                                                                success_message, "test_negative_testing_001")
        sleep(SHORT_WAIT)

    # Create store banners - Only add description
    def test_negative_testing_002(self):
        self.store_banner.create_store_banners_only_add_description_negative_testing(
            StoreBannersTestData.description_negative_testing
        )
        # Define the expected success message
        success_message = 'Image required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_store_banners_negative_testing_assertion(self.driver, self.store_banner, self.logger,
                                                                success_message, "test_negative_testing_002")
        sleep(SHORT_WAIT)

    # Create store banners - Only add image
    def test_negative_testing_003(self):
        self.store_banner.create_store_banners_only_add_image_negative_testing()
        # Define the expected success message
        success_message = 'Successfully created.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_store_banners_negative_testing_assertion(self.driver, self.store_banner, self.logger,
                                                                success_message, "test_negative_testing_003")
        sleep(SHORT_WAIT)

    # Create store banners - Only fill redirect URL
    def test_negative_testing_004(self):
        self.store_banner.create_store_banners_only_fill_redirect_url_negative_testing(
            StoreBannersTestData.redirect_url_negative_testing
        )
        # Define the expected success message
        success_message = 'Image required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_store_banners_negative_testing_assertion(self.driver, self.store_banner, self.logger,
                                                                success_message, "test_negative_testing_004")
        sleep(SHORT_WAIT)
