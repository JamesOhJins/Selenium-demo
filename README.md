# Gmail Test Cases (TC) Automation

This repository contains the automation of Gmail test cases (TC) using the Page Object Model (POM) design pattern. Test cases can be referred to in this 
[Google sheet](https://docs.google.com/spreadsheets/d/1A46Ju8NooTYNNOpMVlWRZYvgEOj5M-cTWn_lKyXVFJ8/edit#gid=0).

## Project Structure

The automation scripts are structured according to the Page Object Model (POM) design pattern, facilitating efficient code maintenance and improved readability.

### Directory Structure:

- **config.ini:** Configuration file for input parameters.
- **readme.md:** This documentation file.
- **pages:** Contains page objects representing each individual webpage. They essentially dictate how the automation interacts with the web elements on the page.
    - **__init__.py**
    - **base_page.py:** Base page containing common methods and functionalities.
    - **basic_information_page.py:** Page object for the basic information page.
    - **choose_addr_page.py:** Page object for the choose address page.
    - **create_account_page.py:** Page object for the create account page.
    - **google_signup_page.py:** Page object representing the Gmail signup page.
- **tests:** Contains the actual test cases.
    - **__init__.py**
    - **google_signup_test.py:** End-to-end test for the Gmail signup process.
- **utils:** Miscellaneous utilities and configurations.
    - **__init__.py**
    - **driver_config.py:** Configuration for the WebDriver.

## Prerequisites

Before initiating the tests, ensure:

- Python 3.x is installed.
- [pytest](https://docs.pytest.org/en/stable/) and [Selenium](https://pypi.org/project/selenium/) are installed.

## Getting Started

1. **Setup Python Environment:**
   
   - If you haven't already, clone or download this repository.
   - Ensure you have the required Python libraries installed:

     ```
     pip install pytest selenium 
     ```

2. **Configure Inputs:**
   
   - Update the `config.ini` file with the necessary inputs.

3. **Running the Test Cases:**

   - Navigate to the repository path in your terminal or command prompt.
   - Execute the test script with the following command:

     ```
     pytest tests/google_signup_test.py
     ```

