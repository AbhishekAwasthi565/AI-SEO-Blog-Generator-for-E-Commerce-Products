from scraper import scrape_best_sellers
from keywords import generate_seo_keywords
from blog_generator import generate_seo_blog
from publisher import save_blog_locally

def slugify(text):
    return text.lower().replace(" ", "_").replace("|", "").replace(",", "")

def main():
    print("STEP 1: Scraping product...")
    products = scrape_best_sellers(limit=1)

    if not products:
        print("No products found. Amazon may be blocking requests.")
        return

    product = products[0]
    print(product)

    print("\nSTEP 2: Generating SEO keywords...")
    keywords = generate_seo_keywords(product["title"])
    print(keywords)

    print("\nSTEP 3: Generating SEO blog...")
    blog = generate_seo_blog(product, keywords)
    print(blog[:200], "...")

    print("\nSTEP 4: Saving blog locally...")
    slug = slugify(product["title"])[:40]
    file_path = save_blog_locally(
        title=f"{product['title']} Review",
        content=blog,
        slug=slug
    )

    print("\n Blog saved at:", file_path)

if __name__ == "__main__":
    main()
