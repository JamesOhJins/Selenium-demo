from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.webdriver.support.expected_conditions import url_changes
import time

class CreateAccountPage(BasePage):
    """
    This class models the Create Google Account page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    #-----------------------------------------------------------------------------------------------#
    #                                          Locators
    #-----------------------------------------------------------------------------------------------#
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    NEXT_BTN = (By.ID, "collectNameNext")
    # NEXT_BTN = (By.CLASS_NAME, "VfPpkd-LgbsSe")

    ACCOUNT_HEADING_TEXT = (By.ID, "headingText")
    ACCOUNT_HEADING_TEXT_STRING = "Create a Google Account"

    ACCOUNT_HEADING_SUBTEXT = (By.ID, "headingSubtext")
    ACCOUNT_HEADING_SUBTEXT_STRING = "Enter your name"

    NAME_ERROR = (By.ID, "nameError")
    NAME_ERROR_STRING = "Enter first name"

    BASE_URL = "https://accounts.google.com/signup/v2/createaccount"
    #-----------------------------------------------------------------------------------------------#
    #                                        Interactions
    #-----------------------------------------------------------------------------------------------#
    def enter_first_name_only(self, first_name):
        self.send_key(self.FIRST_NAME, first_name, True)
    
    def enter_last_name_only(self, last_name):
        self.send_key(self.LAST_NAME, last_name, True)
    
    def enter_first_and_last_name(self, first_name, last_name):
        self.send_key(self.FIRST_NAME, first_name)
        self.send_key(self.LAST_NAME, last_name, True)

    def click_next(self):
        self.click_elem(self.NEXT_BTN)
        self.wait_until_text_is_not_in_element(self.ACCOUNT_HEADING_TEXT, self.ACCOUNT_HEADING_TEXT_STRING)


    def verify_name_error(self):
        assert(self.verify_text_in_element(self.NAME_ERROR, self.NAME_ERROR_STRING))

    def verify_heading_texts(self):
        """Verifies the page heading Text equals to the expected text"""
        # self.wait_until_url_contains(self.BASE_URL)
        assert (self.verify_text_in_element(self.ACCOUNT_HEADING_TEXT, self.ACCOUNT_HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.ACCOUNT_HEADING_SUBTEXT, self.ACCOUNT_HEADING_SUBTEXT_STRING))


