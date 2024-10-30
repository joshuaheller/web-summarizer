from typing import Optional
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

# Controls the workflow by checking whether the URL is a local file path and calling read_local_file or fetch_web_content accordingly.
def request(url: str) -> Optional[bytes]:
    if is_local_file(url):
        return read_local_file(Path(url))
    else:
        return fetch_web_content(url)

# Checks whether the URL passed is a local file path by checking the path and handling a file:// prefix if necessary.
def is_local_file(url: str) -> bool:
    try:
        if url.startswith('file://'):
            path = Path(url[7:])
        else:
            path = Path(url)
        return path.exists()
    except Exception:
        return False

# Attempts to open a local file based on the passed path and return its contents as bytes. Returns None if an error occurs.
def read_local_file(path: Path) -> Optional[bytes]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content.encode('utf-8')
    except Exception as e:
        print(f'Failed to read local file: {e}')
        return None
    
# Performs an HTTP GET request to the passed URL and returns the content as bytes if the status code is successful, or None in case of errors.
def fetch_web_content(url: str) -> Optional[bytes]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'Failed to fetch web content: {e}')
        return None
    
# checks if JavaScript is needed by checking for the noscript tag and the length of the body text.
def check_javascript_needed(body):
    if check_noscript(body):
        return True
    elif len(body.get_text()) <= 2000:
        return True
    else:
        return False
 
# checks for the noscript tag and if it is present, it checks if the text contains certain phrases that indicate the need for JavaScript.
def check_noscript(body):
    noscript_tag = body.find('noscript')
    if noscript_tag:
        body_lc = body.noscript.get_text().lower()
        phrases = ['enable javascript', 'javascript is required', 'javascript is disabled']
        for phrase in phrases:
            if phrase.lower() in body_lc:
                return True
    return False

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