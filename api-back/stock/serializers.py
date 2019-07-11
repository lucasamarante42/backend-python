from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):  # create class to serializer model
    product_name = serializers.ReadOnlyField(source='product.name')
    product_description = serializers.ReadOnlyField(source='product.description')

    class Meta:
        model = Stock
        fields = ('total_quantity', 'product_name', 'product_description', 'product')
