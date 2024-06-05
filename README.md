# Concurrent Web Scraper

## Objective
Build a web scraper that can fetch data from multiple websites concurrently, process the data, and store it in a structured format.

## Project Structure
- `scraper.py`: Contains functions to perform asynchronous web scraping.
- `data_processing.py`: Functions to parse HTML content.
- `storage.py`: Functions to save data in JSON format.
- `cli.py`: Command-line interface to input URLs and scrape data.

## Requirements
- Python 3.7+
- aiohttp
- BeautifulSoup4

## Usage
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   pip install aiohttp beautifulsoup4
   ```

2. Run the scraper using the command line:
   ```
   python cli.py https://example.com https://example.org
   ```
