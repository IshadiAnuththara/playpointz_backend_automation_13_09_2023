import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PopupBannersPage import PopupBannersPage
from test_data.popup_banners_test_data import PopupBannersData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestPopupBanners:
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
        self.banners = PopupBannersPage(self.driver)
        self.banners.click_popup_banners()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_popup_banners(self):
        self.banners.create_popup_banners()
        sleep(SHORT_WAIT)
        self.banners.create_new_popup_banners(PopupBannersData.start_date,
                                              PopupBannersData.start_time,
                                              PopupBannersData.end_date,
                                              PopupBannersData.end_time)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate create pop-up banners
        perform_assertion(self.driver, self.banners, self.logger, success_message,
                          "test_create_popup_banners")

    def test_edit_popup_banners(self):
        self.banners.edit_popup_banners(PopupBannersData.edit_start_date,
                                        PopupBannersData.edit_start_time,
                                        PopupBannersData.edit_end_date,
                                        PopupBannersData.edit_end_time)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update pop-up banners
        perform_assertion(self.driver, self.banners, self.logger, success_message,
                          "test_edit_popup_banners")

    def test_delete_popup_banners(self):
        self.banners.click_delete()
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete pop-up banners
        perform_assertion(self.driver, self.banners, self.logger, success_message,
                          "test_delete_popup_banners")

    def test_cancel_create_popup_banners(self):
        self.banners.create_popup_banners()
        sleep(SHORT_WAIT)
        self.banners.click_cancel()
