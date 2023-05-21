from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    content = models.TextField(max_length=2000)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    edit_date = models.DateTimeField(auto_now_add=True)
    programs = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    def __str__(self):
        return self.id