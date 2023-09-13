import pytest
from self import self
from pageObjects.AnnouncementPage import AnnouncementPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from test_data.announcement_test_data import AnnouncementTestData
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_assertion


class TestAnnouncement:
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
        sleep(MEDIUM_WAIT)

        # Initialize the Announcement Page object
        self.announce = AnnouncementPage(self.driver)
        sleep(SHORT_WAIT)
        self.announce.click_announcement()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_create_announcement(self):
        self.announce.create_new_announcement(AnnouncementTestData.name, AnnouncementTestData.description)
        # Define the expected success message
        success_message = 'Successfully created.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate new announcement creation
        perform_assertion(self.driver, self.announce, self.logger, success_message, "test_create_announcement")

    def test_search_announcement(self):
        self.announce.search_announcements(AnnouncementTestData.search_announcement,
                                           AnnouncementTestData.start_date,
                                           AnnouncementTestData.end_date)

    def test_edit_announcement(self):
        self.announce.edit_announcements(AnnouncementTestData.edit_description)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update announcement
        perform_assertion(self.driver, self.announce, self.logger, success_message, "test_edit_announcement")

    def test_delete_announcement(self):
        self.announce.delete_announcement(AnnouncementTestData.search_announcement)
        # Define the expected success message
        success_message = 'Successfully deleted.'
        sleep(MEDIUM_WAIT)
        # Call the assertion function to validate delete announcement
        perform_assertion(self.driver, self.announce, self.logger, success_message, "test_delete_announcement")
