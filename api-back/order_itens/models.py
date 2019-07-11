from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.
class OrderItens(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    date_order_iten = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When it was update
    deleted_at = models.DateTimeField(null=True) 

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)