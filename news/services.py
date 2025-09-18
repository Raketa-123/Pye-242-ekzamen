import requests
from django.core.cache import cache
from .models import Article

def fetch_articles():
    cached_data = cache.get("articles")
    if cached_data:
        return cached_data

    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=1057e1f435f4492ea38c991ab70379c5"
    response = requests.get(url)
    data = response.json().get("articles", [])

    new_articles = []
    for item in data:
        article, created = Article.objects.get_or_create(
            url=item["url"],
            defaults={
                "title": item["title"],
                "published_at": item.get("publishedAt"),
            },
        )
        if created:
            new_articles.append(article)

    # кешируем список на 30 минут
    cache.set("articles", data, timeout=60 * 30)

    return new_articles
