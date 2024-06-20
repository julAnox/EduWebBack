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


class User(models.Model):
    img_path = models.ImageField(upload_to='users/')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    collage_institution = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

