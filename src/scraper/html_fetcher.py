from typing import Optional
from pathlib import Path
from utils.file_handler import is_local_file, read_local_file
from utils.http_client import fetch_web_content

# Controls the workflow by checking whether the URL is a local file path and calling read_local_file or fetch_web_content accordingly.
def request(url: str) -> Optional[bytes]:
    if is_local_file(url):
        return read_local_file(Path(url))
    else:
        return fetch_web_content(url)