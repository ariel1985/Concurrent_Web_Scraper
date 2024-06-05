import json
from datetime import datetime

def save_to_json(data):
    
    filepath = 'app/scraped_data/'  # save data in 'data' folder
    
    # add current datetime to filename format 'data_YYYY-MM-DD-HH-MM-SS.json'
    filename = f'{filepath}data_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
    
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
