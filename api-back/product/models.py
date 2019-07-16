from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_quantity = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    deleted_at = models.DateTimeField(null=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

