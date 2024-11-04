import argparse
from bs4 import BeautifulSoup
import scraper.html_fetcher as html_fetcher
import parsing.js_detection as js_detection
import parsing.html_parser as html_parser
import llm.summarizer as summarize
from models.website_content import WebsiteContent
import os
from dotenv import load_dotenv

load_dotenv()
DEFAULT_FILE_PATH = os.getenv('DEFAULT_FILE_PATH')
DEFAULT_LANGUAGE = os.getenv('LANGUAGE', 'english')

def run(url=DEFAULT_FILE_PATH, language=DEFAULT_LANGUAGE, summary_focus=None, summary_length='medium'):
    soup = fetch_html_content(url)
    website_content_dict = parse_website_content(soup, url)
    summary = summarize.gpt(website_content_dict, language, summary_focus, summary_length)
    print(summary)
    
# Fetches HTML content and handles JavaScript-dependent pages
def fetch_html_content(url):
    html_content = html_fetcher.request(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    if js_detection.check_javascript_needed(soup.body):
        html_content = html_fetcher.request(url)
        soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# Parses content from HTML and initializes WebsiteContent
def parse_website_content(soup, url):
    website_content = WebsiteContent(
        url=url,
        language=html_parser.language(soup),
        title=html_parser.title(soup),
        headings=html_parser.headings(soup),
        footer=html_parser.footer(soup),
        texts=html_parser.texts(soup),
        images=html_parser.images(soup)
    )
    return website_content.to_dict()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summarize website content.')
    parser.add_argument('url', nargs='?', default=DEFAULT_FILE_PATH, help='URL or file path of the website to summarize')
    parser.add_argument('--language', '-l', default=DEFAULT_LANGUAGE, help='Language of the summary (default: english)')
    parser.add_argument('--focus', '-f', type=str, help='Focus area for the summary (e.g., "company", "product", "technology")')
    parser.add_argument('--length', '-len', default='medium', choices=['small', 'medium', 'long', 'keypoints'], 
                       help='Length of the summary (default: medium)')
    args = parser.parse_args()
    run(args.url, args.language, args.focus, args.length)