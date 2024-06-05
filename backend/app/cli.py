import argparse
import asyncio
from scraper import scrape
from data_processing import parse_html
from storage import save_to_json

def main():
    parser = argparse.ArgumentParser(description="Concurrent Web Scraper")
    parser.add_argument('urls', nargs='+', help="List of URLs to scrape")
    args = parser.parse_args()
    
    html_contents = asyncio.run(scrape(args.urls))
    data = [parse_html(content) for content in html_contents if content]
    save_to_json(data)

if __name__ == "__main__":
    main()
