from selenium import webdriver

def get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument("--lang=en")
    
    return webdriver.Chrome(options=chrome_options)
