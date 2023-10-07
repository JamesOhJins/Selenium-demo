from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SignupPage(BasePage):
    """
    This class models the Google signup page. 
    It contains the locators for the page's elements and methods to interact with them.
    """
    SIGNIN_URL = "https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fsupport.google.com%2Faccounts%2Fanswer%2F27441%3Fhl%3Den&ec=GAZAdQ&hl=en&ifkv=AYZoVhfuGEPuDleyh2MoYQaDqmACKkg196avCjzqwxtLZ6qtrC43MGw-2czaRWKvbAK7hILUei8JYw&passive=true&sjid=4579872496296854529-NA&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S84703643%3A1696101091298744&theme=glif"
    
    # LOCATORS
    CREATE_ACCOUNT = (By.CLASS_NAME, "XOrBDc")
    EXPANDED_CREATE_ACCOUNT = (By.CSS_SELECTOR,"button[aria-expanded='true']")


    PERSONAL_USE = (By.XPATH, "//div[@class='{}']//li[@tabindex='-1']".format(CREATE_ACCOUNT[1]))

    def navigate_to_sign_in_page(self):
        """Navigates to the sign-in page and waits until it's loaded."""
        self.driver.get(self.SIGNIN_URL)
        self.wait_until_page_loaded()

    def verify_url(self):
        """Verifies that the current URL matches the expected URL."""
        self.assertURL(self.SIGNIN_URL)

    def select_personal_use(self):
        # self.click_elem(self.CREATE_ACCOUNT)
        self.click_dropdown(self.CREATE_ACCOUNT, self.PERSONAL_USE)

    def switch_to_second_tab(self):
        """Switches the driver context to the second browser tab/window."""
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))    
        self.driver.switch_to.window(self.driver.window_handles[1])



