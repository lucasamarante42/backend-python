from django.db import models
from client.models import Client

# Create your models here.
class ClientAddress(models.Model):
    id = models.AutoField(primary_key=True)
    cellphone = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When it was update
    deleted_at = models.DateTimeField(null=True) 

    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)