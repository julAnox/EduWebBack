from datetime import timezone

from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    img_path = models.ImageField(upload_to='teachers/')


class Post(models.Model):
    img_path = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
