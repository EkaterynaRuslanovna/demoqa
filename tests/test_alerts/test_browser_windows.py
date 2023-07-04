import allure
import pytest
from allure import severity_level
from allure_commons.types import AttachmentType


@allure.suite('Browser Windows')
class TestBrowserWindows:

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking the opening of a new tab')
    def test_new_tab(self, driver, browser_windows_page):
        text_result = browser_windows_page.check_opened_new_tab()

        assert text_result == 'This is a sample page', "the new tab has not opened or an incorrect tab has opened"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @pytest.mark.skip("Run separately")
    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking the opening of a new window')
    def test_new_window(self, driver, browser_windows_page):
        text_result = browser_windows_page.check_opened_new_tab()

        assert text_result == 'This is a sample page', "the new window has not opened or an incorrect window has opened"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

