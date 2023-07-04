from selenium.webdriver.common.by import By


class TextBoxLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    EMAIL_ERROR = (By.CSS_SELECTOR, "input[class ='mr-sm-2 field-error form-control']")
    TITLE = (By.CSS_SELECTOR, "div[class ='main-header']")
