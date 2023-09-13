import time
import pytest
import self as self
from pageObjects.LoginPage import LoginPage
from pageObjects.SettingsPage import Settings
from test_data.settings_test_data import SettingsTestData
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import sleep, SHORT_WAIT, perform_assertion


class TestGeneral:
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

        # Initialize the Settings Page object
        self.settings = Settings(self.driver)
        self.settings.click_settings()
        sleep(SHORT_WAIT)
        self.settings.click_general()
        sleep(SHORT_WAIT)
        yield
        self.driver.close()

    def test_edit_general(self):

        """self.logger.info("********** Starting edit quiz hard level **********")

        self.settings.clickEditQuizHardLevel()
        time.sleep(2)
        self.settings.editQuizLowerBound("101")
        time.sleep(2)
        self.settings.editQuizUpperBound("100000")
        time.sleep(2)
        self.settings.clickSave()

        self.logger.info("********** Successfully edit quiz hard level **********")

        self.logger.info("********** Starting edit quiz easy level **********")

        self.settings.clickEditQuizEasyLevel()
        time.sleep(2)
        self.settings.editQuizLowerBound("0")
        time.sleep(2)
        self.settings.editQuizUpperBound("100")
        time.sleep(2)
        self.settings.clickSave()

        self.logger.info("********** Successfully edit quiz easy level **********")

        time.sleep(2)"""

        self.settings.set_quiz_limit(SettingsTestData.quiz_limit)
        sleep(SHORT_WAIT)

        # Edit Daily Pointz

        self.settings.set_daily_pointz_easy(SettingsTestData.daily_pointz_easy)
        sleep(SHORT_WAIT)

        self.settings.set_minus_pointz_easy(SettingsTestData.minus_pointz_easy)
        sleep(SHORT_WAIT)

        self.settings.set_daily_pointz_hard(SettingsTestData.daily_pointz_hard)
        sleep(SHORT_WAIT)

        self.settings.set_minus_pointz_hard(SettingsTestData.minus_pointz_hard)
        sleep(SHORT_WAIT)

        # Edit join pointz

        self.settings.set_join_pointz(SettingsTestData.join_pointz)
        sleep(SHORT_WAIT)

        # Edit referral pointz

        self.settings.set_referral_pointz(SettingsTestData.referral_pointz)
        sleep(SHORT_WAIT)

        # Edit recent winner count

        self.settings.set_recent_winner_count(SettingsTestData.winner_count)
        sleep(SHORT_WAIT)

        # Edit schedule expire days

        self.settings.set_schedule_expire(SettingsTestData.schedule_expire)
        sleep(SHORT_WAIT)

        # Set logo

        self.settings.setLogo(SettingsTestData.logo_path)
        sleep(SHORT_WAIT)
        self.settings.preview_logo()
        sleep(SHORT_WAIT)
        self.settings.close()
        time.sleep(5)
        self.settings.settings_save()
        sleep(SHORT_WAIT)

        # Define the expected success message
        success_message = 'Successfully updated'
        sleep(SHORT_WAIT)

        # Call the assertion function to validate update settings
        perform_assertion(self.driver, self.settings, self.logger, success_message, "test_edit_general")
