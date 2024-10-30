# web-summarizer

This is a simple tool that scrapes a single website or landing pages for the most important information and feeds this data into a prompt to OpenAI's GPT4 API.

It will return a short paragraphs summarizing and describing the brand/company, their products/services and other information of the website.

## Requirements
It works on Linux/MacOS and Windows. 

Python 3.10 or higher is required.

You need to have chrome chromedrivers installed.

You need to have an OpenAI API key.

## Get started

To get started copy copy the ``.env.template``and rename it to ``.env``. Add your OpenAI credentials and custom config here (language, default file path).

Then install the packages with ``pip install -r requirements.txt``

If you want to scrape local files, add the path to the file in the ``.env`` file and add it in the data folder.

## Run summarizer with CLI commands

``python src/main.py`` (uses default file path and language from ``.env``)

``python src/main.py --language Schwäbisch`` (uses default file path and specified language)

``python src/main.py https://www.generic.de`` (uses specified url and default language from ``.env``)

``python src/main.py https://www.generic.de -l English`` (uses specified url and specified language)

### Contact me if you have ideas for improvemens for feature requests.