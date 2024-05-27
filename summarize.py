from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(
  organization=os.getenv('ORG_ID'),
  project=os.getenv('PROJECT_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

def gpt(website_content):
    prompt = (f'Summarize the content of the website with this: {website_content['url']}. \n')
    prompt += (f'You will return a detailled summary of all the important information on the page including: the name of the business or person that owns or operates the website, products/service offered, target audience (or potential target audience if not clearly stated), location of the company/person or their services/products, information about them and all other general information.\n')
    prompt += (f'Return the summary of the brand/company/person in one extensive paragraph with the information you have been given. If you have additional knowledge about the brand/company add it to your summary.\n\n')
    prompt += (f'INFORMATION:\n')
    if website_content['language']:
        prompt += (f'Language of the page: {website_content['language']}\n\n')
    if website_content['title']:
        prompt += (f'Title of the page: {website_content['title']}\n\n')
    if website_content['headings']:
        prompt += (f'Headings of the page: {website_content['headings']}\n\n')
    if website_content['texts']:
        prompt += (f'Texts of the page: {website_content['texts']}\n\n')
    if website_content['footer']:
        prompt += (f'Footer of the page: {website_content['footer']}\n\n')

    completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant summarizing the content and information of landing pages."},
        {"role": "user", "content": prompt}
    ]
    )

    response =completion.choices[0].message.content
    return response