import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, driver):
        self.driver = driver
        self.driver.get("https://useinsider.com/")
        yield