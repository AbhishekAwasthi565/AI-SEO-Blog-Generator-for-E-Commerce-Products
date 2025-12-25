from openai import OpenAI

client = OpenAI(
    api_key= "OPENAI API KEY"
    )

def generate_seo_blog(product, keywords):
    prompt = f"""
    Write a 150–200 word SEO blog post.

    Product:
    {product['title']}
    Price: {product['price']}
    Rating: {product['rating']}

    SEO Keywords:
    {', '.join(keywords)}

    Rules:
    - Only this product
    - No bullet points
    - Professional tone
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()
