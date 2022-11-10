from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    second_title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
