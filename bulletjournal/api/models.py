from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(32, max_length=255, unique=True)
    password = models.CharField(100, max_length=255)
    