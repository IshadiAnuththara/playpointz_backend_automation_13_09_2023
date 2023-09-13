import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PopupBannersPage import PopupBannersPage
from test_data.popup_banners_test_data import PopupBannersData_NegativeTesting
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_popup_banners_negative_testing_assertion


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

        # Initialize the Popup Banners Page object
        self.popup_banners = PopupBannersPage(self.driver)
        sleep(SHORT_WAIT)
        self.popup_banners.click_popup_banners()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create popup banners - without fill any field
    def test_negative_testing_001(self):
        self.popup_banners.create_popup_banners_without_fill_any_field_negative_testing()
        # Define the expected success message
        success_message = 'Image required'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)

    # Create popup banners - Only add image
    def test_negative_testing_002(self):
        self.popup_banners.create_popup_banners_only_add_image_negative_testing()
        # Define the expected success message
        success_message = 'Schedule Start Date required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)

    # Create popup banners - Only add schedule end time
    def test_negative_testing_003(self):
        self.popup_banners.create_popup_banners_only_add_schedule_end_time(
            PopupBannersData_NegativeTesting.schedule_end_date,
            PopupBannersData_NegativeTesting.schedule_end_time
        )
        # Define the expected success message
        success_message = 'Image required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)

    # Create popup banners - Only add schedule start time
    def test_negative_testing_004(self):
        self.popup_banners.create_popup_banners_only_add_schedule_start_time(
            PopupBannersData_NegativeTesting.schedule_start_date,
            PopupBannersData_NegativeTesting.schedule_start_time
        )
        # Define the expected success message
        success_message = 'Image required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)

    # Create popup banners - Without set schedule end date
    def test_negative_testing_005(self):
        self.popup_banners.create_popup_banners_without_set_schedule_end_date(
            PopupBannersData_NegativeTesting.schedule_start_date,
            PopupBannersData_NegativeTesting.schedule_start_time
        )
        # Define the expected success message
        success_message = 'Schedule End Date required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)

    # Create popup banners - Without set schedule start date
    def test_negative_testing_006(self):
        self.popup_banners.create_popup_banners_without_set_schedule_start_date(
            PopupBannersData_NegativeTesting.schedule_end_date,
            PopupBannersData_NegativeTesting.schedule_end_time
        )
        # Define the expected success message
        success_message = 'Schedule Start Date required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_popup_banners_negative_testing_assertion(self.driver, self.popup_banners, self.logger,
                                                                success_message)
        sleep(SHORT_WAIT)
