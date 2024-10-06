from selenium.webdriver.common.by import By


class HomePageLocators:
    NAVBAR_BRAND = (By.CLASS_NAME, 'navbar-brand')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'wt-cli-accept-all-btn')
    HOME_CTA_CONTAINER_LIST = (By.CSS_SELECTOR, ".home_cta_container > a")
    COMPANY_DROPDOWN_LIST = (By.ID, 'navbarDropdownMenuLink')
    CAREERS_BTN = (By.XPATH, "//a[text()='Careers']")


class CareersPageLocators:
    BUTTON_GROUP = (By.CSS_SELECTOR, ".button-group > a")
    JOB_TITLE_LIST = (By.CSS_SELECTOR, ".job-title")
    LOCATION_SLIDER = (By.ID, "location-slider")
    LIFE_AT_INSIDER_CONTAINER = (By.CSS_SELECTOR, ".e-swiper-container")
    SEE_ALL_TEAMS_BTN = (By.XPATH, "//a[text()='See all teams']")
    QUALITY_ASSURANCE_BTN = (By.XPATH, "//h3[text()='Quality Assurance']")
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//a[text()='See all QA jobs']")


class JobsPageLocators:
    FILTER_BY_DEPARTMENT_DROPDOWN = (By.ID, "select2-filter-by-department-container")
    FILTER_BY_LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    LOCATION_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "li.select2-results__option")
    POSITION_DEPARTMENT_LIST = (By.CSS_SELECTOR, ".position-department")
    POSITION_TITLE_LIST = (By.CSS_SELECTOR, ".position-title")
    POSITION_LOCATION_LIST = (By.CSS_SELECTOR, ".position-location")
    JOB_POSITION_CARD = (By.CSS_SELECTOR, ".position-list-item-wrapper")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, ".position-list-item-wrapper>a")
    LEVER_APPLY_BUTTON = (By.CSS_SELECTOR, ".postings-btn")
