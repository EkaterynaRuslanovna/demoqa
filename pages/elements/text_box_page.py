from pages.base_page import BasePage
from locators.elements.text_box import TextBoxLocators
from generator.person_gen import generate_person


class TextBoxPage(BasePage):

    locators = TextBoxLocators()

    def fill_all_fields(self):
        person = next(generate_person())
        full_name = person.full_name
        email = person.email
        current_address = person.current_address
        permanent_address = person.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_output_fields(self):
        output_full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return output_full_name, output_email, output_current_address, output_permanent_address
