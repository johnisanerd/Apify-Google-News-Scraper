"""
Google News Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/googlenewsapi?fpr=9n7kx3
Input schema: https://apify.com/johnvc/googlenewsapi/input-schema?fpr=9n7kx3

This script demonstrates how to scrape Google News search results using the
Google News API scraper on Apify. Returns article titles, links, sources,
snippets, and publication dates as structured JSON.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "q": "artificial intelligence breakthroughs 2025",
    "gl": "us",
    "hl": "en",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/googlenewsapi").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
