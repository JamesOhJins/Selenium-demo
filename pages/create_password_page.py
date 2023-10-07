from selenium.webdriver.common.by import By
from .base_page import BasePage


class CreatePasswordPage(BasePage):
    """
    This class models the Create Password page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    # LOCATORS
    HEADING_SUBTEXT = (By.ID, "headingSubtext")
    HEADING_SUBTEXT_STRING = "Create a strong password"

    NAME_ERROR = (By.ID, "nameError")
    NAME_ERROR_STRING = "Create a strong password with a mix of letters, numbers and symbols"

    def verify_heading_texts(self):
        """Verifies the page heading Text equals to the expected text"""
        return (self.verify_text_in_element(self.HEADING_TEXT, self.HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.HEADING_SUBTEXT, self.HEADING_SUBTEXT_STRING))


