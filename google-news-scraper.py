"""
Example: call the Google News API Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The example fetches a single page so the first run is inexpensive. Raise
max_pages when you want deeper coverage; each page is billed separately.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive: one page of results.
run_input = {
    "q": "artificial intelligence",
    "gl": "us",
    "hl": "en",
    "max_pages": 1,
}

print(f"Searching Google News for: {run_input['q']}")
run = client.actor("johnvc/GoogleNewsAPI").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

# One dataset item is returned per page; each page holds a news_results list.
for page in client.dataset(run.default_dataset_id).iterate_items():
    metadata = page.get("search_metadata", {})
    articles = page.get("news_results", [])
    print(
        f"\nPage {page.get('page_number', '?')}: "
        f"{len(articles)} articles (total found: {metadata.get('total_results', 'n/a')})\n"
    )

    for article in articles:
        title = article.get("title", "")
        source = article.get("source", "")
        link = article.get("link", "")
        snippet = (article.get("snippet") or "").replace("\n", " ").strip()

        print(f"{article.get('position', '?')}. {title}")
        print(f"   Source:  {source}")
        print(f"   Link:    {link}")
        if snippet:
            print(f"   Snippet: {snippet[:160]}...")
        print()
