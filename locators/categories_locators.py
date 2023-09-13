class CategoriesLocators:
    hyperlink_categories_xpath = "//a[normalize-space()='Quiz Categories']"
    button_create_category_xpath = "//button[normalize-space()='Create category']"
    input_category_name_xpath = "//*[@id='cat-name']"
    button_save_xpath = "//button[normalize-space()='Save']"
    button_cancel_xpath = "//div[@class='modal-footer']//button[@type='button'][normalize-space()='Cancel']"
    button_edit_xpath = "//body[1]/play-pointz-root[1]/play-pointz-layout[1]/main[1]/div[" \
                        "1]/play-pointz-quiz-categories[1]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/button[1]"
    input_search_xpath = "//input[@placeholder='Search category']"
    button_search_xpath = "(//button[@type='submit'])[2]"
    button_refresh_xpath = "(//button[@type='button'])[10]"
