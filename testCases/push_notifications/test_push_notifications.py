import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.PushNotificationsPage import PushNotificationsPage
from test_data.push_notifications_test_data import PushNotificationsData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestPushNotifications:
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

        # Initialize the Push Notifications Page object
        self.push_notifications = PushNotificationsPage(self.driver)
        sleep(SHORT_WAIT)
        self.push_notifications.click_push_notifications()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_create_push_notification(self):
        self.push_notifications.create_new_push_notification(PushNotificationsData.title,
                                                             PushNotificationsData.message,
                                                             PushNotificationsData.date,
                                                             PushNotificationsData.time)
        # Define the expected success message
        success_message = 'Successfully sent.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate create pop-up banners
        perform_assertion(self.driver, self.push_notifications, self.logger, success_message,
                          "test_create_push_notification")

    def test_edit_notification(self):
        self.push_notifications.edit_push_notifications(PushNotificationsData.edit_message,
                                                        PushNotificationsData.edit_date,
                                                        PushNotificationsData.edit_time)
        # Define the expected success message
        success_message = 'Successfully Updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update pop-up banners
        perform_assertion(self.driver, self.push_notifications, self.logger, success_message,
                          "test_edit_notification")

    def test_search_notification(self):
        self.push_notifications.search_push_notifications(PushNotificationsData.title)

    def test_resend_notification(self, setup):
        self.push_notifications.click_resend()
        # Define the expected success message
        success_message = 'Successfully sent.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate resend pop-up banners
        perform_assertion(self.driver, self.push_notifications, self.logger, success_message,
                          "test_resend_notification")

    def test_delete_notification(self):
        self.push_notifications.delete_notification()
        # Define the expected success message
        success_message = 'Successfully Deleted.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate delete pop-up banners
        perform_assertion(self.driver, self.push_notifications, self.logger, success_message,
                          "test_delete_notification")
