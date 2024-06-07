# Concurrent Web Scraper

## Objective
Build a web scraper that can fetch data from multiple websites concurrently, process the data, and store it in a structured format.

## Project Structure
- `backend/app/`: Core functionality of the web scraper.
- `backend/app/scraper.py`: Contains functions to perform asynchronous web scraping.
- `backend/app/data_processing.py`: Functions to parse HTML content into Pydantic models.
- `backend/app/storage.py`: Class to save and load data in CSV format using Pydantic models.
- `backend/app/config.py`: Configuration management using Pydantic settings.
- `backend/app/api.py`: FastAPI application to serve the scraped data.
- `backend/tests/`: Unit tests for the project.
- `cli.py`: Command-line interface to input URLs and scrape data.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Requirements
- Python 3.7+
- aiohttp
- BeautifulSoup4
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
