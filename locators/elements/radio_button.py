from selenium.webdriver.common.by import By


class RadioButtonLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')

    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')
