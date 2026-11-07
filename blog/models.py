from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=450)
    content = models.TextField()
    img = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserQuote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='saved_quote')
    quote = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s saved quote"
