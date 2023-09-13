from pageObjects.BasePage import BasePage
from locators.quiz_locators import QuizPageLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, LONG_WAIT


class QuizPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = QuizPageLocators
        self.locator = CommonLocators

    def click_quizzes(self):
        self.click_element("button_normal_quiz_xpath", self.locators.button_normal_quiz_xpath)

    def click_normal_quiz_pool(self):
        self.click_element("hyperlink_quiz_pool_xpath", self.locators.hyperlink_quiz_pool_xpath)

    def click_single_quiz(self):
        self.click_element("button_single_quiz_xpath", self.locators.button_single_quiz_xpath)
        sleep(SHORT_WAIT)

    def click_single_quiz_pool(self):
        self.click_element("hyperlink_quiz_pool_2_xpath", self.locators.hyperlink_quiz_pool_2_xpath)

    def click_create_quiz(self):
        self.click_element("button_create_quiz_xpath", self.locators.button_create_quiz_xpath)

    def set_quiz_name(self, quiz_name):
        self.send_keys_to_element(quiz_name, "input_quiz_name_xpath", self.locators.input_quiz_name_xpath)

    def set_plus_pointz(self, plus_pointz):
        self.send_keys_to_element(plus_pointz, "input_plus_points_xpath", self.locators.input_plus_points_xpath)

    def set_minus_pointz(self, minus_pointz):
        self.send_keys_to_element(minus_pointz, "input_minus_points_xpath", self.locators.input_minus_points_xpath)

    def click_scheduled_quiz(self):
        self.click_element("input_scheduled_quiz_xpath", self.locators.input_scheduled_quiz_xpath)

    def click_sponsor_quiz(self):
        self.click_element("input_sponsor_xpath", self.locators.input_sponsor_xpath)

    def click_quiz_type(self):
        self.click_element("option_image_xpath", self.locators.option_image_xpath)
        sleep(SHORT_WAIT)

    def click_upload_image(self):
        self.click_element("button_upload_image_xpath", self.locators.button_upload_image_xpath)

    def click_upload_video(self):
        self.click_element("option_video_xpath", self.locators.option_video_xpath)

    def set_text_area(self, textarea):
        self.send_keys_to_element(textarea, "textarea_description_xpath", self.locators.textarea_description_xpath)

    def set_quiz_category(self, quiz_category):
        self.send_keys_to_element(quiz_category, "input_quiz_category_xpath", self.locators.input_quiz_category_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_computer_science_xpath", self.locators.button_computer_science_xpath)

    def click_quiz_level(self):
        self.click_element("option_easy_xpath", self.locators.option_easy_xpath)

    def click_answers(self):
        self.click_element("button_add_answer_xpath", self.locators.button_add_answer_xpath)

    def set_answers_1(self, answer_1):
        self.send_keys_to_element(answer_1, "input_answer_1_xpath", self.locators.input_answer_1_xpath)
        sleep(4)
        self.click_element("option_correct_answer_xpath", self.locators.option_correct_answer_xpath)

    def set_answers_without_click_correct(self, answer_1):
        self.send_keys_to_element(answer_1, "input_answer_1_xpath", self.locators.input_answer_1_xpath)

    def set_answers_2(self, answer_2):
        self.send_keys_to_element(answer_2, "input_answer_2_xpath", self.locators.input_answer_2_xpath)

    def set_answers_2_correct(self, answer_2):
        self.send_keys_to_element(answer_2, "input_answer_2_xpath", self.locators.input_answer_2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_correct_answer_xpath", self.locators.option_correct_answer_xpath)

    def set_answers_3(self, answer_3):
        self.send_keys_to_element(answer_3, "input_answer_3_xpath", self.locators.input_answer_3_xpath)

    def set_answers_4(self, answer_4):
        self.send_keys_to_element(answer_4, "input_answer_4_xpath", self.locators.input_answer_4_xpath)

    def click_status(self):
        self.click_element("option_status_xpath", self.locators.option_status_xpath)

    def click_approve(self):
        self.click_element("option_approve_xpath", self.locators.option_approve_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators.button_save_xpath)

    def click_edit(self):
        self.click_element("button_edit_xpath", self.locators.button_edit_xpath)
        sleep(SHORT_WAIT)

    def set_edit_quiz_plus_pointz(self, plus_pointz):
        self.clear_fields("input_plus_points_xpath", self.locators.input_plus_points_xpath)
        self.send_keys_to_element(plus_pointz, "input_plus_points_xpath", self.locators.input_plus_points_xpath)

    def set_edit_quiz_minus_pointz(self, minus_pointz):
        self.clear_fields("input_minus_points_xpath", self.locators.input_minus_points_xpath)
        self.send_keys_to_element(minus_pointz, "input_minus_points_xpath", self.locators.input_minus_points_xpath)
        self.click_element("button_update_xpath", self.locators.button_update_xpath)

    def click_delete(self):
        self.click_element("button_delete_xpath", self.locators.button_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators.button_accept_delete_xpath)

    def search_quiz(self, quiz):
        self.send_keys_to_element(quiz, "input_search_quiz_xpath", self.locators.input_search_quiz_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def search_quiz_edit(self, quiz):
        self.send_keys_to_element(quiz, "input_search_quiz_xpath", self.locators.input_search_quiz_xpath)
        sleep(SHORT_WAIT)

    def search_difficulty_default(self):
        self.click_element("option_difficulty_default_xpath", self.locators.option_difficulty_default_xpath)

    def search_difficulty_easy(self):
        self.click_element("option_difficulty_easy_xpath", self.locators.option_difficulty_easy_xpath)

    def search_difficulty_hard(self):
        self.click_element("option_difficulty_hard_xpath", self.locators.option_difficulty_hard_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locators.button_search_xpath)

    def click_refresh(self):
        self.click_element("button_refresh_xpath", self.locators.button_refresh_xpath)

    def select_image(self):
        self.perform_click_and_image_upload("button_upload_image_xpath",
                                            self.locators.button_upload_image_xpath, self.locators.image_path)

    def click_quiz_type_video(self):
        self.click_element("option_video_xpath", self.locators.option_video_xpath)

    def select_video(self, video_path):
        self.send_keys_to_element(video_path, "input_upload_video_xpath", self.locators.input_upload_video_xpath)

    def click_quiz_type_youtube_video(self):
        self.click_element("option_youtube_video_xpath", self.locators.option_youtube_video_xpath)

    def set_youtube_video(self, video_link):
        self.send_keys_to_element(video_link, "input_youtube_video_xpath", self.locators.input_youtube_video_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locator.notification_xpath)

    def search_and_refresh(self):
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_refresh()
        sleep(SHORT_WAIT)

    def create_image_type_single_quiz(self, quiz_name, plus_points, minus_points, desc, category, answer_1, answer_2,
                                      answer_3, answer_4):
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(quiz_name)
        sleep(SHORT_WAIT)
        self.set_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_sponsor_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(LONG_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_video_type_single_quiz(self, quiz_name, plus_points, minus_points, video_path, desc, category, ans_1,
                                      ans_2, ans_3, ans_4):
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_sponsor_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type_video()
        sleep(LONG_WAIT)
        self.select_video(video_path)
        self.set_text_area(desc)
        self.set_quiz_category(category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(ans_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(ans_2)
        self.click_answers()
        self.set_answers_3(ans_3)
        self.click_answers()
        self.set_answers_4(ans_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_youtube_video_type_single_quiz(self, quiz_name, plus_points, minus_points, video_path, desc, category,
                                              ans_1, ans_2, ans_3, ans_4):
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_sponsor_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type_youtube_video()
        sleep(LONG_WAIT)
        self.set_youtube_video(video_path)
        self.set_text_area(desc)
        self.set_quiz_category(category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(ans_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(ans_2)
        self.click_answers()
        self.set_answers_3(ans_3)
        self.click_answers()
        self.set_answers_4(ans_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def search_quizzes(self, quiz_name):
        self.search_quiz(quiz_name)
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.search_difficulty_default()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.search_difficulty_easy()
        sleep(SHORT_WAIT)
        self.search_and_refresh()
        self.search_difficulty_hard()
        sleep(SHORT_WAIT)
        self.search_and_refresh()

    def edit_single_quiz(self, quiz_name, plus_points, minus_points):
        self.search_quiz_edit(quiz_name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_edit_quiz_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_edit_quiz_minus_pointz(minus_points)

    def delete_quiz(self, quiz_name):
        self.search_quiz_edit(quiz_name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_delete()

    def create_image_type_normal_quiz(self, quiz_name, plus_points, minus_points, description, quiz_category, answer_1,
                                      answer_2, answer_3, answer_4):
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(LONG_WAIT)
        self.select_image()
        sleep(LONG_WAIT)
        self.set_text_area(description)
        self.set_quiz_category(quiz_category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_text_type_normal_quiz(self, quiz_name, plus_points, minus_points, desc, category, ans_1,
                                     ans_2, ans_3, ans_4):
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(ans_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(ans_2)
        self.click_answers()
        self.set_answers_3(ans_3)
        self.click_answers()
        self.set_answers_4(ans_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_video_type_normal_quiz(self, quiz_name, plus_points, minus_points, video_path, desc, category, ans_1,
                                      ans_2, ans_3, ans_4):
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type_video()
        sleep(LONG_WAIT)
        self.select_video(video_path)
        sleep(LONG_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(ans_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(ans_2)
        self.click_answers()
        self.set_answers_3(ans_3)
        self.click_answers()
        self.set_answers_4(ans_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_youtube_video_type_normal_quiz(self, quiz_name, plus_points, minus_points, video_path, desc,
                                              category, ans_1, ans_2, ans_3, ans_4):
        self.set_quiz_name(quiz_name)
        self.set_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type_youtube_video()
        sleep(LONG_WAIT)
        self.set_youtube_video(video_path)
        sleep(LONG_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(ans_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(ans_2)
        self.click_answers()
        self.set_answers_3(ans_3)
        self.click_answers()
        self.set_answers_4(ans_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_normal_quiz(self, quiz_name, plus_points, minus_points):
        self.search_quiz_edit(quiz_name)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        self.click_edit()
        sleep(SHORT_WAIT)
        self.set_edit_quiz_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.set_edit_quiz_minus_pointz(minus_points)
        sleep(SHORT_WAIT)

    def create_quiz_without_enter_any_field_negative_testing(self):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_add_answers_negative_testing(self, answer_1, answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_add_wrong_answers_negative_testing(self, answer_1, answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_without_click_correct(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_enter_category_negative_testing(self, category):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_enter_description_negative_testing(self, desc):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_enter_minus_points_negative_testing(self, minus_points):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_minus_pointz(minus_points)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_enter_plus_points_negative_testing(self, plus_points):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_plus_pointz(plus_points)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_enter_quiz_name_negative_testing(self, quiz_name):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(quiz_name)
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_only_select_quiz_level_negative_testing(self):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)

    def create_quiz_without_enter_description_negative_testing(self, name, plus_points, minus_points, category,
                                                               answer_1, answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(MEDIUM_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_quiz_category(category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_without_select_approval_negative_testing(self, name, plus_points, minus_points, desc, category,
                                                             answer_1, answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(MEDIUM_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_without_select_quiz_level_negative_testing(self, name, plus_points, minus_points, desc, category,
                                                               answer_1, answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(MEDIUM_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.set_quiz_category(category)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_without_select_quiz_category_negative_testing(self, name, plus_points, minus_points, desc, answer_1,
                                                                  answer_2, answer_3, answer_4):
        self.click_quizzes()
        sleep(SHORT_WAIT)
        self.click_normal_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_scheduled_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(MEDIUM_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_text_area(desc)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_save()

    def create_quiz_existing_quiz_negative_testing(self, name, plus_points, minus_points, desc, category, answer_1,
                                                   answer_2, answer_3, answer_4):
        self.click_single_quiz()
        sleep(SHORT_WAIT)
        self.click_single_quiz_pool()
        sleep(SHORT_WAIT)
        self.click_create_quiz()
        sleep(SHORT_WAIT)
        self.set_quiz_name(name)
        self.set_plus_pointz(plus_points)
        self.set_minus_pointz(minus_points)
        self.click_sponsor_quiz()
        sleep(SHORT_WAIT)
        self.click_quiz_type()
        sleep(MEDIUM_WAIT)
        self.select_image()
        sleep(MEDIUM_WAIT)
        self.set_text_area(desc)
        self.set_quiz_category(category)
        self.click_quiz_level()
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_1(answer_1)
        sleep(SHORT_WAIT)
        self.click_answers()
        self.set_answers_2(answer_2)
        self.click_answers()
        self.set_answers_3(answer_3)
        self.click_answers()
        self.set_answers_4(answer_4)
        sleep(SHORT_WAIT)
        self.click_status()
        sleep(SHORT_WAIT)
        self.click_approve()
        sleep(SHORT_WAIT)
        self.click_save()



