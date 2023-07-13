import pytest
from selenium import webdriver
from pages.elements.text_box_page import TextBoxPage
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.radio_button_page import PadioButtonPage
from pages.elements.web_table_page import WebTablePage
from pages.alerts.browser_windows_page import BrowserWindowsPage
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="module")
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--executor", action="store", default="192.168.0.100")
#
#
# @pytest.fixture
# def driver(request):
#     browser = request.config.getoption("--browser")
#     executor = request.config.getoption("--executor")
#
#     capabilities = {
#         "browserName": browser
#     }
#
#     driver = webdriver.Remote(
#         command_executor=f"http://{executor}:4444/wd/hub",
#         desired_capabilities=capabilities
#     )
#
#     request.addfinalizer(driver.quit)
#     return driver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://demoqa.com/", help="Base url")


@pytest.fixture(autouse=True)
def driver(request):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "114.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True,
            "enableLog": True
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    request.cls.driver = driver
    url = request.config.getoption("--url")
    driver.get(url)
    driver.maximize_window()
    yield
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
