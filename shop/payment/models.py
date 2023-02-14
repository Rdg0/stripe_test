from django.db import models


class Item(models.Model):
    """Модель для товарный позиций."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def get_dollar_price(self):
        """Получаем стоимость в долларах."""
        return f'{self.price / 100:.2f}'

    def __str__(self):
        return self.name


class Order(models.Model):
    pass


class Discount(models.Model):
    pass

