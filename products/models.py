from django.db import models
from django.utils import timezone
user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()
