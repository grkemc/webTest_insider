from pages.BasePage import BasePage
from utils.web_elements import JobsPageLocators
import time


class JobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_locators(self):
        self.locators = JobsPageLocators

    def is_quality_assurance_filter_displayed(self):
        filter_text = self.get_text(JobsPageLocators.FILTER_BY_DEPARTMENT_DROPDOWN)

        if filter_text == 'Quality Assurance':
            return True
        else:
            return False

    def filter_qa_jobs(self):
        self.wait_until_text_is(JobsPageLocators.FILTER_BY_DEPARTMENT_DROPDOWN, 'Quality Assurance')
        self.click(JobsPageLocators.FILTER_BY_LOCATION_DROPDOWN)
        self.click_element_in_list(JobsPageLocators.LOCATION_DROPDOWN_OPTIONS, 1)

    def check_qa_job_components(self):
        self.wait_until_text_is(JobsPageLocators.FILTER_BY_LOCATION_DROPDOWN, 'Istanbul, Turkey')
        time.sleep(5)
        self.scroll_to_element(JobsPageLocators.JOB_POSITION_CARD)
        departments = self.driver.find_elements(*JobsPageLocators.POSITION_DEPARTMENT_LIST)
        titles = self.driver.find_elements(*JobsPageLocators.POSITION_TITLE_LIST)
        locations = self.driver.find_elements(*JobsPageLocators.POSITION_LOCATION_LIST)

        for department, title, location in zip(departments, titles, locations):
            department_text = department.text
            title_text = title.text
            location_text = location.text

            if 'Quality Assurance' in department_text and 'Quality Assurance' in title_text and 'Istanbul, Turkey' in location_text:
                return True

        return False

    def navigate_to_lever_page(self):
        self.wait_until_visible(JobsPageLocators.VIEW_ROLE_BUTTON)
        self.hover_and_click(JobsPageLocators.JOB_POSITION_CARD, JobsPageLocators.VIEW_ROLE_BUTTON)
        self.switch_to_new_tab()

    def is_lever_page_displayed(self):
        return self.is_element_visible(JobsPageLocators.LEVER_APPLY_BUTTON)

