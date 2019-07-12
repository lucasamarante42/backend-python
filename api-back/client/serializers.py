from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Client
        fields = ('name', 'cpf', 'birthdate', 'id')