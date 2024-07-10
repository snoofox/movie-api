from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    summary = models.TextField(blank=True)
