import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.ItemsPage import ItemsPage
from test_data.item_test_data import ItemScheduleData_NegativeTesting
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_scheduler_negative_testing_assertion


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

        # Initialize the Items Page object
        self.items = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.items.click_main_items()
        sleep(SHORT_WAIT)
        self.items.click_scheduler()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Create Scheduler - Without Enter Any Field
    def test_negative_testing_001(self):
        self.items.click_new_scheduler()
        sleep(SHORT_WAIT)
        self.items.click_save()
        sleep(SHORT_WAIT)
        # Define the expected success message
        success_message = 'Quantity required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_scheduler_negative_testing_assertion(self.driver, self.items, self.logger, success_message)
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Create Scheduler - Only Enter Item Name
    def test_negative_testing_002(self):
        self.items.create_scheduler_negative_testing_only_enter_name(
            ItemScheduleData_NegativeTesting.item_name
        )
        # Define the expected success message
        success_message = 'Quantity required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_scheduler_negative_testing_assertion(self.driver, self.items, self.logger, success_message)
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Create Scheduler - Without Enter End Time
    def test_negative_testing_003(self):
        self.items.create_scheduler_negative_testing_without_end_time(
            ItemScheduleData_NegativeTesting.item_name,
            ItemScheduleData_NegativeTesting.item_quantity
        )
        # Define the expected success message
        success_message = 'End Time required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_scheduler_negative_testing_assertion(self.driver, self.items, self.logger, success_message)
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Create Schedule - Item Quantity Exceed
    def test_negative_testing_004(self):
        self.items.create_scheduler_negative_testing_quantity_exceed(
            ItemScheduleData_NegativeTesting.item_name,
            ItemScheduleData_NegativeTesting.item_quantity
        )
        # Define the expected success message
        success_message = 'Quantity cannot exceed 3.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_create_scheduler_negative_testing_assertion(self.driver, self.items, self.logger, success_message)
        self.items.click_close()
        sleep(SHORT_WAIT)
