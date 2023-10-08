import pytest
from pages.google_signup_page import SignupPage
from pages.basic_information_page import BasicInfoPage
from pages.choose_address_page import ChooseAddrPage
from pages.create_account_page import CreateAccountPage
from utils.driver_config import get_chrome_driver
import configparser


driver = get_chrome_driver()

signup_page = SignupPage(driver)
choose_addr_page = ChooseAddrPage(driver)
basic_info_page = BasicInfoPage(driver)
create_acct_page = CreateAccountPage(driver)

config = configparser.ConfigParser()
config.read('config.ini')

priority = 'all'  # all, high, medium, low

first_name = config.get('SignupDetails', 'valid_first_name')
last_name = config.get('SignupDetails', 'valid_last_name')
username = config.get('SignupDetails', 'valid_username')

def setup_signup_page():
    # Common steps from test_TC004
    signup_page.navigate_to_sign_in_page()
    signup_page.select_personal_use()
    create_acct_page.enter_first_and_last_name(first_name, last_name)
    create_acct_page.click_next()
    create_acct_page.wait_until_page_loaded()

#-----------------------------------------------------------------------------------------------#
#                                          TC001
#-----------------------------------------------------------------------------------------------#
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC001():

    # 1. Navigate to sign in page
    signup_page.navigate_to_sign_in_page()
    # 2 & 3. Select personal use from drop down
    signup_page.select_personal_use()

    # 4. Enter "John" in the first name input.
    create_acct_page.enter_first_name_only(first_name)
    
    # 5. Leave the last name input blank and click "Next".
    create_acct_page.click_next()

    # Verify that the page is redirected to basic information page
    basic_info_page.verify_basic_info_headingTexts()


#-----------------------------------------------------------------------------------------------#
#                                          TC002
#-----------------------------------------------------------------------------------------------#
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-medium priority tests.")
def test_TC002():

    # 1. Navigate to sign in page
    signup_page.navigate_to_sign_in_page()
    
    # 2 & 3. Select personal use from drop down
    signup_page.select_personal_use()

    # 4. Enter "Doe" in the last name input.
    create_acct_page.enter_last_name_only(last_name)    

    # 5. Leave the first name input blank and click "Next".
    create_acct_page.click_next()

    # 6. Verify red text message
    create_acct_page.verify_name_error()


#-----------------------------------------------------------------------------------------------#
#                                          TC003
#-----------------------------------------------------------------------------------------------#
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-medium priority tests.")
def test_TC003():

    # 1. Navigate to sign in page
    signup_page.navigate_to_sign_in_page()
    
    # 2 & 3. Select personal use from drop down
    signup_page.select_personal_use()


    # 4. Leave the first and last name input blank and click "Next".
    create_acct_page.click_next()

    # 5. Verify red text message
    create_acct_page.verify_name_error()


#-----------------------------------------------------------------------------------------------#
#                                          TC004
#-----------------------------------------------------------------------------------------------#
@pytest.mark.dependency(name="TC_004")
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-medium priority tests.")
def test_TC004():

    # 1. Navigate to sign in page
    signup_page.navigate_to_sign_in_page()
    
    # 2 & 3. Select personal use from drop down
    signup_page.select_personal_use()

    
    # 4 & 5. Fill the first and last name input.
    create_acct_page.enter_first_and_last_name(first_name,last_name)

    # 6. Click "Next"
    create_acct_page.click_next()

    # Verify the header text message
    basic_info_page.verify_basic_info_headingTexts()


#-----------------------------------------------------------------------------------------------#
#                                          TC005
#-----------------------------------------------------------------------------------------------#
@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-high priority tests.")
def test_TC005():

    # 1. Run TC004
    setup_signup_page()

    # 2. Press next button with empty field
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_incomplete_error()
    

#-----------------------------------------------------------------------------------------------#
#                                          TC006
#-----------------------------------------------------------------------------------------------#
@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-high priority tests.")
def test_TC006():

    # 1. Run TC004
    setup_signup_page()

    # Get tomorrow's date dictionary
    tomorrow_date = basic_info_page.get_date_after_n_days(1)

    # Unpack dictionary
    year, month, day = tomorrow_date["year"], tomorrow_date["month"], tomorrow_date["day"]
    
    # 2. Enter tomorrow's date
    basic_info_page.select_month(month)
    basic_info_page.enter_day(day)
    basic_info_page.enter_year(year)

    # 3. Enter gender
    basic_info_page.select_gender("Male")
    
    # 4. Press next button
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_invalid_error()


#-----------------------------------------------------------------------------------------------#
#                                          TC007
#-----------------------------------------------------------------------------------------------#
@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-high priority tests.")
def test_TC007():

    # 1. Run TC004
    setup_signup_page()

    # 2. Enter malformed data
    basic_info_page.select_month(1)
    basic_info_page.enter_day(00)
    basic_info_page.enter_year(0000)

    # 3. Press next button
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_invalid_error()
    

#-----------------------------------------------------------------------------------------------#
#                                          TC008
#-----------------------------------------------------------------------------------------------#
@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'medium'], reason="Skipping non-high priority tests.")
def test_TC008():

    # 1. Run TC004
    setup_signup_page()

    # 2. Enter a valid data
    basic_info_page.select_month(1)
    basic_info_page.enter_day(1)
    basic_info_page.enter_year(1999)

    # 3. Press next button
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_gender_error()
    

#-----------------------------------------------------------------------------------------------#
#                                          TC009
# -----------------------------------------------------------------------------------------------#
# @pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC009():

    # 1. Run TC004
    setup_signup_page()

    # 2. Enter a valid data
    basic_info_page.select_month(1)
    basic_info_page.enter_day(1)
    basic_info_page.enter_year(1999)

     # 3. Select gender    
    basic_info_page.select_gender("Male")

    # 4. Press next button
    basic_info_page.click_next()


    # Verify text in page
    choose_addr_page.verify_headingTexts()
    
# driver.quit()