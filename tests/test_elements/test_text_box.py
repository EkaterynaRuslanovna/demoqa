import allure
from allure import severity_level
import pytest
from locators.elements.text_box import TextBoxLocators
from data.invalid_data import INVALID_EMAILS
from allure_commons.types import AttachmentType


@allure.story('Scope of tests "Text-Box page"')
class TestTextBox:

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking that all fields is filled')
    def test_fill_fields(self, driver, text_box_page):

        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_output_fields()

        assert full_name == output_full_name, f"Full name assertion failed. Expected: {full_name}, Actual: {output_full_name}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert email == output_email, f"Email assertion failed. Expected: {email}, Actual: {output_email}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert current_address == output_current_address, f"Current address assertion failed. Expected: {current_address}, Actual: {output_current_address}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert permanent_address == output_permanent_address, f"Permanent address assertion failed. Expected: {permanent_address}, Actual: {output_permanent_address}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that email error is displayed when emails are invalid')
    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
    def test_invalid_email(self, driver, text_box_page, invalid_email):

        text_box_page.element_is_visible(TextBoxLocators.EMAIL).send_keys(invalid_email)
        text_box_page.element_is_visible(TextBoxLocators.SUBMIT).click()

        assert text_box_page.element_is_present(TextBoxLocators.EMAIL_ERROR).is_displayed(), f"Email error is not displayed: {invalid_email}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.MINOR)
    @allure.description('Checking ability to change text area size')
    @pytest.mark.parametrize("text_area, test_name", [(TextBoxLocators.CURRENT_ADDRESS, "CURRENT_ADDRESS"),
                                                      (TextBoxLocators.PERMANENT_ADDRESS, "PERMANENT_ADDRESS")])
    def test_change_text_area_size(self, driver, text_box_page, text_area, test_name):

        textarea = text_box_page.element_is_visible(text_area)
        driver.execute_script("arguments[0].style.width = '600px'; arguments[0].style.height = '400px';", textarea)
        new_size = textarea.size

        assert new_size == {'height': 400, 'width': 600}, f"Text area size assertion failed for {test_name}. Expected: {'height': 400, 'width': 600}, Actual: {new_size}"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.MINOR)
    @allure.description('Checking page title')
    def test_title(self, driver, text_box_page):

        expected_title = "Text Box"
        actual_title = text_box_page.element_is_visible(TextBoxLocators.TITLE).text

        assert actual_title == expected_title, f"Title error. Expected: '{expected_title}', Actual: '{actual_title}'"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
