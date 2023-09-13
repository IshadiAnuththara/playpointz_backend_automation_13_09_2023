from pageObjects.BasePage import BasePage
from locators.categories_locators import CategoriesLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocators()
        self.locator = CommonLocators()

    def click_categories(self):
        self.click_element("hyperlink_categories_xpath", self.locators.hyperlink_categories_xpath)

    def click_create_category(self):
        self.click_element("button_create_category_xpath", self.locators.button_create_category_xpath)

    def set_create_category(self, category_name):
        self.send_keys_to_element(category_name, "input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_cancel(self):
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def edit_category(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)

    def set_edit_category(self, category_name):
        self.clear_fields("input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(category_name, "input_category_name_xpath", self.locators.input_category_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def search_category(self, category):
        self.send_keys_to_element(category, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_new_category(self, category_name):
        self.click_create_category()
        sleep(SHORT_WAIT)
        self.set_create_category(category_name)
        self.click_save()
        sleep(SHORT_WAIT)

    def edit_quiz_category(self, edit_name):
        self.edit_category()
        sleep(SHORT_WAIT)
        self.set_edit_category(edit_name)

    def search_quiz_category(self, category_name):
        self.search_category(category_name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()

    def create_category_without_fill_category_name_negative_testing(self):
        self.click_create_category()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_category_enter_exist_category_negative_testing(self, exist_category):
        self.click_create_category()
        sleep(SHORT_WAIT)
        self.set_create_category(exist_category)
        self.click_save()
