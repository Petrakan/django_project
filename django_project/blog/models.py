from django.db import models


# Create your models here.


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField("Slug - Url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'



class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField("Tag-Slug", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'



class Post(models.Model):
    """Модель постов"""
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    mini_text = models.TextField
    text = models.TextField
    created_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField("Slug-Url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"



class Comment(models.Model):
    """Модель комментариев"""
    text = models.TextField
    created_date = models.DateTimeField(auto_now=True)
    moderation = models.BooleanField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Comment"
        verbose_name_plural="Comments"



































