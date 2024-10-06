from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseFunctions:
    def __init__(self):
        self.driver = None
        self.locators = None

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator, timeout=10):
        self.wait_until_visible(locator, timeout)
        element = self.find_element(locator)
        element.click()

    def js_click(self, locator, timeout=10):
        self.wait_until_visible(locator, timeout)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator, timeout=10):
        self.wait_until_visible(locator, timeout)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def hover_and_click(self, hover_locator, click_locator, timeout=10):
        self.wait_until_visible(hover_locator, timeout)
        hover_element = self.find_element(hover_locator)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()

        self.wait_until_visible(click_locator, timeout)
        click_element = self.find_element(click_locator)

        click_element.click()

    def enter_text(self, locator, text, timeout=10):
        self.wait_until_visible(locator, timeout)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        self.wait_until_visible(locator, timeout)
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def are_element_list_visible(self, locator_list, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(locator_list)
            )

            return all(element.is_displayed() for element in elements)

        except TimeoutException:
            return False

    def wait_until_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(
                f"Element with locator {locator} didn't appear within {timeout} seconds."
            )

    def wait_until_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(
                f"Element with locator {locator} didn't appear within {timeout} seconds."
            )

    def wait_until_text_is(self, locator, expected_text, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.text_to_be_present_in_element(locator, expected_text)
            )
        except TimeoutException:
            raise TimeoutException(
                f"Element with locator {locator} did not have text '{expected_text}' within {timeout} seconds."
            )

    def click_element_in_list(self, locator_list, index, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(locator_list)
            )

            elements = self.driver.find_elements(*locator_list)

            if index >= len(elements):
                raise IndexError(f"Index {index} is out of range for the element list.")

            elements[index].click()

        except TimeoutException:
            raise TimeoutException(
                f"Elements with locator {locator_list} didn't appear within {timeout} seconds."
            )
        except IndexError as e:
            raise e

    def get_text_from_element_in_list(self, locator_list, index, timeout=10):
        try:
            self.wait_until_visible(locator_list, timeout)

            elements = self.driver.find_elements(*locator_list)

            if index >= len(elements):
                raise IndexError(f"Index {index} is out of range for the element list.")

            return elements[index].text

        except TimeoutException:
            raise TimeoutException(
                f"Elements with locator {locator_list} didn't appear within {timeout} seconds."
            )
        except IndexError as e:
            raise e

    def switch_to_new_tab(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        windows = self.driver.window_handles

        for window in windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

    def get_title(self):
        return self.driver.title
