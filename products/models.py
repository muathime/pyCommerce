from traceback import print_exception
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    # email = models.EmailField()
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discount = models.FloatField()