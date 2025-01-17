from django.db import models


# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
