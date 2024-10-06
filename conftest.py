import pytest
from utils.browser import Browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None, help="Browser selection: chrome, firefox, edge"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser_instance = Browser(browser_name)
    _driver = browser_instance.get_driver()
    yield _driver
    _driver.quit()
