import time
import pyautogui
from utilities.helper import take_screenshot

SHORT_WAIT = 4
MEDIUM_WAIT = 8
LONG_WAIT = 10


def sleep(seconds):
    time.sleep(seconds)


def upload_image(image_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(image_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


def upload_video(video_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(video_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


def perform_login_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Login Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_login_scr.png")
        logger.error("*********  Login Test Failed *********")
        assert False


def perform_create_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_announcement_scr.png")
        logger.error("*********  Create Announcement Test Failed *********")
        assert False


def perform_edit_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_announcement_scr.png")
        logger.error("********* Edit announcement Test Failed *********")
        assert False


def perform_delete_announcement_assertion(driver, announcement_page, logger, success_message):
    if success_message in announcement_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete announcement Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_announcement_scr.png")
        logger.error("********* Delete announcement Test Failed *********")
        assert False


def perform_create_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Create campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_campaign_scr.png")
        logger.error("*********  Create campaign Test Failed *********")
        assert False


def perform_edit_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_campaign_scr.png")
        logger.error("********* Edit campaign Test Failed *********")
        assert False


def perform_delete_campaign_assertion(driver, campaign_page, logger, success_message):
    if success_message in campaign_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete campaign Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_campaign_scr.png")
        logger.error("********* Delete campaign Test Failed *********")
        assert False


def perform_ignore_complains_assertion(driver, complain_page, logger, success_message):
    if success_message in complain_page.retrieve_warning_message():
        assert True
        logger.info("********* Ignore complains Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_ignore_complains_scr.png")
        logger.error("********* Ignore Complains Test Failed *********")
        assert False


def perform_create_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new game Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_game_scr.png")
        logger.error("********* Create new game Test Failed *********")
        assert False


def perform_edit_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit game Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_game_scr.png")
        logger.error("********* Edit game Test Failed *********")
        assert False


def perform_delete_game_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete game Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_game_scr.png")
        logger.error("********* Delete game Test Failed *********")
        assert False


def perform_game_settings_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit setting Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_setting_scr.png")
        logger.error("********* Edit setting Test Failed *********")
        assert False


def perform_add_new_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Add new item Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_add_new_item_scr.png")
        logger.error("********* Add new item Test Failed *********")
        assert False


def perform_edit_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit item Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_item_scr.png")
        logger.error("********* Edit item Test Failed *********")
        assert False


def perform_delete_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete item Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_item_scr.png")
        logger.error("********* Delete item Test Failed *********")
        assert False


def perform_create_category_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Add new category Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_add_new_category_scr.png")
        logger.error("********* Add new category Test Failed *********")
        assert False


def perform_edit_category_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit category Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_category_scr.png")
        logger.error("********* Edit category Test Failed *********")
        assert False


def perform_create_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_schedule_scr.png")
        logger.error("********* Create new schedule Test Failed *********")
        assert False


def perform_edit_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_schedule_scr.png")
        logger.error("********* Edit schedule Test Failed *********")
        assert False


def perform_delete_scheduler_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_schedule_scr.png")
        logger.error("********* Delete schedule Test Failed *********")
        assert False


def perform_edit_orders_assertion(driver, order_page, logger, success_message):
    if success_message in order_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit orders Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_orders_scr.png")
        logger.error("********* Edit orders Test Failed *********")
        assert False


def perform_edit_brand_pages_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Brand pages Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_brand_pages_scr.png")
        logger.error("********* Edit Brand pages Test Failed *********")
        assert False


def perform_create_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_popup_banners_scr.png")
        logger.error("********* Create Pop-up Banners Test Failed *********")
        assert False


def perform_edit_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_popup_banners_scr.png")
        logger.error("********* Edit Pop-up Banners Test Failed *********")
        assert False


def perform_delete_popup_banners_assertion(driver, popup_banners_page, logger, success_message):
    if success_message in popup_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Pop-up Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_popup_banners_scr.png")
        logger.error("********* Delete Pop-up Banners Test Failed *********")
        assert False


def perform_create_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Push Notifications Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_push_notifications_scr.png")
        logger.error("********* Create Push Notifications Test Failed *********")
        assert False


def perform_edit_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Push Notifications Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_push_notifications_scr.png")
        logger.error("********* Edit Push Notifications Test Failed *********")
        assert False


def perform_resend_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Resend Notification Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_resend_notifications_scr.png")
        logger.error("********* Resend Notification Test Failed *********")
        assert False


def perform_delete_push_notifications_assertion(driver, push_notifications_page, logger, success_message):
    if success_message in push_notifications_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Notification Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_notifications_scr.png")
        logger.error("********* Delete Notification Test Failed *********")
        assert False


def perform_edit_player_block_status_block_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_block_status_unblock_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_purchase_block_status_block_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_edit_player_purchase_block_status_unblock_assertion(driver, player_management_page, logger,
                                                                success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit player Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_player_scr.png")
        logger.error("********* Edit player Test Failed *********")
        assert False


def perform_create_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Create quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_quiz_scr.png")
        logger.error("********* Create quiz Test Failed *********")
        assert False


def perform_edit_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_quiz_scr.png")
        logger.error("********* Edit quiz Test Failed *********")
        assert False


def perform_delete_quiz_assertion(driver, quiz_page, logger, success_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete quiz Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_quiz_scr.png")
        logger.error("********* Delete quiz Test Failed *********")
        assert False


def perform_reply_support_message_assertion(driver, player_support_page, logger, success_message):
    if success_message in player_support_page.retrieve_warning_message():
        assert True
        logger.info("********* player support Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_reply_support_message_scr.png")
        logger.error("********* player support Test Failed *********")
        assert False


def perform_create_store_banners_assertion(driver, store_banners_page, logger, success_message):
    if success_message in store_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Store Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_store_banners_scr.png")
        logger.error("********* Create Store Banners Test Failed *********")
        assert False


def perform_delete_store_banners_assertion(driver, store_banners_page, logger, success_message):
    if success_message in store_banners_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Store Banners Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_store_banners_scr.png")
        logger.error("********* Delete Store Banners Test Failed *********")
        assert False


def perform_add_new_user_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Add New Member Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_add_new_member_scr.png")
        logger.error("********* Add New Member Test Failed Test Failed *********")
        assert False


def perform_update_user_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Member Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_member_scr.png")
        logger.error("********* Edit Member Test Failed *********")
        assert False


def perform_add_new_user_role_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Add User Role Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_add_new_user_role_scr.png")
        logger.error("********* Add User Role Test Failed *********")
        assert False


def perform_edit_user_role_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit User Role Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_user_role_scr.png")
        logger.error("********* Edit User Role Test Failed *********")
        assert False


def perform_remove_permissions_assertion(driver, user_management_page, logger, success_message):
    if success_message in user_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Remove Permission Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_remove_permissions_scr.png")
        logger.error("********* Remove Permission Test Failed *********")
        assert False


def perform_create_new_quiz_category_assertion(driver, category_page, logger, success_message):
    if success_message in category_page.retrieve_warning_message():
        assert True
        logger.info("********* Create quiz category Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_quiz_category_scr.png")
        logger.error("********* Create quiz category Test Failed *********")
        assert False


def perform_edit_quiz_category_assertion(driver, category_page, logger, success_message):
    if success_message in category_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz category Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_quiz_category_scr.png")
        logger.error("********* Edit quiz category Test Failed *********")
        assert False


def perform_create_new_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_new_quiz_schedule_scr.png")
        logger.error("********* Create new quiz schedule Test Failed *********")
        assert False


def perform_edit_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_quiz_schedule_scr.png")
        logger.error("********* Edit quiz schedule Test Failed *********")
        assert False


def perform_delete_quiz_schedule_assertion(driver, schedule_page, logger, success_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete quiz schedule Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_quiz_schedule_scr.png")
        logger.error("********* Delete quiz schedule Test Failed *********")
        assert False


def perform_create_new_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Create Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_email_domain_scr.png")
        logger.error("********* Create Email Domain Test Failed *********")
        assert False


def perform_edit_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_email_domain_scr.png")
        logger.error("********* Edit Email Domain Test Failed *********")
        assert False


def perform_delete_email_domain_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete Email Domain Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_email_domain_scr.png")
        logger.error("********* Delete Email Domain Test Failed *********")
        assert False


def perform_delete_player_posts_assertion(driver, player_management_page, logger, success_message):
    if success_message in player_management_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete player posts Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_delete_player_posts_scr.png")
        logger.error("********* Delete player posts Test Failed *********")
        assert False


def perform_update_settings_assertion(driver, settings_page, logger, success_message):
    if success_message in settings_page.retrieve_warning_message():
        assert True
        logger.info("********* Update Settings Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_update_settings_scr.png")
        logger.error("********* Update Settings Test Failed *********")
        assert False


# def perform_create_game_negative_testing_assertion(driver, game_page, logger, success_message):
#     if success_message in game_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Create Game Negative Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_create_game_negative_test_scr.png")
#         logger.error("********* Create Game Negative Test Failed *********")
#         assert False


def perform_edit_game_negative_testing_assertion(driver, game_page, logger, success_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit Word Correction game Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_edit_game_negative_test_scr.png")
        logger.error("********* Edit Word Correction game Test Failed *********")
        assert False


# def perform_add_item_negative_testing_assertion(driver, item_page, logger, success_message):
#     if success_message in item_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Add new item - Negative Testing - Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_add_item_negative_test_scr.png")
#         logger.error("********* Add new item - Negative Testing - Test Failed *********")
#         assert False


# def perform_delete_item_exist_event_negative_testing_assertion(driver, item_page, logger, success_message):
#     if success_message in item_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Delete item - Negative Testing - Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_add_item_negative_test_scr.png")
#         logger.error("********* Delete item - Negative Testing - Test Failed *********")
#         assert False


# def perform_add_existing_item_negative_testing_assertion(driver, item_page, logger, success_message):
#     if success_message in item_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Add new item - Existing - Negative Testing - Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_add_item_existing_negative_test_scr.png")
#         logger.error("********* Add new item - Existing - Negative Testing - Test Failed *********")
#         assert False


def perform_create_scheduler_negative_testing_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new schedule - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_schedule_negative_test_scr.png")
        logger.error("********* Create new schedule - Negative Testing - Test Failed *********")
        assert False


def perform_create_popup_banners_negative_testing_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info("********* Create pop-up banners negative testing -  Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "test_create_popup_banners_negative_test_scr.png")
        logger.error("********* Create pop-up banners negative testing -  Test Failed *********")
        assert False


# def perform_create_quizzes_negative_testing_assertion(driver, quiz_page, logger, success_message):
#     if success_message in quiz_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Create quiz negative testing -  Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_create_quiz_negative_test_scr.png")
#         logger.error("********* Create quiz negative testing -  Test Failed *********")
#         assert False


# def perform_create_quiz_categories_negative_testing_assertion(driver, categories_page, logger, success_message):
#     if success_message in categories_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Create quiz categories negative testing -  Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_create_quiz_categories_negative_test_scr.png")
#         logger.error("********* Create quiz categories negative testing -  Test Failed *********")
#         assert False


# def perform_create_quiz_schedule_negative_testing_assertion(driver, schedule_page, logger, success_message):
#     if success_message in schedule_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Create quiz schedule negative testing -  Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_create_quiz_schedule_negative_test_scr.png")
#         logger.error("********* Create quiz schedule negative testing -  Test Failed *********")
#         assert False


# def perform_create_store_banners_negative_testing_assertion(driver, store_banners_page, logger, success_message):
#     if success_message in store_banners_page.retrieve_warning_message():
#         assert True
#         logger.info("********* Create Store banners negative testing -  Test Passed *********")
#     else:
#         take_screenshot(driver, ".\\Screenshots\\", "test_create_store_banners_negative_test_scr.png")
#         logger.error("********* Create Store banners negative testing -  Test Failed *********")
#         assert False


# NEW UPDATES


def perform_assertion(driver, page, logger, success_message, function_name):
    if success_message in page.retrieve_warning_message():
        assert True
        logger.info(f"********* Assertion for {function_name} Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{function_name.lower()}_scr.png")
        logger.error(f"********* Assertion for {function_name} Test Failed *********")
        assert False


def perform_login_with_invalid_credentials_assertion(driver, login_page, logger, success_message, unique_message):
    if success_message in login_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_create_game_negative_testing_assertion(driver, game_page, logger, success_message, unique_message):
    if success_message in game_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_add_item_negative_testing_assertion(driver, item_page, logger, success_message, unique_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_delete_item_exist_event_negative_testing_assertion(driver, item_page, logger, success_message,
                                                               unique_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_add_existing_item_negative_testing_assertion(driver, item_page, logger, success_message,  unique_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_create_quizzes_negative_testing_assertion(driver, quiz_page, logger, success_message, unique_message):
    if success_message in quiz_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_create_quiz_categories_negative_testing_assertion(driver, categories_page, logger, success_message,
                                                              unique_message):
    if success_message in categories_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_create_quiz_schedule_negative_testing_assertion(driver, schedule_page, logger, success_message,
                                                            unique_message):
    if success_message in schedule_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False


def perform_create_store_banners_negative_testing_assertion(driver, store_banners_page, logger, success_message,
                                                            unique_message):
    if success_message in store_banners_page.retrieve_warning_message():
        assert True
        logger.info(f"********* {unique_message} - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", f"{unique_message}_scr.png")
        logger.error(f"********* {unique_message} - Test Failed *********")
        assert False
