from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=16, decimal_places=4)
    quantity=models.IntegerField()
    expired=models.DateField(auto_now=False, auto_now_add=False)
