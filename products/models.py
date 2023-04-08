from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title