from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PriceTable(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
