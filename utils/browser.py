import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from dotenv import load_dotenv


class Browser:
    def __init__(self, browser_name=None):
        load_dotenv()
        self.browser_name = browser_name.lower() if browser_name else 'chrome'
        self.environment = os.getenv('ENVIRONMENT', 'local')
        self.driver = self._initialize_driver()

    def _initialize_driver(self):
        browser = self.browser_name

        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--remote-allow-origins=*")

            if self.environment == 'local':
                service = ChromeService(ChromeDriverManager().install())
            elif self.environment == 'docker':
                options.add_argument("--headless")
                options.binary_location = "/usr/bin/google-chrome"
                service = ChromeService(executable_path="/usr/bin/chromedriver")
            else:
                raise ValueError(f"Unsupported Environment: {self.environment}")

            driver = webdriver.Chrome(service=service, options=options)

        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')

            if self.environment == 'local':
                service = FirefoxService(GeckoDriverManager().install())
            else:
                raise ValueError(f"Unsupported Environment: {self.environment}")

            driver = webdriver.Firefox(service=service, options=options)

        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--start-maximized')

            if self.environment == 'local':
                service = EdgeService(EdgeChromiumDriverManager().install())
            else:
                raise ValueError(f"Unsupported Environment: {self.environment}")

            driver = webdriver.Edge(service=service, options=options)

        else:
            raise ValueError(f"Unsupported Browser Type: {browser}")

        return driver

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
