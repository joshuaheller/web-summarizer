import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def request(url):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.content
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')    
    return html_content

def check_javascript_needed(body):
     noscript_tag = body.find('noscript')
     
     if noscript_tag:
         body_lc = body.noscript.get_text().lower()
         phrases = ['enable javascript', 'javascript is required', 'javascript is disabled']
         for phrase in phrases:
            if phrase.lower() in body_lc:
                return True
            else:
                return False
            
     else:
        if len(body.get_text()) <= 2000:
            need_js = True
        else:
            need_js = False
     return need_js

def selenium(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run headless Chrome for no GUI
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    CHROMEDRIVE_PATH = '/usr/local/bin/chromedriver'    
    # Provide the path to your web driver
    service = Service(CHROMEDRIVE_PATH)  # Update with the path to your ChromeDriver

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    # Wait for the JavaScript to execute and the content to load
    time.sleep(5)  # Adjust the sleep time as needed

    # Get the page source after JavaScript execution
    html_content = driver.page_source
    return html_content
