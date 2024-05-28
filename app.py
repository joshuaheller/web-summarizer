from bs4 import BeautifulSoup
import get_html
import parse
import summarize
from website_content import WebsiteContent

url = "https://imagetocaption.ai"

html_content = get_html.request(url)
soup = BeautifulSoup(html_content, 'html.parser')
body = soup.body
if(get_html.check_javascript_needed(body)):
    html_content = get_html.selenium(url)
    soup = BeautifulSoup(html_content, 'html.parser')

website_content = WebsiteContent()

website_content.url = url
website_content.language = parse.language(soup)
website_content.title = parse.title(soup)
website_content.headings = parse.headings(soup)
website_content.footer = parse.footer(soup)
website_content.texts = parse.texts(soup)
website_content.images = parse.images(soup)

website_content_dict = website_content.to_dict()

summary = summarize.gpt(website_content_dict)
print(summary)