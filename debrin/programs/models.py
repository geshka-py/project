from django.db import models


class TVProgram(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='tele_images/')
    description = models.TextField(max_length=522)
    role = models.CharField(max_length=255)
    year = models.CharField(max_length=10)