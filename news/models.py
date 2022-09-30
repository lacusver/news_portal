from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name_plural = "news"
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    class Meta:
        verbose_name_plural = "comments"
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    news = models.ForeignKey('News', on_delete = models.CASCADE, null=True, related_name='newscomment')

class Likes(models.Model):
    class Meta:
        verbose_name_plural = "likes"
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    news = models.ForeignKey('News', on_delete = models.CASCADE, null=True, related_name='newslike')
    liked = models.BooleanField(default=False)