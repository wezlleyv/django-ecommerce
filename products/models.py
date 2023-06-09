from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    tags = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default="django")

    def __str__(self):
        return self.title