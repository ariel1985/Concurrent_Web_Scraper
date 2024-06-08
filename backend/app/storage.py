from datetime import datetime
from typing import List
from pydantic import BaseModel
import pandas as pd

# Pydantic models for validation and serialization
class DataItem(BaseModel):
    url: str
    scraped_at: datetime
    datatype: str
    data: str

class LinkItem(BaseModel):
    link: str

# Storage class for Data
class DataStorage:
    def __init__(self, filename: str = 'data.csv'):
        self.filename = filename

    def save_to_csv(self, data: List[DataItem]):
        df = pd.DataFrame([item.model_dump() for item in data])
        df.to_csv(self.filename, index=False)

    def load_from_csv(self) -> List[DataItem]:
        df = pd.read_csv(self.filename, parse_dates=['scraped_at'])
        return [DataItem(**row) for _, row in df.iterrows()]

# Storage class for Links
class LinkStorage:
    def __init__(self, filename: str = 'links.csv'):
        self.filename = filename
    
    def load_from_csv(self) -> List[str]:
        df = pd.read_csv(self.filename)
        return df.iloc[:, 0].tolist()
    
# Example Usage
if __name__ == "__main__":
    # Example data
    data_items = [
        DataItem(url="https://example.com", scraped_at=datetime.now(), datatype="example", data="Example data")
    ]

    # Save data items to CSV
    data_storage = DataStorage()
    data_storage.save_to_csv(data_items)

    # Load data items from CSV
    loaded_data_items = data_storage.load_from_csv()
    print(loaded_data_items)

    # Load link items from CSV
    link_storage = LinkStorage()
    loaded_link_items = link_storage.load_from_csv()
    print(loaded_link_items)

