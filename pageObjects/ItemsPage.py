from pageObjects.BasePage import BasePage
from locators.item_locators import ItemsLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class ItemsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemsLocators
        self.locator = CommonLocators()

    def click_main_items(self):
        self.click_element("button_items_xpath", self.locators.button_items_xpath)

    def click_items(self):
        self.click_element("hyperlink_items_xpath", self.locators.hyperlink_items_xpath)

    def click_categories(self):
        self.click_element("hyperlink_categories_xpath", self.locators.hyperlink_categories_xpath)

    def click_scheduler(self):
        self.click_element("hyperlink_scheduler_xpath", self.locators.hyperlink_scheduler_xpath)

    def click_add_items(self):
        self.click_element("button_add_items_xpath", self.locators.button_add_items_xpath)

    def set_item_name(self, name):
        self.send_keys_to_element(name, "input_item_name_xpath", self.locators.input_item_name_xpath)

    def set_category(self):
        self.click_element("option_category_xpath", self.locators.option_category_xpath)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "paragraph_description_xpath", self.locators.paragraph_description_xpath)

    def set_active_status(self):
        self.click_element("option_active_status_xpath", self.locators.option_active_status_xpath)

    def set_stock(self, stock):
        self.send_keys_to_element(stock, "input_stock_xpath", self.locators.input_stock_xpath)

    def set_pointz(self, pointz):
        self.send_keys_to_element(pointz, "input_pointz_xpath", self.locators.input_pointz_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_page(self):
        self.click_element("hyperlink_page_xpath", self.locators.hyperlink_page_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def edit(self, pointz):
        self.click_element("input_pointz_xpath", self.locators.input_pointz_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_pointz_xpath", self.locators.input_pointz_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(pointz, "input_pointz_xpath", self.locators.input_pointz_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_delete_exist_event(self):
        self.click_element("button_delete_item_exist_event_xpath", self.locators.button_delete_item_exist_event_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def search_item(self, item):
        self.send_keys_to_element(item, "input_search_item_xpath", self.locators.input_search_item_xpath)

    def search_category_electronic(self):
        self.click_element("option_electronic_category_xpath", self.locators.option_electronic_category_xpath)

    def search_category_beauty(self):
        self.click_element("option_beauty_category_xpath", self.locators.option_beauty_category_xpath)

    def search_category_toys(self):
        self.click_element("option_toys_category_xpath", self.locators.option_toys_category_xpath)

    def search_category_game(self):
        self.click_element("option_game_category_xpath", self.locators.option_game_category_xpath)

    def search_category_food_drink(self):
        self.click_element("option_food_drink_category_xpath", self.locators.option_food_drink_category_xpath)

    def search_category_gadget(self):
        self.click_element("option_gadget_category_xpath", self.locators.option_gadget_category_xpath)

    def search_category_entertainment(self):
        self.click_element("option_entertainment_category_xpath", self.locators.option_entertainment_category_xpath)

    def search_category_health(self):
        self.click_element("option_health_category_xpath", self.locators.option_health_category_xpath)

    def search_category_special_days(self):
        self.click_element("option_special_days_xpath", self.locators.option_special_days_xpath)

    def search_category_travel(self):
        self.click_element("option_travel_xpath", self.locators.option_travel_xpath)

    def search_category_fashion(self):
        self.click_element("option_fashion_xpath", self.locators.option_fashion_xpath)

    def search_status_default(self):
        self.click_element("option_status_all_xpath", self.locators.option_status_all_xpath)

    def search_status_end(self):
        self.click_element("option_status_end_xpath", self.locators.option_status_end_xpath)

    def search_status_ongoing(self):
        self.click_element("option_status_ongoing_xpath", self.locators.option_status_ongoing_xpath)

    def search_status_pending(self):
        self.click_element("option_status_pending_xpath", self.locators.option_status_pending_xpath)

    def search_active_status_default(self):
        self.click_element("option_active_status_all_xpath", self.locators.option_active_status_all_xpath)

    def search_active_status_active(self):
        self.click_element("option_active_status_active_xpath", self.locators.option_active_status_active_xpath)

    def search_active_status_inactive(self):
        self.click_element("option_active_status_inactive_xpath", self.locators.option_active_status_inactive_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_create_category(self):
        self.click_element("button_create_category_xpath", self.locators.button_create_category_xpath)

    def create_category(self, name):
        self.send_keys_to_element(name, "input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)
        # self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def search_category(self, name):
        self.send_keys_to_element(name, "input_search_category_xpath", self.locators.input_search_category_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_search_category_xpath", self.locators.button_search_category_xpath)

    def click_new_scheduler(self):
        self.click_element("button_new_scheduler_xpath", self.locators.button_new_scheduler_xpath)

    def set_item_schedule(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locators.input_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_item_name_xpath", self.locators.span_item_name_xpath)
        sleep(SHORT_WAIT)

    def set_item_quantity(self, quantity):
        self.send_keys_to_element(quantity, "input_quantity_xpath", self.locators.input_quantity_xpath)

    def click_schedule_start_date(self):
        self.click_element("input_schedule_time_xpath", self.locators.input_schedule_time_xpath)

    def set_schedule_start_date(self):
        self.click_element("input_schedule_time_xpath", self.locators.input_schedule_time_xpath)
        sleep(SHORT_WAIT)
        self.click_element("tabledata_start_time_xpath", self.locators.tabledata_start_time_xpath)

    def set_schedule_end_date(self):
        self.click_element("tabledata_end_time_xpath", self.locators.tabledata_end_time_xpath)

    def set_schedule_start_hours(self):
        self.click_element("option_start_hour_xpath", self.locators.option_start_hour_xpath)

    def set_schedule_end_hours(self):
        self.click_element("option_end_hour_xpath", self.locators.option_end_hour_xpath)

    def set_schedule_start_minute(self):
        self.click_element("option_start_minute_xpath", self.locators.option_start_minute_xpath)

    def set_schedule_end_minute(self):
        self.click_element("option_end_minute_xpath", self.locators.option_end_minute_xpath)

    def set_active_end_date(self):
        self.click_element("input_active_end_time_xpath", self.locators.input_active_end_time_xpath)
        sleep(SHORT_WAIT)
        self.click_element("tabledata_active_end_date_xpath", self.locators.tabledata_active_end_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_active_end_hour_xpath", self.locators.option_active_end_hour_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_active_end_minute_xpath", self.locators.option_active_end_minute_xpath)

    def click_apply(self):
        self.click_element("button_apply_xpath", self.locators.button_apply_xpath)

    def click_apply1(self):
        self.click_element("button_apply1_xpath", self.locators.button_apply1_xpath)

    def edit_scheduler(self, quantity):
        self.click_element("div_edit_schedule_date_xpath", self.locators.div_edit_schedule_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_edit_schedule_xpath", self.locators.button_edit_schedule_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_quantity_xpath", self.locators.input_quantity_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(quantity, "input_quantity_xpath", self.locators.input_quantity_xpath)
        sleep(SHORT_WAIT)

    def delete_schedule(self):
        self.click_element("button_left_arrow_xpath", self.locators.button_left_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_left_arrow_xpath", self.locators.button_left_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_left_arrow_xpath", self.locators.button_left_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_left_arrow_xpath", self.locators.button_left_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_delete_schedule_date_xpath", self.locators.div_delete_schedule_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_delete_schedule_xpath", self.locators.button_delete_schedule_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def click_page2(self):
        self.click_element("hyperlink_page2_xpath", self.locators.hyperlink_page2_xpath)

    def edit_categories(self, categoryName):
        self.click_element("button_edit_categories_xpath", self.locators.button_edit_categories_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(categoryName, "input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def select_image_item(self):
        self.perform_click_and_image_upload("button_upload_image_xpath",
                                            self.locators.button_upload_image_xpath, self.locators.image_item_path)

    def select_image_categories(self):
        self.perform_click_and_image_upload("button_upload_image_xpath", self.locators.button_upload_image_xpath,
                                            self.locators.image_category_path)

    def click_advanced_search(self):
        self.click_element("button_advanced_search_xpath", self.locators.button_advanced_search_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def add_new_item(self, item_name, desc, stock, pointz):
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_stock(stock)
        sleep(SHORT_WAIT)
        self.set_pointz(pointz)
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def search_items(self, item_name):
        self.search_item(item_name)
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_electronic()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_beauty()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_toys()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_food_drink()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_entertainment()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_gadget()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_health()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_special_days()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_travel()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_category_fashion()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_status_default()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_status_end()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_status_ongoing()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_status_pending()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_active_status_default()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_active_status_active()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_active_status_inactive()
        self.search_and_refresh()
        sleep(SHORT_WAIT)
        self.click_advanced_search()
        sleep(SHORT_WAIT)
        self.search_and_refresh()

    def edit_items(self, pointz):
        self.click_page()
        sleep(SHORT_WAIT)
        self.click_edit()
        sleep(SHORT_WAIT)
        self.edit(pointz)
        sleep(SHORT_WAIT)
        self.click_save()

    def delete_item(self, item):
        self.search_item(item)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_delete()

    def create_new_category(self, name):
        self.click_create_category()
        sleep(SHORT_WAIT)
        self.create_category(name)
        sleep(SHORT_WAIT)
        self.select_image_categories()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_category(self, name):
        self.click_page2()
        sleep(SHORT_WAIT)
        self.edit_categories(name)
        sleep(SHORT_WAIT)

    def search_categories(self, name):
        self.search_category(name)
        sleep(SHORT_WAIT)
        self.click_refresh()

    def create_new_schedule(self, name, quantity):
        self.click_new_scheduler()
        sleep(SHORT_WAIT)
        self.set_item_schedule(name)
        sleep(SHORT_WAIT)
        self.set_item_quantity(quantity)
        sleep(SHORT_WAIT)
        self.set_schedule_start_date()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date()
        sleep(SHORT_WAIT)
        self.set_schedule_start_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_start_minute()
        sleep(SHORT_WAIT)
        self.set_schedule_end_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_end_minute()
        sleep(SHORT_WAIT)
        self.click_apply()
        sleep(SHORT_WAIT)
        self.set_active_end_date()
        sleep(SHORT_WAIT)
        self.click_apply1()
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def edit_schedule(self, quantity):
        self.edit_scheduler(quantity)
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def add_item_negative_testing(self, item_name):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_without_stock_negative_testing(self, item_name, description):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_only_fill_item_name_negative_testing(self, item_name):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_without_enter_category_negative_testing(self, item_name, description, stock, points):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_stock(stock)
        sleep(SHORT_WAIT)
        self.set_pointz(points)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_without_enter_status_negative_testing(self, item_name, description, stock, points):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_stock(stock)
        sleep(SHORT_WAIT)
        self.set_pointz(points)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_without_enter_points_negative_testing(self, item_name, description, stock):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_stock(stock)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_without_enter_stock_negative_testing(self, item_name, description, points):
        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_pointz(points)
        sleep(SHORT_WAIT)
        self.click_save()

    def add_item_existing_negative_testing(self, item_name, description, stock, points):

        self.click_add_items()
        sleep(SHORT_WAIT)
        self.set_item_name(item_name)
        sleep(SHORT_WAIT)
        self.set_category()
        sleep(SHORT_WAIT)
        self.set_description(description)
        sleep(SHORT_WAIT)
        self.set_active_status()
        sleep(SHORT_WAIT)
        self.select_image_item()
        sleep(SHORT_WAIT)
        self.set_stock(stock)
        sleep(SHORT_WAIT)
        self.set_pointz(points)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_scheduler_negative_testing_only_enter_name(self, item_name):
        self.click_new_scheduler()
        sleep(SHORT_WAIT)
        self.set_item_schedule(item_name)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_scheduler_negative_testing_without_end_time(self, item_name, item_quantity):
        self.click_new_scheduler()
        sleep(SHORT_WAIT)
        self.set_item_schedule(item_name)
        sleep(SHORT_WAIT)
        self.set_item_quantity(item_quantity)
        sleep(SHORT_WAIT)
        self.set_schedule_start_date()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date()
        sleep(SHORT_WAIT)
        self.set_schedule_start_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_start_minute()
        sleep(SHORT_WAIT)
        self.set_schedule_end_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_end_minute()
        sleep(SHORT_WAIT)
        self.click_apply()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_scheduler_negative_testing_quantity_exceed(self, item_name, item_quantity):
        self.click_new_scheduler()
        sleep(SHORT_WAIT)
        self.set_item_schedule(item_name)
        sleep(SHORT_WAIT)
        self.set_item_quantity(item_quantity)
        sleep(SHORT_WAIT)
        self.set_schedule_start_date()
        sleep(SHORT_WAIT)
        self.set_schedule_end_date()
        sleep(SHORT_WAIT)
        self.set_schedule_start_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_start_minute()
        sleep(SHORT_WAIT)
        self.set_schedule_end_hours()
        sleep(SHORT_WAIT)
        self.set_schedule_end_minute()
        sleep(SHORT_WAIT)
        self.click_apply()
        sleep(SHORT_WAIT)
        self.set_active_end_date()
        sleep(SHORT_WAIT)
        self.click_apply1()
        sleep(SHORT_WAIT)
        self.click_save()
