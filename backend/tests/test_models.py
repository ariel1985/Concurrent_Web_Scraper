from datetime import datetime
from app.storage import DataItem, LinkItem

def test_data_item():
    item = DataItem(url="https://example.com", scraped_at=datetime.now(), datatype="example", data="Example data")
    assert item.url == "https://example.com"

def test_link_item():
    item = LinkItem(link="https://example.com", created_at=datetime.now())
    assert item.link == "https://example.com"
