from django.db import models


class Theatre(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='theatre/')
    description = models.TextField(max_length=522)
    role = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
