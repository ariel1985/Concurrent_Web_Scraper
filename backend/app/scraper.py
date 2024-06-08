import asyncio
import logging
import aiohttp
from bs4 import BeautifulSoup

logging.basicConfig(filename='scraper.log', level=logging.INFO)

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientResponseError as e:
        logging.error(f"Error with the response from {url}: {e}")
        return None
    except aiohttp.ClientConnectionError as e:
        logging.error(f"Error connecting to {url}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error fetching {url}: {e}")
        return None

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = ["https://example.com", "https://example.org"]
    html_contents = asyncio.run(scrape(urls))
    for content in html_contents:
        if content:
            soup = BeautifulSoup(content, 'html.parser')
            print(soup.title.string)
