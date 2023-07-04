import allure
from allure import severity_level
from allure_commons.types import AttachmentType


@allure.story('Scope of tests "Check-Box page"')
class TestCheckBox:

    @allure.severity(severity_level.BLOCKER)
    @allure.description('Checking that checkboxes have been selected')
    def test_check_box(self, driver, check_box_page):

        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()

        assert input_checkbox == output_result, 'Checkboxes have not been selected'
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

