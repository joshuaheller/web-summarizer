import sys
from bs4 import BeautifulSoup
import scraper.html_fetcher as html_fetcher
import parsing.html_parser as html_parser
import llm.summarizer as summarize
from models.website_content import WebsiteContent
import os
from dotenv import load_dotenv

load_dotenv()
DEFAULT_FILE_PATH = os.getenv('DEFAULT_FILE_PATH')

def run(url=DEFAULT_FILE_PATH):
    html_content = html_fetcher.request(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    body = soup.body
    if(html_fetcher.check_javascript_needed(body)):
        html_content = html_fetcher.selenium(url)
        soup = BeautifulSoup(html_content, 'html.parser')

    website_content = WebsiteContent()

    website_content.url = url
    website_content.language = html_parser.language(soup)
    website_content.title = html_parser.title(soup)
    website_content.headings = html_parser.headings(soup)
    website_content.footer = html_parser.footer(soup)
    website_content.texts = html_parser.texts(soup)
    website_content.images = html_parser.images(soup)

    website_content_dict = website_content.to_dict()

    summary = summarize.gpt(website_content_dict)
    print(summary)

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    run(file_path) if file_path else run()