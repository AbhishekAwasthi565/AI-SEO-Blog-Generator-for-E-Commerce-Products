from openai import OpenAI

client = OpenAI(
    api_key= "OPENAI API KEY"
    )

def generate_seo_keywords(product_title):
    prompt = f"""
    Generate exactly 4 SEO keywords for this product.
    Short phrases only.

    Product:
    {product_title}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip().split("\n")
