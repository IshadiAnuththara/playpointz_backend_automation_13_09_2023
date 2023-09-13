import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.ItemsPage import ItemsPage
from test_data.item_test_data import ItemData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestAccessScheduler:
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
        self.scheduler = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.scheduler.click_main_items()
        sleep(SHORT_WAIT)
        self.scheduler.click_scheduler()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_scheduler(self):
        self.scheduler.create_new_schedule(ItemData.schedule_item_name,
                                           ItemData.schedule_item_quantity)
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_create_scheduler")

    def test_edit_scheduler(self):
        self.scheduler.edit_schedule(ItemData.schedule_item_quantity)
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_edit_scheduler")

    def test_delete_scheduler(self):
        self.scheduler.delete_schedule()
        success_message = 'Successfully Deleted.'
        sleep(SHORT_WAIT)
        perform_assertion(self.driver, self.scheduler, self.logger, success_message, "test_delete_scheduler")
