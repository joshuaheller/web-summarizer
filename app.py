from bs4 import BeautifulSoup
import get_html
import parse

url = "https://imagetocaption.ai"

html_content = get_html.request(url)
soup = BeautifulSoup(html_content, 'html.parser')
body = soup.body
if(get_html.check_javascript_needed(body)):
    html_content = get_html.selenium(url)
    soup = BeautifulSoup(html_content, 'html.parser')

parse.language(soup)
parse.title(soup)
parse.headings(soup)
parse.footer(soup)
parse.texts(soup)