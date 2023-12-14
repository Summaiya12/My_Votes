from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    total_vote = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)
    image = models.ImageField(upload_to='media/image', default="")

    def __str__(self):
        return self.title


class CategoryItem(models.Model):
    title = models.CharField(max_length=200)
    total_vote = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    voters = models.ManyToManyField(User, blank=True)
    images = models.ImageField(upload_to='media/image', default="")

    def __str__(self):
        return self.title
