from locators.common_locators import CommonLocators
from locators.quiz_scheduler_locators import SchedulePageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class SchedulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SchedulePageLocators()
        self.locator = CommonLocators()

    def click_normal_quiz_scheduler(self):
        self.click_element("hyperlink_normal_quiz_scheduler_xpath", self.locators.hyperlink_normal_quiz_scheduler_xpath)

    def click_single_quiz_scheduler(self):
        self.click_element("hyperlink_single_quiz_scheduler_xpath", self.locators.hyperlink_single_quiz_scheduler_xpath)

    def click_date(self):
        self.click_element("div_edit_xpath", self.locators.div_edit_xpath)

    def click_edit_schedule(self):
        self.click_element("button_edit_schedule_xpath", self.locators.button_edit_schedule_xpath)

    def edit_schedule(self):
        self.click_element("option_hard_xpath", self.locators.option_hard_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_clear(self):
        self.click_element("button_clear_xpath", self.locators.button_clear_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def click_left_arrow(self):
        self.click_element("arrow_left_xpath", self.locators.arrow_left_xpath)

    def click_day_delete(self):
        self.click_element("div_edit_xpath", self.locators.div_edit_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_cancel(self):
        self.click_element("div_day_grid_delete_xpath", self.locators.div_day_grid_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_reject_delete_xpath", self.locators.button_reject_delete_xpath)

    def click_new_schedule(self):
        self.click_element("button_new_scheduler_xpath", self.locators.button_new_scheduler_xpath)
        sleep(SHORT_WAIT)

    def set_quiz_category(self, category):
        self.send_keys_to_element(category, "input_quiz_category_xpath", self.locators.input_quiz_category_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_quiz_category_xpath", self.locators.span_quiz_category_xpath)

    def set_quiz_level(self):
        self.click_element("option_hard_xpath", self.locators.option_hard_xpath)

    def set_schedule_start_date(self):
        self.click_element("input_schedule_time_xpath", self.locators.input_schedule_time_xpath)
        sleep(SHORT_WAIT)
        self.click_element("table_data_start_time_xpath", self.locators.table_data_start_time_xpath)

    def set_schedule_end_date(self):
        self.click_element("table_data_end_time_xpath", self.locators.table_data_end_time_xpath)

    def set_schedule_start_hours(self):
        self.click_element("option_start_hour_xpath", self.locators.option_start_hour_xpath)

    def set_schedule_end_hours(self):
        self.click_element("option_end_hour_xpath", self.locators.option_end_hour_xpath)

    def click_apply(self):
        self.click_element("button_apply_xpath", self.locators.button_apply_xpath)

    def set_quiz_name(self, name):
        self.send_keys_to_element(name, "input_quiz_name_xpath", self.locators.input_quiz_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_quiz_name_xpath", self.locators.span_quiz_name_xpath)
        sleep(MEDIUM_WAIT)

    def set_single_quiz_schedule_time(self):
        self.click_element("input_single_quiz_xpath", self.locators.input_single_quiz_xpath)

    def click_previous(self):
        self.click_element("table_heading_previous_xpath", self.locators.table_heading_previous_xpath)

    def click_next(self):
        self.click_element("table_heading_next_xpath", self.locators.table_heading_next_xpath)

    def schedule_date(self):
        self.click_element("table_data_single_quiz_start_date_xpath",
                           self.locators.table_data_single_quiz_start_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("table_data_single_quiz_end_date_xpath", self.locators.table_data_single_quiz_end_date_xpath)

    def set_time(self):
        self.click_element("option_single_quiz_start_hour_xpath", self.locators.option_single_quiz_start_hour_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_single_quiz_start_minute_xpath", self.locators.option_single_quiz_start_minute_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_typography_pm_xpath", self.locators.option_typography_pm_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_single_quiz_end_hour_xpath", self.locators.option_single_quiz_end_hour_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_single_quiz_end_minute_xpath", self.locators.option_single_quiz_end_minute_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_typography_am_xpath", self.locators.option_typography_am_xpath)

    def set_edit_quiz_level(self):
        quizLevel = self.find_element("select_quiz_level_xpath", self.locators.select_quiz_level_xpath)
        if quizLevel == 'Hard':
            self.click_element("option_quiz_level_easy_xpath", self.locators.option_quiz_level_easy_xpath)
        else:
            self.click_element("option_quiz_level_hard_xpath", self.locators.option_quiz_level_hard_xpath)

    def delete_quiz_scheduler(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_new_schedule_single_quiz(self, category):
        self.click_new_schedule()
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.set_quiz_level()
        sleep(SHORT_WAIT)
        self.set_schedule_start_date()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date()
        sleep(SHORT_WAIT)
        self.set_schedule_start_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_end_hours()
        sleep(SHORT_WAIT)
        self.click_apply()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_quiz_schedule_single_quiz(self):
        self.click_date()
        sleep(SHORT_WAIT)
        self.click_edit_schedule()
        sleep(SHORT_WAIT)
        # self.editSchedule()
        self.set_edit_quiz_level()
        sleep(SHORT_WAIT)
        self.click_save()

    def delete_quiz_schedule_single_quiz(self):
        sleep(SHORT_WAIT)
        self.click_date()
        sleep(MEDIUM_WAIT)
        self.delete_quiz_scheduler()

    def create_new_schedule_normal_quiz(self, name):
        self.click_new_schedule()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        sleep(SHORT_WAIT)
        self.set_single_quiz_schedule_time()
        sleep(SHORT_WAIT)
        self.click_previous()
        sleep(SHORT_WAIT)
        self.click_next()
        sleep(SHORT_WAIT)
        self.schedule_date()
        sleep(SHORT_WAIT)
        self.set_time()
        self.click_apply()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_schedule_normal_quiz(self):
        self.click_date()
        sleep(SHORT_WAIT)
        self.click_edit_schedule()
        sleep(SHORT_WAIT)
        self.set_single_quiz_schedule_time()
        sleep(SHORT_WAIT)
        self.click_previous()
        sleep(SHORT_WAIT)
        self.click_next()
        sleep(SHORT_WAIT)
        self.schedule_date()
        sleep(SHORT_WAIT)
        self.set_time()
        self.click_apply()
        sleep(SHORT_WAIT)
        self.click_save()

    def delete_schedule_normal_quiz(self):
        self.click_date()
        sleep(SHORT_WAIT)
        self.delete_quiz_scheduler()
        sleep(SHORT_WAIT)

    def create_quiz_schedule_without_fill_any_field_negative_testing(self):
        self.click_new_schedule()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_schedule_only_enter_quiz_category_negative_testing(self, category):
        self.click_new_schedule()
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_schedule_without_enter_start_time(self, category):
        self.click_new_schedule()
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.set_quiz_level()
        sleep(SHORT_WAIT)
        self.click_save()
