from pages.BasePage import BasePage
from utils.web_elements import CareersPageLocators


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_locators(self):
        self.locators = CareersPageLocators

    def get_find_job_button_text(self):
        return self.get_text_from_element_in_list(CareersPageLocators.BUTTON_GROUP, 1)

    def is_job_title_list_opened(self):
        return self.are_element_list_visible(CareersPageLocators.JOB_TITLE_LIST)

    def is_locations_slider_opened(self):
        return self.is_element_visible(CareersPageLocators.LOCATION_SLIDER)

    def is_life_at_insider_container_displayed(self):
        return self.is_element_visible(CareersPageLocators.LIFE_AT_INSIDER_CONTAINER)

    def navigate_to_quality_assurance_jobs_page(self):
        self.js_click(CareersPageLocators.SEE_ALL_TEAMS_BTN)
        self.js_click(CareersPageLocators.QUALITY_ASSURANCE_BTN)
        self.js_click(CareersPageLocators.SEE_ALL_QA_JOBS_BTN)

