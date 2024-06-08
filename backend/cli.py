import argparse
import asyncio
from app.scraper import scrape
from app.data_processing import parse_html
from app.storage import Storage

def main():
    parser = argparse.ArgumentParser(description="Concurrent Web Scraper")
    parser.add_argument('urls', nargs='+', help="List of URLs to scrape")
    args = parser.parse_args()

    html_contents = asyncio.run(scrape(args.urls))
    parsed_data = [parse_html(content, url) for content, url in zip(html_contents, args.urls) if content]

    storage = Storage()
    storage.save_to_csv(parsed_data)

if __name__ == "__main__":
    main()
