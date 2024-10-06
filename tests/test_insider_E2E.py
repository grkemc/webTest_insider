from pages.CareersPage import CareersPage
from pages.HomePage import HomePage
from pages.JobsPage import JobsPage
from tests.base_test import BaseTest


class TestInsiderE2E(BaseTest):
    def test_verify_home_page(self):
        home_page = HomePage(self.driver)
        home_page.accept_cookies()
        assert home_page.is_navbar_brand_visible(), "The navbar-brand element is not visible on the homepage."
        assert home_page.get_homepage_button_text(), "Get a Demo"

        home_page.navigate_to_careers_page()
        careers_page = CareersPage(self.driver)
        assert careers_page.get_find_job_button_text(), "Find your dream job"
        assert careers_page.is_job_title_list_opened()
        assert careers_page.is_locations_slider_opened()
        assert careers_page.is_life_at_insider_container_displayed()

        careers_page.navigate_to_quality_assurance_jobs_page()
        jobs_page = JobsPage(self.driver)
        jobs_page.is_quality_assurance_filter_displayed()
        jobs_page.filter_qa_jobs()
        assert jobs_page.check_qa_job_components()

        jobs_page.navigate_to_lever_page()
        assert jobs_page.is_lever_page_displayed()



