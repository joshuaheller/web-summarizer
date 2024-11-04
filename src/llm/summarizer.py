from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
  organization=os.getenv('ORG_ID'),
  project=os.getenv('PROJECT_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

# this function builds the prompt for the LLM and returns the complete prompt as a string
def build_prompt(website_content, language, summary_focus=None, summary_length='medium'):
    prompt = (f"Summarize the content of the website with this URL: {website_content['url']}. ")
    
    # Add length instruction
    length_instructions = {
        'small': 'Provide a one-sentence summary.',
        'medium': 'Provide a detailed summary in one extensive paragraph.',
        'long': 'Provide a detailed one-page summary.',
        'keypoints': 'List only the key points in bullet points.'
    }
    prompt += length_instructions.get(summary_length, length_instructions['medium']) + "\n"
        
    # General summary
    if not summary_focus:
        prompt += ("Include: the name of the business or person that owns or operates the website, products/services offered, "
               "target audience (or potential target audience if not clearly stated), location of the company/person or their services/products, "
               "information about them, and all other general information.\n")
        prompt += ("Return the summary of the brand/company/person in one extensive paragraph with the information you have been given. "
               "If you have additional knowledge about the brand/company, add it to your summary.\n\n")
        
    # Focused summary
    if summary_focus:
        prompt += (f"Focus only on the following topic: {summary_focus}.\n\n")
    
    prompt += "INFORMATION:\n"

    if website_content.get('language'):
        prompt += f"Language of the page: {website_content['language']}\n\n"
    if website_content.get('title'):
        prompt += f"Title of the page: {website_content['title']}\n\n"
    if website_content.get('headings'):
        prompt += f"Headings of the page: {website_content['headings']}\n\n"
    if website_content.get('texts'):
        prompt += f"Texts of the page: {website_content['texts']}\n\n"
    if website_content.get('footer'):
        prompt += f"Footer of the page: {website_content['footer']}\n\n"
    if website_content.get('images'):
        prompt += f"Images of the page (alt texts): {website_content['images']}\n\n"

    # Add language instruction if not English
    if language.lower() != 'english':
        prompt += f"\nPlease return the summary in {language}."
        
    return prompt

# this function sends the prompt to the LLM and returns the response
def gpt(website_content, language, summary_focus=None, summary_length='medium'):
    prompt = build_prompt(website_content, language, summary_focus, summary_length)
    print(prompt)
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant summarizing the content and information of landing pages."},
        {"role": "user", "content": prompt}
    ]
    )

    response =completion.choices[0].message.content
    return response