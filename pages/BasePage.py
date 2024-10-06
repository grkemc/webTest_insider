from selenium.webdriver.support.ui import WebDriverWait
from utils.base_functions import BaseFunctions


class BasePage(BaseFunctions):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = None
        self.load_locators()

    def load_locators(self):
        self.locators = {}
