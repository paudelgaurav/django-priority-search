from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title
