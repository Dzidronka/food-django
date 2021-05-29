from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_type = models.TextField()
    ingredients = models.TextField(blank=True)
    produced_by = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=5, default='0')
    calories = models.CharField(max_length=5, default='0')
    proteins = models.CharField(max_length=5, default='0')
    carbohydrates = models.CharField(max_length=5, default='0')
    fat = models.CharField(max_length=5, default='0')
    fibre = models.CharField(max_length=5, default='0', blank=True)
    salt = models.CharField(max_length=5, default='0', blank=True)
    calories_per100 = models.CharField(max_length=5, default='0')
    proteins_per100 = models.CharField(max_length=5, default='0')
    carbohydrates_per100 = models.CharField(max_length=5, default='0')
    fat_per100 = models.CharField(max_length=5, default='0')
    fibre_per100 = models.CharField(max_length=5, default='0', blank=True)
    salt_per100 = models.CharField(max_length=5, default='0', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    product_image = models.ImageField(upload_to=settings.MEDIA_ROOT, default='/static/img/default.png')
    additional_image = models.ImageField(upload_to='additional', blank=True)
    miniature_image = models.ImageField(upload_to='minis', blank=True)
    tags = TaggableManager()

    def upload_image(self, filename):
        return 'product/{}/{}'.format(self.product_name, filename)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_name

    def publish_comments(self):
        return self.comments


class Comment(models.Model):
    product = models.ForeignKey('FoodLibrary.Product', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
