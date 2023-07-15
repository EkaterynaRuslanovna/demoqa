import pytest
from selenium import webdriver
from pages.elements.text_box_page import TextBoxPage
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.radio_button_page import PadioButtonPage
from pages.elements.web_table_page import WebTablePage
from pages.alerts.browser_windows_page import BrowserWindowsPage


# def pytest_addoption(parser):
#     parser.addoption("--url", action="store", default="https://demoqa.com/", help="Base url")


@pytest.fixture(autouse=True, scope="module")
def driver():
    capabilities = {
        "browserName": "firefox",
        "browserVersion": "114.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def text_box_page(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    return page


@pytest.fixture()
def check_box_page(driver):
    page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
    page.open()
    return page


@pytest.fixture()
def radio_button_page(driver):
    page = PadioButtonPage(driver, 'https://demoqa.com/radio-button')
    page.open()
    return page


@pytest.fixture()
def web_table_page(driver):
    page = WebTablePage(driver, 'https://demoqa.com/webtables')
    page.open()
    return page


@pytest.fixture()
def browser_windows_page(driver):
    page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
    page.open()
    return page
