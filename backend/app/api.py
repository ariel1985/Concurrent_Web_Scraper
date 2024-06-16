from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .storage import DataStorage, LinkStorage

app = FastAPI()
data_storage = DataStorage()
link_storage = LinkStorage()

# Add CORS middleware
origins = [
    "http://localhost:9000",  # Allow this origin
    "*" # Allow all origins - FOR DEVELOPMENT ONLY!!!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def read_data():
    data = data_storage.load_from_csv()
    return data

@app.get("/links")
def read_links():
    links = link_storage.load_from_csv()
    return links
