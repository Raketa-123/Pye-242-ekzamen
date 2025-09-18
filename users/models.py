from django.db import models
import uuid

class User(models.Model):
    is_active = models.BooleanField(
        verbose_name="активированный аккаунт",
        default=False
    )

    name = models.CharField(
        verbose_name="имя",
        max_length=30
    )

    email = models.EmailField(
        verbose_name="эл. почта",
        max_length=100,
        unique=True
    )

    activation_code = models.UUIDField(
        verbose_name="код активации",
        unique=True,
        default=uuid.uuid4
    )