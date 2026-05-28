# 📰 Google News Scraper: Scrape Google News Search Results with Python

> **The most efficient, reliable, and developer-friendly Google News search scraper**

**Actor page:** [apify.com/johnvc/googlenewsapi](https://apify.com/johnvc/googlenewsapi?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/googlenewsapi/input-schema](https://apify.com/johnvc/googlenewsapi/input-schema?fpr=9n7kx3)

Scrape Google News search results with Python using the [Google News API on Apify](https://apify.com/johnvc/googlenewsapi?fpr=9n7kx3). Returns structured JSON with article titles, URLs, source names, snippets, and publication dates - with support for location-based search, language filtering, and pagination.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-News-Scraper.git
   cd Apify-Google-News-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you don't have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-news-scraper.py
   ```

### Alternative: Set API Key Directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-news-scraper.py
```

## 🌟 Why Use This Google News Scraper?

The [Google News scraper on Apify](https://apify.com/johnvc/googlenewsapi?fpr=9n7kx3) delivers structured article data straight from Google News search results - the same index that aggregates coverage from thousands of publishers, updated in near real-time, ranked by Google's relevance signals.

**Real-Time News Coverage at Scale**: Google News indexes content from tens of thousands of publishers simultaneously. Rather than maintaining individual scrapers for each news source, this scraper queries Google's aggregated news index and returns ranked results across all of them in a single API call.

**Geo-Targeted News Data**: Filter results by country code (`gl`), language (`hl`), Google domain (`google_domain`), and location string. Whether you need US English tech news or French-language business coverage, the input parameters give you precise control over the geographic and linguistic scope of your results. See the full [input schema](https://apify.com/johnvc/googlenewsapi/input-schema?fpr=9n7kx3) for all options.

**Configurable Depth and Pagination**: Set `max_pages` to collect a quick headline snapshot or a deep historical dataset. The scraper handles Google's pagination automatically and returns each page as a discrete dataset item, making results easy to stream, filter, or load into a pipeline.

**Pay-Per-Event, No Subscriptions**: Pricing is $0.02 per run plus $0.02 per page scraped. You pay only for what you use - no monthly seat licenses, no minimum volume commitments. Scale up for breaking news monitoring or back down between campaigns.

**Production-Ready JSON Output**: Every article comes back with a consistent set of fields: title, URL, source name, snippet, and publication date. No schema variance between publishers, no post-processing required before loading into a database or analysis tool.

**Built for News Intelligence Workflows**: The [Google News API](https://apify.com/johnvc/googlenewsapi?fpr=9n7kx3) is a natural fit for media monitoring, competitive intelligence, trend detection, and LLM context pipelines that need fresh, structured news data on demand.

## 🎯 Common Use Cases for Google News Data

**Media Monitoring**: Track coverage of your brand, product, or executives across thousands of publishers without managing individual news API subscriptions.

**Competitive Intelligence**: Monitor news about competitors, industry trends, and market developments as they break, filtered by language and region.

**Trend Detection**: Identify emerging topics by tracking keyword frequency and source diversity in Google News results over time.

**LLM Context and RAG Pipelines**: Feed fresh, structured news articles into retrieval-augmented generation systems to keep language model responses grounded in current events.

**Sentiment Analysis**: Collect news coverage around a topic or entity and run it through an NLP pipeline to measure media sentiment across sources and regions.

**Academic and Journalism Research**: Gather structured datasets of news coverage for media studies, political science, or investigative journalism projects.

## ⚡ Features

### Core Capabilities
- **Google News Index**: Queries Google's aggregated news index across thousands of publishers simultaneously
- **Location-Based Search**: Filter by country code (`gl`), language (`hl`), and Google domain for geo-targeted results
- **Multi-Language Support**: Retrieve news in any language supported by Google News
- **Configurable Pagination**: Set `max_pages` to control collection depth
- **Domain Targeting**: Specify a custom Google domain (e.g. `google.co.uk`) to localize results
- **Duplicate Filtering**: Use the `filter` parameter to suppress near-duplicate results

### Data Quality
- **Consistent JSON Schema**: Every article shares the same field structure regardless of publisher
- **Source Attribution**: Publisher name, displayed URL, and publication date on every result
- **Full Snippet Text**: Complete article snippet, not just headline
- **Per-Page Dataset Items**: Results are pushed as discrete items for accurate billing and easy downstream processing
- **Auto-Correction Control**: Use `nfpr` to disable query auto-correction for exact-match searches

## 📖 Usage Examples

### Basic Search: Scrape Google News for Any Keyword

```json
{
  "q": "artificial intelligence",
  "max_pages": 1
}
```

### Advanced Search: Geo-Targeted News with Language Filtering

Retrieve US English AI news from google.com with 3 pages of results.

```json
{
  "q": "artificial intelligence breakthroughs 2025",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "safe": "off",
  "max_pages": 3
}
```

## 🔍 Input Parameters

Full input schema reference: [apify.com/johnvc/googlenewsapi/input-schema](https://apify.com/johnvc/googlenewsapi/input-schema?fpr=9n7kx3)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `str` | YES | - | Search query |
| `location` | `str` | no | - | Location string (e.g. `"United States"`) |
| `google_domain` | `str` | no | - | Google domain (e.g. `"google.co.uk"`) |
| `gl` | `str` | no | - | Country code (e.g. `"us"`, `"gb"`) |
| `hl` | `str` | no | - | Language code (e.g. `"en"`, `"fr"`) |
| `lr` | `str` | no | - | Language restriction (e.g. `"lang_en"`) |
| `safe` | `str` | no | `"off"` | Safe search: `"active"` or `"off"` |
| `nfpr` | `str` | no | `"0"` | Disable auto-correction: `"0"` or `"1"` |
| `filter` | `str` | no | `"0"` | Filter duplicate results: `"0"` or `"1"` |
| `max_pages` | `int` | no | `1` | Maximum pages to scrape |
| `output_file` | `str` | no | - | Optional output filename |

## 📊 Output Format

Each run returns a dataset of structured JSON objects. Sample output:

```json
{
  "query": "artificial intelligence breakthroughs 2025",
  "gl": "us",
  "hl": "en",
  "max_pages": 2,
  "pages_processed": 2,
  "news_results": [
    {
      "position": 1,
      "title": "Researchers unveil new AI model that outperforms GPT-4 on reasoning tasks",
      "link": "https://techcrunch.com/2025/03/example-article",
      "displayed_link": "techcrunch.com",
      "source": "TechCrunch",
      "snippet": "A team of researchers has published results showing a new architecture that significantly improves multi-step reasoning in large language models...",
      "date": "2025-03-15",
      "thumbnail": "https://example.com/thumbnail.jpg"
    },
    {
      "position": 2,
      "title": "OpenAI announces major update to its flagship model",
      "link": "https://www.theverge.com/2025/03/example",
      "displayed_link": "theverge.com",
      "source": "The Verge",
      "snippet": "The company says the update brings significant improvements to code generation and factual accuracy...",
      "date": "2025-03-14",
      "thumbnail": null
    }
  ],
  "search_metadata": {
    "total_results_found": 143,
    "pages_processed": 2,
    "safe_search": "off",
    "google_domain": "google.com"
  }
}
```

---

[**Made with love**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your data collection with the most reliable and efficient scraper on the market.*

Last Updated: 2026.05.29
