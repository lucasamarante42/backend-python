from rest_framework import serializers
from .models import ClientAddress

class ClientAddressSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = ClientAddress
        fields = ('cellphone', 'telephone', 'street', 'details', 'number', 'neighborhood', 'city', 'state', 'country', 'client')