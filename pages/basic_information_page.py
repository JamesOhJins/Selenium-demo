from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class BasicInfoPage(BasePage):
    """
    This class models the Basic Information page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    # LOCATORS
    MONTH = (By.ID, "firstName")
    DAY = (By.ID, "lastName")
    YEAR = (By.ID, "year")
    GENDER = (By.ID, "gender")

    NEXT_BTN = (By.ID, "birthdaygenderNext")
   
   
    HEADING_TEXT = (By.ID, "headingText")
    HEADING_TEXT_STRING = "Basic information"

    HEADING_SUBTEXT = (By.ID, "headingSubtext")
    HEADING_SUBTEXT_STRING = "Enter your birthday and gender"

    DATE_ERROR = (By.ID, "dateError")
    DATE_ERROR_INCOMPLETE_STRING = "Please fill in a complete birthday"
    DATE_ERROR_INVALID_STRING = "Please enter a valid date"

    GENDER_ERROR = (By.ID, "genderError")
    GENDER_ERROR_STRING = "Please select your gender"

    def select_month(self, month_string):
        self.select_from_dropdown(self.MONTH, month_string)
    
    def select_gender(self, gender_string):
        self.select_from_dropdown(self.GENDER, gender_string)
    
    def enter_day(self, day):
        self.send_key(self.DAY, day)

    def enter_year(self, year):
        self.send_key(self.YEAR, year)
    
    def click_next(self):
        self.click_elem(self.NEXT_BTN)

    def verify_date_incomplete_error(self):
        return self.verify_text_in_element(self.DATE_ERROR, self.DATE_ERROR_INCOMPLETE_STRING)

    def verify_date_invalid_error(self):
        return self.verify_text_in_element(self.DATE_ERROR, self.DATE_ERROR_INVALID_STRING)
    
    def verify_gender_error(self):
        return self.verify_text_in_element(self.GENDER_ERROR, self.GENDER_ERROR_STRING)

    def verify_headingTexts(self):
        """Verifies the page heading Text equals to the expected text"""
        return (self.verify_text_in_element(self.HEADING_TEXT, self.HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.HEADING_SUBTEXT, self.HEADING_SUBTEXT_STRING))

