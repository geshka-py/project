from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='film_images/')
    description = models.TextField(max_length=512)
    role = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
