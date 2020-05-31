from django.db import models


class Interview(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='interview_images/')
    text = models.TextField(max_length=3096)
