import os
from datetime import datetime

def save_blog_locally(title, content, slug):
    base_dir = "output/blogs"
    os.makedirs(base_dir, exist_ok=True)

    file_path = f"{base_dir}/{slug}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{title}\n\n")
        f.write(f"Published on: {datetime.now()}\n\n")
        f.write(content)

    return file_path
