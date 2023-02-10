from django.db import models


class Item(models.Model):
    """Модель для товарный позиций."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()


