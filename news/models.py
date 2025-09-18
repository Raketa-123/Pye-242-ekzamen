from django.db import models
from rest_framework.response import Response
from news.services import fetch_articles

class News(models.Model):
    source_id = models.UUIDField(
        verbose_name="айди",
        unique=True,
        null=True,
    )

    source_name = models.CharField(
        verbose_name="название источника",
        max_length=100,
    )

    author = models.CharField(
        verbose_name="автор",
        max_length=100,
    )

    title = models.CharField(
        verbose_name="название",
        max_length=100,
    )

    description = models.TextField(
        verbose_name="описание",
        max_length=500,
    )

    url = models.URLField(
        verbose_name="юрл",
        unique=True
    )

    url_to_image = models.URLField(
        verbose_name="юрл на картинку",
        unique=False,
    )

    content = models.TextField(
        verbose_name="содержание",
        max_length=500,
    )
    
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
