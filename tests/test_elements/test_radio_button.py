import pytest
import allure
from allure_commons.types import AttachmentType
from allure import severity_level


@allure.story('Scope of tests "Radio button page"')
class TestRadioButton:

    @pytest.mark.skip("There is a bug with button 'no'")
    @allure.severity(severity_level.BLOCKER)
    def test_radio_button(self, driver, radio_button_page):

        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()

        assert output_yes == 'Yes', "'Yes' have not been selected"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert output_impressive == 'Impressive', "'Impressive' have not been selected"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert output_no == "No", "'No' have not been selected"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

