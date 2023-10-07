import pytest
from pages.google_signup_page import SignupPage
from pages.basic_information_page import BasicInfoPage
from pages.choose_address_page import ChooseAddrPage
from pages.create_account_page import CreateAccountPage
from pages.create_password_page import CreatePasswordPage
from utils.driver_config import get_chrome_driver
import configparser

priority = 'all'  # default value, can be changed at runtime


driver = get_chrome_driver()

signup_page = SignupPage(driver)
choose_addr_page = ChooseAddrPage(driver)
basic_info_page = BasicInfoPage(driver)
create_acct_page = CreateAccountPage(driver)
create_pswd_page = CreatePasswordPage(driver)

config = configparser.ConfigParser()
config.read('config.ini')

first_name = config.get('SignupDetails', 'valid_first_name')
last_name = config.get('SignupDetails', 'valid_last_name')
username = config.get('SignupDetails', 'valid_username')

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
    assert basic_info_page.verify_headingTexts

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
    pass
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-medium priority tests.")
def test_TC003():

    # 1. Navigate to sign in page
    signup_page.navigate_to_sign_in_page()
    
    # 2 & 3. Select personal use from drop down
    signup_page.select_personal_use()


    # 4. Leave the first and last name input blank and click "Next".
    create_acct_page.click_next()

    # 5. Verify red text message
    create_acct_page.verify_name_error()
    pass


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
    basic_info_page.verify_headingTexts()
    pass


@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC005():

    # 1. Run TC004
    test_TC004

    # 2. Press next button with empty field
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_incomplete_error()
    

    pass

@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC005():

    # 1. Run TC004
    test_TC004

    # 2. Press next button with empty field
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_incomplete_error()
    
    pass

@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC006():

    # 1. Run TC004
    test_TC004

    # 2. Press next button with empty field
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_incomplete_error()
    
    pass


@pytest.mark.dependency(depends=["TC_004"])
@pytest.mark.skipif(priority not in ['all', 'high'], reason="Skipping non-high priority tests.")
def test_TC007():

    # 1. Run TC004
    test_TC004

    # 2. Press next button with empty field
    basic_info_page.click_next()

    # Verify red warning text
    basic_info_page.verify_date_incomplete_error()
    
    pass
# @pytest.fixture
# def setup():

#     # yield all necessary objects and configurations for tests
#     yield {
#         'driver': driver,
#         'signup_page': signup_page,
#         'choose_addr_page': choose_addr_page,
#         'basic_info_page': basic_info_page,
#         'create_acct_page': create_acct_page,
#         'create_pswd_page': create_pswd_page,
#         'first_name': first_name,
#         'last_name': last_name,
#         'username': username
#     }

#     # After yielding, the code below will act as a teardown function
#     driver.quit()





# def teardown_function(function, setup):
#     # Pass setup fixture to the teardown_function
#     driver = setup['driver']
#     driver.quit()