# Concurrent Web Scraper

## Objective
Build a web scraper that can fetch data from multiple websites concurrently, process the data, and store it in a structured format.

## Project Structure
<<<<<<< Updated upstream
- `scraper.py`: Contains functions to perform asynchronous web scraping.
- `data_processing.py`: Functions to parse HTML content.
- `storage.py`: Functions to save data in JSON format.
- `cli.py`: Command-line interface to input URLs and scrape data.
=======

- `frontend/`: Contains the frontend code for the web interface.
- `backend/`: Contains the backend code for web scraping and data processing.
- `tests/`: Contains unit tests for the backend and API code.

** Concider creating a storage folder to store the scraped data in root folder.
>>>>>>> Stashed changes

## Requirements
- Python 3.7+
- aiohttp
- BeautifulSoup4

## Usage
1. Set up a virtual environment using `venv`:

   ```
   python -m venv myenv
   source myenv/bin/activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
   or
   ```
   pip install aiohttp beautifulsoup4
   ```

3. Run the scraper using the command line:
   ```
   python cli.py https://example.com https://example.org
   ```
