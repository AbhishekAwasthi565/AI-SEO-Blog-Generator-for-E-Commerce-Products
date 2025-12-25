import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/gp/bestsellers/electronics/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

def scrape_best_sellers(limit=1):
    response = requests.get(URL, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "lxml")

    products = []

    # Each product block has data-asin
    items = soup.select("div[data-asin]")

    for item in items:
        if len(products) >= limit:
            break

        title_tag = item.select_one("img")
        link_tag = item.select_one("a.a-link-normal")

        if not title_tag or not link_tag:
            continue

        title = title_tag.get("alt", "").strip()
        link = "https://www.amazon.in" + link_tag.get("href", "")

        if not title or "/dp/" not in link:
            continue

        products.append({
            "title": title,
            "price": "N/A",
            "rating": "N/A",
            "url": link
        })

    return products
