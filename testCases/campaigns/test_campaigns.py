import pytest
from self import self
from pageObjects.CampaignPage import CampaignPage
from pageObjects.LoginPage import LoginPage
from test_data.campaigns_test_data import CampaignsData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_assertion


class TestCampaigns:
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

        # Initialize the Campaigns Page object
        self.campaigns = CampaignPage(self.driver)
        sleep(SHORT_WAIT)
        self.campaigns.click_campaigns()
        sleep(MEDIUM_WAIT)
        yield
        self.driver.close()

    def test_create_campaigns(self):
        self.campaigns.create_new_campaign(CampaignsData.campaign_name, CampaignsData.headline, CampaignsData.sponsor,
                                           CampaignsData.website)
        # Define the expected success message
        success_message = 'Successfully created'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate campaigns creation
        perform_assertion(self.driver, self.campaigns, self.logger, success_message, "test_create_campaigns")

    def test_search_campaigns(self):
        self.campaigns.click_campaigns()
        sleep(SHORT_WAIT)
        self.campaigns.search_campaigns(CampaignsData.search_campaign_name,
                                        CampaignsData.start_date,
                                        CampaignsData.end_date)

    def test_edit_campaigns(self):
        self.campaigns.edit_campaigns(CampaignsData.primary_text)
        # Define the expected success message
        success_message = 'Successfully updated.'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate update campaigns
        perform_assertion(self.driver, self.campaigns, self.logger, success_message, "test_edit_campaigns")

    def test_export_campaigns(self):
        self.campaigns.click_export()

    def test_delete_campaigns(self):
        self.campaigns.click_delete()
        # Define the expected success message
        success_message = 'Successfully deleted'
        sleep(SHORT_WAIT)
        # Call the assertion function to validate campaigns deletion
        perform_assertion(self.driver, self.campaigns, self.logger, success_message, "test_delete_campaigns")
