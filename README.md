# hyperconnect-assessment
This repository contains the automation assessment for Hyperconnect using the Page Object Model (POM) design pattern

# Project Structure

The automation scripts adhere to the Page Object Model (POM) design pattern. This helps in maintaining the code and improving its readability. 

## Directory Structure:

- **config.ini:** Configuration file for input parameters.
- **readme.md:** This documentation file.
- **pages:** This directory contains page objects that represent individual web pages.
    - **base_page.py:** Base page containing common methods and functionalities.
    - **goodvibe_works_page.py:** Page object for the GoodVibe Works page.
    - **illuminarean_onboarding_page.py:** Page object for the Illuminarean Onboarding page.
- **tests:** Contains the actual test cases.
    - **goodvibe_works_test.py:** Tests for GoodVibe Works.
- **utils:** Utilities and configurations.
    - **driver_config.py:** Configuration for the WebDriver.



## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed.
- [Selenium](https://pypi.org/project/selenium/)

## Getting Started

**Python Script:**

   - Clone or download this repository.
   - Install the required Python libraries if you haven't already:

     ```
     pip install selenium 
     ```

2. **Modify config.ini file for input**

3. **Run the Script:**

   - cd to the repository path
   - python -m unittest tests.google_signup_test

