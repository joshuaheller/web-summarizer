from pathlib import Path
from typing import Optional

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