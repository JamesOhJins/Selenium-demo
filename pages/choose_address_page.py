from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ChooseAddrPage(BasePage):
    """
    This class models the Choose Gmail Address page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    
    # LOCATORS
    MONTH = (By.ID, "firstName")
    DAY = (By.ID, "lastName")
    YEAR = (By.ID, "year")
    GENDER = (By.ID, "gender")

    NEXT_BTN = (By.ID, "next")
   
    FIRST_EMAIL_RADIO = (By.CSS_SELECTOR, "[role='radio'][aria-posinset='1']")
    SECOND_EMAIL_RADIO = (By.CSS_SELECTOR, "[role='radio'][aria-posinset='2']")
    CREATE_EMAIL_RADIO = (By.CSS_SELECTOR, "[role='radio'][aria-posinset='2']")

    HEADING_TEXT = (By.ID, "headingText")
    HEADING_TEXT_STRING = "Choose your Gmail address"

    HEADING_SUBTEXT = (By.ID, "headingSubtext")
    HEADING_SUBTEXT_STRING = "Pick a Gmail address or create your own"

    EMAIL_ERROR = (By.CSS_SELECTOR, ".o6cuMc.Jj6Lae")
    EMAIL_ERROR_STRING = "Choose a Gmail address"

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

    def verify_email_error(self):
        return self.verify_text_in_element(self.EMAIL_ERROR, self.EMAIL_ERROR_STRING)


    def verify_headingTexts(self):
        """Verifies the page heading Text equals to the expected text"""
        return (self.verify_text_in_element(self.HEADING_TEXT, self.HEADING_TEXT_STRING
                ) and self.verify_text_in_element(self.HEADING_SUBTEXT, self.HEADING_SUBTEXT_STRING))

