import time
import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.ItemsPage import ItemsPage
from test_data.item_test_data import ItemData_NegativeTesting
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_add_item_negative_testing_assertion, \
    perform_delete_item_exist_event_negative_testing_assertion, perform_add_existing_item_negative_testing_assertion


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

        # Initialize the Item Page object
        self.items = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.items.click_main_items()
        sleep(SHORT_WAIT)
        self.items.click_items()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Add new item - Without Fill Any Field
    def test_negative_testing_001(self):
        self.items.click_add_items()
        sleep(SHORT_WAIT)
        self.items.click_save()
        sleep(SHORT_WAIT)
        # Define the expected success message
        success_message = 'Stock amount required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 001")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Only Enter Name - Category
    def test_negative_testing_002(self):
        self.items.add_item_negative_testing(ItemData_NegativeTesting.item_name_bairaha)
        # Define the expected success message
        success_message = 'Stock amount required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 002")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Only Enter Name, Category & Description
    def test_negative_testing_003(self):
        self.items.add_item_without_stock_negative_testing(
            ItemData_NegativeTesting.item_name_hair_brush,
            ItemData_NegativeTesting.description
        )
        # Define the expected success message
        success_message = 'Stock amount required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 003")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Only Fill Item Name
    def test_negative_testing_004(self):
        self.items.add_item_only_fill_item_name_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha
        )
        # Define the expected success message
        success_message = 'Stock amount required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 004")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Without Enter Category
    def test_negative_testing_005(self):
        self.items.add_item_without_enter_category_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha,
            ItemData_NegativeTesting.description,
            ItemData_NegativeTesting.stock,
            ItemData_NegativeTesting.points
        )
        # Define the expected success message
        success_message = 'Item category required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 005")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Without Enter Item Status
    def test_negative_testing_006(self):
        self.items.add_item_without_enter_status_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha,
            ItemData_NegativeTesting.description,
            ItemData_NegativeTesting.stock,
            ItemData_NegativeTesting.points
        )
        # Define the expected success message
        success_message = 'Item active status required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 006")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item - Without Enter Pointz
    def test_negative_testing_007(self):
        self.items.add_item_without_enter_points_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha,
            ItemData_NegativeTesting.description,
            ItemData_NegativeTesting.stock
        )
        # Define the expected success message
        success_message = 'Price in points required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 007")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add new item -  Without Enter Stock
    def test_negative_testing_008(self):
        self.items.add_item_without_enter_stock_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha,
            ItemData_NegativeTesting.description,
            ItemData_NegativeTesting.points
        )
        # Define the expected success message
        success_message = 'Stock amount required.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                    "Test 008")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Delete Items - Exist event
    def test_negative_testing_009(self):
        self.items.click_delete_exist_event()
        sleep(SHORT_WAIT)
        # Define the expected success message
        success_message = 'Event exists for this Item. Cannot delete'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_delete_item_exist_event_negative_testing_assertion(self.driver, self.items, self.logger,
                                                                   success_message, "Test 009")
        self.items.click_close()
        sleep(SHORT_WAIT)

    # Add Item -  Existing
    def test_negative_testing_010(self):
        self.items.add_item_existing_negative_testing(
            ItemData_NegativeTesting.item_name_bairaha,
            ItemData_NegativeTesting.description,
            ItemData_NegativeTesting.points,
            ItemData_NegativeTesting.stock
        )
        # Define the expected success message
        success_message = 'That Item already exists.'
        print("Expected message : " + success_message)
        sleep(SHORT_WAIT)
        # Call the assertion function to validate game creation
        perform_add_existing_item_negative_testing_assertion(self.driver, self.items, self.logger, success_message,
                                                             "test_negative_testing_010")
        self.items.click_close()
        sleep(SHORT_WAIT)
        time.sleep(5)
