from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.webdriver.support.expected_conditions import url_changes
import time

class ChooseAddrPage(BasePage):
    """
    This class models the Choose Gmail Address page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    #-----------------------------------------------------------------------------------------------#
    #                                          Locators
    #-----------------------------------------------------------------------------------------------#
    NEXT_BTN = (By.ID, "next")
   
    GMAIL_HEADING_TEXT = (By.ID, "headingText")
    GMAIL_HEADING_TEXT_STRING = "Choose your Gmail address"
    GMAIL_HEADING_TEXT_STRING_SIGN = "How you’ll sign in"

    GMAIL_HEADING_SUBTEXT = (By.ID, "headingSubtext")
    GMAIL_HEADING_SUBTEXT_STRING = "Pick a Gmail address or create your own"
    GMAIL_HEADING_SUBTEXT_STRING_SIGN = "Create a Gmail address for signing in to your Google Account"


    EMAIL_ERROR = (By.CSS_SELECTOR, ".o6cuMc.Jj6Lae")
    EMAIL_ERROR_STRING = "Choose a Gmail address"

    BASE_URL = "https://accounts.google.com/signup/v2/createusername"


    #-----------------------------------------------------------------------------------------------#
    #                                        Interactions
    #-----------------------------------------------------------------------------------------------#
    def click_next(self):
        self.click_elem(self.NEXT_BTN)
        self.wait_until_text_is_not_in_element(self.GMAIL_HEADING_TEXT, self.GMAIL_HEADING_TEXT_STRING)
        self.wait_until_text_is_not_in_element(self.GMAIL_HEADING_TEXT_STRING, self.GMAIL_HEADING_TEXT_STRING_SIGN)

    def verify_email_error(self):
        assert self.verify_text_in_element(self.EMAIL_ERROR, self.EMAIL_ERROR_STRING)


    def verify_headingTexts(self):
        """Verifies the page heading Text equals to the expected text"""
        # self.wait_until_url_contains(self.BASE_URL)
        assert (self.verify_either_texts_in_element(self.GMAIL_HEADING_TEXT, self.GMAIL_HEADING_TEXT_STRING, self.GMAIL_HEADING_TEXT_STRING_SIGN
                )and self.verify_either_texts_in_element(self.GMAIL_HEADING_SUBTEXT, self.GMAIL_HEADING_SUBTEXT_STRING, self.GMAIL_HEADING_SUBTEXT_STRING_SIGN))


