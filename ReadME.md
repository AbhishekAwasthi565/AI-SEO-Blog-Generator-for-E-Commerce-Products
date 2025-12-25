# Amazon Best Seller to SEO Blog Generator

This Python project fully automates the process of finding a trending product on Amazon and creating content for it. It scrapes the "Best Sellers" list, uses AI to generate SEO keywords, writes a complete blog post, and saves the result locally.

## Workflow

1.  **Scrape:** The bot visits Amazon India's "Best Sellers in Electronics" page and picks the top trending product.
2.  **Analyze:** It sends the product title to OpenAI (GPT-4o-mini) to generate high-value SEO keywords.
3.  **Write:** It uses the product data and keywords to draft a professional, SEO-optimized blog post.
4.  **Publish:** The final article is saved locally as a text file for review.

## Project Structure

```text
amazon-blog-bot/
│
├── main.py              # The controller script that runs the full pipeline
├── scraper.py           # Handles Amazon scraping (BeautifulSoup + Requests)
├── keywords.py          # Generates SEO keywords using OpenAI API
├── blog_generator.py    # Writes the blog post using OpenAI API
├── publisher.py         # Saves the final text file locally
└── README.md            # Documentation

```

## Prerequisites

* **Python 3.8+**
* **OpenAI API Key:** You need a valid API key with credits.

## Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/amazon-blog-bot.git](https://github.com/yourusername/amazon-blog-bot.git)
cd amazon-blog-bot

```


2. **Install dependencies:**
Run the following command to install the required libraries:
```bash
pip install requests beautifulsoup4 openai lxml

```



## Configuration

Before running, you must add your OpenAI API Key.

1. Open `keywords.py` and replace `"OPENAI API KEY"` with your actual key:
```python
client = OpenAI(api_key="sk-proj-...")

```


2. Open `blog_generator.py` and do the same:
```python
client = OpenAI(api_key="sk-proj-...")

```



*(Note: For better security, consider using environment variables instead of hardcoding keys.)*

## Usage

Simply run the main script:

```bash
python main.py

```

**Expected Output in Terminal:**

```text
STEP 1: Scraping product...
{'title': 'OnePlus Nord Buds 2r...', 'price': 'N/A', ...}

STEP 2: Generating SEO keywords...
['wireless earbuds', 'bluetooth headphones', 'OnePlus audio', 'budget earbuds']

STEP 3: Generating SEO blog...
The OnePlus Nord Buds 2r have taken the market by storm...

STEP 4: Saving blog locally...
Blog saved at: oneplus_nord_buds_review.txt

```

## Important Notes

* **Amazon Blocking:** Amazon aggressively blocks scrapers. If you see "No products found," try updating the `User-Agent` string in `scraper.py` or wait a few minutes before trying again.
* **Pricing/Ratings:** The current scraper sets Price/Rating to "N/A" to avoid complex parsing errors, but the AI will write the blog focusing on the product title and general features.

## License

This project is open-source. Feel free to modify and use it for your content automation needs.
