from bs4 import BeautifulSoup
from datetime import datetime
from pydantic import BaseModel

class ParsedData(BaseModel):
    url: str
    scraped_at: datetime
    datatype: str
    data: str

def parse_html(html_content: str, url: str) -> ParsedData:
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    return ParsedData(
        url=url,
        scraped_at=datetime.now(),
        datatype="title",
        data=title
    )
