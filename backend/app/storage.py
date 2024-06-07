import csv
from datetime import datetime
from typing import List
from .config import settings
from .data_processing import ParsedData

class Storage:
    def __init__(self, filename=settings.data_file):
        self.filename = filename
        
    def save_to_csv(self, data: List[ParsedData]):
        """_summary_

        Args:
            data (List[ParsedData]): _description_
        """
        with open(self.filename, 'a', newline='') as csvfile:
            fieldnames = ['url', 'scraped_at', 'datatype', 'data']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Only write the header if the file is empty
            if csvfile.tell() == 0:
                writer.writeheader()

            for item in data:
                writer.writerow(item.model_dump())

    def load_from_csv(self) -> List[ParsedData]:
        data = []
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['scraped_at'] = datetime.fromisoformat(row['scraped_at'])
                item = ParsedData(**row)
                data.append(item)
        return data
