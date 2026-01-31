import requests
from bs4 import BeautifulSoup

def load_pep(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove nav + footer junk
    for tag in soup(["nav", "footer", "script", "style"]):
        tag.decompose()
        
    return soup.get_text(separator="\n")