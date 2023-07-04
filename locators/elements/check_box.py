from selenium.webdriver.common.by import By


class CheckBoxLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")

    CHECKED_ITEMS = (By.CSS_SELECTOR, "label:has(input:checked) > span.rct-title")

    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    TOGGLE = (By.CSS_SELECTOR, "button[class='rct-collapse rct-collapse-btn']")
    NESTED = (By.CSS_SELECTOR, "li[class='rct-node rct-node-parent rct-node-collapsed']")
