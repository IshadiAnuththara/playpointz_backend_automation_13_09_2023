class OrderShippingLocators:
    hyperlink_order_shipping_xpath = "//a[normalize-space()='Orders and shipping']"
    input_search_xpath = "//input[@name='search']"
    button_search_xpath = "//button[normalize-space()='Search']"
    input_start_date_xpath = "//input[@title='Date from']"
    input_end_date_xpath = "//input[@title='Date to']"
    button_refresh_xpath = "(//button[@class='btn btn-search-sub ms-2 rounded_'])[1]"
    select_status_xpath = "(//select[@id='status'])[2]"
    option_placed_xpath = "(//option[@value='Placed'][normalize-space()='Placed'])[2]"
    option_processing_xpath = "(//option[@value='Processing'][normalize-space()='Processing'])[2]"
    option_shipped_xpath = "(//option[@value='Shipped'][normalize-space()='Shipped'])[2]"
    option_delivered_xpath = "(//option[@value='Delivered'][normalize-space()='Delivered'])[2]"
    button_edit_xpath = "(//button[@data-bs-toggle='modal'])[8]"
    hyperlink_page_xpath = "//a[normalize-space()='13']"
    button_export_xpath = "//button[normalize-space()='Export']"
    button_save_xpath = "//button[@type='submit'][normalize-space()='Save']"
    option_delivered_edit_xpath = "(//option[@value='Delivered'][normalize-space()='Delivered'])[1]"
    option_shipped_edit_xpath = "(//option[@value='Shipped'][normalize-space()='Shipped'])[1]"
    button_advanced_filter_xpath = "//button[normalize-space()='Advanced Filters']"
