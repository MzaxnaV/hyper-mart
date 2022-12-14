import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    expiry_date = models.DateField()

    def get_near_expiry(self):
        return (self.expiry_date - datetime.datetime.now(timezone.utc).date()) <= 8

    def __str__(self) -> str:
        return f"{self.product_name, self.expiry_date}"


class Brand(models.Model):
    products = models.ManyToManyField("Product")
    address = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return ", ".join([product for product in self.products])