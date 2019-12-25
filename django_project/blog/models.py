from django.db import models


# Create your models here.


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField("Url", max_length=100)
