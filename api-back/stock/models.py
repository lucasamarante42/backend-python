from django.db import models
from product.models import Product

# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    total_quantity = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    deleted_at = models.DateTimeField(null=True) 

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.total_quantity

