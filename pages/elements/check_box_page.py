import random
from pages.base_page import BasePage
from locators.elements.check_box import CheckBoxLocators


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            data.append(box.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()

    def expand_all_checkboxes(self, parent_locator):
        expand_button = self.element_is_visible(parent_locator)
        expand_button.click()

        nested_expand_buttons = self.elements_are_visible(self.locators.NESTED_EXPAND_BUTTONS)
        for button in nested_expand_buttons:
            self.expand_all_checkboxes(button)