from rest_framework import serializers
from .models import Seller

class SellerSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Seller
        fields = ('name', 'id')