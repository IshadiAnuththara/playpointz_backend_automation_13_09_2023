from pageObjects.BasePage import BasePage
from locators.game_locators import GameLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class GamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = GameLocators()
        self.locator = CommonLocators()

    def click_games(self):
        self.click_element("hyperlink_game_xpath", self.locators.hyperlink_game_xpath)

    def click_finding_missing_character(self):
        self.click_element("hyperlink_missing_character_xpath", self.locators.hyperlink_missing_character_xpath)

    def click_word_correction(self):
        self.click_element("hyperlink_word_correction_xpath", self.locators.hyperlink_word_correction_xpath)

    def click_create_game(self):
        self.click_element("button_create_game_xpath", self.locators.button_create_game_xpath)

    def add_word(self, word):
        self.send_keys_to_element(word, "input_word_xpath", self.locators.input_word_xpath)

    def click_shuffle(self):
        self.click_element("button_shuffle_xpath", self.locators.button_shuffle_xpath)

    def add_plus_pointz(self, plus_pointz):
        self.send_keys_to_element(plus_pointz, "input_plus_pointz_xpath", self.locators.input_plus_pointz_xpath)

    def add_minus_pointz(self, minus_pointz):
        self.send_keys_to_element(minus_pointz, "input_minus_pointz_xpath", self.locators.input_minus_pointz_xpath)

    def click_option(self):
        self.click_element("option_easy_xpath", self.locators.option_easy_xpath)

    def click_add_answer(self):
        self.click_element("button_add_answers_xpath", self.locators.button_add_answers_xpath)

    def add_answers_1(self, answer_1):
        input1 = self.find_element("input_answer1_xpath", self.locators.input_answer1_xpath)
        current_value = input1.get_attribute("value")
        if not current_value:
            input1.send_keys(answer_1)
        else:
            print("Input field already has a value, no letter was entered.")

    def add_answers_2(self, answer_2):
        input2 = self.find_element("input_answer2_xpath", self.locators.input_answer2_xpath)
        current_value = input2.get_attribute("value")
        if not current_value:
            input2.send_keys(answer_2)
        else:
            print("Input field already has a value, no letter was entered.")

    def add_answers_3(self, answer_3):
        input3 = self.find_element("input_answer3_xpath", self.locators.input_answer3_xpath)
        current_value = input3.get_attribute("value")
        if not current_value:
            input3.send_keys(answer_3)
        else:
            print("Input field already has a value, no letter was entered.")

    def add_answers_4(self, answer_4):
        input4 = self.find_element("input_answer4_xpath", self.locators.input_answer4_xpath)
        current_value = input4.get_attribute("value")
        if not current_value:
            input4.send_keys(answer_4)
        else:
            print("Input field already has a value, no letter was entered.")

    def add_answer_1(self, answer_1):
        self.send_keys_to_element(answer_1, "input_answer_2_xpath", self.locators.input_answer_2_xpath)

    def click_status_option(self):
        self.click_element("option_status_xpath", self.locators.option_status_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_cancel(self):
        self.click_element("button_cancel_xpath", self.locators.button_cancel_xpath)

    def search_by_word(self, word):
        self.send_keys_to_element(word, "input_search_xpath", self.locators.input_search_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_difficulty(self):
        self.click_element("select_difficulty_xpath", self.locators.select_difficulty_xpath)

    def click_option_default(self):
        self.click_element("option_difficulty_Default_xpath", self.locators.option_difficulty_Default_xpath)

    def click_option_easy(self):
        self.click_element("option_difficulty_Easy_xpath", self.locators.option_difficulty_Easy_xpath)

    def click_option_hard(self):
        self.click_element("option_difficulty_Hard_xpath", self.locators.option_difficulty_Hard_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def click_edit(self):
        self.click_element("button_edit_game1_xpath", self.locators.button_edit_game1_xpath)

    def edit_plus_pointz(self, plus_pointz):
        self.clear_fields("input_plus_pointz_xpath", self.locators.input_plus_pointz_xpath)
        self.send_keys_to_element(plus_pointz, "input_plus_pointz_xpath", self.locators.input_plus_pointz_xpath)

    def edit_minus_pointz(self, minus_pointz):
        self.clear_fields("input_minus_pointz_xpath", self.locators.input_minus_pointz_xpath)
        self.send_keys_to_element(minus_pointz, "input_minus_pointz_xpath", self.locators.input_minus_pointz_xpath)

    def edit_active_status(self):
        self.click_element("option_status_inactive_xpath", self.locators.option_status_inactive_xpath)

    def delete_game(self):
        self.find_element("table_deleteRow_xpath", self.locators.table_deleteRow_xpath)
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_deleteAccept_xpath", self.locators.button_deleteAccept_xpath)

    def click_edit_2(self):
        self.find_element("table_row2_xpath", self.locators.table_row2_xpath)
        self.click_element("button_edit_game2_xpath", self.locators.button_edit_game2_xpath)

    def click_settings(self, minutes):
        self.click_element("button_settings_xpath", self.locators.button_settings_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_scheduleMinutes_xpath", self.locators.input_scheduleMinutes_xpath)
        self.send_keys_to_element(minutes, "input_scheduleMinutes_xpath", self.locators.input_scheduleMinutes_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_activeStatus_xpath", self.locators.option_activeStatus_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_update_xpath", self.locators.button_update_xpath)

    def click_edit_answered_game(self):
        self.click_element("button_edit_answeredGame_xpath", self.locators.button_edit_answeredGame_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locators.button_close_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def create_finding_missing_character_game(self, word, plus_points, minus_points, answer_1, answer_2, answer_3,
                                              answer_4):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answer_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answer_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_game(self, plus_points, minus_points):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.edit_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.edit_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.edit_active_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def search_and_refresh(self):
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def search_game(self, word):
        self.search_by_word(word)
        self.search_and_refresh()
        self.click_option_default()
        self.search_and_refresh()
        self.click_option_easy()
        self.search_and_refresh()
        self.click_option_hard()
        self.search_and_refresh()

    def create_word_correction_game(self, word, plus_pointz, minus_pointz):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_pointz)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_pointz)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_word_correction_game(self, plus_pointz, minus_pointz):
        self.click_edit_2()
        sleep(SHORT_WAIT)
        self.edit_plus_pointz(plus_pointz)
        sleep(SHORT_WAIT)
        self.edit_minus_pointz(minus_pointz)
        sleep(SHORT_WAIT)
        self.edit_active_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_duplicate_answers(self, word, plus_points, minus_points,
                                                                                 answer_1,
                                                                                 answer_2, answer_3, answer_4):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answer_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answer_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create__finding_missing_character_game_negative_testing_no_shuffle(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_not_add_answers(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_without_add_points(self, word, answers_1, answers_2,
                                                                                  answers_3,
                                                                                  answers_4):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answers_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answers_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answers_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answers_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_without_enter_minus_points(self, word, plus_points,
                                                                                          answers_1,
                                                                                          answers_2, answers_3,
                                                                                          answers_4):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answers_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answers_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answers_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answers_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_without_enter_plus_points(
            self, word, minus_points, answers_1, answers_2, answers_3, answers_4):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answers_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answers_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answers_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answers_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_without_select_game_level(
            self, word, plus_points, minus_points, answers_1, answers_2, answers_3, answers_4):

        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.add_answers_1(answers_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answers_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answers_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answers_4)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_finding_missing_character_game_negative_testing_without_select_status(
            self, word, plus_points, minus_points, answers_1, answers_2, answers_3, answers_4):

        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.add_answers_1(answers_1)
        sleep(SHORT_WAIT)
        self.add_answers_2(answers_2)
        sleep(SHORT_WAIT)
        self.add_answers_3(answers_3)
        sleep(SHORT_WAIT)
        self.add_answers_4(answers_4)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_duplicate_answers(self, word, plus_points, minus_points, answer_1):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_add_answer()
        sleep(SHORT_WAIT)
        self.add_answer_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_enter_numbers(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_enter_symbols(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_no_shuffle(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_without_plus_points(self, word, minus_point):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_point)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_without_minus_points(self, word, plus_point):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_point)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_without_points(self, word):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_only_fill_word_no_shuffle(self, word):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_only_fill_word_and_shuffle(self, word):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_word_correction_game_negative_testing_without_select_status(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_word_correction_game_negative_testing_edit_answered_game(self, plus_points, minus_points):
        self.click_edit_answered_game()
        sleep(SHORT_WAIT)
        self.edit_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.edit_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.edit_active_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_word_correction_game_negative_testing_create_exist_game(self, word, plus_points, minus_points):
        self.click_create_game()
        sleep(SHORT_WAIT)
        self.add_word(word)
        sleep(SHORT_WAIT)
        self.click_shuffle()
        sleep(SHORT_WAIT)
        self.add_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.add_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_option()
        sleep(SHORT_WAIT)
        self.click_status_option()
        sleep(SHORT_WAIT)
        self.click_save()
