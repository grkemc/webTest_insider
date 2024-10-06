from pages.BasePage import BasePage
from utils.web_elements import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_locators(self):
        self.locators = HomePageLocators

    def accept_cookies(self):
        self.wait_until_visible(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        self.click(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        self.wait_until_invisible(HomePageLocators.ACCEPT_COOKIES_BUTTON)

    def is_navbar_brand_visible(self):
        return self.is_element_visible(HomePageLocators.NAVBAR_BRAND)

    def get_homepage_button_text(self):
        element_list = HomePageLocators.HOME_CTA_CONTAINER_LIST
        return self.get_text_from_element_in_list(element_list, 1)

    def navigate_to_careers_page(self):
        self.click_element_in_list(HomePageLocators.COMPANY_DROPDOWN_LIST, 4)
        self.click(HomePageLocators.CAREERS_BTN)
