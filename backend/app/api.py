from fastapi import FastAPI
from .storage import Storage

app = FastAPI()
storage = Storage()

@app.get("/data")
def read_data():
    data = storage.load_from_csv()
    return data
