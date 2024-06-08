"""Module for data processing.

Returns:
    ParsedData: Data class for parsed data
    parse_html: Function to parse HTML content
"""

from datetime import datetime
from bs4 import BeautifulSoup
from pydantic import BaseModel

class ParsedData(BaseModel):
    """Data class for parsed data.

    Args:
        BaseModel (_type_): Pydantic BaseModel
    """
    url: str
    scraped_at: datetime
    datatype: str
    data: str

def parse_html(html_content: str, url: str) -> ParsedData:
    """ Parse the HTML content and return the title.

    Args:
        html_content (str): string of HTML content
        url (str): URL of the page

    Returns:
        ParsedData: ParsedData object with the title
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    return ParsedData(
        url=url,
        scraped_at=datetime.now(),
        datatype="title",
        data=title
    )
