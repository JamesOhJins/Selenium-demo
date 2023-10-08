from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.webdriver.support.expected_conditions import url_changes
import time



import calendar

class BasicInfoPage(BasePage):
    """
    This class models the Basic Information page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    #-----------------------------------------------------------------------------------------------#
    #                                          Locators
    #-----------------------------------------------------------------------------------------------#
    MONTH = (By.ID, "month")
    DAY = (By.ID, "day")
    YEAR = (By.ID, "year")
    GENDER = (By.ID, "gender")

    NEXT_BTN = (By.ID, "birthdaygenderNext")
   
   
    BASIC_INFO_HEADING_TEXT = (By.ID, "headingText")
    BASIC_INFO_HEADING_TEXT_STRING = "Basic information"

    BASIC_INFO_HEADING_SUBTEXT = (By.ID, "headingSubtext")
    BASIC_INFO_HEADING_SUBTEXT_STRING = "Enter your birthday and gender"

    DATE_ERROR = (By.ID, "dateError")
    DATE_ERROR_INCOMPLETE_STRING = "Please fill in a complete birthday"
    DATE_ERROR_INVALID_STRING = "Please enter a valid date"

    GENDER_ERROR = (By.ID, "genderError")
    GENDER_ERROR_STRING = "Please select your gender"

    BASE_URL = "https://accounts.google.com/signup/v2/birthdaygender"

    #-----------------------------------------------------------------------------------------------#
    #                                         Interactions
    #-----------------------------------------------------------------------------------------------#
    
    def select_month(self, numeric_month):
        string_month = calendar.month_name[numeric_month]
        self.select_from_dropdown(self.MONTH, string_month)

    def enter_day(self, day):
        self.send_key(self.DAY, day)

    def enter_year(self, year):
        self.send_key(self.YEAR, year)
    
    def select_gender(self, gender_string):
        self.select_from_dropdown(self.GENDER, gender_string)

    def click_next(self):
        self.click_elem(self.NEXT_BTN)
        self.wait_until_text_is_not_in_element(self.BASIC_INFO_HEADING_TEXT, self.BASIC_INFO_HEADING_TEXT_STRING)

    def verify_date_incomplete_error(self):
        assert self.verify_text_in_element(self.DATE_ERROR, self.DATE_ERROR_INCOMPLETE_STRING)

    def verify_date_invalid_error(self):
        assert self.verify_text_in_element(self.DATE_ERROR, self.DATE_ERROR_INVALID_STRING)
    
    def verify_gender_error(self):
        assert self.verify_text_in_element(self.GENDER_ERROR, self.GENDER_ERROR_STRING)


    def verify_basic_info_headingTexts(self):
        """Verifies the page heading Text equals to the expected text"""
        # self.wait_until_url_contains(self.BASE_URL)
        assert (self.verify_text_in_element(self.BASIC_INFO_HEADING_TEXT, self.BASIC_INFO_HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.BASIC_INFO_HEADING_SUBTEXT, self.BASIC_INFO_HEADING_SUBTEXT_STRING))

