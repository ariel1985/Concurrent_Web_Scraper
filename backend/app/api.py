from fastapi import FastAPI
from .storage import load_from_json

app = FastAPI()

@app.get("/data")
def read_data():
    data = load_from_json()
    return data
