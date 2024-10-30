from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

def selenium(url):
    chrome_options = setup_chrome_options()
    driver = initialize_webdriver(chrome_options)
    load_page(driver, url)
    html_content = driver.page_source
    return html_content

# configures the Chrome options and add specific browser arguments. Configuration of chrome options
def setup_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run headless Chrome for no GUI
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    return chrome_options

# initializes and returns the WebDriver with the configured options. It takes over the setup of the Chrome WebDriver
def initialize_webdriver(options):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# loads the URL and, if necessary, inserts a pause for the JavaScript content to load completely. This function isolates the loading logic and provides flexibility, e.g. when adjusting the waiting time.
def load_page(driver, url):
    driver.get(url)
    time.sleep(5)