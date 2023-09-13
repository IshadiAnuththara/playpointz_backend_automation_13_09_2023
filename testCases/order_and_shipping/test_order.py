import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.OrderShippingPage import OrderShippingPage
from test_data.order_shipping_test_data import OrderData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestOrderShipping:
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

        # Initialize the Order and Shipping Page object
        self.orders = OrderShippingPage(self.driver)
        sleep(SHORT_WAIT)
        self.orders.click_order_and_shipping()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_export_orders(self):
        self.orders.click_export()
        sleep(SHORT_WAIT)

    def test_search_orders(self):
        self.orders.search_orders(OrderData.search_order, OrderData.start_date, OrderData.end_date)

    def test_edit_orders(self):
        self.orders.edit_orders()
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate edit orders
        perform_assertion(self.driver, self.orders, self.logger, success_message, "test_edit_orders")
