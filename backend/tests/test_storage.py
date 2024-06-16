import pytest
from app.storage import LinkStorage, LinkItem
from datetime import datetime

@pytest.fixture
def link_storage():
    return LinkStorage(filename="test_links.csv")

def test_save_load_link(link_storage):
    link = LinkItem(link="https://example.com", created_at=datetime.now())
    link_storage.save_to_csv([link])
    
    loaded_links = link_storage.load_from_csv()
    assert len(loaded_links) == 1
    assert loaded_links[0].link == "https://example.com"

def test_delete_link(link_storage):
    link1 = LinkItem(link="https://example1.com", created_at=datetime.now())
    link2 = LinkItem(link="https://example2.com", created_at=datetime.now())
    link_storage.save_to_csv([link1, link2])
    
    link_storage.delete_from_csv(0)
    
    loaded_links = link_storage.load_from_csv()
    assert len(loaded_links) == 1
    assert loaded_links[0].link == "https://example2.com"
