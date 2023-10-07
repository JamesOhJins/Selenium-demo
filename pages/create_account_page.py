from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CreateAccountPage(BasePage):
    """
    This class models the Create Google Account page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    # LOCATORS
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    NEXT_BTN = (By.ID, "collectNameNext")


    HEADING_TEXT = (By.ID, "headingText")
    HEADING_TEXT_STRING = "Create a Google Account"

    HEADING_SUBTEXT = (By.ID, "headingSubtext")
    HEADING_SUBTEXT_STRING = "Enter your name"

    NAME_ERROR = (By.ID, "nameError")
    NAME_ERROR_STRING = "Enter first name"

    def enter_first_name_only(self, first_name):
        self.send_key(self.FIRST_NAME, first_name, True)
    
    def enter_last_name_only(self, last_name):
        self.send_key(self.LAST_NAME, last_name, True)
    
    def enter_first_and_last_name(self, first_name, last_name):
        self.send_key(self.FIRST_NAME, first_name)
        self.send_key(self.LAST_NAME, last_name, True)

    def click_next(self):
        self.click_elem(self.NEXT_BTN)

    def verify_name_error(self):
        return(self.verify_text_in_element(self.NAME_ERROR, self.NAME_ERROR_STRING))

    def verify_heading_texts(self):
        """Verifies the page heading Text equals to the expected text"""
        return (self.verify_text_in_element(self.HEADING_TEXT, self.HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.HEADING_SUBTEXT, self.HEADING_SUBTEXT_STRING))


