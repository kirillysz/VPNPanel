from urllib.parse import urlparse, urlunparse

def extract_api_url(panel_url: str) -> str:
    parsed = urlparse(panel_url)
    api_url = urlunparse((parsed.scheme, parsed.netloc, '', '', '', ''))
    
    return api_url