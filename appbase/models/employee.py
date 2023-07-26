from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    salary=models.DecimalField(max_digits=16, decimal_places=4)
    join_dt=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)
    