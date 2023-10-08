from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException , TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta
import logging
import pytest



logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_url(self, url):
        """Opens a specified URL."""
        self.driver.get(url)

    def get_date_after_n_days(self, n):
        """Returns a dictionary of data with current year, month, and day."""
        current_date = datetime.now() + timedelta(days=n)
        return {
            "year": current_date.year,
            "month": current_date.month,
            "day": current_date.day
        }
    
    #-------------------------------------------------------------------------
    #                              Verifications 
    #-------------------------------------------------------------------------
    def assertURL(self, expected_url):
        """Asserts the current URL against the expected URL."""
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        assert current_url == expected_url, f"Expected URL '{expected_url}' but got '{current_url}'"



    def verify_text_in_element(self, element, text):
        """
        Verifies if the specified text is present in the element.

        Args:
            element(tuple): Locator of the element.
            text(str): Text to verify.

        Returns:
            bool: True if text is present in the element after 3 trials, False otherwise.
        """
        for attempt in range(1, 4):
            try:
                time.sleep(5)
                elem = self.find_elem(element)
                if text in elem.text:
                    return True
                else:
                    self.logger.error(f"#{attempt} Expected '{text}' to be in element text, but found '{elem.text}' instead.")
            except (NoSuchElementException, StaleElementReferenceException):
                self.logger.error(f"#{attempt} Error accessing {element}. It might not be present or has gone stale.")
            except Exception as e:
                self.logger.error(f"#{attempt} Unexpected error verifying text in {element}. Error: {str(e)}")

        # Return False if the function hasn't returned True after 3 attempts
        pytest.fail(f"Failed to find '{text}' in element {element} after 3 attempts.")
        return False


    def verify_either_texts_in_element(self, element, text_opt_one, text_opt_two):
        """
        Verifies if the either of specified text is present in the element.

        Args:
            element(tuple): Locator of the element.
            text_opt_one(str): Text to verify first option
            text_opt_two(str): Text to verify second option

        Returns:
            bool: True if text is present in the element, False otherwise.
        """
        try:
            elem = self.find_elem(element)
            if elem:
                assert text_opt_one in elem.text or text_opt_two in elem.text, f"Expected '{text_opt_one}' or '{text_opt_two}' to be in element text, but found '{elem.text}' instead."
                return True
            else:
                raise AssertionError(f"Element {element} not found.")
        except Exception as e:
            self.logger.error(f"Error verifying text in {element}. Error: {str(e)}")
            raise e 

    #-------------------------------------------------------------------------
    #                               Interactions 
    #-------------------------------------------------------------------------
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """Waits until the element becomes visible."""
        try:
            self.logger.info(f"Wating for {locator} to be visible")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f"Element {locator} was not visible after {timeout} seconds. Error: {str(e)}")

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Waits until the element becomes clickable."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.logger.error(f"Element {locator} was not clickable after {timeout} seconds. Error: {str(e)}")

    def wait_until_page_loaded(self, timeout=5):
        """Waits until the page is fully loaded."""
        ready_state_script = 'return document.readyState'
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script(ready_state_script) == "complete"
            )
        except Exception as e:
            self.logger.error(f"Page was not loaded after {timeout} seconds. Error: {str(e)}")

    def wait_until_url_contains(self, baseURL, timeout=10):
        """Waits until the page is in expected URL"""
        print(f'url: {self.driver.current_url}')
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: baseURL in driver.current_url
            )
        except TimeoutException:
            print(f"URL did not contain '{baseURL}' after waiting for {timeout} seconds.")
    
    def wait_until_text_is_not_in_element(self, locator, text, timeout=10):
        """
        Waits until the specified text is not present in the element.
        
        Args:
            locator(tuple): Locator of the element.
            text(str): Text to check against.
            timeout(int): Time to wait for condition to become true.
        """
        try:
            self.logger.info(f"Waiting for {text} to NOT be in element {locator}")
            
            # Define a lambda function for the custom expected condition
            condition = lambda driver: text not in driver.find_element(*locator).text
            
            WebDriverWait(self.driver, timeout).until(condition)
        except Exception as e:
            self.logger.error(f"Text '{text}' was still present in element {locator} after {timeout} seconds. Error: {str(e)}")






    #-------------------------------------------------------------------------
    #                               Interactions 
    #-------------------------------------------------------------------------
    def send_key(self, element, text, enter = False):
        """Sends specified keys to the element. Also sends enter if enter = True is passed"""
        try:
            elem = self.find_elem(element)
            if elem:
                elem.send_keys(text)
                if enter:
                    elem.send_keys(Keys.RETURN)
        except Exception as e:
            self.logger.error(f"Error sending keys to {element}. Error: {str(e)}")


    def click_elem(self, element):
        """Clicks on a specified element."""
        try:
            elem = self.find_elem(element)
            elem.click()    
        except Exception as e:
            self.logger.error(f"Error clicking on {element}. Error: {str(e)}")


    def click_dropdown(self, dropdown, option):
        """
        Clicks on a dropdown and then on an option.

        Args:
            dropdown(tuple): Locator of the dropdown.
            option(tuple): Locator of the option to click.
        """
        try:
            self.click_elem(dropdown)
            self.wait_for_element_to_be_visible(option)
            self.click_elem(option)
        except Exception as e:
            self.logger.error(f"Error clicking on dropdown {dropdown} or option {option}. Error: {str(e)}")

    
    def select_from_dropdown(self, dropdown_locator, option_text):
        """
        Selects an option from a <select> type dropdown using the visible text.

        Args:
            dropdown_locator(tuple): Locator of the dropdown.
            option_text(str): Visible text of the option to select.
        """
        try:
            # Find the dropdown using the given locator
            dropdown_elem = self.find_elem(dropdown_locator)
            
            # Create a Select object
            select_dropdown = Select(dropdown_elem)
            
            # Select the option by its visible text
            select_dropdown.select_by_visible_text(option_text)

            self.logger.info(f"Successfully selected '{option_text}' from the dropdown {dropdown_locator}")

        except Exception as e:
            self.logger.error(f"Error selecting '{option_text}' from dropdown {dropdown_locator}. Error: {str(e)}")

    
    # def find_elem(self, locator):
    #     """Finds an element based on the locator. Returns None if not found."""
    #     try:
            
    #         return self.driver.find_element(*locator)
    #     except NoSuchElementException:
    #         self.logger.error(f"Element {locator} not found.")
    #         return None
    def find_elem(self, locator, retry_number=5):
        """Finds an element based on the locator. Returns None if not found."""
        time.sleep(3)
        for attempt in range(1, retry_number + 1):
            try:
                element = self.driver.find_element(*locator)
                self.logger.info(f"Found the element {locator} on try #{attempt}.")
                return element
            except StaleElementReferenceException:
                self.logger.warning(f"StaleElementReferenceException on try #{attempt}/{retry_number}.")
                continue
            except NoSuchElementException:
                self.logger.error(f"Element {locator} not found on try #{attempt}/{retry_number}.")
                continue
        return None
    
    def scroll_to_elem(self, locator):
        """Scrolls to a specified element."""
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.find_elem(locator)).perform()
        except Exception as e:
            self.logger.error(f"Error scrolling to element {locator}. Error: {str(e)}")