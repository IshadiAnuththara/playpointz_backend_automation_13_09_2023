import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.ItemsPage import ItemsPage
from test_data.item_test_data import ItemData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestAccessItems:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.items = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.items.click_main_items()
        sleep(SHORT_WAIT)
        self.items.click_items()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    # Add new item
    def test_add_items(self):
        self.items.click_add_items()
        sleep(SHORT_WAIT)
        self.items.add_new_item(ItemData.item_name, ItemData.description, ItemData.stock, ItemData.pointz)
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.items, self.logger, success_message, "test_add_items")

    # Search Items
    def test_search_items(self):
        self.items.search_items(ItemData.search_item)

    # Edit Items
    def test_edit_items(self):
        self.items.edit(ItemData.edit_pointz)
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.items, self.logger, success_message, "test_edit_items")

    # Delete Items
    def test_delete_items(self):
        self.items.delete_item(ItemData.item_name)
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.items, self.logger, success_message, "test_delete_items")
