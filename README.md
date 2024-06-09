# Concurrent Web Scraper

This project is a web scraper that fetches data from multiple websites concurrently, processes the data, and stores it in a structured format.

## Prerequisites

- Python 3.x
- Node.js
- npm

## Setup

### Backend

1. Navigate to the `backend` directory.
2. Install the Python dependencies by running `pip install -r requirements.txt`.
3. Run the backend for API by executing `uvicorn app.api:app --reload`.

### Frontend

1. Navigate to the `frontend` directory.
2. Install the Node.js dependencies by running `npm install`.
3. Start the app in development mode by executing `quasar dev`.

## Usage

After setting up both the backend and frontend, you can start using the web scraper. The frontend will be accessible at `http://localhost:9000` (or the port specified in your `.env` file).

More information can be found in the respective `README.md` files in the `backend` and `frontend` directories.

