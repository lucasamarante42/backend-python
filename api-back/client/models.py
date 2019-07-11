from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, unique=True)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When it was update
    deleted_at = models.DateTimeField(null=True) 

    def __str__(self):
        return self.name