from django.db import models


class Element(models.Model):
    """
    A model representing a periodic table element.
    """
    atomic_number = models.IntegerField(unique=True)
    symbol = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50)
    atomic_weight = models.FloatField()
    group = models.IntegerField()
    period = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.symbol})"
