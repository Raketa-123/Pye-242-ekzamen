import requests
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article

API_KEY = "1057e1f435f4492ea38c991ab70379c5"
API_URL = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={API_KEY}"

class ArticleListView(APIView):
    def get(self, request):
        cached_data = cache.get("articles")
        if cached_data:
            return Response(cached_data)

        response = requests.get(API_URL)
        data = response.json().get("articles", [])

        articles = []
        for item in data:
            article, _ = Article.objects.get_or_create(
                url=item["url"],
                defaults={
                    "title": item["title"],
                    "published_at": item.get("publishedAt"),
                },
            )
            articles.append({"title": article.title, "url": article.url})

        cache.set("articles", articles, timeout=60 * 30)

        return Response(articles)
