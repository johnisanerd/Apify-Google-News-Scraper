# 📰 Google News API: News Search Results in Clean JSON

> The efficient, reliable, and developer-friendly way to use the Google News API.

**Actor page:** [apify.com/johnvc/GoogleNewsAPI](https://apify.com/johnvc/GoogleNewsAPI?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/GoogleNewsAPI/input-schema](https://apify.com/johnvc/GoogleNewsAPI/input-schema?fpr=9n7kx3)

The Google News API searches Google News and returns clean, structured JSON, one item per page of results. Each item carries the search parameters, search metadata (total results, pages processed), and a `news_results` array where every article includes title, link, source, snippet, and ranking position. Supports location targeting, country and language filtering, safe search, duplicate filtering, and pagination control.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-News-Scraper.git
   cd Apify-Google-News-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
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

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-news-scraper.py
```

## Why Use This Google News API?

**Real-time coverage at scale.** Google News aggregates tens of thousands of publishers. Instead of maintaining a client for each outlet, you query the aggregated index and get ranked results across all of them in a single call.

**Geo-targeted results.** Filter by country code (`gl`), language (`hl`), Google domain, and location string for precise control over the geographic and linguistic scope.

**Configurable depth.** Set `max_pages` for a quick headline snapshot or a deeper sweep. Each page is returned as a discrete item, easy to stream, filter, or load into a pipeline.

**Predictable, pay-per-use pricing.** A small per-run setup fee plus a per-page fee, with no subscription. You control cost with the page limit.

**Consistent JSON output.** Every article comes back with the same fields (title, link, source, snippet, position), so there is no schema variance between publishers.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can pull fresh news for you on demand.

## Features

### Core Capabilities
- **Aggregated news search** across thousands of publishers in one call
- **Location targeting** by country code (`gl`), language (`hl`), and Google domain
- **Safe search** and **duplicate filtering** toggles
- **Auto-correction control** with `nfpr` for exact-match queries
- **Pagination control** with a configurable page cap

### Data Quality
- **One item per page** with a stable structure
- **`news_results` array** with title, link, source, snippet, and position per article
- **Search metadata** (total results, pages processed) on every item
- **Echoed search parameters** so each item is self-describing
- **Consistent JSON** shape across every query

## Usage Examples

### Basic search
```json
{
  "q": "artificial intelligence",
  "max_pages": 1
}
```

### Geo-targeted search with language filtering
```json
{
  "q": "artificial intelligence breakthroughs",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "safe": "off",
  "max_pages": 2
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `string` | Yes | - | Search query, e.g. `artificial intelligence`, `coffee`. |
| `location` | `string` | No | - | Location string for localized results, e.g. `Austin, TX, Texas, United States`. |
| `google_domain` | `string` | No | `google.com` | Google domain to search, e.g. `google.co.uk`. |
| `gl` | `string` | No | - | Country code (ISO 3166-1 alpha-2), e.g. `us`, `gb`. |
| `hl` | `string` | No | - | Language code (ISO 639-1), e.g. `en`, `fr`. |
| `lr` | `string` | No | - | Language restriction, e.g. `lang_en`. |
| `safe` | `string` | No | `off` | Safe search: `active` or `off`. |
| `nfpr` | `string` | No | `0` | Exclude auto-corrected results: `0` or `1`. |
| `filter` | `string` | No | `0` | Filter duplicate results: `0` or `1`. |
| `max_pages` | `integer` | No | `1` | Maximum pages to fetch (~10 articles each); `0` = unlimited. Each page is billed separately. |
| `output_file` | `string` | No | - | Optional filename to save results. |

## Output Format

A real result for `artificial intelligence` (one item per page; the `news_results` array is trimmed to a single article here, and `search_information` carries additional fields).

```json
{
  "search_parameters": {
    "q": "artificial intelligence",
    "gl": "us",
    "hl": "en",
    "safe": "off",
    "nfpr": "0",
    "filter": "0",
    "max_pages": 1
  },
  "search_metadata": {
    "total_results": 9,
    "news_count": 9,
    "pages_processed": 1,
    "max_pages_set": 1,
    "pagination_limit_reached": false
  },
  "search_information": {
    "query_displayed": "artificial intelligence"
  },
  "search_timestamp": "2026-05-29T11:27:03",
  "page_number": 1,
  "news_results": [
    {
      "position": 1,
      "title": "Improving multimodal wearable sensing for healthcare with artificial intelligence",
      "link": "https://www.nature.com/articles/s41587-026-03134-z",
      "source": "Nature",
      "snippet": "This Comment explores artificial intelligence-driven strategies to accelerate the clinical translation of multimodal wearable sensors."
    }
  ]
}
```

Each page item echoes the `search_parameters` you sent, reports `search_metadata` (total results and pages processed), and lists every article in `news_results` with its ranking position, title, link, source, and snippet.

---

## Use as an MCP tool

You can load the Google News API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google News API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google News API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google News API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/GoogleNewsAPI`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI`, using OAuth when prompted.
5. Ask Claude to run the Google News API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google News API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/GoogleNewsAPI`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google News API to power media monitoring, competitive intelligence, trend detection, and LLM context pipelines with reliable, structured results.*

## Featured Tasks

Ready-to-run examples on the Apify Store.

- [Export Google News Results to CSV](https://apify.com/johnvc/GoogleNewsAPI/examples/export-google-news-results-to-csv?fpr=9n7kx3)

Last Updated: 2026.07.28
