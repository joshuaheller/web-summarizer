from typing import Optional
import requests

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