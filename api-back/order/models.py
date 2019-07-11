from django.db import models
from client.models import Client
from seller.models import Seller

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_quantity = models.IntegerField()
    value_total = models.FloatField()
    date_order = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When it was update
    deleted_at = models.DateTimeField(null=True) 

    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)