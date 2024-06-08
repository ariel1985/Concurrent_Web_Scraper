from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .storage import Storage

app = FastAPI()

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

storage = Storage()

@app.get("/data")
def read_data():
    data = storage.load_from_csv()
    return data