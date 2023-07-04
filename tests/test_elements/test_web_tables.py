import random
import pytest
import allure
from allure_commons.types import AttachmentType
from allure import severity_level


@allure.story('Scope of tests "Web table page"')
class TestWebTable:

    @allure.severity(severity_level.CRITICAL)
    def test_web_table_add_person(self, driver, web_table_page):

        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()

        assert new_person in table_result
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.BLOCKER)
    def test_web_table_search_person(self, driver, web_table_page):

        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()

        assert key_word in table_result, "the person was not found in the table"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.BLOCKER)
    def test_web_table_update_person_info(self, driver, web_table_page):

        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()

        assert age in row, "the person card has not been changed"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    def test_web_table_delete_person(self, driver,  web_table_page):

        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()

        assert text == "No rows found"
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @pytest.mark.skip("There is a bug with footer for 25, 50, 100 options")
    @allure.severity(severity_level.NORMAL)
    def test_web_table_change_count_row(self, driver, web_table_page):

        count = web_table_page.select_up_to_some_rows()

        assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has changed incorrectly'
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
