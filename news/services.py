import requests
from django.core.cache import cache
from .models import Article, News

API_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=1057e1f435f4492ea38c991ab70379c5"

def fetch_articles():
    cached_data = cache.get("articles")
    if cached_data:
        return cached_data

    response = requests.get(API_URL)
    data = response.json().get("articles", [])

    articles = []

    for item in data:
        title = item.get("title") or "Без названия"
        url = item.get("url")
        if not url:
            continue

        description = item.get("description") or ""
        image = item.get("urlToImage") or ""
        published_at = item.get("publishedAt")

        article, _ = Article.objects.get_or_create(
            url=url,
            defaults={
                "title": title,
                "published_at": published_at,
                "description": description,
                "image": image
            }
        )
        articles.append(article)

        News.objects.get_or_create(
            title=title,
            url=url,
            defaults={
                "description": description,
                "image": image,
                "published_at": published_at
            }
        )

    cache.set("articles", articles, timeout=60*30)
    return articles
