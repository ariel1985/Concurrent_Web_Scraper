import json
from datetime import datetime


# TODO: use pydantic models

def save_to_json(data):
    filepath = 'app/scraped_data/'  # save data in 'data' folder
    # add current datetime to filename format 'data_YYYY-MM-DD-HH-MM-SS.json'
    filename = f'{filepath}data_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_json(filename='data.json'):
    with open(filename, 'r') as f:
        return json.load(f)
